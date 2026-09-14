---
name: tf-quant-finance
description: Google's TensorFlow-based library for quantitative finance. Use when pricing derivatives (vanilla/American/Asian/barrier options, swaptions, interest rate caps/floors) under Black-Scholes, Heston, SABR, Hull-White, HJM, or CIR models, when solving PDEs (finite-difference) or running GPU/TPU-accelerated Monte Carlo simulations of Ito processes, when constructing or bootstrapping yield/swap curves (Hagan-West, monotone convex, Nelson-Siegel-Svensson), or when doing date/schedule/day-count calendar math for financial instruments. Requires a TensorFlow installation, so it is heavier than pandas-based finance libraries — prefer it only when you need automatic differentiation (Greeks via autodiff), vectorized batch pricing, or GPU acceleration; for simple scalar Black-Scholes formulas or data wrangling, a lighter library is usually a better fit. Note the upstream repo is archived (no longer maintained by Google) but remains usable and pip-installable.
license: Apache-2.0
---

# tf-quant-finance

Vendored from [google/tf-quant-finance](https://github.com/google/tf-quant-finance) (Apache-2.0, ~5,500 stars). Source lives in `tf_quant_finance/` (test files, `BUILD` Bazel files, Jupyter notebooks, the Docker/k8s demo app under `examples/demos/`, and PDF guides were stripped to keep this skill lean and readable — none of it is needed to use the library from Python).

> **Archived project.** As of the vendored snapshot, Google no longer maintains this library (the README carries an "ARCHIVED" notice suggesting users fork it for further development). It still installs and runs fine via pip, and the math/pricing code is stable, well-tested numerical code — just don't expect new features or bug fixes upstream. If you need active maintenance, weigh that against forking.

## What it is

TF Quant Finance provides TensorFlow-accelerated building blocks across three tiers:

1. **Foundational math** (`tf_quant_finance/math/`) — root finders (Newton, Brent), optimizers, linear/cubic/2D interpolation, numerical integration (Gauss-Legendre, Gauss-Kronrod, Simpson), quasi-random sequences (Sobol, Halton, lattice rules), PDE finite-difference solvers and steppers, automatic differentiation helpers.
2. **Mid-level methods** (`tf_quant_finance/models/`) — a general Ito process framework with Euler/Milstein path samplers, and concrete stochastic processes: Geometric Brownian Motion, Heston, SABR, Hull-White (1-factor and vector), Gaussian/Quasi-Gaussian HJM, CIR, Longstaff-Schwartz (American option Monte Carlo).
3. **Pricing & instruments** (`tf_quant_finance/black_scholes/`, `tf_quant_finance/rates/`, `tf_quant_finance/experimental/`) — closed-form and semi-analytic pricers (Black-Scholes vanilla/binary/Asian/barrier, American options via Bjerksund-Stensland/Andersen-Lake), implied volatility solvers, swap/bond/cap-floor pricing, and yield-curve construction (Hagan-West bootstrapping, monotone convex interpolation, Nelson-Siegel-Svensson).

Because it's built on TensorFlow, every function operates on batched tensors, supports `tf.function`/XLA compilation for speed, runs on GPU/TPU without code changes, and gets Greeks for free via `tf.GradientTape` autodiff instead of finite-difference bumping.

## When this is (and isn't) the right tool

**Use it when:**
- You need to price large batches of instruments at once (vectorized over strikes/expiries/vols) — much faster than looping in a pandas/numpy pricer.
- You want Greeks via automatic differentiation rather than hand-derived formulas or bump-and-reprice.
- You need GPU acceleration for Monte Carlo simulation of SDEs (e.g., thousands of paths for exotic payoff pricing) or for solving PDEs.
- You're building yield curves from swap quotes and want a robust, tested bootstrapping/optimization routine (Hagan-West).

**Skip it when:**
- You just need one-off scalar Black-Scholes/Greeks — a small closed-form implementation or a lighter library avoids pulling in TensorFlow (a multi-hundred-MB dependency with its own version/CUDA compatibility concerns).
- Your workflow is primarily data wrangling, backtesting, or portfolio analytics on pandas DataFrames — see `finance-toolkit-lib`, `finance-shashankvemuri`, or `gs-quant`'s `timeseries` module in this same `finance-tools` directory for that.
- You need active upstream support — this project is archived; you're on your own for new TensorFlow version compatibility issues.

## Installation

```bash
pip install --upgrade tensorflow   # install TF first; not a transitive dep by design
pip install --upgrade tf-quant-finance
```

Requires Python 3.7+ and TensorFlow >= 2.7 (per the vendored README; in practice pin to a TF version known to work with your CUDA/driver stack, since the project is no longer updated for newer TF releases). For the vendored copy in this skill, treat `tf_quant_finance/` as reference source to read/search — install the real package from PyPI to run code.

## Key modules and usage patterns

### Black-Scholes pricing (`tf_quant_finance.black_scholes`)

```python
import numpy as np
import tf_quant_finance as tff

# Price a batch of 5 vanilla call options.
volatilities = np.array([0.0001, 102.0, 2.0, 0.1, 0.4])
forwards = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
strikes = np.array([3.0])       # broadcasts to shape [5]
expiries = 1.0                  # broadcasts to shape [5]

prices = tff.black_scholes.option_price(
    volatilities=volatilities,
    strikes=strikes,
    expiries=expiries,
    forwards=forwards)
```

Implied volatility (Newton root-finder, seeded by the Radoicic-Stefanica closed-form approximation):

```python
implied_vols = tff.black_scholes.implied_vol(
    prices=prices,
    strikes=strikes,
    expiries=expiries,
    forwards=forwards,
    is_call_options=np.array([True] * 5))
```

Other pricers in this module: `barrier_price`, `binary_price`, `asian_option_price`, `swaption_price`, `variance_swap_fair_strike`, and American-option approximations under `tf_quant_finance.black_scholes.approximations` (Bjerksund-Stensland, Andersen-Lake).

### Stochastic models & Monte Carlo (`tf_quant_finance.models`)

```python
import tf_quant_finance as tff

process = tff.models.GeometricBrownianMotion(mean_drift=0.05, volatility=0.2, dtype=tf.float64)
paths = process.sample_paths(
    times=[0.1, 0.5, 1.0],
    num_samples=100000,
    initial_state=100.0)
```

Also available: `tff.models.HestonModel`, `tff.models.hull_white.HullWhiteModel1F` / `VectorHullWhiteModel`, `tff.models.hjm.GaussianHJM` / `QuasiGaussianHJM`, `tff.models.sabr.SabrModel`, `tff.models.CirModel`, and Longstaff-Schwartz least-squares Monte Carlo (`tff.models.longstaff_schwartz`) for American-style exercise.

### PDE solvers (`tf_quant_finance.math.pde`)

Finite-difference solvers for linear parabolic PDEs (e.g., the Black-Scholes PDE), with a family of time-stepping schemes (explicit, implicit, Crank-Nicolson, Douglas ADI) under `tf_quant_finance.math.pde.steppers`. Entry point is `tff.math.pde.fd_solvers.solve_backward` (and `solve_forward`); see `tf_quant_finance/math/pde/README.md` in the vendored source, which points to a fuller PDF guide upstream (`pde_solvers.pdf`, not vendored here — fetch it from the GitHub repo if you need the full derivation).

### Yield/swap curve construction (`tf_quant_finance.rates`)

```python
import numpy as np
import tf_quant_finance as tff

dtype = np.float64
# Set up cashflow times/day-count fractions/PVs for a set of vanilla swaps,
# then fit a zero curve so that repricing the swaps matches market PVs:
curve = tff.rates.swap_curve_fit(
    float_leg_start_times=float_leg_start_times,
    float_leg_end_times=float_leg_end_times,
    float_leg_daycount_fractions=float_leg_daycount_fractions,
    fixed_leg_start_times=fixed_leg_start_times,
    fixed_leg_end_times=fixed_leg_end_times,
    fixed_leg_daycount_fractions=fixed_leg_daycount_fractions,
    fixed_leg_cashflows=fixed_leg_cashflows,
    present_values=present_values,
    initial_curve_rates=initial_curve_rates)
# curve.rates and curve.times give the fitted zero rates and their tenors.
```

Full worked example with 1Y/2Y/3Y/4Y LIBOR swaps is in the docstring of `tf_quant_finance/rates/swap_curve_fit.py`. Also available: `tf_quant_finance.rates.hagan_west` (bond-curve bootstrapping, monotone convex interpolation), `tf_quant_finance.rates.nelson_seigel_svensson`, and `tf_quant_finance.rates.analytics` (cashflow/forward/swap valuation helpers).

### Dates and schedules (`tf_quant_finance.datetime`)

Vectorized `DateTensor`, business-day conventions, holiday calendars, day-count conventions (ACT/360, 30/360, etc.), and schedule generation for building instrument cashflow schedules — see `tf_quant_finance/datetime/README.md`.

### Experimental (`tf_quant_finance.experimental`)

Instrument definitions (bonds, swaps, caps/floors, FRAs, eurodollar futures) and a fuller "pricing platform" framework under `tf_quant_finance/experimental/pricing_platform/` (includes `.proto` schema definitions for instruments — not compiled here; you'd need `protoc` to regenerate the Python bindings if you want to use that sub-framework directly). Also: local volatility and local-stochastic-volatility model calibration, SVI parameterization/calibration for vol surfaces, and Longstaff-Schwartz variants.

## Source layout

```
tf-quant-finance/
├── LICENSE                    # Apache-2.0
├── README.md                  # upstream README (includes the archived-project notice)
└── tf_quant_finance/
    ├── black_scholes/         # closed-form/semi-analytic option pricing, implied vol
    │   └── approximations/    # American option approximations (Bjerksund-Stensland, etc.)
    ├── datetime/               # DateTensor, holiday calendars, day-counts, schedules
    ├── math/
    │   ├── integration/       # Gauss-Legendre, Gauss-Kronrod, Simpson quadrature
    │   ├── interpolation/     # linear, cubic, 2D interpolation
    │   ├── optimizer/         # conjugate gradient, etc.
    │   ├── pde/               # finite-difference PDE solvers
    │   │   └── steppers/      # explicit/implicit/Crank-Nicolson/Douglas ADI schemes
    │   ├── qmc/                # quasi-Monte Carlo: Sobol, digital nets, lattice rules
    │   ├── random_ops/        # Sobol, Halton, multivariate normal sampling
    │   └── root_search/       # Newton, Brent root finders
    ├── models/                 # Ito process framework + concrete models
    │   ├── cir/, heston/, hull_white/, hjm/, sabr/, geometric_brownian_motion/
    │   └── longstaff_schwartz/ # American-option least-squares Monte Carlo
    ├── rates/                  # swap curve fitting/bootstrapping, analytics
    │   ├── hagan_west/         # Hagan-West bootstrapping, monotone convex
    │   └── nelson_seigel_svensson/
    ├── experimental/           # instrument definitions, pricing platform, local vol/SVI
    ├── types/                  # shared type aliases (RealTensor, BoolTensor, ...)
    └── utils/                  # shape/dataclass/tf-function helpers
```

Stripped from the vendored copy: all `*_test.py` files, `BUILD` Bazel build files, Jupyter notebook tutorials (`*.ipynb`), PDF guides, and the Docker/Kubernetes demo microservice under `tf_quant_finance/examples/demos/` — none of these are needed to import and use the library, and the notebooks/demo are more easily viewed on the [live GitHub repo](https://github.com/google/tf-quant-finance).
