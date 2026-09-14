---
name: yfinance
description: Download market data from Yahoo Finance's unofficial API. Use for pulling historical OHLCV price data, real-time/delayed quotes, fundamentals (balance sheet, income statement, cash flow), dividends and stock splits, options chains, analyst estimates, earnings calendars, holders data, and news for stocks, ETFs, indices, currencies, and cryptocurrencies via Python's `yfinance` package (`yf.Ticker`, `yf.Tickers`, `yf.download`).
license: Apache-2.0
---

# yfinance

Vendored from [ranaroussi/yfinance](https://github.com/ranaroussi/yfinance) (Apache-2.0, ~25k stars). Source lives in `yfinance/` (the core package). The `tests/`, `doc/` (Sphinx docs site + notebooks), and CI/config files were stripped to keep this skill lean — none are needed to use the library.

## What it is

**yfinance** offers a Pythonic way to fetch financial and market data from Yahoo! Finance. It is an open-source community project — **not affiliated with, endorsed by, or vetted by Yahoo, Inc.** It scrapes/calls Yahoo's public (unofficial) endpoints, which Yahoo can change or rate-limit without notice. Yahoo's terms of use say the data is for personal use only — read them before using this in anything commercial.

Main components:

- `Ticker` — all data for a single ticker (price history, financials, options, holders, news, etc.)
- `Tickers` — a convenience wrapper for multiple `Ticker` objects
- `download()` — bulk historical price download for one or many tickers into a single DataFrame
- `Market` — market summary/status info
- `Search` — search Yahoo Finance (quotes + news)
- `Sector` / `Industry` — sector and industry classification data
- `EquityQuery` / `Screener` — build and run a market screener query
- `WebSocket` / `AsyncWebSocket` (`ticker.live()`) — live streaming quote data

## Installation

```bash
pip install yfinance
```

Requires Python 3.9+. `yfinance` depends on `curl_cffi` (to impersonate a browser TLS fingerprint, needed to avoid Yahoo blocking plain `requests` traffic), `pandas`, `numpy`, `requests`, `beautifulsoup4`, `platformdirs`, `pytz`, `frozendict`, `peewee`, `protobuf`, and `websockets`. To install without `curl_cffi` (fallback to plain `requests`, less resilient to blocking):

```bash
curl -fsSL https://raw.githubusercontent.com/ranaroussi/yfinance/main/requirements.txt | grep -vi '^curl_cffi' | pip install -r /dev/stdin
pip install --no-deps yfinance
```

Treat the vendored `yfinance/` folder here as reference source to read/search — install the real package from PyPI to actually run code.

## Key API

### `Ticker` — single-symbol data

```python
import yfinance as yf

dat = yf.Ticker("MSFT")

# historical market data (OHLCV)
dat.history(period="1mo")            # period: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
dat.history(start="2023-01-01", end="2023-06-01", interval="1d")

# options
dat.options                          # tuple of expiration dates
chain = dat.option_chain(dat.options[0])
chain.calls
chain.puts

# fundamentals / financial statements
dat.balance_sheet
dat.quarterly_income_stmt
dat.cashflow
dat.quarterly_cashflow

# corporate actions
dat.dividends
dat.splits
dat.actions

# dates / calendar (next earnings date, ex-dividend date, etc.)
dat.calendar

# general company/quote info
dat.info

# analyst data
dat.analyst_price_targets
dat.recommendations
dat.earnings_estimate

# holders
dat.major_holders
dat.institutional_holders

# news
dat.news

# live streaming quotes (websocket)
dat.live()
```

### `download()` — bulk historical prices for multiple tickers

```python
import yfinance as yf

data = yf.download("SPY AAPL", period="1mo")
data = yf.download(
    tickers="SPY AAPL MSFT",
    start="2023-01-01", end="2023-12-31",
    interval="1d",          # 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    group_by="column",      # or "ticker"
    auto_adjust=True,       # adjust OHLC for splits/dividends
    actions=False,          # include dividends/splits columns
    threads=True,           # parallelize per-ticker requests
    repair=False,           # attempt to fix known Yahoo data errors (100x unit mixups, bad div/split adjustments)
)
```

Notes: intraday intervals (anything under `1d`) cannot extend more than the last 60 days. `30m` bars are fetched as `15m` and resampled client-side to work around a Yahoo API bug.

### `Tickers` — convenience wrapper for multiple tickers

```python
import yfinance as yf

tickers = yf.Tickers("msft aapl goog")
tickers.tickers["MSFT"].info
tickers.tickers["AAPL"].history(period="1mo")
tickers.tickers["GOOG"].actions
tickers.live()
```

### Other entry points

```python
# search
yf.Search("Apple").quotes

# sector / industry
yf.Sector("technology").top_companies
yf.Industry("semiconductors").top_companies

# market status
yf.Market("US").status

# screener
from yfinance import EquityQuery, screener
q = EquityQuery("gt", ["intradaymarketcap", 2_000_000_000_000])
screener.screen(q)
```

## Rate limiting and caching

Yahoo's endpoints are **unofficial and rate-limited**; hammering them (especially with `threads=True` across many tickers, or in a loop with no delay) commonly triggers HTTP 429 responses. yfinance raises `yfinance.exceptions.YFRateLimitError` when Yahoo returns 429 on the crumb/auth flow, and its internal `data.py` HTTP layer also detects 429 on regular requests. There is no automatic backoff/retry built in beyond crumb-refresh handling — callers should add their own retry/backoff and avoid excessive concurrent requests, or pass a shared `requests`/`curl_cffi` `session` (with e.g. `requests_cache` or `requests_ratelimiter`) to `Ticker(ticker, session=...)` / `download(..., session=...)` to throttle and cache calls.

Separately, yfinance keeps a small **persistent local cache** (independent of the above) for timezone lookups and auth cookies, to cut down on repeated requests:

- Windows: `C:/Users/<USER>/AppData/Local/py-yfinance`
- Linux: `/home/<USER>/.cache/py-yfinance`
- macOS: `/Users/<USER>/Library/Caches/py-yfinance`

Redirect it with:

```python
import yfinance as yf
yf.set_tz_cache_location("custom/cache/location")
```

## Source layout

```
yfinance/
  __init__.py        # public API surface (Ticker, Tickers, download, Search, Sector, Industry, Market, EquityQuery, Screener, ...)
  ticker.py           # Ticker class (thin wrapper around TickerBase)
  base.py             # TickerBase — the bulk of per-ticker data-fetching logic
  tickers.py          # Tickers — multi-ticker convenience wrapper
  multi.py            # download() — bulk multi-ticker historical price download
  data.py             # low-level HTTP client: crumb/cookie auth, request signing, 429 handling
  _http.py            # HTTP session helpers (curl_cffi / requests)
  cache.py            # persistent tz/cookie cache (peewee-backed sqlite)
  calendars.py         # trading calendar / market hours utilities
  config.py           # module-level configuration
  const.py             # constants: valid periods/intervals, market/exchange metadata
  exceptions.py        # YFException, YFRateLimitError, YFTickerMissingError, etc.
  live.py              # WebSocket / AsyncWebSocket live quote streaming
  lookup.py            # symbol lookup
  search.py            # Search — Yahoo Finance search (quotes + news)
  shared.py             # shared module-level state (e.g. error tracking across threaded downloads)
  utils.py              # shared utilities (date/tz handling, data parsing, decorators)
  version.py            # package version string
  scrapers/
    analysis.py         # analyst estimates, price targets, growth/revenue estimates
    fundamentals.py     # financial statements dispatch (balance sheet, income, cash flow)
    funds.py            # mutual fund / ETF specific data
    history.py          # OHLCV price history fetching + price-repair logic (largest file, ~189KB)
    holders.py           # major/institutional/mutualfund holders, insider transactions
    quote.py             # `.info`, fast_info, and quote-summary parsing (~39KB)
  domain/
    domain.py            # base classes for Sector/Industry
    sector.py, industry.py, market.py   # Sector, Industry, Market domain objects
  screener/
    query.py             # EquityQuery / FundQuery builders
    screener.py          # screen() — run a query against Yahoo's screener endpoint
```

`LICENSE.txt` and `README.md` are vendored as-is at the skill root.
