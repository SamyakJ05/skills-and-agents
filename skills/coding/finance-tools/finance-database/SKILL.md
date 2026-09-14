---
name: finance-database
description: Query the FinanceDatabase Python package to look up ticker/symbol metadata or screen Equities, ETFs, Funds, Indices, Currencies, Cryptocurrencies, and Money Markets by sector, industry, country, exchange, category, or free-text search. Use when a task needs to find symbols matching criteria (e.g. "insurance companies in the Netherlands", "fixed-income ETFs", "pension funds"), enumerate valid filter values for an asset class, or map a company/fund/index to its classification metadata. License: MIT.
---

# finance-database

Vendored from [JerBouma/FinanceDatabase](https://github.com/JerBouma/FinanceDatabase) (MIT, ~9.1k stars).
This is a reference for the package's Python API, not a data snapshot — the actual repo is
~5GB of CSV data (300,000+ symbols) which is intentionally **not** vendored here. The
`financedatabase/` folder in this skill contains only the small `.py` source files that
define the query interface, kept for reference. In practice, install the real package with
pip — it downloads/loads its own data at runtime — rather than importing from this folder.

## What it does

FinanceDatabase provides categorization metadata (not live prices/fundamentals) for:

- **Equities** (~112k) — sector, industry_group, industry, country, exchange, market, market_cap, isin, cusip, figi, etc.
- **ETFs** (~36k) — category_group, category, family (issuer), exchange
- **Funds** (~58k) — category_group, category, family, exchange
- **Indices** (~91k) — category_group, category, exchange
- **Currencies** (~2.5k), **Cryptocurrencies** (~3.4k), **Money Markets** (~1.4k)

The aim is to find *which* symbols exist matching some criteria — not to fetch OHLCV or
fundamentals (pair with `financetoolkit`/`yfinance` etc. for that, see `to_toolkit` below).

## Installation

```bash
pip install financedatabase -U
```

```python
import financedatabase as fd
```

Data is fetched/loaded lazily by the package itself when you instantiate a class — nothing
is bundled in this skill. First use of each asset class may take a moment to load its CSVs.

## Core API

Each asset class is a class with `.select()`, `.search()`, and `.show_options()`. Initialize
once per asset class and reuse the instance:

```python
equities = fd.Equities()
etfs = fd.ETFs()
funds = fd.Funds()
indices = fd.Indices()
currencies = fd.Currencies()
cryptos = fd.Cryptos()
moneymarkets = fd.Moneymarkets()
```

### `show_options` — discover valid filter values without loading full data

Module-level, for a quick peek without instantiating:

```python
fd.show_options("equities")
# -> {'currency': array([...]), 'sector': array([...]), 'industry_group': array([...])}
```

Or narrowed via an instance, optionally filtered by other columns:

```python
equities.show_options(country="Netherlands")
equities.show_options(selection="industry", sector="Financials", country="Netherlands")
# -> array(['Banks', 'Capital Markets', 'Consumer Finance', ...])
```

### `select` — filter the database by column values (exact match, category-style)

```python
equities.select(country="Netherlands", industry="Insurance")

# Narrow to one exchange/market to avoid duplicate listings of the same company:
equities.select(
    country="Netherlands",
    industry="Insurance",
    market="Euronext Amsterdam",
)

# only_primary_listing avoids duplicate cross-exchange listings (useful for US tickers):
equities.select(country="United States", industry="Insurance", only_primary_listing=True)

# Any parameter accepts a list for OR-matching:
equities.select(
    country=["Netherlands", "United States"],
    industry="Insurance",
    market=["Euronext Amsterdam", "New York Stock Exchange", "NASDAQ Global Select"],
)
```

ETFs/Funds/Indices use `category_group`/`category`/`family` instead of sector/industry:

```python
etfs.select(category_group="Fixed Income")
```

Cryptos use asset-specific params like `cryptocurrency`:

```python
cryptos.select(cryptocurrency="ETH")
```

### `search` — free-text substring search across any column

```python
equities.search(
    summary=["Robotics", "Education"],  # OR-matched substrings in the summary column
    industry_group="Equipment",
    market="Frankfurt",
    index=".F",  # filters the symbol/index column itself
)

funds.search(summary="Pension")
```

Search is case-insensitive by default; pass `case_sensitive=True` to change that.

### `to_toolkit` — hand results off to FinanceToolkit for actual financial data

FinanceDatabase results integrate directly with
[FinanceToolkit](https://github.com/JerBouma/FinanceToolkit) (a separate package) for
historical prices and 60+ financial ratios. Requires a free FinancialModelingPrep API key.

```python
API_KEY = "FINANCIAL_MODELING_PREP_API_KEY"

dutch_insurance = equities.select(
    country="Netherlands", industry="Insurance", market="Euronext Amsterdam",
)
toolkit = dutch_insurance.to_toolkit(api_key=API_KEY)

toolkit.get_historical_data()
toolkit.ratios.collect_all_ratios()
```

## Notes

- No data is vendored in this skill — everything above assumes `pip install financedatabase`
  and the package's own data loading at runtime. The `.py` files under `financedatabase/`
  here are for reference on the exact method signatures/behavior, not for import.
- Package source vendored: `Cryptos.py`, `Currencies.py`, `ETFs.py`, `Equities.py`,
  `Funds.py`, `Indices.py`, `Moneymarkets.py`, `helpers.py` (defines module-level
  `show_options`), `__init__.py`, and `validation/validate_identifiers.py`.
- Full README (with more examples and a Q&A section on data sourcing/freshness) is at
  `README.md` in this folder; `LICENSE` is the upstream MIT license.
