# Security-Token and Compliance Branch

These standards govern eligibility to hold a token — identity, investor qualification, and transfer restrictions. They are adjacent to tranching rather than part of it: they compose alongside a waterfall but do not specify one. They are relevant only where the target is a regulated or real-world-asset structure.

## ERC-1400 and ERC-1410 — unofficial

These are not official EIPs. They were opened as GitHub issues by Adam Dossa of Polymath in September 2018: [issue #1411 (ERC-1400)](https://github.com/ethereum/EIPs/issues/1411) and [issue #1410 (ERC-1410)](https://github.com/ethereum/EIPs/issues/1410). Both are closed and labelled stale. The canonical specification is maintained in a community repository rather than in the Ethereum Foundation repository: [`SecurityTokenStandard/EIP-Spec`](https://github.com/SecurityTokenStandard/EIP-Spec).

ERC-1400 is an umbrella over five sub-standards: ERC-1594 (core transfer), ERC-1410 (partitions), ERC-1643 (document management), and ERC-1644 (controller operations). The tranche-relevant element is ERC-1410's partition model: balances are divided into `bytes32` partitions, and `canTransferByPartition` returns a status reason code. This corresponds to a tranche-as-partition representation.

## ERC-3643 — T-REX — [specification](https://eips.ethereum.org/EIPS/eip-3643) (Final, 2021-07-09; requires ERC-20, ERC-173)

The finalised and most widely adopted member of this branch. It specifies permissioned, compliant transfer with on-chain identity (ONCHAINID) for investor eligibility. The specification does not address tranching, seniority, or waterfall logic; it governs which parties may hold tranche tokens, not how a structure is tranched.

## ERC-7518 — DyCIST — [specification](https://eips.ethereum.org/EIPS/eip-7518) (Review, 2023-09-14; requires ERC-165, ERC-1155)

A more recent successor to the ERC-1400/1410 line, built over ERC-1155 partitions with off-chain compliance vouchers, token locking, and forced transfers.

## Summary

The ERC-1410 partition model is useful as prior art rather than as a citable standard. For a finalised compliance layer, ERC-3643 is the appropriate standard to compose with, and ERC-7518 is the relevant proposal to track. None of these standards specifies the engine described in [`../00-thesis-and-direction.md`](../00-thesis-and-direction.md).
