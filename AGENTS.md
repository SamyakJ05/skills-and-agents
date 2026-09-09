# AGENTS.md

Agent-agnostic index of vendored skills and subagents in this repo. Codex, OpenCode, and other AGENTS.md-aware harnesses should read this file to discover available skills/agents. Claude Code users: see `.claude/skills/` and `.claude/agents/` (generated from the same sources — do not edit directly).

Regenerate after changes: `python3 scripts/build-adapters.py`


## Design skills

- **antislop** (`skills/design/anti-slop/antislop`) — Anti Slop: Rules for AI Coding Agents. The core filter. Load always to stop generic AI slop.
- **antislop-code** (`skills/design/anti-slop/antislop-code`) — Code comment hygiene for AI coding agents: remove generic AI-slop comments, keep the valuable ones, never touch the code.
- **antislop-copywriting** (`skills/design/anti-slop/antislop-copywriting`) — Copy and text skill for antislop. Use when writing or editing prose: headlines, tone, CTAs, and anti-AI-writing patterns. Load with the core.
- **antislop-human** (`skills/design/anti-slop/antislop-human`) — Human and accessibility skill for antislop. Contrast, keyboard, focus, and states for real people. Includes the contrast checker.
- **antislop-layoutmobile** (`skills/design/anti-slop/antislop-layoutmobile`) — Mobile layout skill for antislop. Use for layouts that reflow on small screens: grids, overflow, tap targets. Load with the core.
- **antislop-ui** (`skills/design/anti-slop/antislop-ui`) — UI and visual skill for antislop. Use when building or editing any interface: color, layout, components, motion. Load with the core.
- **baoyu-design** (`skills/design/baoyu-design`) — Create polished design artifacts as self-contained HTML: UI mockups, interactive prototypes, wireframes, landing pages, dashboards, app screens, mobile apps, sl
- **animate** (`skills/design/emilkowalski/animate`) — Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose, which tool, 
- **animate-expo** (`skills/design/emilkowalski/animate-expo`) — Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it animate, which thread it runs o
- **animation-vocabulary** (`skills/design/emilkowalski/animation-vocabulary`) — Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens" → Pop in
- **apple-design** (`skills/design/emilkowalski/apple-design`) — Apple's approach to interface design and fluid, physical motion, translated for the web. Use when building or reviewing gesture-driven UI, spring animations, dr
- **ask-sonner** (`skills/design/emilkowalski/ask-sonner`) — Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading toasts, updating, dismissing and pe
- **emil-design-eng** (`skills/design/emilkowalski/emil-design-eng`) — This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great.
- **find-animation-opportunities** (`skills/design/emilkowalski/find-animation-opportunities`) — Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. Read-only; it proposes motion with exact values, it does
- **improve-animations** (`skills/design/emilkowalski/improve-animations`) — Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans for other age
- **pick-ui-library** (`skills/design/emilkowalski/pick-ui-library`) — Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus, virtualization, drag and drop, t
- **prototype** (`skills/design/emilkowalski/prototype`) — Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through them live and promote the one th
- **review-animations** (`skills/design/emilkowalski/review-animations`) — Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; approval is earned.
- **write-swift** (`skills/design/emilkowalski/write-swift`) — How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent, main-actor-by-default, actors, t
- **hue** (`skills/design/hue`) — Meta-skill that generates new design language skills. Works on Claude Code and Codex. Use when the user says 'create a design skill', 'generate design language'
- **impeccable** (`skills/design/impeccable`) — Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, extract, or otherwise
- **nothing-design** (`skills/design/nothing-design`) — This skill should be used when the user explicitly says "Nothing style", "Nothing design", "/nothing-design", or directly asks to use/apply the Nothing design s
- **ss-a11y** (`skills/design/styleseed/ss-a11y`) — Audit a component or page for accessibility issues and fix them
- **ss-audit** (`skills/design/styleseed/ss-audit`) — Audit screens for UX issues using Nielsen's heuristics and modern mobile UX best practices
- **ss-build** (`skills/design/styleseed/ss-build`) — Build a screen with StyleSeed's composed design method — choose or compile an output grammar, apply a brand recipe plus domain/page/profile/lock constraints, th
- **ss-component** (`skills/design/styleseed/ss-component`) — Generate a new UI component following the StyleSeed design conventions
- **ss-copy** (`skills/design/styleseed/ss-copy`) — Generate UX microcopy (button labels, error messages, empty states, toasts) following a casual-but-polite voice and tone
- **ss-dial** (`skills/design/styleseed/ss-dial`) — Turn ONE design axis up or down as a coordinated, deterministic transform — "denser", "sharper corners", "more muted", "bolder", "flatter", "livelier". Not a vi
- **ss-feedback** (`skills/design/styleseed/ss-feedback`) — Add appropriate user feedback states (loading, success, error, empty) to a component or page
- **ss-flow** (`skills/design/styleseed/ss-flow`) — Design user flows and navigation structure following proven UX patterns
- **ss-lint** (`skills/design/styleseed/ss-lint`) — Quick automated lint — detects common design system violations in seconds
- **ss-motion** (`skills/design/styleseed/ss-motion`) — Apply a named StyleSeed motion to a component — either one of the 5 personality seeds (Spring/Silk/Snap/Float/Pulse × entrance/exit/hover/press/layout) or a dis
- **ss-page** (`skills/design/styleseed/ss-page`) — Scaffold a new product page or screen from the compiled StyleSeed output grammar, surface adapter, brand recipe, and project lock.
- **ss-pattern** (`skills/design/styleseed/ss-pattern`) — Generate a composed UI pattern from the active StyleSeed grammar and brand recipe using existing primitives.
- **ss-reference** (`skills/design/styleseed/ss-reference`) — Compile screenshots, URLs, Figma exports, or an existing UI into a project-local StyleSeed output grammar with evidence, tokens, confidence, anti-patterns, and 
- **ss-resolve** (`skills/design/styleseed/ss-resolve`) — Compile a small, deterministic StyleSeed rule bundle for one agent, output grammar, surface adapter, domain, page type, brand recipe, palette recipe, and option
- **ss-restyle** (`skills/design/styleseed/ss-restyle`) — Apply one optional StyleSeed aesthetic profile without changing the selected output grammar, product job, or core design judgment.
- **ss-review** (`skills/design/styleseed/ss-review`) — Review UI code for design system compliance, accessibility, and best practices
- **ss-score** (`skills/design/styleseed/ss-score`) — Score a visual artifact's implementation quality 0-100 against its composed StyleSeed rule set — category breakdown, evidence, and prioritized fixes.
- **ss-setup** (`skills/design/styleseed/ss-setup`) — Configure StyleSeed by selecting the output grammar, domain, page type, brand recipe, semantic palette recipe, optional aesthetic profile, and bounded brand tok
- **ss-studio** (`skills/design/styleseed/ss-studio`) — Turn a product brief and optional references into three distinct creative directions, a human-selected StyleSeed interaction plan, generated image/video asset j
- **ss-tokens** (`skills/design/styleseed/ss-tokens`) — Generate an accessible semantic palette from a key color, or view, add, and modify StyleSeed design tokens. Use when a user supplies a brand color, asks which c
- **ss-update** (`skills/design/styleseed/ss-update`) — Check and update an existing StyleSeed installation by exact rule/skill revision, preserve project-owned design decisions, then recompile and verify the effecti
- **ss-verify** (`skills/design/styleseed/ss-verify`) — The VISUAL gate — render a UI or visual artifact through its surface adapter, inspect the actual pixels, then fix and re-render until it passes the composed Sty
- **styleseed** (`skills/design/styleseed/styleseed`) — Route a StyleSeed request to exactly one first workflow after resolving the current artifact boundary. Use when the user asks generally for StyleSeed help rathe
- **superdesign** (`skills/design/superdesign`) — Design or redesign frontend UI, presentations, and graphics on the Superdesign canvas with a choice of leading AI models. Use whenever the user wants to design 
- **brandkit** (`skills/design/taste-skill/brandkit`) — Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. Trained fo
- **industrial-brutalist-ui** (`skills/design/taste-skill/brutalist-skill`) — Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog 
- **gpt-taste** (`skills/design/taste-skill/gpt-tasteskill`) — Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial typograph
- **image-to-code** (`skills/design/taste-skill/image-to-code-skill`) — Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then impl
- **imagegen-frontend-mobile** (`skills/design/taste-skill/imagegen-frontend-mobile`) — Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile product
- **imagegen-frontend-web** (`skills/design/taste-skill/imagegen-frontend-web`) — Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizontal
- **minimalist-ui** (`skills/design/taste-skill/minimalist-skill`) — Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows.
- **full-output-enforcement** (`skills/design/taste-skill/output-skill`) — Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any ta
- **redesign-existing-projects** (`skills/design/taste-skill/redesign-skill`) — Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without bre
- **high-end-visual-design** (`skills/design/taste-skill/soft-skill`) — Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. 
- **stitch-design-taste** (`skills/design/taste-skill/stitch-skill`) — Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, ca
- **design-taste-frontend** (`skills/design/taste-skill/taste-skill`) — Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that d
- **design-taste-frontend-v1** (`skills/design/taste-skill/taste-skill-v1`) — The original v1 taste-skill, preserved for projects depending on its exact behavior. The current default is `design-taste-frontend` (v2 experimental), which is 
- **banner-design** (`skills/design/ui-ux-pro-max/banner-design`) — Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with optional generated or supplied visuals. Ac
- **brand** (`skills/design/ui-ux-pro-max/brand`) — Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, marketing assets, brand co
- **design** (`skills/design/ui-ux-pro-max/design`) — Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini, Atlas Cloud, or MuAPI AI), corporate identity program
- **design-system** (`skills/design/ui-ux-pro-max/design-system`) — Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS variables, spacing/typography scales,
- **slides** (`skills/design/ui-ux-pro-max/slides`) — Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies.
- **ui-styling** (`skills/design/ui-ux-pro-max/ui-styling`) — Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visu
- **ui-ux-pro-max** (`skills/design/ui-ux-pro-max/ui-ux-pro-max`) — UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building, reviewing, or fixing interfaces, including pages, co

## Coding skills

_(none yet — coding assistance here is via subagents below)_

## Coding subagents

