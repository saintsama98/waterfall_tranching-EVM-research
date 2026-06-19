# Reference Architecture

The following is the abstract architecture against which the surveyed protocols are assessed. Each protocol is evaluated against components ① through ⑤. Component ④ is absent in all of them.

```
 ┌───────────────────────────────────────────────────────┐
 │ ① Asset pool / strategy   (source of cash flow and loss)│
 └─────────────────────────────┬─────────────────────────┘
                               │ yield generated, loss realised
 ┌─────────────────────────────▼─────────────────────────┐
 │ ② Net-asset-value and loss accounting                  │
 └─────────────────────────────┬─────────────────────────┘
 ┌─────────────────────────────▼─────────────────────────┐
 │ ③ Waterfall engine — priority of payments              │
 │ ④ Coverage tests (OC/IC) and active cure               │
 └─────────────────────────────┬─────────────────────────┘
        ┌──────────────────────┴───────────────────┐
        ▼                                           ▼
  Senior tranche token                       Junior tranche token
  (paid first, loss last)                    (paid last, loss first)

 ⑤ Settlement / epoch layer   (synchronous or asynchronous; ERC-4626 / ERC-7540)
```

## Mapping to standards

- **①** — A strategy adapter, normalised through [EIP-5115 SY](../standards/vault-and-yield-layer.md) or an ERC-4626 source.
- **②** — Net-asset-value and loss recognition. This component carries the principal trust assumption and is not standardised; see [`../synthesis/open-questions-and-next.md`](../synthesis/open-questions-and-next.md).
- **③ and ④** — The engine, which the proposed standard defines. See [`../mechanics/oc-ic-coverage-tests.md`](../mechanics/oc-ic-coverage-tests.md).
- **Tokens** — The substrate selection between ERC-3475 and ERC-6909 with ERC-7201; see [`../synthesis/substrate-fork.md`](../synthesis/substrate-fork.md).
- **⑤** — Settlement, composing [ERC-7540](../standards/vault-and-yield-layer.md); the epoch boundary is the point at which component ③ executes.

## Composite assessment

The closest existing assembly combines Idle's `IdleCDO` engine and dynamic split, Centrifuge's subordination-ratio gate, ERC-7540 settlement, and Goldfinch's fixed excess-spread allocation. Together these approximate the reference architecture with the exception of component ④, the active diversion of cash flow on a coverage breach, which no surveyed protocol implements. Detail in [`loss-tranching-protocols.md`](./loss-tranching-protocols.md).
