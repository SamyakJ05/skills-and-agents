---
name: finance-ai-assistant
description: Reference for building a conversational financial-research app on Valyu's DeepResearch API — TypeScript patterns for launching/polling long-running research tasks, parsing an agent's tool-call transcript (research/execute_code/createChart) into a renderable activity feed, structuring financial workflows as parameterized templates (IB/PE/hedge-fund/sales-intelligence domains), computing local financial ratios/metrics, and estimating research time/cost savings. Not a standalone financial-data library — the actual data retrieval and tool-calling agent run inside Valyu's hosted backend.
license: MIT
---

# Finance (yorkeccak/finance)

Vendored from [yorkeccak/finance](https://github.com/yorkeccak/finance) (MIT licensed, ~899 stars) — the open-source Next.js app behind [finance.valyu.ai](https://finance.valyu.ai), marketed as "Bloomberg-grade financial data behind a chat interface."

## Read this before using it: what this repo actually is

This is **not** a financial-data library or a set of MCP tool definitions you can call directly. It's a Next.js 15 chat/dashboard UI wrapping **Valyu's hosted DeepResearch API**. When a user asks a financial question, the app:

1. POSTs the query to Valyu's `/v1/deepresearch` (or workflow) endpoint via `@valyu/ai-sdk` / a thin REST client.
2. Valyu's own backend — a proprietary agent with its own `research`, `execute_code` (sandboxed Python via Daytona), and `createChart` tools — does the actual data retrieval, code execution, and charting. That agent's tool definitions, prompts, and financial data sources (SEC filings, market data, patents, academic papers, web search) are **not in this repository**; they live behind Valyu's API.
3. This app polls the task status and renders the resulting transcript (reasoning, tool calls, sources, charts, code output) in a chat/report UI.

Everything else in the upstream repo — Supabase auth/billing, Next.js pages, shadcn/ui components, PDF export via Puppeteer, Posthog analytics, Docker/Vercel deploy config — is app-specific SaaS infrastructure with no standalone reuse value, and is **not** vendored here.

## What's vendored (`vendor/`)

Only the framework-agnostic TypeScript modules with logic worth reading or reusing, none of which require Supabase, auth, or the rest of the Next.js app:

- **`lib/valyu-workflows.ts`** — REST client for Valyu's DeepResearch/Workflows API: `createDeepResearchTask()`, task polling, `ValyuError`/`valyuErrorStatus`/`isTransientValyuError` (the status endpoint throws intermittent 5xx *during* a run — these helpers distinguish "keep polling" from "actually failed"). Requires a Valyu API key or OAuth token; illustrates how to drive a long-running async research task from a web backend, not a generic financial API.
- **`lib/reports.ts`** (referenced by, not copied verbatim into `vendor/` — see note below) and the activity-parsing logic embedded in `valyu-workflows.ts` usage: `parseActivityFromMessages()` turns an agent's raw message transcript (`reasoning` / `text` / `tool-call` / `tool-result` parts) into typed `ActivityItem`s (`step` with sources, `code` with output, `chart` with image). This is the most broadly reusable pattern here — a template for rendering *any* AI SDK tool-calling transcript as a live activity feed, independent of Valyu.
- **`lib/domains.ts`** — the finance "vertical" taxonomy (Investment Banking/M&A, Private Equity/VC, Hedge Funds, Sales/GTM) and run-depth modes (`fast`/`standard`/`heavy`) used to organize workflow templates.
- **`lib/workflow-types.ts`** — `WorkflowDTO`/`WorkflowVariable` shapes and `normalizeWorkflow()`, showing how a workflow template's input form (text/textarea/number/date/enum fields) is derived from a raw catalog entry.
- **`lib/metrics-calculator.ts`** — pure local computation (no external calls) estimating "time saved" and "money saved" for a research session from message parts: sources analyzed, words processed, and a minutes/cost breakdown (source finding, reading, writing, chart/CSV creation, code execution) at an assumed $200/hr analyst rate. Useful as a template for this kind of ROI-framing metric, not as authoritative financial data.
- **`lib/deliverable-suggest.ts`** — heuristics that suggest which output artifacts (CSV, PDF, PPTX, DOCX) a query likely wants, based on keywords/intent.
- **`lib/csv-utils.ts`**, **`lib/markdown-utils.ts`**, **`lib/text-utils.ts`**, **`lib/citation-utils.ts`** — small formatting/parsing helpers (CSV generation from tabular tool output, markdown cleanup, citation-marker parsing/rendering) used to turn agent output into displayable content.
- **`example-reports/`** — four full captured DeepResearch runs (`investment-banking.json`, `private-equity.json`, `hedge-funds.json`, `sales-intelligence.json`, ~75-115KB each) plus `registry.ts`. These are real seeded example outputs shipped in the app as a "trust layer" (show output quality before spending a credit) — useful here as concrete, realistic examples of what a finished financial research report (with sources, activity trace, and prose) looks like end-to-end.

`README.md` and `LICENSE` (MIT, Copyright 2025 Valyu) are the upstream originals, kept as-is.

### Note on `lib/reports.ts`

The `parseActivityFromMessages()` function and `ReportDTO`/`ActivityItem` types actually live in `src/lib/reports.ts` upstream (not copied into `vendor/lib/` verbatim to avoid pulling in its Supabase-shaped `ReportDTO` fields). If you want the parser standalone, extract just `parseActivityFromMessages()` and the `ActivityItem` union from that file — the logic is transport-agnostic and works on any Vercel AI SDK-style message transcript with `reasoning`/`text`/`tool-call`/`tool-result` parts.

## How to use this

- **Building a similar "chat with financial data" product**: read `valyu-workflows.ts` for the async task lifecycle pattern (launch → poll with backoff → distinguish transient vs. terminal errors) and the activity-parsing pattern for rendering a tool-calling agent's transcript live. These patterns apply to any AI SDK-based agent (Valyu-backed or not).
- **Wanting actual financial data**: this skill won't give it to you — you need a Valyu API key (`platform.valyu.ai`) to hit the same backend this app calls, or pair this pattern with one of the sibling skills in `skills/coding/finance-tools/` (`finance-database`, `finance-toolkit-lib`, `finance-shashankvemuri`, `gs-quant`, `yfinance`, `financepy`) that vendor actual data-fetching/calculation libraries.
- **Wanting local financial ratio/metric math**: `metrics-calculator.ts` is a research-ROI estimator, not a financial-statement calculator — for real ratios/valuation models use `finance-toolkit-lib` instead.
- **Wanting workflow/prompt-template structuring ideas**: `domains.ts` + `workflow-types.ts` show a clean pattern for exposing a fixed catalog of parameterized "run this kind of analysis" templates (title, variables with types/validation, recommended depth, expected deliverables) to a UI — reusable as a design pattern regardless of what backend executes the workflow.

## Honest assessment

Of the ~899-star repo, the genuinely portable "library" surface is small: an async task client, a transcript-to-activity-feed parser, a workflow-template type system, and a handful of formatting helpers — a few hundred lines of real logic total. The advertised "institutional-grade financial data" and "advanced tool calling" (SEC filings search, market data, sandboxed Python execution, chart generation) are Valyu's proprietary hosted capabilities, not code in this repository. Treat this vendor drop as reference patterns for building a DeepResearch-style chat UI, not as a financial data or analysis toolkit in its own right.
