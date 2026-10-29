---
name: financepy
description: "Price and risk-manage financial derivatives with the FinancePy Python library — fixed-income (bonds, bond options, mortgages, convertibles), interest rate products (swaps, swaptions, caps/floors, FRAs, IBOR/OIS curves), equity derivatives (vanilla/American/Asian/barrier/variance options), FX derivatives (vanilla/barrier/digital FX options), and credit derivatives (CDS, CDS indices, CDS baskets/tranches). Use when a task needs to build discount/credit curves, value or risk a derivative, compute Greeks, or price a bond/swap/option analytically or via trees/Monte Carlo. License: GPL-3.0 (copyleft) — see the License section below before using this in code you plan to distribute."
license: GPL-3.0
---

# financepy

Vendored from [domokane/FinancePy](https://github.com/domokane/FinancePy).

## License

**This skill is GPL-3.0 (copyleft) — different from the sibling finance skills in this
directory (`finance-database`, `finance-toolkit-lib`, `finance-shashankvemuri`, `gs-quant`),
which are MIT/Apache licensed.** The full license text is vendored as-is in `LICENSE`.

What this means in practice:

- FinancePy itself is free to use, per the GPL-3.0 terms.
- Under GPL-3.0, a work that **links against or incorporates** FinancePy and is then
  **distributed** (shipped as a product, published as a library, deployed as software
  handed to a third party) generally must itself be licensed under GPL-3.0 (or a compatible
  copyleft license) and have its source made available. This is the "copyleft" / viral
  clause that MIT and Apache-licensed code does not carry.
- Purely internal use (e.g., running FinancePy in-house for analysis, research, or as part
  of a service you don't distribute as software) does not typically trigger the copyleft
  distribution obligation, but SaaS/AGPL-adjacent nuances and your organization's own policy
  should still be checked with counsel if this matters to you.
- **If you use this skill to generate code that will be distributed** — a package, a binary,
  an open-source repo, a commercial product shipped to customers — be aware that any code
  derived from or importing FinancePy may need to comply with GPL-3.0 obligations (source
  disclosure, same-license redistribution). This is unlike the other finance skills in this
  repo, which impose no such requirement.

When in doubt, treat FinancePy as appropriate for internal analytics, research, prototyping,
and education, and flag GPL-3.0 compliance as a explicit checklist item before shipping
anything that embeds it.

## What it does

FinancePy is a Python library for pricing and risk-managing derivatives, written to be
readable (pure Python) while achieving C++-like speed via Numba JIT compilation. Coverage
spans:

- **Fixed income** — government/corporate bonds, bond options, callable/puttable bonds,
  convertibles, FRNs, mortgages, bond futures, amortizing bonds
- **Rates** — IBOR/OIS deposits, FRAs, IBOR & OIS swaps, basis swaps, caps/floors,
  European/Bermudan swaptions, single- and dual-curve bootstrapping, curve risk engines
- **Equity derivatives** — vanilla/American/Asian/barrier/basket/digital/variance-swap
  options, under Black-Scholes and other models
- **FX derivatives** — vanilla, barrier, digital, and variance-swap FX options, FX vol
  surfaces (including the "plus" smile-consistent variant)
- **Credit derivatives** — single-name CDS, CDS curves (survival-probability
  bootstrapping), CDS index products, CDS baskets/tranches, CDS options
- **Market objects** — discount curve construction (flat, Nelson-Siegel, NS-Svensson,
  piecewise flat/linear forward, polynomial, zero-rate, Hagan-West monotone convex,
  bond bootstrap/parametric), inflation index/swap curves, volatility curves/surfaces
- **Models** — Black, Black-Scholes (analytic, MC, trees), Bachelier, BDT/BK/HW/Vasicek
  short-rate trees, Heston, SABR (lognormal/normal/shifted), CEV, Merton jump-diffusion,
  Dupire local vol, SVI/SSVI and lognormal-mixture vol surfaces, and Monte Carlo engines
  (with Sobol quasi-random sequences)
- **Utils** — `Date` (with day-count conventions, business-day calendars, holiday
  schedules), schedule generation, currency/frequency/day-count enums, financial math
  helpers

The design principle is **VALUATION = PRODUCT + MODEL + MARKET**: a product object's
`.value()` method takes a model and a market (curve/vol surface) to produce a price.

Only `financepy.utils` re-exports names; the `products/*` and `market/curves` subpackages
are lazy (`EAGER_IMPORTS = False`) and `models`/`market` export nothing at package level,
so import classes from their defining modules, e.g.
`from financepy.products.bonds.bond import Bond`.

## Installation

```bash
pip install financepy
# upgrade:
pip install --upgrade financepy
```

Dependencies: NumPy, Numba, SciPy. First import after install can take several seconds
because Numba JIT-compiles the numerical kernels on first use; subsequent imports are fast
since the compiled code is cached.

```python
from financepy.utils import *

# sanity check
Date(19, 2, 2026).add_days(2)
# -> 21-FEB-2026
```

## Usage examples

### Pricing a bond

```python
from financepy.utils import *
from financepy.products.bonds.bond import Bond

issue_dt = Date(13, 5, 2010)
maturity_dt = Date(13, 5, 2022)
coupon = 0.027                                   # 2.7% annualised coupon
freq_type = FrequencyTypes.SEMI_ANNUAL
dc_type = DayCountTypes.THIRTY_E_360

bond = Bond(issue_dt, maturity_dt, coupon, freq_type, dc_type)

settle_dt = Date(21, 7, 2017)
bond.print_payments(settle_dt)
print("Accrued =", bond.accrued_interest(settle_dt))

# yield/price conversion
clean_price = bond.clean_price_from_ytm(settle_dt, ytm=0.0345)
ytm = bond.yield_to_maturity(settle_dt, clean_price=99.5)
```

### Valuing a European equity option

```python
from financepy.utils import *
from financepy.products.equity.equity_vanilla_option import EquityVanillaOption
from financepy.models.black_scholes import BlackScholes
from financepy.market.curves.flat_discount_curve import FlatDiscountCurve

expiry_dt = Date(1, 6, 2026)
strike_price = 50.0
call_option = EquityVanillaOption(expiry_dt, strike_price, OptionTypes.EUROPEAN_CALL)

value_dt = Date(1, 6, 2025)
stock_price = 55.0
volatility = 0.20
risk_free_rate = 0.03
dividend_yield = 0.01

discount_curve = FlatDiscountCurve(value_dt, risk_free_rate)
dividend_curve = FlatDiscountCurve(value_dt, dividend_yield)
model = BlackScholes(volatility)

price = call_option.value(value_dt, stock_price, discount_curve, dividend_curve, model)
delta = call_option.delta(value_dt, stock_price, discount_curve, dividend_curve, model)
```

### Building a CDS curve and valuing a CDS

```python
from financepy.utils import *
from financepy.products.credit.cds import CDS
from financepy.market.curves.cds_curve import CDSCurve

value_dt = Date(10, 1, 2026)
effective_dt = Date(1, 12, 2024)
maturity_dt = Date(20, 3, 2028)
cds_coupon = 0.010          # 100bp running coupon
notional = ONE_MILLION
long_protection = True

cds_contract = CDS(effective_dt, maturity_dt, cds_coupon, notional, long_protection)

# build an IBOR discount curve from market deposits/swaps
# (financepy.market.curves.ibor_single_curve.IborSingleCurve), then a CDSCurve
# (issuer/hazard curve, which carries the discount curve) from market CDS quotes, then:
# cds_contract.value(value_dt, issuer_curve, contract_recovery_rate)
```

### Building a discount curve

```python
from financepy.utils import Date
from financepy.market.curves.flat_discount_curve import FlatDiscountCurve
from financepy.market.curves.zero_rates_discount_curve import ZeroRatesDiscountCurve
from financepy.market.curves.ns_discount_curve import NSDiscountCurve   # Nelson-Siegel

value_dt = Date(1, 1, 2026)
flat_curve = FlatDiscountCurve(value_dt, 0.04)
df = flat_curve.df(Date(1, 1, 2031))       # discount factor
zero_rate = flat_curve.zero_rate(Date(1, 1, 2031))
```

## Source layout

```
financepy/
├── utils/          # Date, calendars, day-count/frequency/currency enums, schedules, math helpers
├── market/
│   ├── curves/     # *_discount_curve.py: flat, zero_rates, ns, nss, poly, pwf, pwl, bond bootstrap/parametric; IBOR/OIS bootstrapping, CDS and inflation curves
│   ├── prices/     # price/quote container objects
│   └── volatility/ # equity/FX/IBOR-cap/swaption vol curves and surfaces
├── models/         # pricing models: Black, Black-Scholes (bs_*.py analytic/MC), Bachelier, BDT/BK/HW/Vasicek trees, Heston, SABR, CEV, Dupire, SVI/SSVI, Monte Carlo (Sobol)
├── trades/         # Trade wrapper
└── products/
    ├── bonds/      # Bond, BondFRN, BondConvertible, BondMortgage, BondFuture, BondOption, BondPortfolio, inflation bond, ...
    ├── rates/      # IborDeposit, IborFRA, IborSwap, OIS, caps/floors, swaptions (European/Bermudan), inflation swap, swaps/ (IBOR basis, x-ccy), curve risk/smoothing tools
    ├── equity/     # EquityVanillaOption, American/Asian/Barrier/Power/Gap/Quanto/Variance-swap options
    ├── fx/         # FX spot/rate/forward, vanilla/barrier/digital/variance-swap options
    └── credit/     # CDS, CDSCurve, CDSBasket, CDSTranche, CDSIndexOption, CDSIndexPortfolio
```

Every module above is vendored under `financepy/` in this skill directory (mirrors the
upstream package 1:1, ~3MB of pure Python source, no notebooks/tests/docs binaries).
`README.md` in this folder is the upstream project README (installation notes and package
structure overview); the upstream `docs/` (generated HTML API docs), `examples/` notebooks
and `tests/` are not vendored.

## Notes

- Import can be slow (several seconds) on first use per machine due to Numba JIT
  compilation; this is expected and only happens once (cached afterward).
- The library favors explicit, readable Python over clever abstractions — expect one class
  per product/model rather than heavy inheritance hierarchies.
- Curve modules were renamed upstream (e.g. `discount_curve_flat.DiscountCurveFlat` is now
  `flat_discount_curve.FlatDiscountCurve`, `DiscountCurveZeros` → `ZeroRatesDiscountCurve`,
  `DiscountCurveNS` → `NSDiscountCurve`) and the old `legacy/` curves were removed; code
  written against older FinancePy releases needs those imports updated.
- Full author contact and contribution guidelines are in the vendored `README.md`.
