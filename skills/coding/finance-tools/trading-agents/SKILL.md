---
name: trading-agents
description: Multi-agent LLM-driven trading analysis and decision framework (TauricResearch/TradingAgents, Apache-2.0). Simulates a trading firm — fundamentals/sentiment/news/technical analysts, bull-vs-bear researcher debate, a trader, a risk-management team (aggressive/conservative/neutral debators), and a portfolio manager — to research a ticker and produce a BUY/SELL/HOLD decision with reasoning. Use when asked to do multi-agent stock/crypto analysis, simulate an investment committee or trading-desk debate, build an LLM trading pipeline, or evaluate a ticker with structured analyst reports and risk review.
license: Apache-2.0
---

# TradingAgents

Multi-agent LLM framework that mirrors a real trading firm's org chart to
analyze a ticker and reach a trading decision through structured debate.
Vendored from [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
(~105k GitHub stars), built on LangGraph. Research tool only — **not
financial, investment, or trading advice**; performance depends heavily on
the chosen LLMs, prompts, and data quality.

## What it does

Given a ticker and an analysis date, `TradingAgentsGraph.propagate(ticker, date)`
runs a LangGraph pipeline of role-specialized LLM agents that each read and
write into a shared state, culminating in a final trade decision:

1. **Analyst team** (parallel, tool-using agents that pull real market data):
   - `fundamentals_analyst` — company financials, balance sheet, income
     statement, cash flow, insider transactions; flags intrinsic value and red flags.
   - `market_analyst` — technical indicators (MACD, RSI, moving averages, etc.)
     via `stockstats`, grounded in a verified OHLCV snapshot.
   - `news_analyst` — global/macro news and event impact (also pulls FRED
     macro indicators and Polymarket prediction-market data).
   - `sentiment_analyst` / `social_media_analyst` — aggregates StockTwits,
     Reddit, and news headlines into a short-term sentiment read.
2. **Researcher team** — `bull_researcher` vs `bear_researcher` debate the
   analyst reports for `max_debate_rounds` rounds, arguing opposing theses;
   a `research_manager` synthesizes the debate into an investment plan.
3. **Trader** (`agents/trader/trader.py`) — turns the investment plan into a
   concrete trade proposal (timing, direction, sizing rationale).
4. **Risk management team** — `aggressive_debator`, `conservative_debator`,
   and `neutral_debator` critique the trade proposal from different risk
   postures over `max_risk_discuss_rounds` rounds.
5. **Portfolio manager** (`agents/managers/portfolio_manager.py`) — approves
   or rejects the final proposal; on approval this becomes the returned
   decision (BUY/SELL/HOLD plus reasoning).

The graph, conditional routing between debate rounds, and state schema live
under `tradingagents/graph/` (`setup.py`, `conditional_logic.py`,
`propagation.py`, `signal_processing.py`, `reflection.py`, `checkpointer.py`,
`trading_graph.py` — the orchestrating `TradingAgentsGraph` class).

### Persistence

- **Decision log** (always on): each run appends its decision to
  `~/.tradingagents/memory/trading_memory.md`. On a later run for the same
  ticker, the framework fetches realized return (raw + alpha vs. a benchmark
  like SPY), writes a one-paragraph reflection, and injects recent
  same-ticker and cross-ticker lessons into the Portfolio Manager's prompt —
  so judgment compounds across runs. Override path via
  `TRADINGAGENTS_MEMORY_LOG_PATH`.
- **Checkpoint/resume** (opt-in, `checkpoint_enabled` / `--checkpoint`):
  LangGraph persists state per node to a per-ticker SQLite DB under
  `~/.tradingagents/cache/checkpoints/<TICKER>.db`, so an interrupted run
  resumes instead of restarting. `--clear-checkpoints` resets them.

## Installation

```bash
cd tradingagents  # this skill's vendored package root
pip install .
# or: pip install -r requirements.txt
```

Requires Python >= 3.10. Built on `langgraph`, `langchain-*` provider
integrations, `yfinance`, `stockstats`, `pandas`, `typer`/`questionary`/`rich`
(for the CLI), and `redis`/`backtrader` as supporting deps (see
`pyproject.toml` / `requirements.txt`).

### API keys — pick an LLM provider (required) and, optionally, data vendors

The framework needs **one LLM provider key** at minimum. Set it as an
environment variable (or copy `.env.example` to `.env`):

```bash
export OPENAI_API_KEY=...          # OpenAI (GPT) — default provider
export ANTHROPIC_API_KEY=...       # Anthropic (Claude)
export GOOGLE_API_KEY=...          # Google (Gemini)
export XAI_API_KEY=...             # xAI (Grok)
export DEEPSEEK_API_KEY=...        # DeepSeek
export DASHSCOPE_API_KEY=...       # Qwen (international)
export ZHIPU_API_KEY=...           # GLM via Z.AI
export MINIMAX_API_KEY=...         # MiniMax
export OPENROUTER_API_KEY=...      # OpenRouter (many models via one key)
```

Also supported: **AWS Bedrock** (`pip install ".[bedrock]"`, AWS creds via
env/`~/.aws/credentials`/IAM role, `llm_provider: "bedrock"`), **Azure
OpenAI** (`.env.enterprise.example` → `.env.enterprise`), **local models**
via **Ollama** (`llm_provider: "ollama"`, default `http://localhost:11434/v1`),
and **any OpenAI-compatible endpoint** (vLLM, LM Studio, llama.cpp) via
`llm_provider: "openai_compatible"` + `backend_url`.

Data defaults to **Yahoo Finance** (`yfinance`, keyless) for stock/technical/
fundamental/news data. Optional data vendors, set in `data_vendors` config or
via key:

```bash
export ALPHA_VANTAGE_API_KEY=...   # richer fundamentals/indicators/news (alt. to yfinance)
# FRED (macro indicators) and Polymarket (prediction markets) need no key
# beyond FRED_API_KEY for FRED: export FRED_API_KEY=...
```

Markets: any ticker Yahoo Finance covers, with exchange suffix — `AAPL`,
`0700.HK`, `7203.T`, `AZN.L`, `RELIANCE.NS`, `600519.SS` (Shanghai),
`BTC-USD` (crypto), etc. The alpha benchmark (e.g. SPY, Nikkei 225, Hang
Seng) is auto-selected per market via `benchmark_map` in `default_config.py`.

## Usage

### CLI (interactive)

```bash
tradingagents          # installed entry point
python -m cli.main      # or run directly from source (cli/main.py)
```

Walks through ticker, analysis date, LLM provider/models, and research depth
(debate rounds) interactively, then streams each agent's output as it runs.

### Python API

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())
_, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)
```

Custom configuration (provider, models, debate depth, checkpointing):

```python
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "openai"          # openai, anthropic, google, deepseek,
                                            # openrouter, ollama, bedrock,
                                            # openai_compatible, ...
