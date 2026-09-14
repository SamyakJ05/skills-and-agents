---
name: finance-shashankvemuri
description: >
  Python toolkit for quantitative finance: market data retrieval, technical
  indicators, return/risk analytics, stock screening, trading-strategy
  signals, backtesting, portfolio optimization, and statistical/ML models
  (ARIMA, PCA, clustering, factor analysis). Use when the task involves
  analyzing stocks or other instruments, computing technical indicators
  (RSI, MACD, Bollinger Bands, ATR, VWAP, Ichimoku, etc.), building or
  backtesting a trading strategy, screening equities (Minervini, relative
  strength, growth, dividend), optimizing a portfolio (efficient frontier,
  discrete allocation, Monte Carlo simulation), valuing a company (DCF,
  fundamental ratios), or running quant research (regression, CAPM, PCA,
  clustering, ARIMA forecasting, cointegration). Vendored from
  shashankvemuri/Finance (MIT licensed).
license: MIT
---

# Finance Toolkit

Vendored copy of the `finance` Python package from
[shashankvemuri/Finance](https://github.com/shashankvemuri/Finance) (MIT
license, ~4.3k GitHub stars). It is a composable library of pure calculation
functions plus a thin data-access layer — not a black-box framework. Read
`README.md` in this directory for the authoritative usage guide; this file
is a map to help you find the right module fast.

## What's vendored

- `src/finance/` — the installable package (`pip install -e .` from this
  directory, or copy the subpackages you need into a host project).
- `examples/` — one runnable script per major workflow (uses synthetic data
  by default; pass `--live` for real network calls).
- `apps/research.py` — a Streamlit research app tying the modules together.
- `docs/methodology.md`, `docs/providers.md`, `docs/workflows.md` — the
  calculation/execution conventions, data-provider contracts and caveats,
  and longer worked research workflows.
- `README.md`, `LICENSE`, `pyproject.toml` — as-is from upstream.

Not vendored: `tests/`, `.github/` CI config, `scripts/`, `CONTRIBUTING.md`,
`AGENTS.md` — repo-maintenance files not needed to use the library.

## Design conventions (important for correct use)

- Importing the package never fetches data or hits the network — network
  I/O only happens when you call a `finance.data` function explicitly.
- Returns and rates are fractions (0.01 = 1%), not percentages; RSI and
  similar oscillators are on their natural 0–100 scale.
- Indicator functions return series with the same index as the input;
  warm-up periods are left as `NaN` rather than back-filled or dropped.
- The backtester assumes signals are generated on the close and executed at
  the next bar's open — it tracks cash, fractional shares, long/short
  fills, commission, slippage, and borrow costs.
- Core dependencies are only NumPy and pandas. Everything else (yfinance,
  scipy, scikit-learn, statsmodels, matplotlib, streamlit, vaderSentiment,
  torch, prophet, openpyxl) is an optional extra — install only what a task
  needs, e.g. `pip install -e '.[data]'` or `pip install -e '.[portfolio,models]'`.

## Module map

