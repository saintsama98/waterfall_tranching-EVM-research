# Waterfall Tranching — First Principles

## Structure

A pool of capital generates income and may incur losses through default. Investors have differing risk preferences. Tranching serves these preferences from a single pool by arranging claims into priority layers.

```
  Senior  (e.g. 80M)  — lower yield, paid first, absorbs loss last
  Junior  (e.g. 20M)  — higher yield, paid last,  absorbs loss first
        the pool sits beneath both layers
```

## Direction of flows

- **Cash flow descends.** Income fills the senior claim first; the remainder is distributed to the junior claim.
- **Loss ascends.** A default reduces the junior layer first; the senior layer incurs loss only after the junior layer is exhausted.

Two distinct waterfalls typically operate in parallel: an interest waterfall and a principal waterfall.

```
   income → [1. senior coupon, paid in full] → [2. junior receives the remainder]
```

## Worked example

Consider a 100M pool funded as 80M senior and 20M junior.

- **No defaults, 8M of interest.** The senior coupon of 4M is paid; the junior layer receives the remaining 4M, an approximate 20% return on 20M.
- **15M of defaults.** The junior layer absorbs the loss first, reducing it to 5M; the senior layer remains whole at 80M. If a coverage test is breached, junior distributions are additionally suspended and redirected to de-lever the senior layer — see [`oc-ic-coverage-tests.md`](./oc-ic-coverage-tests.md).

## Definition

The junior tranche earns the larger return in favourable conditions and absorbs loss first in adverse conditions; the senior tranche earns a smaller, steadier return and is protected. Coverage tests are the conditions that enforce this protection as the pool deteriorates.

## On-chain status

Surveyed on-chain protocols reproduce the layered structure (senior and junior tokens) but omit the coverage tests: their junior layer absorbs loss passively, with no redirection of cash flow. This omission defines the scope addressed by the proposed standard; see [`../protocols/reference-architecture.md`](../protocols/reference-architecture.md).