| Name | Source | Tools | Model | Description |
|---|---|---|---|---|
| `api-designer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when designing new APIs, creating API specifications, or refactoring existing API architecture for scalability and developer  |
| `backend-developer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when building server-side APIs, microservices, and backend systems that require robust architecture, scalability planning, an |
| `design-bridge` | voltagent | Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch | inherit | Use this agent when you need to translate a DESIGN.md from the VoltAgent/awesome-design-md repository into polished Claude Code instructions |
| `electron-pro` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when building Electron desktop applications that require native OS integration, cross-platform distribution, security hardeni |
| `frontend-developer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building complete frontend applications across React, Vue, and Angular frameworks requiring multi-framework expertise and full-stac |
| `fullstack-developer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to build complete features spanning database, API, and frontend layers together as a cohesive unit. |
| `graphql-architect` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use this agent when designing or evolving GraphQL schemas across microservices, implementing federation architectures, or optimizing query p |
| `microservices-architect` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use when designing distributed system architecture, decomposing monolithic applications into independent microservices, or establishing comm |
| `mobile-developer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when building cross-platform mobile applications requiring native performance optimization, platform-specific features, and o |
| `ui-designer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when designing visual interfaces, creating design systems, building component libraries, or refining user-facing aesthetics r |
| `websocket-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when implementing real-time bidirectional communication features using WebSockets, Socket.IO, or similar technologies at scal |
| `angular-architect` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when architecting enterprise Angular 15+ applications with complex state management, optimizing RxJS patterns, designing micro-frontend  |
| `cpp-pro` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when building high-performance C++ systems requiring modern C++20/23 features, template metaprogramming, or zero-overhead abs |
| `csharp-developer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when building ASP.NET Core web APIs, cloud-native .NET solutions, or modern C# applications requiring async patterns, depende |
| `django-developer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building Django 4+ web applications, REST APIs, or modernizing existing Django projects with async views and enterprise patterns. |
| `dotnet-core-expert` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building .NET Core applications requiring cloud-native architecture, high-performance microservices, modern C# patterns, or cross-p |
| `dotnet-framework-4.8-expert` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when working on legacy .NET Framework 4.8 enterprise applications that require maintenance, modernization, or integration wit |
| `elixir-expert` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to build fault-tolerant, concurrent systems leveraging OTP patterns, GenServer architectures, and Phoenix frame |
| `expo-react-native-expert` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building mobile applications with Expo and React Native that require native module integration, navigation setup, performant animat |
| `fastapi-developer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building modern async Python APIs with FastAPI, implementing Pydantic v2 validation, dependency injection patterns, or deploying hi |
| `flutter-expert` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building cross-platform mobile applications with Flutter 3+ that require custom UI implementation, complex state management, native |
| `golang-pro` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building Go applications requiring concurrent programming, high-performance systems, microservices, or cloud-native architectures w |
| `java-architect` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when designing enterprise Java architectures, migrating Spring Boot applications, or establishing microservices patterns for  |
| `javascript-pro` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to build, optimize, or refactor modern JavaScript code for browser, Node.js, or full-stack applications requiri |
| `kotlin-specialist` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building Kotlin applications requiring advanced coroutine patterns, multiplatform code sharing, or Android/server-side development  |
| `laravel-specialist` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building Laravel 10+ applications, architecting Eloquent models with complex relationships, implementing queue systems for async pr |
| `nextjs-developer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when building production Next.js 14+ applications that require full-stack development with App Router, server components, and |
| `node-specialist` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to build, optimize, or debug Node.js backend applications, APIs, CLIs, or microservices requiring deep ecosyste |
| `php-pro` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when working with PHP 8.3+ projects that require strict typing, modern language features, and enterprise framework expertise  |
| `powershell-5.1-expert` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when automating Windows infrastructure tasks requiring PowerShell 5.1 scripts with RSAT modules for Active Directory, DNS, DHCP, GPO man |
| `powershell-7-expert` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building cross-platform cloud automation scripts, Azure infrastructure orchestration, or CI/CD pipelines requiring PowerShell 7+ wi |
| `python-pro` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to build type-safe, production-ready Python code for web APIs, system utilities, or complex applications requir |
| `rails-expert` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building or modernizing Rails applications requiring API development, Hotwire reactivity, real-time features, background job proces |
| `react-specialist` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when optimizing existing React applications for performance, implementing advanced React 18+ features, or solving complex state manageme |
| `rust-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building Rust systems where memory safety, ownership patterns, zero-cost abstractions, and performance optimization are critical fo |
| `spring-boot-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when building enterprise Spring Boot 3+ applications requiring microservices architecture, cloud-native deployment, or reacti |
| `sql-pro` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to optimize complex SQL queries, design efficient database schemas, or solve performance issues across PostgreS |
| `swift-expert` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when building native iOS, macOS, or server-side Swift applications requiring advanced concurrency patterns, protocol-oriented |
| `symfony-specialist` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building Symfony 6+/7+/8+ applications, architecting Doctrine ORM entities with complex relationships, implementing Messenger compo |
| `typescript-pro` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when implementing TypeScript code requiring advanced type system patterns, complex generics, type-level programming, or end-to-end type  |
| `vue-expert` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when building Vue 3 applications that require Composition API mastery, reactivity optimization, or Nuxt 3 development with en |
| `azure-infra-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when designing, deploying, or managing Azure infrastructure with focus on network architecture, Entra ID integration, PowerShell automat |
| `cloud-architect` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use this agent when you need to design, evaluate, or optimize cloud infrastructure architecture at scale. Invoke when designing multi-cloud  |
| `database-administrator` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when optimizing database performance, implementing high-availability architectures, setting up disaster recovery, or managing |
| `deployment-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | haiku | Use this agent when designing, building, or optimizing CI/CD pipelines and deployment automation strategies. |
| `devops-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when building or optimizing infrastructure automation, CI/CD pipelines, containerization strategies, and deployment workflows |
| `devops-incident-responder` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when actively responding to production incidents, diagnosing critical service failures, or conducting incident postmortems to implement  |
| `docker-expert` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to build, optimize, or secure Docker container images and orchestration for production environments. |
| `incident-responder` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when an active security breach, service outage, or operational incident requires immediate response, evidence preservation, a |
| `kubernetes-specialist` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to design, deploy, configure, or troubleshoot Kubernetes clusters and workloads in production environments. |
| `network-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when designing, optimizing, or troubleshooting cloud and hybrid network infrastructures, or when addressing network security, |
| `platform-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use when building or improving internal developer platforms (IDPs), designing self-service infrastructure, or optimizing developer workflows |
| `security-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use this agent when implementing comprehensive security solutions across infrastructure, building automated security controls into CI/CD pip |
| `sre-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to establish or improve system reliability through SLO definition, error budget management, and automation. Inv |
| `terraform-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building, refactoring, or scaling infrastructure as code using Terraform with focus on multi-cloud deployments, module architecture |
| `terragrunt-expert` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Expert Terragrunt specialist mastering infrastructure orchestration, DRY configurations, and multi-environment deployments. Masters stacks,  |
| `windows-infra-admin` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when managing Windows Server infrastructure, Active Directory, DNS, DHCP, and Group Policy configurations, especially for enterprise-sca |
| `accessibility-tester` | voltagent | Read, Grep, Glob, Bash | haiku | Use this agent when you need comprehensive accessibility testing, WCAG compliance verification, or assessment of assistive technology suppor |
| `ad-security-reviewer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use this agent when you need to audit Active Directory security posture, evaluate privilege escalation risks, review identity delegation pat |
| `ai-writing-auditor` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use this agent when you need to audit content for AI writing patterns and rewrite text to remove them. |
| `architect-reviewer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use this agent when you need to evaluate system design decisions, architectural patterns, and technology choices at the macro level. |
| `chaos-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to design and execute controlled failure experiments, validate system resilience before incidents occur, or con |
| `code-reviewer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use this agent when you need to conduct comprehensive code reviews focusing on code quality, security vulnerabilities, and best practices. |
| `compliance-auditor` | voltagent | Read, Grep, Glob | inherit | Use this agent when you need to achieve regulatory compliance, implement compliance controls, or prepare for audits across frameworks like G |
| `debugger` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to diagnose and fix bugs, identify root causes of failures, or analyze error logs and stack traces to resolve i |
| `error-detective` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to diagnose why errors are occurring in your system, correlate errors across services, identify root causes, an |
| `gdpr-ccpa-compliance` | voltagent | Read, Grep, Glob, WebFetch, WebSearch |  | Use when the user needs to understand GDPR or CCPA compliance, review data practices, or assess privacy requirements. Triggers on: 'GDPR', ' |
| `penetration-tester` | voltagent | Read, Grep, Glob, Bash | inherit | Use this agent when you need to conduct authorized security penetration tests to identify real vulnerabilities through active exploitation a |
| `performance-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to identify and eliminate performance bottlenecks in applications, databases, or infrastructure systems, and wh |
| `powershell-security-hardening` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use this agent when you need to harden PowerShell automation, secure remoting configuration, enforce least-privilege design, or align script |
| `qa-expert` | voltagent | Read, Grep, Glob, Bash | sonnet | Use this agent when you need comprehensive quality assurance strategy, test planning across the entire development cycle, or quality metrics |
| `security-auditor` | voltagent | Read, Grep, Glob | inherit | Use this agent when conducting comprehensive security audits, compliance assessments, or risk evaluations across systems, infrastructure, an |
| `test-automator` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to build, implement, or enhance automated test frameworks, create test scripts, or integrate testing into CI/CD |
| `ui-ux-tester` | voltagent | Read, Write, Edit, Bash, Glob, Grep, WebSearch, chrome-mcp, computer-use | sonnet | Use this agent when you need exhaustive UI and UX functionality testing driven by documented user flows, with browser or desktop interaction |
| `ai-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use this agent when architecting, implementing, or optimizing end-to-end AI systems—from model selection and training pipelines to productio |
| `data-analyst` | voltagent | Read, Write, Edit, Bash, Glob, Grep | haiku | Use when you need to extract insights from business data, create dashboards and reports, or perform statistical analysis to support decision |
| `data-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to design, build, or optimize data pipelines, ETL/ELT processes, and data infrastructure. Invoke when designing |
| `data-scientist` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to analyze data patterns, build predictive models, or extract statistical insights from datasets. Invoke this a |
| `database-optimizer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to analyze slow queries, optimize database performance across multiple systems, or implement indexing strategie |
| `llm-architect` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use when designing LLM systems for production, implementing fine-tuning or RAG architectures, optimizing inference serving infrastructure, o |
| `machine-learning-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to deploy, optimize, or serve machine learning models at scale in production environments. |
| `ml-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when building production ML systems requiring model training pipelines, model serving infrastructure, performance optimizatio |
| `mlops-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to design and implement ML infrastructure, set up CI/CD for machine learning models, establish model versioning |
| `nlp-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when building production NLP systems, implementing text processing pipelines, developing language models, or solving domain-specific NLP |
| `postgres-pro` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when you need to optimize PostgreSQL performance, design high-availability replication, or troubleshoot database issues at scale. Invoke |
| `prompt-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to design, optimize, test, or evaluate prompts for large language models in production systems. |
| `reinforcement-learning-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when designing RL environments, training agents with reward optimization, implementing policy gradient methods, or deploying decision-ma |
| `build-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | haiku | Use this agent when you need to optimize build performance, reduce compilation times, or scale build systems across growing teams. |
| `cli-developer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when building command-line tools and terminal applications that require intuitive command design, cross-platform compatibilit |
| `dependency-manager` | voltagent | Read, Write, Edit, Bash, Glob, Grep | haiku | Use this agent when you need to audit dependencies for vulnerabilities, resolve version conflicts, optimize bundle sizes, or implement autom |
| `docs-drift-editor` | voltagent | Read, Edit, Grep, Glob, Bash | sonnet | Use this agent to update Markdown documentation pages that have drifted out of sync with a code change, inside an isolated git worktree, wit |
| `documentation-engineer` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | haiku | Use this agent when you need to create, architect, or overhaul comprehensive documentation systems including API docs, tutorials, guides, an |
| `dx-optimizer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when optimizing the complete developer workflow including build times, feedback loops, testing efficiency, and developer sati |
| `git-workflow-manager` | voltagent | Read, Write, Edit, Bash, Glob, Grep | haiku | Use this agent when you need to design, establish, or optimize Git workflows, branching strategies, and merge management for a project or te |
| `legacy-modernizer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when modernizing legacy systems that need incremental migration strategies, technical debt reduction, and risk mitigation whi |
| `mcp-developer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to build, debug, or optimize Model Context Protocol (MCP) servers and clients that connect AI systems to extern |
| `powershell-module-architect` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when architecting and refactoring PowerShell modules, designing profile systems, or creating cross-version compatible automat |
| `powershell-ui-architect` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when designing or building desktop graphical interfaces (WinForms, WPF, Metro-style dashboards) or terminal user interfaces (TUIs) for P |
| `readme-generator` | voltagent | Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch | sonnet | Use this agent when you need a maintainer-ready README built from exact repository reality, with deep codebase scanning, zero hallucination, |
| `refactoring-specialist` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when you need to transform poorly structured, complex, or duplicated code into clean, maintainable systems while preserving all existing |
| `slack-expert` | voltagent | Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch | sonnet | Use this agent when developing Slack applications, implementing Slack API integrations, or reviewing Slack bot code for security and best pr |
| `tooling-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when you need to build or enhance developer tools including CLIs, code generators, build tools, and IDE extensions. |
| `visual-asset-generator` | voltagent | Read, Write, Bash, mcp__prompt-to-asset | sonnet | Use this agent when you need to generate production-ready visual assets for a project — app icons, favicons, OG images, logos, wordmarks, or |
| `api-documenter` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | haiku | Use this agent when creating or improving API documentation, writing OpenAPI specifications, building interactive documentation portals, or  |
| `blockchain-developer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when building smart contracts, DApps, and blockchain protocols that require expertise in Solidity, gas optimization, security |
| `email-deliverability-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when configuring email authentication, integrating transactional or marketing email providers, diagnosing deliverability prob |
| `embedded-systems` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when developing firmware for resource-constrained microcontrollers, implementing RTOS-based applications, or optimizing real-time system |
| `fintech-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use when building payment systems, financial integrations, or compliance-heavy financial applications that require secure transaction proces |
| `game-developer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when implementing game systems, optimizing graphics rendering, building multiplayer networking, or developing gameplay mechan |
| `healthcare-admin` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use when working on healthcare administration tasks including revenue cycle management, HIPAA/compliance auditing, medical coding (ICD-10, C |
| `hipaa-compliance` | voltagent | Read, Grep, Glob, WebFetch, WebSearch |  | Use when the user is building a healthcare product and needs to understand HIPAA compliance. Triggers on: 'HIPAA', 'protected health informa |
| `iot-engineer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when designing and deploying IoT solutions requiring expertise in device management, edge computing, cloud integration, and handling cha |
| `m365-admin` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use when automating Microsoft 365 administrative tasks including Exchange Online mailbox provisioning, Teams collaboration management, Share |
| `mobile-app-developer` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use this agent when developing iOS and Android mobile applications with focus on native or cross-platform implementation, performance optimi |
| `payment-integration` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use this agent when implementing payment systems, integrating payment gateways, or handling financial transactions that require PCI complian |
| `quant-analyst` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use this agent when you need to develop quantitative trading strategies, build financial models with rigorous mathematical foundations, or c |
| `risk-manager` | voltagent | Read, Write, Edit, Bash, Glob, Grep | inherit | Use this agent when you need to identify, quantify, and mitigate enterprise-level risks across financial, operational, regulatory, and strat |
| `seo-specialist` | voltagent | Read, Grep, Glob, WebFetch, WebSearch | haiku | Use this agent when you need comprehensive SEO optimization encompassing technical audits, keyword strategy, content optimization, and searc |
| `x-api-integration` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | haiku | Use this agent when building X/Twitter data products, integrating X API alternatives, designing tweet search workflows, or documenting socia |
| `assumption-mapping` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch |  | Use when the user needs to identify and prioritize risky assumptions in a product idea, feature, or strategy. Triggers on: 'assumptions', 'w |
| `backlog-grooming` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch |  | Use when the user needs to groom, refine, or clean up a product backlog. Triggers on: 'groom backlog', 'backlog refinement', 'backlog groomi |
| `business-analyst` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | sonnet | Use when analyzing business processes, gathering requirements from stakeholders, or identifying process improvement opportunities to drive o |
| `content-marketer` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | haiku | Use this agent when you need to develop comprehensive content strategies, create SEO-optimized marketing content, or execute multi-channel c |
| `content-quality-editor` | voltagent | Read, Write, Edit, Bash | haiku | Use this agent before publishing any AI-generated content — blog posts, READMEs, release notes, commit messages, PR descriptions, documentat |
| `customer-success-manager` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | sonnet | Use this agent when you need to assess customer health, develop retention strategies, identify upsell opportunities, or maximize customer li |
| `growth-loops` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch |  | Use when the user wants to design a growth loop, understand PLG mechanics, or build sustainable acquisition. Triggers on: 'growth loop', 'fl |
| `landing-page-copywriter` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | sonnet | Use this agent when writing or optimizing landing page copy, hero sections, CTAs, or conversion-focused funnel content for a specific audien |
| `legal-advisor` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | sonnet | Use this agent when you need to draft contracts, review compliance requirements, develop IP protection strategies, or assess legal risks for |
| `license-engineer` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | inherit | Use this agent when architecting, implementing, or optimizing end-to-end legal licensing systems—from OSI standard selection and dependency  |
| `product-manager` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | haiku | Use this agent when you need to make product strategy decisions, prioritize features, or define roadmap plans based on user needs and busine |
| `project-manager` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | haiku | Use this agent when you need to establish project plans, track execution progress, manage risks, control budget/schedule, and coordinate sta |
| `sales-engineer` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | sonnet | Use this agent when you need to conduct technical pre-sales activities including solution architecture, proof-of-concept development, and te |
| `scrum-master` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | haiku | Use when teams need facilitation, process optimization, velocity improvement, or agile ceremony management—especially for sprint planning, r |
| `technical-writer` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | haiku | Use this agent when you need to create, improve, or maintain technical documentation including API references, user guides, SDK documentatio |
| `ux-researcher` | voltagent | Read, Grep, Glob, WebFetch, WebSearch | sonnet | Use this agent when you need to conduct user research, analyze user behavior, or generate actionable insights to validate design decisions a |
| `wordpress-master` | voltagent | Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch | sonnet | Use this agent when you need to architect, optimize, or troubleshoot WordPress implementations ranging from custom theme/plugin development  |
| `agent-installer` | voltagent | Bash, WebFetch, Read, Write, Glob | haiku | Use this agent when the user wants to discover, browse, or install Claude Code agents from the awesome-claude-code-subagents repository. |
| `agent-organizer` | voltagent | Read, Write, Edit, Glob, Grep | sonnet | Use when you need to break a complex task into subtasks, match each to the capabilities of available subagents, and write a concrete team/wo |
| `codebase-orchestrator` | voltagent | Read, Write, Edit, Bash, Glob, Grep, WebFetch, airis-mcp-gateway, context-manager, error-coordinator, pied-piper, subagent-catalog:search, subagent-catalog:fetch | inherit | Use this agent when you need repository-wide refactor governance with explicit approval loops, weighted risk prioritization, diff previews,  |
| `context-manager` | voltagent | Read, Write, Edit, Glob, Grep | sonnet | Use to organize the shared context and state that a multi-agent workflow keeps in files — deciding directory/file structure, naming conventi |
| `error-coordinator` | voltagent | Read, Write, Edit, Glob, Grep | sonnet | Use when you need to mine error logs and agent output for recurring failure and cascade patterns, then document grounded recovery and cascad |
| `it-ops-orchestrator` | voltagent | Read, Write, Edit, Bash, Glob, Grep | sonnet | Use for orchestrating complex IT operations tasks that span multiple domains (PowerShell automation, .NET development, infrastructure manage |
| `knowledge-synthesizer` | voltagent | Read, Write, Edit, Glob, Grep | sonnet | Use when you need to mine recurring patterns from agent logs, session transcripts, and workflow history, then write grounded, evidence-cited |
| `multi-agent-coordinator` | voltagent | Read, Write, Edit, Glob, Grep | inherit | Use when you need to plan how multiple concurrent subagents should communicate, sequence their work, share state through files, and handle f |
| `performance-monitor` | voltagent | Read, Write, Edit, Glob, Grep | haiku | Use when you need to analyze existing metric, log, and output files to spot performance patterns and anomalies, then write a grounded, evide |
| `task-distributor` | voltagent | Read, Write, Edit, Glob, Grep | haiku | Use when you need to design and document a task-distribution strategy across multiple agents or workers — how to split work, order queues, r |
| `workflow-orchestrator` | voltagent | Read, Write, Edit, Glob, Grep | inherit | Use when you need to design workflow and state-machine definitions — states, transitions, error handling, and compensation/rollback logic —  |
| `ab-test-analysis` | voltagent | Read, Grep, Glob, WebFetch, WebSearch |  | Use when the user wants to analyze A/B test results, interpret p-values, determine statistical significance, or make a ship/no-ship decision |
| `cohort-analysis` | voltagent | Read, Grep, Glob, WebFetch, WebSearch |  | Use when the user wants to analyze retention, cohort behavior, engagement trends, or understand how different user groups perform over time. |
| `competitive-analyst` | voltagent | Read, Grep, Glob, WebFetch, WebSearch | sonnet | Use when you need to analyze direct and indirect competitors, benchmark against market leaders, or develop strategies to strengthen competit |
| `data-researcher` | voltagent | Read, Grep, Glob, WebFetch, WebSearch | sonnet | Use this agent when you need to discover, collect, and validate data from multiple sources to fuel analysis and decision-making. Invoke this |
| `first-principles-thinking` | voltagent | Read, Grep, Glob, WebFetch, WebSearch |  | Use when the user wants to challenge assumptions, break down a complex problem from scratch, or approach something with first principles rea |
| `market-researcher` | voltagent | Read, Grep, Glob, WebFetch, WebSearch | sonnet | Use this agent when you need to analyze markets, understand consumer behavior, assess competitive landscapes, and size opportunities to info |
| `project-idea-validator` | voltagent | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch | sonnet | Use this agent when you need an idea pressure-tested with brutal honesty, competitor teardown, market validation, and clear go/no-go guidanc |
| `research-analyst` | voltagent | Read, Grep, Glob, WebFetch, WebSearch | sonnet | Use this agent when you need comprehensive research across multiple sources with synthesis of findings into actionable insights, trend ident |
| `scientific-literature-researcher` | voltagent | Read, WebFetch, WebSearch, mcp__bgpt__search_papers | sonnet | Use when you need to search scientific literature and retrieve structured experimental data from published studies. Invoke this agent when t |
| `search-specialist` | voltagent | Read, Grep, Glob, WebFetch, WebSearch | sonnet | Use when you need to find specific information across multiple sources using advanced search strategies, query optimization, and targeted in |
| `trend-analyst` | voltagent | Read, Grep, Glob, WebFetch, WebSearch | sonnet | Use when analyzing emerging patterns, predicting industry shifts, or developing future scenarios to inform strategic planning and competitiv |
| `ui-visual-validator` | wshobson |  | sonnet | Rigorous visual validation expert specializing in UI testing, design system compliance, and accessibility verification. Masters screenshot a |
| `screen-reader-testing` | wshobson |  |  | Test web applications with screen readers including VoiceOver, NVDA, and JAWS. Use when validating screen reader compatibility, debugging ac |
| `wcag-audit-patterns` | wshobson |  |  | Conduct WCAG 2.2 accessibility audits with automated testing, manual verification, and remediation guidance. Use when auditing websites for  |
| `agent-orchestration-context-manager` | wshobson |  | inherit | Elite AI context engineering specialist mastering dynamic context management, vector databases, knowledge graphs, and intelligent memory sys |
| `team-debugger` | wshobson | Read, Glob, Grep, Bash, TaskList, TaskGet, TaskUpdate, SendMessage | opus | Hypothesis-driven debugging investigator that investigates one assigned hypothesis, gathering evidence to confirm or falsify it with file:li |
| `team-implementer` | wshobson | Read, Write, Edit, Glob, Grep, Bash, TaskList, TaskGet, TaskUpdate, SendMessage | opus | Parallel feature builder that implements components within strict file ownership boundaries, coordinating at integration points via messagin |
| `team-lead` | wshobson | Read, Glob, Grep, Bash, Agent, TeamCreate, TeamDelete, TaskCreate, TaskList, TaskGet, TaskUpdate, SendMessage | fable | Team orchestrator that decomposes work into parallel tasks with file ownership boundaries, manages team lifecycle, and synthesizes results.  |
| `team-reviewer` | wshobson | Read, Glob, Grep, Bash, TaskList, TaskGet, TaskUpdate, SendMessage | opus | Multi-dimensional code reviewer that operates on one assigned review dimension (security, performance, architecture, testing, or accessibili |
| `multi-reviewer-patterns` | wshobson |  |  | Coordinate parallel code reviews across multiple quality dimensions with finding deduplication, severity calibration, and consolidated repor |
| `parallel-debugging` | wshobson |  |  | Debug complex issues using competing hypotheses with parallel investigation, evidence collection, and root cause arbitration. Use this skill |
| `parallel-feature-development` | wshobson |  |  | Coordinate parallel feature development with file ownership strategies, conflict avoidance rules, and integration patterns for multi-agent i |
| `task-coordination-strategies` | wshobson |  |  | Decompose complex tasks, design dependency graphs, and coordinate multi-agent work with proper task descriptions and workload balancing. Use |
| `team-communication-protocols` | wshobson |  |  | Structured messaging protocols for agent team communication including message type selection, plan approval, shutdown procedures, and anti-p |
| `team-composition-patterns` | wshobson |  |  | Design optimal agent team compositions with sizing heuristics, preset configurations, and agent type selection. Use this skill when deciding |
| `api-scaffolding-backend-architect` | wshobson |  | inherit | Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. Masters REST/GraphQL/gRPC |
| `api-scaffolding-django-pro` | wshobson |  | opus | Master Django 5.x with async views, DRF, Celery, and Django Channels. Build scalable web applications with proper architecture, testing, and |
| `api-scaffolding-fastapi-pro` | wshobson |  | opus | Build high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. Master microservices, WebSockets, and modern Python async p |
| `api-scaffolding-graphql-architect` | wshobson |  | opus | Master modern GraphQL with federation, performance optimization, and enterprise security. Build scalable schemas, implement advanced caching |
| `fastapi-templates` | wshobson |  |  | Create production-ready FastAPI projects with async patterns, dependency injection, and comprehensive error handling. Use when building new  |
| `api-testing-observability-api-documenter` | wshobson |  | sonnet | Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices. Create interactive docs, generate SD |
| `application-performance-frontend-developer` | wshobson |  | inherit | Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern fron |
| `application-performance-observability-engineer` | wshobson |  | inherit | Build production-ready monitoring, logging, and tracing systems. Implements comprehensive observability strategies, SLI/SLO management, and  |
| `application-performance-performance-engineer` | wshobson |  | inherit | Expert performance engineer specializing in modern observability, application optimization, and scalable system performance. Masters OpenTel |
| `arm-cortex-expert` | wshobson | [] | inherit | Senior embedded software engineer specializing in firmware and driver development for ARM Cortex-M microcontrollers (Teensy, STM32, nRF52, S |
| `avoid-ai-writing` | wshobson |  |  | Audit and rewrite prose so it stops reading as machine-generated. Use this skill when asked to remove AI-isms, clean up AI writing, edit a d |
| `backend-api-security-backend-architect` | wshobson |  | inherit | Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. Masters REST/GraphQL/gRPC |
| `backend-api-security-backend-security-coder` | wshobson |  | sonnet | Expert in secure backend coding practices specializing in input validation, authentication, and API security. Use PROACTIVELY for backend se |
| `backend-development-backend-architect` | wshobson |  | inherit | Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. Masters REST/GraphQL/gRPC |
| `event-sourcing-architect` | wshobson |  | inherit | Expert in event sourcing, CQRS, and event-driven architecture patterns. Masters event store design, projection building, saga orchestration, |
| `backend-development-graphql-architect` | wshobson |  | opus | Master modern GraphQL with federation, performance optimization, and enterprise security. Build scalable schemas, implement advanced caching |
| `backend-development-performance-engineer` | wshobson |  | sonnet | Profile and optimize application performance including response times, memory usage, query efficiency, and scalability. Use for performance  |
| `backend-development-security-auditor` | wshobson |  | sonnet | Review code and architecture for security vulnerabilities, OWASP Top 10, auth flaws, and compliance issues. Use for security review during f |
| `backend-development-tdd-orchestrator` | wshobson |  | opus | Master TDD orchestrator specializing in red-green-refactor discipline, multi-agent workflow coordination, and comprehensive test-driven deve |
| `temporal-python-pro` | wshobson |  | inherit | Master Temporal workflow orchestration with Python SDK. Implements durable workflows, saga patterns, and distributed transactions. Covers as |
| `backend-development-test-automator` | wshobson |  | sonnet | Create comprehensive test suites including unit, integration, and E2E tests. Supports TDD/BDD workflows. Use for test creation during featur |
| `api-design-principles` | wshobson |  |  | Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers. Use when designin |
| `architecture-patterns` | wshobson |  |  | Implement proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Driven Design. Use this skil |
| `cqrs-implementation` | wshobson |  |  | Implement Command Query Responsibility Segregation for scalable architectures. Use when separating read and write models, optimizing query p |
| `event-store-design` | wshobson |  |  | Design and implement event stores for event-sourced systems. Use when building event sourcing infrastructure, choosing event store technolog |
| `microservices-patterns` | wshobson |  |  | Design microservices architectures with service boundaries, event-driven communication, and resilience patterns. Use when building distribut |
| `projection-patterns` | wshobson |  |  | Build read models and projections from event streams. Use when implementing CQRS read sides, building materialized views, or optimizing quer |
| `saga-orchestration` | wshobson |  |  | Implement saga patterns for distributed transactions and cross-aggregate workflows. Use this skill when implementing distributed transaction |
| `temporal-python-testing` | wshobson |  |  | Test Temporal workflows with pytest, time-skipping, and mocking strategies. Covers unit testing, integration testing, replay testing, and lo |
| `workflow-orchestration-patterns` | wshobson |  |  | Design durable workflows with Temporal for distributed systems. Covers workflow vs activity separation, saga patterns, state management, and |
| `before-you-build` | wshobson |  |  | Pre-build product and feature risk review for founders, product managers, and AI-assisted builders. Use this skill when the user is about to |
| `block-no-verify-hook` | wshobson |  |  | Configure a PreToolUse hook to prevent AI agents from skipping git pre-commit hooks with --no-verify and other bypass flags. Use when settin |
| `blockchain-developer` | wshobson |  | opus | Build production-ready Web3 applications, smart contracts, and decentralized systems. Implements DeFi protocols, NFT platforms, DAOs, and en |
| `defi-protocol-templates` | wshobson |  |  | Implement DeFi protocols with production-ready templates for staking, AMMs, governance, and flash loans. Use when building decentralized fin |
| `nft-standards` | wshobson |  |  | Implement NFT standards (ERC-721, ERC-1155) with proper metadata handling, minting strategies, and marketplace integration. Use when creatin |
| `solidity-security` | wshobson |  |  | Master smart contract security best practices to prevent common vulnerabilities and implement secure Solidity patterns. Use when writing sma |
| `web3-testing` | wshobson |  |  | Test smart contracts comprehensively using Hardhat and Foundry with unit tests, integration tests, and mainnet forking. Use when testing Sol |
| `brand-landingpage` | wshobson |  |  | Brand-first landing page designer — runs a brand-identity interview (colors, typography, shape language), then generates and iterates on a p |
| `business-analyst` | wshobson |  | sonnet | Master modern business analysis with AI-powered analytics, real-time dashboards, and data-driven insights. Build comprehensive KPI framework |
| `data-storytelling` | wshobson |  |  | Transform data into compelling narratives using visualization, context, and persuasive structure. Use when presenting analytics to stakehold |
| `kpi-dashboard-design` | wshobson |  |  | Design effective KPI dashboards with metrics selection, visualization best practices, and real-time monitoring patterns. Use this skill when |
| `c4-code` | wshobson |  | haiku | Expert C4 Code-level documentation specialist. Analyzes code directories to create comprehensive C4 code-level documentation including funct |
| `c4-component` | wshobson |  | sonnet | Expert C4 Component-level documentation specialist. Synthesizes C4 Code-level documentation into Component-level architecture, defining comp |
| `c4-container` | wshobson |  | sonnet | Expert C4 Container-level documentation specialist. Synthesizes Component-level documentation into Container-level architecture, mapping com |
| `c4-context` | wshobson |  | sonnet | Expert C4 Context-level documentation specialist. Creates high-level system context diagrams, documents personas, user journeys, system feat |
| `cicd-automation-cloud-architect` | wshobson |  | opus | Expert cloud architect specializing in AWS/Azure/GCP/OCI multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps co |
| `cicd-automation-deployment-engineer` | wshobson |  | haiku | Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation. Masters GitHub Acti |
| `cicd-automation-devops-troubleshooter` | wshobson |  | sonnet | Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability. Masters log analysis, di |
| `cicd-automation-kubernetes-architect` | wshobson |  | opus | Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container o |
| `cicd-automation-terraform-specialist` | wshobson |  | opus | Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. Handles co |
| `deployment-pipeline-design` | wshobson |  |  | Design multi-stage CI/CD pipelines with approval gates, security checks, and deployment orchestration. Use this skill when designing zero-do |
| `github-actions-templates` | wshobson |  |  | Create production-ready GitHub Actions workflows for automated testing, building, and deploying applications. Use when setting up CI/CD with |
| `gitlab-ci-patterns` | wshobson |  |  | Build GitLab CI/CD pipelines with multi-stage workflows, caching, and distributed runners for scalable automation. Use when implementing Git |
| `secrets-management` | wshobson |  |  | Implement secure secrets management for CI/CD pipelines using Vault, AWS Secrets Manager, or native platform solutions. Use when handling se |
| `cloud-infrastructure-cloud-architect` | wshobson |  | opus | Expert cloud architect specializing in AWS/Azure/GCP/OCI multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps co |
| `cloud-infrastructure-deployment-engineer` | wshobson |  | haiku | Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation. Masters GitHub Acti |
| `hybrid-cloud-architect` | wshobson |  | opus | Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP/OCI and private clouds (OpenStack/VMware).  |
| `cloud-infrastructure-kubernetes-architect` | wshobson |  | opus | Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container o |
| `cloud-infrastructure-network-engineer` | wshobson |  | sonnet | Expert network engineer specializing in modern cloud networking, security architectures, and performance optimization. Masters multi-cloud c |
| `service-mesh-expert` | wshobson |  | opus | Expert service mesh architect specializing in Istio, Linkerd, and cloud-native networking patterns. Masters traffic management, security pol |
| `cloud-infrastructure-terraform-specialist` | wshobson |  | opus | Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. Handles co |
| `cost-optimization` | wshobson |  |  | Optimize cloud costs across AWS, Azure, GCP, and OCI through resource rightsizing, tagging strategies, reserved instances, and spending anal |
| `hybrid-cloud-networking` | wshobson |  |  | Configure secure, high-performance connectivity between on-premises infrastructure and cloud platforms using VPN and dedicated connections.  |
| `istio-traffic-management` | wshobson |  |  | Configure Istio traffic management including routing, load balancing, circuit breakers, and canary deployments. Use when implementing servic |
| `linkerd-patterns` | wshobson |  |  | Implement Linkerd service mesh patterns for lightweight, security-focused service mesh deployments. Use when setting up Linkerd, configuring |
| `mtls-configuration` | wshobson |  |  | Configure mutual TLS (mTLS) for zero-trust service-to-service communication. Use when implementing zero-trust networking, certificate manage |
| `multi-cloud-architecture` | wshobson |  |  | Design multi-cloud architectures using a decision framework to select and integrate services across AWS, Azure, GCP, and OCI. Use when build |
| `service-mesh-observability` | wshobson |  |  | Implement comprehensive observability for service meshes including distributed tracing, metrics, and visualization. Use when setting up mesh |
| `terraform-module-library` | wshobson |  |  | Build reusable Terraform modules for AWS, Azure, GCP, and OCI infrastructure following infrastructure-as-code best practices. Use when creat |
| `code-documentation-code-reviewer` | wshobson |  | opus | Elite code review expert specializing in modern AI-powered code analysis, security vulnerabilities, performance optimization, and production |
| `code-documentation-docs-architect` | wshobson |  | sonnet | Creates comprehensive technical documentation from existing codebases. Analyzes architecture, design patterns, and implementation details to |
| `code-documentation-tutorial-engineer` | wshobson |  | sonnet | Creates step-by-step tutorials and educational content from code. Transforms complex concepts into progressive learning experiences with han |
| `code-refactoring-code-reviewer` | wshobson |  | opus | Elite code review expert specializing in modern AI-powered code analysis, security vulnerabilities, performance optimization, and production |
| `code-refactoring-legacy-modernizer` | wshobson |  | sonnet | Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. Handles technical debt, dependency updates, and |
| `codebase-cleanup-code-reviewer` | wshobson |  | opus | Elite code review expert specializing in modern AI-powered code analysis, security vulnerabilities, performance optimization, and production |
| `codebase-cleanup-test-automator` | wshobson |  | sonnet | Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. Build scalable testing  |
| `deps-audit` | wshobson |  |  | Audit project dependencies for vulnerabilities, outdated packages, license conflicts, and supply chain risks — then provide actionable remed |
| `refactor-clean` | wshobson |  |  | Refactor provided code for cleanliness, maintainability, and alignment with SOLID principles and modern best practices — no over-engineering |
| `comprehensive-review-architect-review` | wshobson |  | opus | Master software architect specializing in modern architecture patterns, clean architecture, microservices, event-driven systems, and DDD. Re |
| `comprehensive-review-code-reviewer` | wshobson |  | opus | Elite code review expert specializing in modern AI-powered code analysis, security vulnerabilities, performance optimization, and production |
| `comprehensive-review-security-auditor` | wshobson |  | opus | Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks. Masters vulnerability assessment, |
| `conductor-validator` | wshobson | Read, Glob, Grep, Bash | opus | Validates Conductor project artifacts for completeness, consistency, and correctness. Use after setup, when diagnosing issues, or before imp |
| `context-driven-development` | wshobson |  |  | Creates and maintains project context artifacts (product.md, tech-stack.md, workflow.md, tracks.md) in a `conductor/` directory. Scaffolds n |
| `track-management` | wshobson |  |  | Use this skill when creating, managing, or working with Conductor tracks - the logical work units for features, bugs, and refactors. Applies |
| `workflow-patterns` | wshobson |  |  | Use this skill when implementing tasks according to Conductor's TDD workflow, handling phase checkpoints, managing git commits for tasks, or |
| `content-marketer` | wshobson |  | haiku | Elite content marketing strategist specializing in AI-powered content creation, omnichannel distribution, SEO optimization, and data-driven  |
| `search-specialist` | wshobson |  | haiku | Expert web researcher using advanced search techniques and synthesis. Masters search operators, result filtering, and multi-source verificat |
| `context-management-context-manager` | wshobson |  | inherit | Elite AI context engineering specialist mastering dynamic context management, vector databases, knowledge graphs, and intelligent memory sys |
| `customer-support` | wshobson |  | haiku | Elite AI-powered customer support specialist mastering conversational AI, automated ticketing, sentiment analysis, and omnichannel support e |
| `sales-automator` | wshobson |  | haiku | Draft cold emails, follow-ups, and proposal templates. Creates pricing pages, case studies, and sales scripts. Use PROACTIVELY for sales out |
| `data-engineering-backend-architect` | wshobson |  | inherit | Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. Masters REST/GraphQL/gRPC |
| `data-engineer` | wshobson |  | opus | Build scalable data pipelines, modern data warehouses, and real-time streaming architectures. Implements Apache Spark, dbt, Airflow, and clo |
| `airflow-dag-patterns` | wshobson |  |  | Build production Apache Airflow DAGs with best practices for operators, sensors, testing, and deployment. Use when creating data pipelines,  |
| `data-quality-frameworks` | wshobson |  |  | Implement data quality validation with Great Expectations, dbt tests, and data contracts. Use when building data quality pipelines, implemen |
| `dbt-transformation-patterns` | wshobson |  |  | Master dbt (data build tool) for analytics engineering with model organization, testing, documentation, and incremental strategies. Use when |
| `spark-optimization` | wshobson |  |  | Optimize Apache Spark jobs with partitioning, caching, shuffle optimization, and memory tuning. Use when improving Spark performance, debugg |
| `data-validation-suite-backend-security-coder` | wshobson |  | sonnet | Expert in secure backend coding practices specializing in input validation, authentication, and API security. Use PROACTIVELY for backend se |
| `database-cloud-optimization-backend-architect` | wshobson |  | inherit | Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. Masters REST/GraphQL/gRPC |
| `database-cloud-optimization-cloud-architect` | wshobson |  | sonnet | Expert cloud architect specializing in AWS/Azure/GCP/OCI multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps co |
| `database-cloud-optimization-database-architect` | wshobson |  | inherit | Expert database architect specializing in data layer design from scratch, technology selection, schema modeling, and scalable database archi |
| `database-cloud-optimization-database-optimizer` | wshobson |  | inherit | Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures. Masters advanced indexi |
| `database-design-database-architect` | wshobson |  | opus | Expert database architect specializing in data layer design from scratch, technology selection, schema modeling, and scalable database archi |
| `sql-pro` | wshobson |  | inherit | Master modern SQL with cloud-native databases, OLTP/OLAP optimization, and advanced query techniques. Expert in performance tuning, data mod |
| `postgresql-table-design` | wshobson |  |  | Use this skill when designing or reviewing a PostgreSQL-specific schema. Covers best-practices, data types, indexing, constraints, performan |
| `database-admin` | wshobson |  | sonnet | Expert database administrator specializing in modern cloud databases, automation, and reliability engineering. Masters AWS/Azure/GCP/OCI dat |
| `database-migrations-database-optimizer` | wshobson |  | inherit | Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures. Masters advanced indexi |
| `migration-observability` | wshobson |  |  | Migration monitoring, CDC, and observability infrastructure |
| `debugging-toolkit-debugger` | wshobson |  | sonnet | Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues. |
| `debugging-toolkit-dx-optimizer` | wshobson |  | sonnet | Developer Experience specialist. Improves tooling, setup, and workflows. Use PROACTIVELY when setting up new projects, after team feedback,  |
| `dependency-management-legacy-modernizer` | wshobson |  | sonnet | Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. Handles technical debt, dependency updates, and |
| `deployment-strategies-deployment-engineer` | wshobson |  | haiku | Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation. Masters GitHub Acti |
| `deployment-strategies-terraform-specialist` | wshobson |  | opus | Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. Handles co |
| `deployment-validation-cloud-architect` | wshobson |  | sonnet | Expert cloud architect specializing in AWS/Azure/GCP/OCI multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps co |
| `monorepo-architect` | wshobson |  | opus | Expert in monorepo architecture, build systems, and dependency management at scale. Masters Nx, Turborepo, Bazel, and Lerna for efficient mu |
| `auth-implementation-patterns` | wshobson |  |  | Master authentication and authorization patterns including JWT, OAuth2, session management, and RBAC to build secure, scalable access contro |
| `bazel-build-optimization` | wshobson |  |  | Optimize Bazel builds for large-scale monorepos. Use when configuring Bazel, implementing remote execution, or optimizing build performance  |
| `code-review-excellence` | wshobson |  |  | Master effective code review practices to provide constructive feedback, catch bugs early, and foster knowledge sharing while maintaining te |
| `debugging-strategies` | wshobson |  |  | Master systematic debugging techniques, profiling tools, and root cause analysis to efficiently track down bugs across any codebase or techn |
| `e2e-testing-patterns` | wshobson |  |  | Master end-to-end testing with Playwright and Cypress to build reliable test suites that catch bugs, improve confidence, and enable fast dep |
| `error-handling-patterns` | wshobson |  |  | Master error handling patterns across languages including exceptions, Result types, error propagation, and graceful degradation to build res |
| `git-advanced-workflows` | wshobson |  |  | Master advanced Git workflows including rebasing, cherry-picking, bisect, worktrees, and reflog to maintain clean history and recover from a |
| `monorepo-management` | wshobson |  |  | Master monorepo management with Turborepo, Nx, and pnpm workspaces to build efficient, scalable multi-package repositories with optimized bu |
| `nx-workspace-patterns` | wshobson |  |  | Configure and optimize Nx monorepo workspaces. Use when setting up Nx, configuring project boundaries, optimizing build caching, or implemen |
| `sql-optimization-patterns` | wshobson |  |  | Master SQL query optimization, indexing strategies, and EXPLAIN analysis to dramatically improve database performance and eliminate slow que |
| `turborepo-caching` | wshobson |  |  | Configure Turborepo for efficient monorepo builds with local and remote caching. Use when setting up Turborepo, optimizing build pipelines,  |
| `dgx-spark-ops-engineer` | wshobson |  | sonnet | NVIDIA DGX Spark environment doctor for GB10/aarch64/CUDA-13 systems. Diagnoses and fixes ML stack setup, unified-memory, and thermal issues |
| `spark-environment-setup` | wshobson |  |  | Set up a working ML training/inference environment on NVIDIA DGX Spark (GB10, aarch64, CUDA 13). Use when installing PyTorch/Unsloth/TRL/vLL |
| `spark-memory-thermal-ops` | wshobson |  |  | Manage unified memory and thermals during long-running ML jobs on NVIDIA DGX Spark. Use when planning memory headroom for a training run on  |
| `spark-training-gotchas` | wshobson |  |  | Preflight and diagnose the ten known failure modes for ML training on NVIDIA DGX Spark. Use when a training run on DGX Spark fails to start, |
| `distributed-debugging-devops-troubleshooter` | wshobson |  | sonnet | Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability. Masters log analysis, di |
| `distributed-debugging-error-detective` | wshobson |  | sonnet | Search logs and codebases for error patterns, stack traces, and anomalies. Correlates errors across systems and identifies root causes. Use  |
| `documentation-generation-api-documenter` | wshobson |  | sonnet | Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices. Create interactive docs, generate SD |
| `documentation-generation-docs-architect` | wshobson |  | sonnet | Creates comprehensive technical documentation from existing codebases. Analyzes architecture, design patterns, and implementation details to |
| `mermaid-expert` | wshobson |  | haiku | Create Mermaid diagrams for flowcharts, sequences, ERDs, and architectures. Masters syntax for all diagram types and styling. Use PROACTIVEL |
| `reference-builder` | wshobson |  | haiku | Creates exhaustive technical references and API documentation. Generates comprehensive parameter listings, configuration guides, and searcha |
| `documentation-generation-tutorial-engineer` | wshobson |  | sonnet | Creates step-by-step tutorials and educational content from code. Transforms complex concepts into progressive learning experiences with han |
| `architecture-decision-records` | wshobson |  |  | Write and maintain Architecture Decision Records (ADRs) following best practices for technical decision documentation. Use when documenting  |
| `changelog-automation` | wshobson |  |  | Automate changelog generation from commits, PRs, and releases following Keep a Changelog format. Use when setting up release workflows, gene |
| `openapi-spec-generation` | wshobson |  |  | Generate and maintain OpenAPI 3.1 specifications from code, design-first specs, and validation patterns. Use when creating API documentation |
| `grounded-vault` | wshobson |  |  | Use when maintaining a durable Markdown knowledge store that agents compile from sources, when every number or quote in a wiki page must tra |
| `hads` | wshobson |  |  | Use when writing technical documentation that needs to be readable by both humans and AI models, converting existing docs to HADS format, va |
| `dotnet-architect` | wshobson |  | sonnet | Expert .NET backend architect specializing in C#, ASP.NET Core, Entity Framework, Dapper, and enterprise application patterns. Masters async |
| `dotnet-backend-patterns` | wshobson |  |  | Master C#/.NET backend development patterns for building robust APIs, MCP servers, and enterprise applications. Covers async/await, dependen |
| `error-debugging-debugger` | wshobson |  | sonnet | Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues. |
| `error-debugging-error-detective` | wshobson |  | sonnet | Search logs and codebases for error patterns, stack traces, and anomalies. Correlates errors across systems and identifies root causes. Use  |
| `error-diagnostics-debugger` | wshobson |  | sonnet | Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues. |
| `error-diagnostics-error-detective` | wshobson |  | sonnet | Search logs and codebases for error patterns, stack traces, and anomalies. Correlates errors across systems and identifies root causes. Use  |
| `file-conversion` | wshobson |  |  | Convert files between formats — PDF to Word, HEIC to JPG, MP4 to MP3, CSV to JSON, EPUB to MOBI, and 999 total routes across images, video,  |
| `framework-migration-architect-review` | wshobson |  | opus | Master software architect specializing in modern architecture patterns, clean architecture, microservices, event-driven systems, and DDD. Re |
| `framework-migration-legacy-modernizer` | wshobson |  | fable | Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. Handles technical debt, dependency updates, and |
| `angular-migration` | wshobson |  |  | Migrate from AngularJS to Angular using hybrid mode, incremental component rewriting, and dependency injection updates. Use when upgrading A |
| `database-migration` | wshobson |  |  | Execute database migrations across ORMs and platforms with zero-downtime strategies, data transformation, and rollback procedures. Use when  |
| `dependency-upgrade` | wshobson |  |  | Manage major dependency version upgrades with compatibility analysis, staged rollout, and comprehensive testing. Use when upgrading framewor |
| `react-modernization` | wshobson |  |  | Upgrade React applications to latest versions, migrate from class components to hooks, and adopt concurrent features. Use when modernizing R |
| `frontend-mobile-development-frontend-developer` | wshobson |  | inherit | Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern fron |
| `frontend-mobile-development-mobile-developer` | wshobson |  | inherit | Develop React Native, Flutter, or native mobile apps with modern architecture patterns. Masters cross-platform development, native integrati |
| `nextjs-app-router-patterns` | wshobson |  |  | Master Next.js 14+ App Router with Server Components, streaming, parallel routes, and advanced data fetching. Use when building Next.js appl |
| `react-native-architecture` | wshobson |  |  | Build production React Native apps with Expo, navigation, native modules, offline sync, and cross-platform patterns. Use when developing mob |
| `react-state-management` | wshobson |  |  | Master modern React state management with Redux Toolkit, Zustand, Jotai, and React Query. Use when setting up global state, managing server  |
| `tailwind-design-system` | wshobson |  |  | Build scalable design systems with Tailwind CSS v4, design tokens, component libraries, and responsive patterns. Use when creating component |
| `frontend-mobile-security-frontend-developer` | wshobson |  | inherit | Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern fron |
| `frontend-security-coder` | wshobson |  | sonnet | Expert in secure frontend coding practices specializing in XSS prevention, output sanitization, and client-side security patterns. Use PROAC |
| `mobile-security-coder` | wshobson |  | sonnet | Expert in secure mobile coding practices specializing in input validation, WebView security, and mobile-specific security patterns. Use PROA |
| `full-stack-orchestration-deployment-engineer` | wshobson |  | haiku | Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation. Masters GitHub Acti |
| `full-stack-orchestration-performance-engineer` | wshobson |  | inherit | Expert performance engineer specializing in modern observability, application optimization, and scalable system performance. Masters OpenTel |
| `full-stack-orchestration-security-auditor` | wshobson |  | opus | Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks. Masters vulnerability assessment, |
| `full-stack-orchestration-test-automator` | wshobson |  | sonnet | Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. Build scalable testing  |
| `elixir-pro` | wshobson |  | inherit | Write idiomatic Elixir code with OTP patterns, supervision trees, and Phoenix LiveView. Masters concurrency, fault tolerance, and distribute |
| `haskell-pro` | wshobson |  | sonnet | Expert Haskell engineer specializing in advanced type systems, pure functional design, and high-reliability software. Use PROACTIVELY for ty |
| `minecraft-bukkit-pro` | wshobson |  | opus | Master Minecraft server plugin development with Bukkit, Spigot, and Paper APIs. Specializes in event-driven architecture, command systems, w |
| `unity-developer` | wshobson |  | opus | Build Unity games with optimized C# scripts, efficient rendering, and proper asset management. Masters Unity 6 LTS, URP/HDRP pipelines, and  |
| `godot-gdscript-patterns` | wshobson |  |  | Master Godot 4 GDScript patterns including signals, scenes, state machines, and optimization. Use when building Godot games, implementing ga |
| `unity-ecs-patterns` | wshobson |  |  | Master Unity ECS (Entity Component System) with DOTS, Jobs, and Burst for high-performance game development. Use when building data-oriented |
| `git-pr-workflows-code-reviewer` | wshobson |  | opus | Elite code review expert specializing in modern AI-powered code analysis, security vulnerabilities, performance optimization, and production |
| `hermes-tweet` | wshobson |  |  | Install and operate Hermes Tweet, a Hermes Agent plugin for X/Twitter research, timeline reading, tweet analysis, and approval-gated private |
| `hr-pro` | wshobson |  | sonnet | Professional, ethical HR partner for hiring, onboarding/offboarding, PTO and leave, performance, compliant policies, and employee relations. |
| `legal-advisor` | wshobson |  | sonnet | Draft privacy policies, terms of service, disclaimers, and legal notices. Creates GDPR-compliant texts, cookie policies, and data processing |
| `employment-contract-templates` | wshobson |  |  | Create employment contracts, offer letters, and HR policy documents following legal best practices. Use when drafting employment agreements, |
| `gdpr-data-handling` | wshobson |  |  | Implement GDPR-compliant data handling with consent management, data subject rights, and privacy by design. Use when building systems that p |
| `incident-response-code-reviewer` | wshobson |  | sonnet | Reviews code for logic flaws, type safety gaps, error handling issues, architectural concerns, and similar vulnerability patterns. Provides  |
| `incident-response-debugger` | wshobson |  | sonnet | Performs deep root cause analysis through code path tracing, git bisect automation, dependency analysis, and systematic hypothesis testing f |
| `incident-response-devops-troubleshooter` | wshobson |  | sonnet | Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability. Masters log analysis, di |
| `incident-response-error-detective` | wshobson |  | sonnet | Analyzes error traces, logs, and observability data to identify error signatures, reproduction steps, user impact, and timeline context for  |
| `incident-responder` | wshobson |  | sonnet | Expert SRE incident responder specializing in rapid problem resolution, modern observability, and comprehensive incident management. Masters |
| `incident-response-test-automator` | wshobson |  | sonnet | Creates comprehensive test suites including unit, integration, regression, and security tests. Validates fixes with full coverage and cross- |
| `incident-runbook-templates` | wshobson |  |  | Create structured incident response runbooks with step-by-step procedures, escalation paths, and recovery actions. Use this skill when build |
| `on-call-handoff-patterns` | wshobson |  |  | Master on-call shift handoffs with context transfer, escalation procedures, and documentation. Use this skill when transitioning on-call res |
| `postmortem-writing` | wshobson |  |  | Write effective blameless postmortems with root cause analysis, timelines, and action items. Use when conducting incident reviews, writing p |
| `javascript-pro` | wshobson |  | inherit | Master modern JavaScript with ES6+, async patterns, and Node.js APIs. Handles promises, event loops, and browser/Node compatibility. Use PRO |
| `typescript-pro` | wshobson |  | opus | Master TypeScript with advanced types, generics, and strict type safety. Handles complex type systems, decorators, and enterprise-grade patt |
| `javascript-testing-patterns` | wshobson |  |  | Implement comprehensive testing strategies using Jest, Vitest, and Testing Library for unit tests, integration tests, and end-to-end testing |
| `modern-javascript-patterns` | wshobson |  |  | Master ES6+ features including async/await, destructuring, spread operators, arrow functions, promises, modules, iterators, generators, and  |
| `nodejs-backend-patterns` | wshobson |  |  | Build production-ready Node.js backend services with Express/Fastify, implementing middleware patterns, error handling, authentication, data |
| `typescript-advanced-types` | wshobson |  |  | Master TypeScript's advanced type system including generics, conditional types, mapped types, template literals, and utility types for build |
| `julia-pro` | wshobson |  | sonnet | Master Julia 1.10+ with modern features, performance optimization, multiple dispatch, and production-ready practices. Expert in the Julia ec |
| `csharp-pro` | wshobson |  | inherit | Write modern C# code with advanced features like records, pattern matching, and async/await. Optimizes .NET applications, implements enterpr |
| `java-pro` | wshobson |  | opus | Master Java 21+ with modern features like virtual threads, pattern matching, and Spring Boot 3.x. Expert in the latest Java ecosystem includ |
| `scala-pro` | wshobson |  | inherit | Master enterprise-grade Scala development with functional programming, distributed systems, and big data processing. Expert in Apache Pekko, |
| `kubernetes-operations-kubernetes-architect` | wshobson |  | opus | Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container o |
| `gitops-workflow` | wshobson |  |  | Implement GitOps workflows with ArgoCD and Flux for automated, declarative Kubernetes deployments with continuous reconciliation. Use when i |
| `helm-chart-scaffolding` | wshobson |  |  | Design, organize, and manage Helm charts for templating and packaging Kubernetes applications with reusable configurations. Use when creatin |
| `k8s-manifest-generator` | wshobson |  |  | Create production-ready Kubernetes manifests for Deployments, Services, ConfigMaps, and Secrets following best practices and security standa |
| `k8s-security-policies` | wshobson |  |  | Implement Kubernetes security policies including NetworkPolicy, PodSecurityPolicy, and RBAC for production-grade security. Use when securing |
| `ai-engineer` | wshobson |  | inherit | Build production-ready LLM applications, advanced RAG systems, and intelligent agents. Implements vector search, multimodal AI, agent orches |
| `prompt-engineer` | wshobson |  | inherit | Expert prompt engineer specializing in advanced prompting techniques, LLM optimization, and AI system design. Masters chain-of-thought, cons |
| `vector-database-engineer` | wshobson |  | inherit | Expert in vector databases, embedding strategies, and semantic search implementation. Masters Pinecone, Weaviate, Qdrant, Milvus, and pgvect |
| `embedding-strategies` | wshobson |  |  | Select and optimize embedding models for semantic search and RAG applications. Use when choosing embedding models, implementing chunking str |
| `hybrid-search-implementation` | wshobson |  |  | Combine vector and keyword search for improved retrieval. Use when implementing RAG systems, building search engines, or when neither approa |
| `langchain-architecture` | wshobson |  |  | Design LLM applications using LangChain 1.x and LangGraph for agents, memory, and tool integration. Use when building LangChain applications |
| `llm-evaluation` | wshobson |  |  | Implement comprehensive evaluation strategies for LLM applications using automated metrics, human feedback, and benchmarking. Use when testi |
| `prompt-engineering-patterns` | wshobson |  |  | This skill should be used when the user asks to "optimize a prompt", "improve prompt performance", "design a prompt template", "write better |
| `rag-implementation` | wshobson |  |  | Build Retrieval-Augmented Generation (RAG) systems for LLM applications with vector databases and semantic search. Use when implementing kno |
| `similarity-search-patterns` | wshobson |  |  | Implement efficient similarity search with vector databases. Use when building semantic search, implementing nearest neighbor queries, or op |
| `vector-index-tuning` | wshobson |  |  | Optimize vector index performance for latency, recall, and memory. Use when tuning HNSW parameters, selecting quantization strategies, or sc |
| `llm-finetuning-architect` | wshobson |  | opus | Fine-tuning strategist who owns the eval gate and method/model selection. Refuses to plan training without a baselined eval harness. Use PRO |
| `llm-finetuning-eval-engineer` | wshobson |  | sonnet | Evaluation gatekeeper for fine-tuning — builds golden sets and graders, calibrates judges, baselines base models, and issues checkpoint prom |
| `llm-finetuning-training-engineer` | wshobson |  | sonnet | Fine-tuning implementation workhorse — prepares datasets, generates Unsloth-first training scripts, launches and monitors runs, and exports  |
| `checkpoint-promotion` | wshobson |  |  | Gate fine-tuned checkpoints with drift budgets, paired comparison, and forgetting checks before promotion. Use after a training run produces |
| `dataset-curation` | wshobson |  |  | Prepare, format, and validate datasets for supervised fine-tuning and preference training. Use when converting raw data into training format |
| `eval-harness-first` | wshobson |  |  | Build the evaluation harness that gates every fine-tuning run — golden sets, per-failure-mode graders, judge calibration, and base-model bas |
| `finetuning-method-selection` | wshobson |  |  | Decide whether to fine-tune at all, and route to the right method (SFT, DPO/ORPO/KTO, GRPO/RLVR, continued pretraining) and base model. Use  |
| `grpo-rlvr-training` | wshobson |  |  | Train reasoning and verifiable-task behavior with GRPO and reinforcement learning from verifiable rewards (RLVR). Use when task success is a |
| `lora-qlora-recipes` | wshobson |  |  | Configure LoRA and QLoRA supervised fine-tuning with current best-practice hyperparameters. Use when writing or reviewing a LoRA/QLoRA train |
| `preference-optimization` | wshobson |  |  | Align a fine-tuned model with preference data using DPO, ORPO, KTO, or SimPO. Use when preference pairs or thumbs-up/down feedback exist, wh |
| `quantized-export` | wshobson |  |  | Export a promoted fine-tuned model in the right deployment format — merged safetensors, LoRA-only, GGUF with imatrix, or FP8. Use after a ch |
| `trace-to-training-data` | wshobson |  |  | Convert evaluation traces and production logs into SFT examples and preference pairs. Use when graded traces or failure examples exist and n |
| `vision-sft` | wshobson |  |  | Fine-tune vision-language models (VLMs) with supervised learning on image+text data. Use when adapting a VLM to a visual domain or task, con |
| `data-scientist` | wshobson |  | inherit | Expert data scientist for advanced analytics, machine learning, and statistical modeling. Handles complex data analysis, predictive modeling |
| `ml-engineer` | wshobson |  | inherit | Build production ML systems with PyTorch 2.x, TensorFlow, and modern ML frameworks. Implements model serving, feature engineering, A/B testi |
| `mlops-engineer` | wshobson |  | inherit | Build comprehensive ML pipelines, experiment tracking, and model registries with MLflow, Kubeflow, and modern MLOps tools. Implements automa |
| `ml-pipeline-workflow` | wshobson |  |  | Build end-to-end MLOps pipelines from data preparation through model training, validation, and production deployment. Use when creating ML p |
| `recsys-pipeline-architect` | wshobson |  |  | Design composable recommendation, ranking, and feed pipelines using the six-stage Source→Hydrator→Filter→Scorer→Selector→SideEffect framewor |
| `gallery-researcher` | wshobson | mcp__meigen__search_gallery, mcp__meigen__get_inspiration | haiku | Gallery search and inspiration agent. Delegates here when user wants to find references, explore styles, build a mood board, or needs inspir |
| `image-generator` | wshobson | mcp__meigen__generate_image | inherit | Image generation executor agent. Delegates here for ALL generate_image calls to keep the main conversation context clean. Spawn one per imag |
| `prompt-crafter` | wshobson |  | haiku | Batch prompt writing agent. Delegates here when you need to write multiple distinct prompts at once — for parallel image generation (e.g., " |
| `multi-platform-apps-backend-architect` | wshobson |  | inherit | Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. Masters REST/GraphQL/gRPC |
| `flutter-expert` | wshobson |  | inherit | Master Flutter development with Dart 3, advanced widgets, and multi-platform deployment. Handles state management, animations, testing, and  |
| `multi-platform-apps-frontend-developer` | wshobson |  | inherit | Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern fron |
| `ios-developer` | wshobson |  | inherit | Develop native iOS applications with Swift/SwiftUI. Masters iOS 18, SwiftUI, UIKit integration, Core Data, networking, and App Store optimiz |
| `multi-platform-apps-mobile-developer` | wshobson |  | inherit | Develop React Native, Flutter, or native mobile apps with modern architecture patterns. Masters cross-platform development, native integrati |
| `ui-ux-designer` | wshobson |  | sonnet | Create interface designs, wireframes, and design systems. Masters user research, accessibility standards, and modern design tools. Specializ |
| `observability-monitoring-database-optimizer` | wshobson |  | inherit | Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures. Masters advanced indexi |
| `observability-monitoring-network-engineer` | wshobson |  | sonnet | Expert network engineer specializing in modern cloud networking, security architectures, and performance optimization. Masters multi-cloud c |
| `observability-monitoring-observability-engineer` | wshobson |  | inherit | Build production-ready monitoring, logging, and tracing systems. Implements comprehensive observability strategies, SLI/SLO management, and  |
| `observability-monitoring-performance-engineer` | wshobson |  | inherit | Expert performance engineer specializing in modern observability, application optimization, and scalable system performance. Masters OpenTel |
| `distributed-tracing` | wshobson |  |  | Implement distributed tracing with Jaeger and Tempo to track requests across microservices and identify performance bottlenecks. Use when de |
| `grafana-dashboards` | wshobson |  |  | Create and manage production Grafana dashboards for real-time visualization of system and application metrics. Use when building monitoring  |
| `prometheus-configuration` | wshobson |  |  | Set up Prometheus for comprehensive metric collection, storage, and monitoring of infrastructure and applications. Use when implementing met |
| `slo-implementation` | wshobson |  |  | Define and implement Service Level Indicators (SLIs) and Service Level Objectives (SLOs) with error budgets and alerting. Use when establish |
| `code-review-preshipment` | wshobson | Bash, Read, Glob, Grep | sonnet | Comprehensive pre-ship review of all changes since the last deploy or a specified commit. Walks correctness, atomicity and race conditions,  |
| `deploy-with-verification` | wshobson | Bash, Read, Edit | sonnet | Use when deploying to production. Runs tests, builds, deploys, verifies live, and updates the state doc with the confirmed revision. Stops i |
| `prod-logs-health-check` | wshobson | Bash, Read | haiku | Pulls recent production logs filtered for errors, warnings, and anomalies. Use after any deploy, after a load test, or any time you suspect  |
| `session-end` | wshobson | Read, Edit, Bash | haiku | Use at the end of every significant work session. Finalizes the session — lessons, open issues, next steps, and any state not already writte |
| `session-start` | wshobson | Read, Bash, Edit | haiku | Use at the start of every work session. Reads the canonical state doc, verifies live state, reconciles drift from external deploys or dirty  |
| `payment-integration` | wshobson |  | sonnet | Integrate Stripe, PayPal, and payment processors. Handles checkout flows, subscriptions, webhooks, and PCI compliance. Use PROACTIVELY when  |
| `billing-automation` | wshobson |  |  | Build automated billing systems for recurring payments, invoicing, subscription lifecycle, and dunning management. Use when implementing sub |
| `paypal-integration` | wshobson |  |  | Integrate PayPal payment processing with support for express checkout, subscriptions, and refund management. Use when implementing PayPal pa |
| `pci-compliance` | wshobson |  |  | Implement PCI DSS compliance requirements for secure handling of payment card data and payment systems. Use when securing payment processing |
| `stripe-integration` | wshobson |  |  | Implement Stripe payment processing for robust, PCI-compliant payment flows including checkout, subscriptions, and webhooks. Use when integr |
| `performance-testing-review-performance-engineer` | wshobson |  | inherit | Expert performance engineer specializing in modern observability, application optimization, and scalable system performance. Masters OpenTel |
| `performance-testing-review-test-automator` | wshobson |  | sonnet | Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. Build scalable testing  |
| `eval-judge` | wshobson | Read, Grep, Glob | sonnet | LLM judge for plugin quality assessment. Scores skills on triggering accuracy, orchestration fitness, output quality, and scope calibration  |
| `eval-orchestrator` | wshobson |  | opus | Orchestrates plugin quality evaluation. Use PROACTIVELY when evaluating, scoring, or certifying plugin quality. |
| `evaluation-methodology` | wshobson |  |  | PluginEval quality methodology — dimensions, rubrics, statistical methods, and scoring formulas. Use this skill when understanding how plugi |
| `pptx-deck-creation-builder` | wshobson |  | inherit | Use when creating, repairing, or auditing a production-ready editable PowerPoint (PPTX) deck from a brief, source material, or reference dec |
| `pptx-deck-context` | wshobson |  |  | Use when preparing the narrative, sources, and design context for a new editable PPTX deck. |
| `pptx-quality-gates` | wshobson |  |  | Use when validating or repairing an editable PPTX deck for geometry, accessibility, native editability, source lineage, and OOXML package in |
| `pptx-reference-deck-analysis` | wshobson |  |  | Use when analyzing a reference PPTX for read-only structure, theme, typography, layout rhythm, diagnostics, derived template catalogs, or sa |
| `pptx-slide-specification` | wshobson |  |  | Use when authoring or repairing a coordinate-explicit JSON specification for an editable PPTX deck. |
| `pptx-visual-assets` | wshobson |  |  | Use when selecting and placing approved supporting icons, images, SVGs, diagrams, or infographics in an editable PPTX deck. |
| `policy-enforcer` | wshobson |  | opus | Cedar policy author and reviewer for Claude Code tool calls. Writes, audits, and explains Cedar policies that govern Bash, Edit, Write, WebF |
| `receipt-verifier` | wshobson |  | sonnet | Expert in Ed25519 signed receipts, JCS canonicalization, hash chains, and offline verification. Use when you need to verify receipt authenti |
| `protect-mcp-setup` | wshobson |  |  | Configure Cedar policy enforcement and Ed25519 signed receipts for Claude Code tool calls. Use when setting up projects that need cryptograp |
| `python-development-django-pro` | wshobson |  | opus | Master Django 5.x with async views, DRF, Celery, and Django Channels. Build scalable web applications with proper architecture, testing, and |
| `python-development-fastapi-pro` | wshobson |  | opus | Build high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. Master microservices, WebSockets, and modern Python async p |
| `python-pro` | wshobson |  | opus | Master Python 3.12+ with modern features, async programming, performance optimization, and production-ready practices. Expert in the latest  |
| `async-python-patterns` | wshobson |  |  | Master Python asyncio, concurrent programming, and async/await patterns for high-performance applications. Use when building async APIs, con |
| `python-anti-patterns` | wshobson |  |  | Use this skill when reviewing Python code for common anti-patterns to avoid. Use as a checklist when reviewing code, before finalizing imple |
| `python-background-jobs` | wshobson |  |  | Python background job patterns including task queues, workers, and event-driven architecture. Use when implementing async task processing, j |
| `python-code-style` | wshobson |  |  | Python code style, linting, formatting, naming conventions, and documentation standards. Use when writing new code, reviewing style, configu |
| `python-configuration` | wshobson |  |  | Python configuration management via environment variables and typed settings. Use when externalizing config, setting up pydantic-settings, m |
| `python-design-patterns` | wshobson |  |  | Python design patterns including KISS, Separation of Concerns, Single Responsibility, and composition over inheritance. Use this skill when  |
| `python-error-handling` | wshobson |  |  | Python error handling patterns including input validation, exception hierarchies, and partial failure handling. Use when implementing valida |
| `python-observability` | wshobson |  |  | Python observability patterns including structured logging, metrics, and distributed tracing. Use when adding logging, implementing metrics  |
| `python-packaging` | wshobson |  |  | Create distributable Python packages with proper project structure, setup.py/pyproject.toml, and publishing to PyPI. Use when packaging Pyth |
| `python-performance-optimization` | wshobson |  |  | Profile and optimize Python code using cProfile, memory profilers, and performance best practices. Use when debugging slow Python code, opti |
| `python-project-structure` | wshobson |  |  | Python project organization, module architecture, and public API design. Use when setting up new projects, organizing modules, defining publ |
| `python-resilience` | wshobson |  |  | Python resilience patterns including automatic retries, exponential backoff, timeouts, and fault-tolerant decorators. Use when adding retry  |
| `python-resource-management` | wshobson |  |  | Python resource management with context managers, cleanup patterns, and streaming. Use when managing connections, file handles, implementing |
| `python-testing-patterns` | wshobson |  |  | Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development. Use when writing Python tests, setti |
| `python-type-safety` | wshobson |  |  | Python type safety with type hints, generics, protocols, and strict type checking. Use when adding type annotations, implementing generic cl |
| `uv-package-manager` | wshobson |  |  | Master the uv package manager for fast Python dependency management, virtual environments, and modern Python project workflows. Use when set |
| `quant-analyst` | wshobson |  | inherit | Build financial models, backtest trading strategies, and analyze market data. Implements risk metrics, portfolio optimization, and statistic |
| `risk-manager` | wshobson |  | inherit | Monitor portfolio risk, R-multiples, and position limits. Creates hedging strategies, calculates expectancy, and implements stop-losses. Use |
| `backtesting-frameworks` | wshobson |  |  | Build robust backtesting systems for trading strategies with proper handling of look-ahead bias, survivorship bias, and transaction costs. U |
| `risk-metrics-calculation` | wshobson |  |  | Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. Use when measuring portfolio risk, implementin |
| `firmware-analyst` | wshobson |  | opus | Expert firmware analyst specializing in embedded systems, IoT security, and hardware reverse engineering. Masters firmware extraction, analy |
| `malware-analyst` | wshobson |  | opus | Expert malware analyst specializing in defensive malware research, threat intelligence, and incident response. Masters sandbox analysis, beh |
| `reverse-engineer` | wshobson |  | opus | Expert reverse engineer specializing in binary analysis, disassembly, decompilation, and software analysis. Masters IDA Pro, Ghidra, radare2 |
| `anti-reversing-techniques` | wshobson |  |  | Understand anti-reversing, obfuscation, and protection techniques encountered during software analysis. Use this skill when analyzing malwar |
| `binary-analysis-patterns` | wshobson |  |  | Master binary analysis patterns including disassembly, decompilation, control flow analysis, and code pattern recognition. Use when analyzin |
| `memory-forensics` | wshobson |  |  | Master memory forensics techniques including memory acquisition, process analysis, and artifact extraction using Volatility and related tool |
| `protocol-reverse-engineering` | wshobson |  |  | Master network protocol reverse engineering including packet analysis, protocol dissection, and custom protocol documentation. Use when anal |
| `review-policy-author` | wshobson |  | sonnet | Cedar policy author specialized in gating AI agent review actions (PR comments, reviews, merges, CI edits) behind human approval. Use when w |
| `review-agent-setup` | wshobson |  |  | Configure human-in-the-loop gating for AI agent review actions in Claude Code. Use when setting up a project where an agent may post PR revi |
| `security-compliance-security-auditor` | wshobson |  | opus | Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks. Masters vulnerability assessment, |
| `security-scanning-security-auditor` | wshobson |  | opus | Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks. Masters vulnerability assessment, |
| `threat-modeling-expert` | wshobson |  | opus | Expert in threat modeling methodologies, security architecture review, and risk assessment. Masters STRIDE, PASTA, attack trees, and securit |
| `security-sast` | wshobson |  |  | Static Application Security Testing (SAST) for code vulnerability analysis across multiple languages and frameworks |
| `attack-tree-construction` | wshobson |  |  | Build comprehensive attack trees to visualize threat paths. Use when mapping attack scenarios, identifying defense gaps, or communicating se |
| `sast-configuration` | wshobson |  |  | Configure Static Application Security Testing (SAST) tools for automated vulnerability detection in application code. Use when setting up se |
| `security-requirement-extraction` | wshobson |  |  | Derive security requirements from threat models and business context. Use when translating threats into actionable requirements, creating se |
| `stride-analysis-patterns` | wshobson |  |  | Apply STRIDE methodology to systematically identify threats. Use when analyzing system security, conducting threat modeling sessions, or cre |
| `threat-mitigation-mapping` | wshobson |  |  | Map identified threats to appropriate security controls and mitigations. Use when prioritizing security investments, creating remediation pl |
| `seo-authority-builder` | wshobson |  | sonnet | Analyzes content for E-E-A-T signals and suggests improvements to build authority and trust. Identifies missing credibility elements. Use PR |
| `seo-cannibalization-detector` | wshobson |  | haiku | Analyzes multiple provided pages to identify keyword overlap and potential cannibalization issues. Suggests differentiation strategies. Use  |
| `seo-content-refresher` | wshobson |  | haiku | Identifies outdated elements in provided content and suggests updates to maintain freshness. Finds statistics, dates, and examples that need |
| `seo-content-auditor` | wshobson |  | sonnet | Analyzes provided content for quality, E-E-A-T signals, and SEO best practices. Scores content and provides improvement recommendations base |
| `seo-content-planner` | wshobson |  | haiku | Creates comprehensive content outlines and topic clusters for SEO. Plans content calendars and identifies topic gaps. Use PROACTIVELY for co |
| `seo-content-writer` | wshobson |  | sonnet | Writes SEO-optimized content based on provided keywords and topic briefs. Creates engaging, comprehensive content following best practices.  |
| `seo-keyword-strategist` | wshobson |  | haiku | Analyzes keyword usage in provided content, calculates density, suggests semantic variations and LSI keywords based on the topic. Prevents o |
| `seo-meta-optimizer` | wshobson |  | haiku | Creates optimized meta titles, descriptions, and URL suggestions based on character limits and best practices. Generates compelling, keyword |
| `seo-snippet-hunter` | wshobson |  | haiku | Formats content to be eligible for featured snippets and SERP features. Creates snippet-optimized content blocks based on best practices. Us |
| `seo-structure-architect` | wshobson |  | haiku | Analyzes and optimizes content structure including header hierarchy, suggests schema markup, and internal linking opportunities. Creates sea |
| `bash-pro` | wshobson |  | sonnet | Master of defensive Bash scripting for production automation, CI/CD pipelines, and system utilities. Expert in safe, portable, and testable  |
| `posix-shell-pro` | wshobson |  | sonnet | Expert in strict POSIX sh scripting for maximum portability across Unix-like systems. Specializes in shell scripts that run on any POSIX-com |
| `bash-defensive-patterns` | wshobson |  |  | Master defensive Bash programming techniques for production-grade scripts. Use when writing robust shell scripts, CI/CD pipelines, or system |
| `bats-testing-patterns` | wshobson |  |  | Master Bash Automated Testing System (Bats) for comprehensive shell script testing. Use when writing tests for shell scripts, CI/CD pipeline |
| `shellcheck-configuration` | wshobson |  |  | Master ShellCheck static analysis configuration and usage for shell script quality. Use when setting up linting infrastructure, fixing code  |
| `architect` | wshobson |  | inherit | Architect agent. Reads orchestrator-output.md, AGENTS.md, and project-doc.md to produce a numbered step-by-step implementation plan. Pauses  |
| `implement` | wshobson |  | sonnet | Developer agent. Implements the architect plan step-by-step, guided by AGENTS.md guardrails. Writes tests, leaves no TODOs, and flags plan d |
| `orchestrate` | wshobson |  | sonnet | Product Orchestrator agent. Reads the active story file, asks clarifying product questions one at a time, confirms task type (FRONTEND/BACKE |
| `playwright` | wshobson |  | sonnet | Playwright testing agent. Only runs for FRONTEND tasks. Verifies acceptance criteria in a real browser using the page object pattern. Passes |
| `qa` | wshobson |  | sonnet | QA Agent. Tests all acceptance criteria and edge cases from orchestrator-output.md. Generates a structured qa-report.md with pass/fail per c |
| `review` | wshobson |  | inherit | PR Reviewer agent. Reviews implemented code using a 3-tier taxonomy (🔴 Critical / 🟡 Should Fix / 💡 Consider). Auto-resolves minor issues, pa |
| `scan` | wshobson |  |  | Scans the codebase to generate project-doc.md and AGENTS.md. Use when bootstrapping a new agent-driven repo, refreshing project documentatio |
| `signed-audit-trails-recipe` | wshobson |  |  | Step-by-step cookbook for setting up cryptographically signed audit trails on Claude Code tool calls. Use when explaining, evaluating, or de |
| `ai-debt-detector` | wshobson |  |  | Use after generating code, after accepting AI suggestions, or when reviewing AI-written modules. Also use when code works but feels brittle, |
| `session-guard` | wshobson |  |  | Use when working on complex multi-step tasks, when a session is getting long (40+ tool calls), when the agent starts ignoring rules it follo |
| `visual-edit-precision` | wshobson |  |  | Use when making UI/frontend changes guided by visual context, when the user selects elements visually, draws annotations, or provides screen |
| `social-publishing-publisher` | wshobson | Read, Write, Bash, WebFetch | haiku | Agent-first social media publishing specialist. Use this agent to schedule and publish posts across 13 platforms (X, LinkedIn, Instagram, Fa |
| `social-publishing` | wshobson |  |  | Schedule and publish social media posts across 13 platforms (X, LinkedIn, Instagram, Facebook Pages, TikTok, Discord, Telegram, YouTube, Red |
| `startup-analyst` | wshobson |  | inherit | Expert startup business analyst specializing in market sizing, financial modeling, competitive analysis, and strategic planning for early-st |
| `competitive-landscape` | wshobson |  |  | Analyze competition, identify differentiation opportunities, and develop winning market positioning strategies using Porter's Five Forces, B |
| `market-sizing-analysis` | wshobson |  |  | Calculate TAM/SAM/SOM for market opportunities using top-down, bottom-up, and value theory methodologies. Use this skill when sizing markets |
| `startup-financial-modeling` | wshobson |  |  | Build comprehensive 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for early |
| `startup-metrics-framework` | wshobson |  |  | Track, calculate, and optimize key performance metrics for SaaS, marketplace, consumer, and B2B startups from seed through Series A, includi |
| `team-composition-analysis` | wshobson |  |  | Design optimal team structures, hiring plans, compensation strategies, and equity allocation for early-stage startups from pre-seed through  |
| `superself` | wshobson |  |  | Use when a project keeps its state in Superself (a `<!-- superself:begin` block in AGENTS.md or CLAUDE.md, or `self setup` resolves the dire |
| `c-pro` | wshobson |  | opus | Write efficient C code with proper memory management, pointer arithmetic, and system calls. Handles embedded systems, kernel modules, and pe |
| `cpp-pro` | wshobson |  | opus | Write idiomatic C++ code with modern features, RAII, smart pointers, and STL algorithms. Handles templates, move semantics, and performance  |
| `golang-pro` | wshobson |  | opus | Master Go 1.21+ with modern patterns, advanced concurrency, performance optimization, and production-ready microservices. Expert in the late |
| `rust-pro` | wshobson |  | opus | Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming. Expert in the latest  |
| `go-concurrency-patterns` | wshobson |  |  | Master Go concurrency with goroutines, channels, sync primitives, and context. Use when building concurrent Go applications, implementing wo |
| `memory-safety-patterns` | wshobson |  |  | Implement memory-safe programming with RAII, ownership, smart pointers, and resource management across Rust, C++, and C. Use when writing sa |
| `rust-async-patterns` | wshobson |  |  | Master Rust async programming with Tokio, async traits, error handling, and concurrent patterns. Use when building async Rust applications,  |
| `tdd-workflows-code-reviewer` | wshobson |  | opus | Elite code review expert specializing in modern AI-powered code analysis, security vulnerabilities, performance optimization, and production |
| `tdd-workflows-tdd-orchestrator` | wshobson |  | opus | Master TDD orchestrator specializing in red-green-refactor discipline, multi-agent workflow coordination, and comprehensive test-driven deve |
| `team-collaboration-dx-optimizer` | wshobson |  | sonnet | Developer Experience specialist. Improves tooling, setup, and workflows. Use PROACTIVELY when setting up new projects, after team feedback,  |
| `accessibility-expert` | wshobson |  | inherit | Expert accessibility specialist ensuring WCAG compliance, inclusive design, and assistive technology compatibility. Masters screen reader op |
| `design-system-architect` | wshobson |  | inherit | Expert design system architect specializing in design tokens, component libraries, theming infrastructure, and scalable design operations. M |
| `ui-designer` | wshobson |  | inherit | Expert UI designer specializing in component creation, layout systems, and visual design implementation. Masters modern design patterns, res |
| `accessibility-compliance` | wshobson |  |  | Implement WCAG 2.2 compliant interfaces with mobile accessibility, inclusive design patterns, and assistive technology support. Use when aud |
| `design-system-patterns` | wshobson |  |  | Build scalable design systems with design tokens, theming infrastructure, and component architecture patterns. Use when creating design toke |
| `interaction-design` | wshobson |  |  | Design and implement microinteractions, motion design, transitions, and user feedback patterns. Use when adding polish to UI interactions, i |
| `mobile-android-design` | wshobson |  |  | Master Material Design 3 and Jetpack Compose patterns for building native Android apps. Use when designing Android interfaces, implementing  |
| `mobile-ios-design` | wshobson |  |  | Master iOS Human Interface Guidelines and SwiftUI patterns for building native iOS apps. Use when designing iOS interfaces, implementing Swi |
| `react-native-design` | wshobson |  |  | Master React Native styling, navigation, and Reanimated animations for cross-platform mobile development. Use when building React Native app |
| `responsive-design` | wshobson |  |  | Implement modern responsive layouts using container queries, fluid typography, CSS Grid, and mobile-first breakpoint strategies. Use when bu |
| `visual-design-foundations` | wshobson |  |  | Apply typography, color theory, spacing systems, and iconography principles to create cohesive visual designs. Use when establishing design  |
| `web-component-design` | wshobson |  |  | Master React, Vue, and Svelte component patterns including CSS-in-JS, composition strategies, and reusable component architecture. Use when  |
| `unit-testing-debugger` | wshobson |  | sonnet | Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues. |
| `unit-testing-test-automator` | wshobson |  | sonnet | Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. Build scalable testing  |
| `php-pro` | wshobson |  | inherit | Write idiomatic PHP code with generators, iterators, SPL data structures, and modern OOP features. Use PROACTIVELY for high-performance PHP  |
| `ruby-pro` | wshobson |  | inherit | Write idiomatic Ruby code with metaprogramming, Rails patterns, and performance optimization. Specializes in Ruby on Rails, gem development, |
