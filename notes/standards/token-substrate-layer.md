# Token Substrate Layer

This note surveys the candidates for representing a tranche as a token, ordered from least to most expressive.

## ERC-20 — [specification](https://eips.ethereum.org/EIPS/eip-20) (Final)

A single fungible token per tranche, with the senior and junior tokens deployed as separate contracts. ERC-20 provides no shared accounting across tranches and no concept of seniority. It is the minimal baseline, and, as the [adoption matrix](../protocols/standards-adoption-matrix.md) shows, the representation that most surveyed protocols use in practice.

## ERC-1155 — [specification](https://eips.ethereum.org/EIPS/eip-1155) (Final)

Multiple token identifiers within one contract, allowing the senior tranche to occupy identifier 0 and the junior tranche identifier 1. ERC-1155 establishes the multiple-classes-in-one-contract pattern but carries no bond or redemption semantics, and it mandates receiver callbacks and batch operations.

## ERC-6909 — [specification](https://eips.ethereum.org/EIPS/eip-6909) (Final; interface identifier `0x0f632fb3`)

A minimal multi-token interface that retains the `balanceOf(owner, id)` model of ERC-1155 while removing its heavier requirements:

- No mandatory receiver callbacks, reducing reentrancy surface and permitting non-aware counterparties.
- Both granular per-identifier allowances and a blanket operator authorisation.
- Batch operations omitted from the core interface.

ERC-6909 is used in production by Uniswap v4. In effect it is an ERC-20 interface extended with an identifier argument.

## ERC-3475 — [specification](https://eips.ethereum.org/EIPS/eip-3475) (Final; requires ERC-20, ERC-721, ERC-1155)

The only standard designed specifically to represent tranche-like instruments, by means of a class and nonce model:

- `classId` denotes a class of instrument, which maps onto a tranche (senior, mezzanine, junior).
- `nonceId` denotes an issuance series within a class, each with its own supply, metadata, and net asset value.
- A balance is addressed as `balanceOf(account, classId, nonceId)`.

ERC-3475 specifies tranche identity, on-chain per-class and per-nonce metadata (`Values` and `Metadata`), a supply lifecycle (`activeSupply`, `redeemedSupply`, `burnedSupply`), and a redemption-condition accessor (`getProgress`).

It does not specify a seniority ordering between classes, and it does not specify a waterfall: redemption conditions and payment priority are left to the implementing contract.

## Selection

ERC-3475 is the most complete representation but is also the most complex and has minimal production adoption; ERC-6909 is lighter and more widely adopted, at the cost of requiring the tranche semantics to be defined by the implementer, typically over [ERC-7201 storage](./storage-substrate.md). This selection is examined in [`../synthesis/substrate-fork.md`](../synthesis/substrate-fork.md).

ERC-721 also appears in production for the dated or non-fungible leg of a structure — the BarnBridge senior bonds (sBONDs) and the Goldfinch junior position tokens (PoolTokens); see [`../protocols/loss-tranching-protocols.md`](../protocols/loss-tranching-protocols.md).
