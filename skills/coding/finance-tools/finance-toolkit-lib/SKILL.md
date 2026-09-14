---
name: finance-toolkit-lib
description: Use when you need to compute financial ratios, valuation/credit-risk models (DCF, DuPont, WACC, Altman Z-Score, etc.), technical indicators, or risk/performance metrics (Sharpe, Sortino, VaR, CVaR, drawdowns, factor exposures) from company financial statement and market data in Python. Wraps the FinanceToolkit package (financetoolkit on PyPI) — pulls balance sheet/income/cash-flow statements and historical prices from Financial Modeling Prep or Yahoo Finance and exposes 500+ transparently-implemented formulas through a single `Toolkit` object.
license: MIT
---

# FinanceToolkit

Vendored from [JerBouma/FinanceToolkit](https://github.com/JerBouma/FinanceToolkit) (MIT licensed, ~5.3k stars). "Transparent and Efficient Financial Analysis" — an open-source Python package that turns raw financial statements and market data into 500+ ratios, indicators, and models, with every formula written out in plain, readable Python (no black-box calculations).

Distinct from the sibling skill `finance-toolkit` in this repo, which vendors a different project — do not confuse the two.

## What it does

Given one or more tickers, `FinanceToolkit` fetches (or accepts pre-loaded) balance sheet, income statement, cash flow statement, and historical price data, then computes:

- **Ratios** (`ratios` module, 80+): efficiency, liquidity, profitability, solvency, valuation — P/E, PEG, ROE/ROA/ROIC, current/quick ratio, debt-to-equity, EV multiples, and more, plus support for fully custom ratios.
- **Models** (`models` module, 10+): DuPont & Extended DuPont analysis, Weighted Average Cost of Capital (WACC), Economic Value Added (EVA), Altman Z-Score, Beneish M-Score, Piotroski F-Score, Graham Number, intrinsic/DCF-style valuation, enterprise value, growth models.
- **Technicals** (`technicals` module, 40+): moving averages, RSI, MACD, Bollinger Bands, Ichimoku Cloud, momentum/overlap/volatility/breadth indicators.
- **Risk** (`risk` module, 20+): Value at Risk (historical, Gaussian, Student-t, Cornish-Fisher, EVT/POT), Conditional VaR, Entropic VaR, GARCH/EWMA volatility, maximum drawdown & duration, Hurst exponent, copulas.
- **Performance** (`performance` module, 20+): Sharpe, Sortino, Calmar, Omega ratios, CAPM/beta, Fama-French factor correlations, correlation matrices, alpha/tracking error.
- **Options** (`options` module): Black-Scholes, binomial trees, implied volatility, and first/second/third-order Greeks (Delta, Gamma, Theta, Vega, Vanna, Charm, Vomma, Speed, Zomma, Color, Ultima).
- **Fixed Income** (`fixedincome` module): bond pricing, yield curves, Fed/ECB/Euribor rate series.
- **Economics** (`economics` module): macro indicators via FRED/OECD/Yahoo Finance.
- **Econometrics** (`econometrics` module): regression, causality, cointegration, panel data, time-series diagnostics.
- **Discovery** (standalone `Discovery` class): stock/crypto/forex/ETF screeners, sector/industry performance, news feeds — no financial statements needed.
- **Portfolio** (standalone `Portfolio` class): portfolio-level overview and performance from a holdings dataset.

Nearly every `get_*`/`collect_*` method across these modules supports `rolling=<n>` (sliding window), `trailing=<n>` (trailing sum/average, e.g. TTM), `growth=True` with `lag=<n>` (period-over-period or YoY growth), and `standardize=True` (Z-score normalization) — so a single metric call can become a time series, a growth series, or a comparably-scaled score with one extra kwarg.

## Installation

```bash
pip install financetoolkit -U
```

Requires an API key from [Financial Modeling Prep](https://www.jeroenbouma.com/fmp) for full financial-statement coverage (free tier: 250 requests/day, 5 years, US-listed only). Without a working FMP key, the toolkit automatically falls back to Yahoo Finance for historical price data (statement data is FMP-only); pass `enforce_source="FinancialModelingPrep"` or `enforce_source="YahooFinance"` to pin one source, either at `Toolkit(...)` init or per-call on `get_historical_data`, `get_treasury_data`, and the four statement getters.

## Core API: the `Toolkit` object

```python
from financetoolkit import Toolkit

companies = Toolkit(
    tickers=["AAPL", "MSFT"],
    api_key="FINANCIAL_MODELING_PREP_KEY",
    start_date="2017-12-31",
)
```

Key `Toolkit(...)` parameters (see `financetoolkit/toolkit_controller.py`): `tickers`, `api_key`, `start_date`/`end_date`, `quarterly` (annual vs. quarterly data), `use_cached_data` (bool or a cache directory path — the cache is incremental: widening the date range or adding a ticker only fetches what's missing), `risk_free_rate`, `benchmark_ticker` (defaults to `"SPY"`), `enforce_source`, and pre-loaded `historical`/`balance`/`income`/`cash` DataFrames if you want to skip the API entirely and supply your own data.

Each analysis domain is a property on the `Toolkit` instance, backed by a controller class:

| Property | Returns | Source file |
|---|---|---|
| `companies.ratios` | `Ratios` | `financetoolkit/ratios/ratios_controller.py` |
| `companies.models` | `Models` | `financetoolkit/models/models_controller.py` |
| `companies.technicals` | `Technicals` | `financetoolkit/technicals/technicals_controller.py` |
| `companies.risk` | `Risk` | `financetoolkit/risk/risk_controller.py` |
| `companies.performance` | `Performance` | `financetoolkit/performance/performance_controller.py` |
| `companies.options` | `Options` | `financetoolkit/options/options_controller.py` |
| `companies.fixedincome` | `FixedIncome` | `financetoolkit/fixedincome/fixedincome_controller.py` |
| `companies.economics` | `Economics` | `financetoolkit/economics/economics_controller.py` |
| `companies.econometrics` | `Econometrics` | `financetoolkit/econometrics/econometrics_controller.py` |

Plus two standalone top-level classes that don't need a `Toolkit` instance: `Discovery` (`financetoolkit/discovery/discovery_controller.py`) and `Portfolio` (`financetoolkit/portfolio/portfolio_controller.py`).

Every module has individual `get_<metric>()` methods (one formula) and one or more `collect_<category>()` methods (a whole category at once, e.g. `collect_profitability_ratios()`), returning `pandas` DataFrames indexed by ticker (or ticker × period).

## Usage examples (from upstream README)

Historical price data:
```python
historical_data = companies.get_historical_data()
historical_data.xs("AAPL", axis=1, level=1)
```

Financial statements:
```python
income_statement = companies.get_income_statement()   # or get_balance_sheet_statement(), get_cash_flow_statement()
income_statement.loc["AAPL"]
```

Ratios:
```python
profitability_ratios = companies.ratios.collect_profitability_ratios()
profitability_ratios.loc["MSFT"]
```

Models (Extended DuPont):
```python
extended_dupont_analysis = companies.models.get_extended_dupont_analysis()
extended_dupont_analysis.loc["AAPL"]
```

Options and Greeks:
```python
delta = companies.options.get_delta(expiration_time_range=180)
delta.loc["AAPL"]
```

Performance (Fama-French factor correlations, quarterly):
```python
factor_asset_correlations = companies.performance.get_factor_asset_correlations(period="quarterly")
factor_asset_correlations["AAPL"]
```

Risk (weekly Value at Risk):
```python
companies.risk.get_value_at_risk(period="weekly")
```

Technicals (Ichimoku Cloud):
```python
ichimoku_cloud = companies.technicals.get_ichimoku_cloud()
ichimoku_cloud.loc["AAPL"]
```

Discovery (standalone, no tickers/statements required):
```python
from financetoolkit import Discovery

discovery = Discovery(api_key="FINANCIAL_MODELING_PREP_KEY")
discovery.get_stock_screener(
    market_cap_higher=1_000_000,
    price_higher=100,
    price_lower=200,
    beta_higher=1,
    beta_lower=1.5,
    dividend_higher=1,
)
```

## Vendored source layout

`financetoolkit/` in this skill directory is the actual upstream package source (copied as-is, minus the `mcp_server/` subpackage, which wraps the toolkit as an MCP server and isn't needed to use the library directly in code). Notable files:

- `toolkit_controller.py` — the `Toolkit` class itself (init, property accessors for each module, financial-statement fetch/normalize logic).
- `ratios/`, `models/`, `technicals/`, `risk/`, `performance/`, `options/`, `economics/`, `fixedincome/`, `econometrics/` — one `<name>_controller.py` (the public methods) plus one or more `<topic>_model.py` files (the actual formulas, fully readable — e.g. `ratios/valuation_model.py` for every valuation ratio's exact calculation) per module.
- `discovery/`, `portfolio/` — the standalone `Discovery` and `Portfolio` classes and their model files.
- `normalization/` — CSV mapping tables used to normalize raw FMP/Yahoo Finance statement line items into the toolkit's canonical field names.
- `cache/` — the incremental on-disk caching layer used by `use_cached_data`.
- `fmp_model.py`, `yfinance_model.py`, `historical_model.py`, `fundamentals_model.py`, `currencies_model.py`, `helpers.py` — data-fetching and shared utility helpers.
- `utilities/` — logging, error handling, request retries, dataframe helpers.

Import from the package root exactly as upstream does — `from financetoolkit import Toolkit, Discovery, Portfolio, Economics, FixedIncome` — since `financetoolkit/__init__.py` re-exports these directly; everything else (ratios, models, technicals, risk, performance, options, econometrics) is reached only through a `Toolkit` instance's properties, not imported standalone.

`README.md` (upstream, kept as-is) has the full walkthrough with more worked examples per module and expected DataFrame output shapes. `LICENSE.txt` is the original MIT license — preserve it in any redistribution.

## Notes

- This is a code library, not a CLI — use it by writing/running Python that imports `financetoolkit`.
- Full API documentation (every one of the 500+ methods with formulas and parameters) lives at https://www.jeroenbouma.com/projects/financetoolkit/docs — not reproduced here; read the relevant `_model.py` source file in this skill directory for the exact formula instead.
- Financial-statement fetching requires network access and (for full coverage) a paid or free-tier FMP API key; historical price data alone works via the Yahoo Finance fallback with no key.
- Companion project: [FinanceDatabase](https://github.com/JerBouma/FinanceDatabase) (300,000+ symbols) pairs well with this for ticker discovery, feeding results into `Toolkit(tickers=...)`.
