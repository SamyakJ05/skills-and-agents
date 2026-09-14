---
name: gs-quant
description: Goldman Sachs' Python toolkit for quantitative finance. Use when pricing derivatives (swaps, options, swaptions, FX/rate/equity instruments), computing risk measures (delta, gamma, vega, theta), constructing or analyzing portfolios, running timeseries analytics on financial data, or backtesting trading strategies in Python. Covers what works standalone (timeseries analytics, instrument definitions) versus what requires a Goldman Sachs Marquee API session (live pricing, risk calcs, market data, backtesting).
license: Apache-2.0
---

# gs-quant

Vendored from [goldmansachs/gs-quant](https://github.com/goldmansachs/gs-quant) (Apache-2.0, ~13k stars). Source lives in `src/gs_quant/` (the `test/` and `content/` notebook/tutorial directories were stripped to keep this skill lean — `test/` was test fixtures, `content/` was Jupyter notebook tutorials with embedded images, neither needed to use the library).

## What it is

GS Quant is built and maintained by Goldman Sachs quants. It provides:

- **Instrument definitions** — dataclass-style objects for swaps, swaptions, caps/floors, FX/equity/rates options, bonds, and more (`gs_quant/target/instrument.py`, re-exported via `gs_quant.instrument`).
- **Risk measures** — objects like `DollarPrice`, `IRDelta`, `EqDelta`, `Theta`, `Vega` that you pass to an instrument's `.calc()` (`gs_quant.risk`).
- **Markets / PricingContext** — a context manager that batches and dispatches pricing/risk requests (`gs_quant.markets.core.PricingContext`).
- **Timeseries analytics** — a large library of pure pandas/numpy functions for smoothing, returns, volatility, correlation, technical indicators, etc. (`gs_quant.timeseries`).
- **Backtesting** — a strategy/engine framework (`gs_quant.backtests`) for simulating trading strategies over historical periods.
- **Data access** — `gs_quant.data.Dataset` for pulling market/reference data from Goldman's Marquee platform.

## Installation

```bash
pip install gs-quant
```

Requires Python 3.9+. For the vendored copy in this skill, treat `src/gs_quant/` as reference source to read/search rather than reinstalling — install the real package from PyPI to actually run code (`pip install gs-quant`), since this vendored tree omits `gs_quant/test/` and `gs_quant/content/`.

## The critical caveat: what needs a GS session, what doesn't

Most of gs-quant's headline features — **live pricing, risk calcs, market data, and backtesting — require an authenticated session against Goldman's Marquee API**, which needs a client ID and secret issued to institutional GS clients (via GS Sales coverage). There is no offline/local pricing mode: `Instrument.calc()`, `Instrument.price()`, `Instrument.resolve()`, and `PricingContext` all resolve through `GsSession.current`, and `gs_quant.data.Dataset` posts requests through the same session.

```python
from gs_quant.session import GsSession, Environment

GsSession.use(
    Environment.PROD,
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    scopes=('run_analytics', 'read_product_data'),
)
```

**What does work standalone, with no GS credentials:**

- **Instrument construction** (just building the dataclass objects, without calling `.resolve()`, `.price()`, or `.calc()`) — e.g. `IRSwap('Pay', '10y', 'USD')` constructs fine offline; it's only asking gs-quant to *resolve or price* it that requires a session.
- **Timeseries analytics** — functions in `gs_quant.timeseries.analysis`, `.statistics`, `.algebra`, `.econometrics`, and similar modules operate on plain `pandas.Series` you already have (e.g. from your own data source) and make no network calls. Import these submodules directly rather than the top-level `gs_quant.timeseries` package, because the top-level `__init__.py` also re-exports `measures_*` submodules (e.g. `measures_rates`, `measures_fx_vol`) that *do* call the GS data APIs and require a session to actually execute (though importing them costs nothing until called).

If you're prototyping without GS credentials, stick to instrument construction (no resolve/price/calc) and `gs_quant.timeseries.analysis` / `.statistics` / `.algebra` on your own data. Anything touching pricing, risk, live data, or backtesting needs the Marquee session above.

## Key modules and usage patterns

### Instruments (`gs_quant.instrument`)

```python
from gs_quant.instrument import IRSwap, IRCap, EqOption

swap = IRSwap('Pay', '10y', 'USD')      # pay_or_receive, termination, notional_currency
cap = IRCap('1y', 'USD')
option = EqOption('.SPX', '3m', 'ATMF', 'Call', 'European')
```

Instrument classes are auto-generated dataclasses in `gs_quant/target/instrument.py` (~90+ types: `IRSwap`, `IRSwaption`, `FXOption`, `FXForward`, `Bond`, `CommodOTCSwapLeg`, etc.), re-exported through `gs_quant.instrument`.

### Risk measures (`gs_quant.risk`) — requires a session

```python
from gs_quant.instrument import IRCap
from gs_quant.risk import IRDelta

cap = IRCap('1y', 'USD')
delta = cap.calc(IRDelta)   # dispatches through PricingContext -> GsSession.current
```

Common measures: `DollarPrice`, `IRDelta`, `EqDelta`, `Theta`, `Vega` (defined in `gs_quant/target/measures.py` and `gs_quant/risk/measures.py`).

### Markets / PricingContext — requires a session

```python
from gs_quant.markets import PricingContext

with PricingContext():
    price_f = cap.dollar_price()   # returns a future; resolved when the context exits
price = price_f.result()
```

`PricingContext` batches requests for efficiency but always dispatches through `GsSession.current` — there's no local pricing backend.

### Timeseries analytics — standalone-capable

```python
import pandas as pd
from gs_quant.timeseries.statistics import zscores, percentile
from gs_quant.timeseries.analysis import diff, smooth_outliers

prices = pd.Series(...)          # your own data, no GS session needed
z = zscores(prices)
d = diff(prices, obs=1)
```

### Backtesting (`gs_quant.backtests`) — requires a session for the pricing loop

```python
from gs_quant.backtests.generic_engine import GenericEngine
from gs_quant.backtests.strategy import Strategy

engine = GenericEngine()
result = engine.run_backtest(strategy, start=start_date, end=end_date, frequency='1m')
```

`GenericEngine.run_backtest` opens a `PricingContext` internally for each simulated valuation date, so even though you can supply your own historical trigger data via `gs_quant.backtests.data_sources`, the actual pricing/risk step in the loop still needs an authenticated `GsSession`.

### Data access (`gs_quant.data`) — requires a session

```python
from gs_quant.data import Dataset

ds = Dataset('EDRVOL_PERCENT_STANDARD')
df = ds.get_data(start=start_date, end=end_date, bbid='AAPL UW')
```

`Dataset` posts through `GsSession.current.sync.post(...)` — no session, no data.

## Layout of this vendored copy

```
gs-quant/
├── SKILL.md          (this file)
├── README.md          upstream README
├── LICENSE            Apache-2.0
├── NOTICE.txt          upstream NOTICE
├── setup.py, requirements.txt
└── src/gs_quant/       package source (test/ and content/ stripped)
    ├── instrument/, target/instrument.py   instrument definitions
    ├── risk/, target/measures.py           risk measure objects
    ├── markets/                             PricingContext, Portfolio
    ├── timeseries/                          analytics (standalone-capable submodules + GS-data measures)
    ├── backtests/                           Strategy/engine backtesting framework
    ├── data/                                Dataset, market data access
    └── session.py                           GsSession / authentication
```

For full API reference and tutorials, see [developer.gs.com/docs/gsquant](https://developer.gs.com/docs/gsquant/) — the upstream `content/` notebooks (not vendored here) live at `gs_quant/content/` in the original repo if deeper worked examples are needed.
