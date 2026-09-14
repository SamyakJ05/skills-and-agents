---
name: howtrader
description: Crypto quant trading framework (forked from VNPY) for developing, backtesting, and live-executing trading strategies on Binance and OKX. Use when writing a CTA-style crypto strategy, building a backtesting/optimization pipeline over historical kline data, wiring TradingView webhook signals into automated order execution, or working with the event-driven engine/gateway architecture. Covers strategy templates, the backtesting engine, exchange gateways, and the TradingView signal app. IMPORTANT: this is not just an analysis library — its gateways place real orders against real exchange accounts when run live with API keys, so treat any code path that reaches BinanceUsdtGateway/BinanceSpotGateway/BinanceInverseGateway/OkxGateway or MainEngine.send_order as capable of executing real trades with real money.
license: MIT
---

# howtrader

Vendored from [51bitquant/howtrader](https://github.com/51bitquant/howtrader) (MIT, ~959 stars). Source lives in `howtrader/` (the core package) and `examples/` (backtest/portfolio/strategy examples). Binary UI assets (`.ico` icons, doc screenshots) and the Docker packaging were stripped since they add nothing for reading/writing strategy code; the Qt desktop UI source itself (`howtrader/trader/ui/`, `howtrader/app/*/ui/`) is kept for reference but is optional — everything below works headless (`examples/no_ui.py` is the pattern for that).

## What it is

HowTrader is a fork of the well-known [VNPY](https://github.com/vnpy/vnpy) quant trading framework, adapted specifically for crypto (Binance and OKX). It keeps VNPY's event-driven architecture but changes numeric types to `Decimal` for order/trade/contract precision, fixes gateway reconnect handling, and adds a `tradingview` app for consuming third-party webhook signals (e.g. from TradingView alerts) and turning them into live orders.

Core pieces:

- **Event engine** (`howtrader/event/engine.py`) — a generic pub/sub `EventEngine` that queues and dispatches `Event` objects to registered handlers on a background thread. Everything else (gateways, engines, UI) communicates through events.
- **Main engine & gateways** (`howtrader/trader/engine.py`, `howtrader/gateway/`) — `MainEngine` owns gateway instances and app engines. Gateways translate exchange-specific REST/WebSocket protocols into the framework's common `OrderData`/`TradeData`/`TickData`/`PositionData` objects:
  - `howtrader/gateway/binance/` — `BinanceSpotGateway`, `BinanceUsdtGateway` (USDT-margined futures), `BinanceInverseGateway` (coin-margined futures)
  - `howtrader/gateway/okx/` — `OkxGateway`
- **CTA strategy app** (`howtrader/app/cta_strategy/`) — the main strategy framework: `CtaTemplate` (base class for live/backtest strategies), `CtaEngine` (runs strategies live), `BacktestingEngine` + `OptimizationSetting` (backtests and parameter optimization, including genetic algorithm optimization).
- **TradingView app** (`howtrader/app/tradingview/`) — receives webhook payloads (e.g. from a Flask endpoint you run) as `EVENT_TV_SIGNAL` events and routes them into strategy templates: `SimpleTVStrategy`, `BestLimitTVStrategy`, `TwapTVStrategy`, `BestLimitMultiTVSignalsStrategy`, etc. under `howtrader/app/tradingview/strategies/`, plus simpler example variants (`my_tv_simple_strategy.py`, `my_tv_best_limit_strategy.py`) under `examples/strategies/`. This is the integration point for "TradingView sends a buy/sell alert, howtrader places the order."
- **Other apps** — `algo_trading` (execution algos: TWAP, iceberg, sniper, grid, DMA, arbitrage), `spread_trading`, `portfolio_strategy`, `portfolio_manager`, `data_manager`, `data_recorder`, `risk_manager` — all under `howtrader/app/`.
- **Database layer** (`howtrader/trader/database.py`, `howtrader/trader/dbconnectors/`) — pluggable bar-data storage: SQLite (default), MySQL, or MongoDB.

## Installation

```bash
pip install git+https://github.com/51bitquant/howtrader.git
```

Requires Python 3.9 (the upstream project recommends Anaconda for the pandas/NumPy/TA-Lib dependency stack). TA-Lib often needs a platform-specific wheel on Windows — see the upstream README for details. The vendored copy here is for reading/searching source and adapting strategy code; install the real package to actually run it.

## Architecture in practice

1. **`EventEngine`** runs a background thread pulling `Event(type, data)` off a queue and dispatching to handlers registered via `register(event_type, handler)`.
2. **`MainEngine(event_engine)`** is the top-level object you instantiate. You call `main_engine.add_gateway(BinanceUsdtGateway)` for each exchange connection you want, and `main_engine.add_app(CtaStrategyApp)` / `add_app(TradingViewApp)` for the functionality you need.
3. Strategies subclass `CtaTemplate` (`howtrader/app/cta_strategy/template.py`) and implement `on_init`, `on_start`, `on_stop`, `on_tick`, `on_bar`, `on_trade`, `on_order`. Order entry/exit happens through `self.buy()`, `self.sell()`, `self.short()`, `self.cover()` (all wrap `send_order`), and helpers like `load_bar()` pull historical klines for warmup.
4. The **same strategy class** runs in both `CtaEngine` (live) and `BacktestingEngine` (historical simulation) — the engine intercepts `buy`/`sell`/etc. and either sends real orders or simulates fills against historical bars, which is the standard VNPY/howtrader pattern for keeping backtest and live logic identical.

## Usage example: define and backtest a strategy

A minimal CTA strategy (see `examples/strategies/atr_rsi_strategy.py` for the full vendored version):

```python
from howtrader.app.cta_strategy import CtaTemplate
from howtrader.trader.object import BarData

class AtrRsiStrategy(CtaTemplate):
    author = "51bitquant"

    atr_length = 22
    atr_ma_length = 10
    rsi_length = 5
    fixed_size = 1

    parameters = ["atr_length", "atr_ma_length", "rsi_length", "fixed_size"]
    variables = []

    def on_init(self):
        self.write_log("strategy initializing")
        self.load_bar(10)  # warm up with 10 days of historical bars

    def on_bar(self, bar: BarData):
        # compute indicators, then act, e.g.:
        # if not self.pos and signal_long:
        #     self.buy(bar.close_price, self.fixed_size)
        pass
```

Backtest it (from the README, `vt_symbol` is `SYMBOL.EXCHANGE`, lowercase symbol for spot markets, uppercase for futures):

```python
from howtrader.app.cta_strategy.backtesting import BacktestingEngine, OptimizationSetting
from howtrader.trader.object import Interval
from datetime import datetime
from strategies.atr_rsi_strategy import AtrRsiStrategy

engine = BacktestingEngine()
engine.set_parameters(
    vt_symbol="BTCUSDT.BINANCE",
    interval=Interval.MINUTE,
    start=datetime(2020, 1, 1),
    end=datetime(2020, 5, 1),
    rate=4 / 10000,     # taker fee
    slippage=0,
    size=1,
    pricetick=0.01,
    capital=1_000_000,
)
engine.add_strategy(AtrRsiStrategy, {})
engine.load_data()          # loads bars from the configured database (see crawl_data.py to populate it)
engine.run_backtesting()
df = engine.calculate_result()
engine.calculate_statistics()
engine.show_chart()

# optional parameter optimization (genetic algorithm)
setting = OptimizationSetting()
setting.set_target("sharpe_ratio")
setting.add_parameter("atr_length", 3, 39, 1)
setting.add_parameter("atr_ma_length", 10, 30, 1)
result = engine.run_ga_optimization(setting)
```

Historical bar data must exist in the configured database before `load_data()` works — `crawl_data.py` (vendored at the repo root here) shows the pattern for pulling klines from Binance's public REST API (`/api/v3/klines`, `/fapi/v1/klines`, `/dapi/v1/klines`) and writing them via `database.save_bar_data(buf)`.

## TradingView webhook integration

The pattern (from `tv_script.py` / the README's `main.py` example): run a Flask endpoint that receives TradingView alert webhooks, checks a shared `passphrase`, and pushes an `EVENT_TV_SIGNAL` event into the framework's event engine, which the `TradingViewApp` routes to a strategy:

```python
@app.route('/webhook', methods=['POST'])
def webhook():
    data = json.loads(request.data)
    if data.get('passphrase') != SETTINGS.get("passphrase", ""):
        return {"status": "failure", "msg": "passphrase is incorrect"}
    del data['passphrase']
    event_engine.put(Event(type=EVENT_TV_SIGNAL, data=data))
    return {"status": "success", "msg": ""}
```

Strategy variants under `examples/strategies/` (`my_tv_simple_strategy.py`, `my_tv_best_limit_strategy.py`) show how to consume these signals and place best-limit or market orders in response.

## Critical caveat: this framework places real orders with real money

Everything above the backtesting engine is designed to run against **live exchange accounts**:

- `BinanceSpotGateway`, `BinanceUsdtGateway`, `BinanceInverseGateway`, and `OkxGateway` connect to real Binance/OKX REST and WebSocket APIs using **your API key and secret**, and `CtaEngine`/`MainEngine.send_order()` submit real orders that execute with real funds.
- The TradingView webhook path is explicitly designed to turn an external signal (which could be misconfigured, delayed, spoofed if the passphrase leaks, or simply wrong) directly into a live order with no human in the loop.
- Grid/martingale strategies vendored under `howtrader/app/cta_strategy/strategies/` (e.g. `martingle_future_strategy*.py`) are leveraged, unbounded-risk-by-design strategies — martingale-style position sizing can produce large losses on adverse moves even though individual trades look small.
- There is no built-in dry-run/paper-trading gateway distinct from backtesting — running any strategy through `CtaEngine` with a real gateway attached means it is live. Use `BacktestingEngine` for historical simulation, and treat adding a gateway + running `MainEngine` as the live-trading boundary.
- API keys should be scoped to trading only (no withdrawal permission), and IP-whitelisted where the exchange supports it (Binance Spot Ed25519 keys in particular require IP whitelisting per the upstream README).

Do not wire up a gateway with real API credentials, and do not point the TradingView webhook at a strategy that calls `buy`/`sell`/`short`/`cover`, unless real trading with real financial risk is actually intended.