config["deep_think_llm"] = "gpt-5.6"       # complex reasoning (researchers, PM)
config["quick_think_llm"] = "gpt-5.6-luna" # fast/cheap tasks (analysts)
config["max_debate_rounds"] = 2            # bull/bear researcher rounds
config["max_risk_discuss_rounds"] = 2       # risk-team rounds
config["checkpoint_enabled"] = True         # resume interrupted runs
config["temperature"] = 0.0                 # lower = more reproducible (non-reasoning models only)

ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate("NVDA", "2026-01-15")
```

See `tradingagents/default_config.py` for every option (news lookback
windows, data-vendor routing per tool category, memory log rotation,
per-provider reasoning-effort/thinking-level knobs, etc.).

### Reproducibility caveat

LLM sampling is non-deterministic (more so for reasoning models, which
mostly ignore `temperature`), and live news/social data changes run to run
even for the same historical date. Pinning the analysis date fixes price and
indicator data but not news/sentiment freshness. Treat this as a research
scaffold for studying multi-agent analysis, not a strategy with a fixed,
replicable return.

## Source layout (vendored)

```
tradingagents/
  agents/
    analysts/          fundamentals_analyst, market_analyst, news_analyst,
                        sentiment_analyst, social_media_analyst
    researchers/        bull_researcher, bear_researcher
    managers/            research_manager (synthesizes debate), portfolio_manager (final call)
    risk_mgmt/          aggressive_debator, conservative_debator, neutral_debator
    trader/trader.py    turns investment plan into a trade proposal
    utils/               shared tool bindings (stock/fundamental/news/macro/
                         technical-indicator/prediction-market data tools),
                         agent_states.py (LangGraph state schema), memory.py
                         (decision log), schemas.py, structured.py, rating.py
  graph/
    trading_graph.py    TradingAgentsGraph orchestrator class
    setup.py            builds the LangGraph graph (nodes + edges)
    conditional_logic.py routing between debate/risk rounds
    propagation.py       Propagator — runs a ticker+date through the graph
    reflection.py        Reflector — post-hoc alpha/return reflection for memory log
    signal_processing.py extracts the final BUY/SELL/HOLD signal
    checkpointer.py      SQLite-backed LangGraph checkpoint/resume
  llm_clients/          per-provider chat clients (openai, anthropic, google,
                        azure, bedrock) + factory.py, model_catalog.py, capabilities.py
  dataflows/            data-vendor integrations: y_finance.py, yfinance_news.py,
                        alpha_vantage*.py, fred.py, polymarket.py, reddit.py,
                        stocktwits.py, stockstats_utils.py, market_data_validator.py
  default_config.py     DEFAULT_CONFIG dict + TRADINGAGENTS_* env-var overrides
  reporting.py          writes per-run report tree to results_dir
cli/                    Typer/questionary/rich interactive CLI (main.py, config.py, models.py)
main.py                 minimal script-style entry point (see README Python Usage)
pyproject.toml, requirements.txt
.env.example, .env.enterprise.example
CHANGELOG.md
LICENSE                 Apache-2.0 (original TauricResearch license, preserved as-is)
README.md               original upstream README (preserved as-is)
```

Not vendored (available upstream if needed): `tests/` (extensive pytest
suite), `assets/` (README screenshots/diagrams, ~3.6 MB of PNGs),
`.github/` CI workflows, `Dockerfile`/`docker-compose.yml`, `scripts/`.

## Citation

```
@misc{xiao2025tradingagentsmultiagentsllmfinancial,
      title={TradingAgents: Multi-Agents LLM Financial Trading Framework},
      author={Yijia Xiao and Edward Sun and Di Luo and Wei Wang},
      year={2025},
      eprint={2412.20138},
      archivePrefix={arXiv},
      primaryClass={q-fin.TR},
      url={https://arxiv.org/abs/2412.20138},
}
```
