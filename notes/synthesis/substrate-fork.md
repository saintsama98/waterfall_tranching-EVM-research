# Token-Substrate Selection

The first substantive specification decision concerns the token used to represent a tranche. Two viable approaches are considered.

## Option A — ERC-3475

- **In favour.** ERC-3475 provides bond semantics directly: class and nonce identity, on-chain per-series net asset value and metadata, a supply lifecycle, and a redemption-condition accessor. It is the closest existing representation of a tranche.
- **Against.** It is comparatively complex (the batched `Transaction` interface), it has minimal production adoption (see [`../protocols/standards-adoption-matrix.md`](../protocols/standards-adoption-matrix.md)), and it specifies neither a seniority ordering nor a waterfall, both of which would have to be added regardless.

## Option B — ERC-6909 with ERC-7201

- **In favour.** ERC-6909 is lightweight, has an ERC-20-like interface, and has practical adoption (Uniswap v4). The tranche identifier serves as the class key, and the net-asset-value, seniority, and coverage-test state are laid out in [namespaced storage](../standards/storage-substrate.md) keyed by that identifier. This approach gives full control of the tranche model.
- **Against.** More of the semantics are defined by the implementer, which increases the specification surface and reduces reuse of an existing standard.

## Current position

Option B (ERC-6909 with ERC-7201) is preferred at this stage, for three reasons. First, the minimal adoption of ERC-3475 — mirrored by the stagnation of EIP-5095 on the cash-flow axis — indicates that the standard is either an imperfect fit or too heavy for the role. Second, the elements of ERC-3475 that would be reused (metadata and net asset value) are the elements most readily defined directly. Third, the value of the proposed standard lies in the engine (components ③ and ④), not in the token; the substrate should therefore be chosen to minimise friction and maximise composability.

## Net-new elements, independent of the selection

- An explicit, monotonic seniority index, which neither ERC-3475 nor ERC-6909 provides.
- The waterfall and coverage-test interface; see [`../mechanics/oc-ic-coverage-tests.md`](../mechanics/oc-ic-coverage-tests.md).
- Governable, auditable calibration parameters; see [`../mechanics/heuristics-vs-plumbing.md`](../mechanics/heuristics-vs-plumbing.md).

This position is provisional and should be revisited if a case for ERC-3475 adoption emerges or a lighter alternative is identified.