| Package | Import from | Covers |
| --- | --- | --- |
| `finance.data` | `finance.data` | `YahooFinance` (OHLCV/intraday history), `Finviz` screener client, `TradingView` client, S&P 500 / exchange universes, dividend calendars, COT futures positioning, earnings calendars, batch fetch (`fetch_many`), news/RSS/Reddit/transcript content helpers, OHLCV/ticker normalization |
| `finance.indicators` | `finance.indicators` | Trend (`sma`, `ema`, `wma`, `dema`, `tema`, `hma`, `trima`, `smma`, `ribbon`), momentum (`rsi`, `macd`, `stochastic`, `stochastic_rsi`, `williams_r`, `cci`, `roc`, `adx`, `aroon`, `tsi`, `ultimate_oscillator`, ...), volatility (`bollinger_bands`, `atr`, `keltner`, `donchian`, `supertrend`, `standard_deviation`, `realized_volatility`, ...), volume (`vwap`, `vwma`, `obv`, `mfi`, `chaikin_money_flow`, `force_index`, `accumulation_distribution`, ...), levels/breadth (`pivot_points`, `fibonacci_levels`, `ichimoku`, `gann_fan`, `mcclellan`, `arms_index`, ...), and rolling statistics (`zscore`, `beta`, `correlation`, `rolling_regression`, `geometric_return`) |
| `finance.analytics` | `finance.analytics` | Returns/performance (`returns`, `cumulative_returns`, `drawdown`, `performance`, `seasonality`), risk (`value_at_risk`, `expected_shortfall`, `kelly_fraction`, `position_size`, `risk_reward`), regression (`ols`, `capm`, `correlation_pairs`), valuation (`discounted_cash_flow`, `fundamental_ratios`, `scenario_valuation`, `statement_ratios`), sentiment scoring, and company/index scenario & seasonal research |
| `finance.screening` | `finance.screening` | `minervini` (trend template), `relative_strength` / `ibd_relative_strength`, `rsi_screen`, `rsi_trend_screen`, `growth_screen`, `dividend_screen`, `fundamental_screen`, `technical_screen`, `green_line_screen` |
| `finance.strategies` | `finance.strategies` | Signal generators (`crossover`, `moving_average`, `bollinger_reversion`, `rsi_reversion`, `breakout`, `pairs_trade`, `trailing_stop`, `ribbon_trend`, `macd_trend`, `keltner_breakout`, `ichimoku_trend`, `stochastic_reversion`, `williams_reversion`) and `select_strategy` for chronological strategy selection |
| `finance.backtesting` | `finance.backtesting` | `backtest(open, close, target_positions, commission=..., slippage=..., borrow_cost=...) -> BacktestResult` plus `completed_trades` / `trade_statistics` for FIFO trade-level reporting |
| `finance.portfolio` | `finance.portfolio` | `portfolio_statistics`, `optimize` / `efficient_frontier` (constrained mean-variance optimization), `random_allocations`, `discrete_allocation` (share-count rounding), `geometric_brownian_motion`, `simulate_portfolio`, `lump_sum_vs_dca` |
| `finance.models` | `finance.models` | `pca`, `cluster_assets` / `cluster_features`, `cointegration_pairs`, `partial_correlations` (+ CV variant), `anomaly_scores`, `factor_analysis`, ARIMA (`arima_forecast`, `arima_diagnostics`, `select_arima_order`), `forecast_features` / `evaluate_forecast` / `evaluate_arima` / `evaluate_direction`, `volatility_regimes`, `student_t_fit`, plus optional neural/Prophet experiment evaluators |
| `finance.reports` | `finance.reports` | `candles`, `correlation_heatmap`, `equity_chart` (matplotlib), `export_table` (CSV/Excel), `research_report` (HTML), `network_gexf` (graph export) |
| `finance.integrations` | `finance.integrations` | `Alpaca` broker client, `preview_order` / `reconcile_orders`, and explicit `send_email` / `send_sms` / `send_webhook` / `email_report` notification transports |

## Usage patterns

Install (editable, with only the extras a task needs):

```bash
cd skills/coding/finance-tools/finance-toolkit
python -m venv .venv && source .venv/bin/activate
python -m pip install -e '.[data,portfolio,models,plot]'
```

Fetch data, then compute indicators (no network access happens until you
call the data function):

```python
from finance.data import YahooFinance
from finance.indicators import bollinger_bands, rsi

prices = YahooFinance().history("AAPL", "2023-01-01", "2025-01-01")
strength = rsi(prices["close"], window=14)
bands = bollinger_bands(prices["close"], window=20)
```

Generate signals and backtest them (close-time signal, next-open fill):

```python
from finance.backtesting import backtest
from finance.strategies import moving_average

targets = moving_average(prices["close"], fast=20, slow=50)
result = backtest(prices["open"], prices["close"], targets, commission=0.001)
print(result.metrics)
```

Screen a universe, optimize a portfolio, or run quant research the same
way — import the function you need from the relevant subpackage and pass
plain pandas Series/DataFrames. The `examples/` directory has one runnable
script per workflow (`calculate_indicators.py`, `backtest_moving_average.py`,
`optimize_portfolio.py`, `screen_minervini.py`, `research_models.py`,
`value_a_company.py`, `cluster_assets.py`, `forecast_time_series.py`, etc.) —
read the one closest to the task instead of guessing at call signatures.

## When to read further

- Before interpreting backtest or indicator output: `docs/methodology.md`
  (calculation and execution conventions).
- Before relying on a data provider (Yahoo Finance, Finviz, TradingView):
  `docs/providers.md` (rate limits, schema caveats, point-in-time
  limitations — universes/fundamentals are current snapshots, not
  historical point-in-time data).
- For longer end-to-end research workflows and optional installs:
  `docs/workflows.md`.

## Disclaimer

Upstream states: *"The material in this repository is for educational
purposes only and should not be considered professional investment
advice."* Carry that caveat into any output built with this toolkit.
