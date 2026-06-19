# Standards Landscape

This section surveys the existing standards relevant to tranching: what each specifies, and the point at which each stops short of seniority ordering or waterfall logic. All header fields (status, creation date, dependencies) were retrieved from `eips.ethereum.org` on 2026-06-19.

- [`timeline-and-reading-order.md`](./timeline-and-reading-order.md) — Chronological sequence and a dependency-ordered reading path
- [`token-substrate-layer.md`](./token-substrate-layer.md) — Representation of a tranche as a token: ERC-20, ERC-1155, ERC-6909, ERC-3475
- [`vault-and-yield-layer.md`](./vault-and-yield-layer.md) — The settlement and yield-wrapper base: ERC-4626, ERC-7540, ERC-7575, and the cash-flow-split tokens EIP-5115 and EIP-5095
- [`storage-substrate.md`](./storage-substrate.md) — ERC-7201 namespaced storage
- [`security-token-branch.md`](./security-token-branch.md) — ERC-1400/1410, ERC-3643, ERC-7518; compliance and identity, adjacent to but distinct from tranching

The token and settlement layers are adequately standardised. No standard on any layer specifies payment priority, loss-allocation order, or coverage tests; see [`../00-thesis-and-direction.md`](../00-thesis-and-direction.md).
