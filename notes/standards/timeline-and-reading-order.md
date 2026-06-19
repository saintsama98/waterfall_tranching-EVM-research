# Timeline and Reading Order

The standards relevant to tranching, ordered by creation date. Header fields verified on 2026-06-19; current status is shown in the final column.

| Created | ERC | Title | Status | Role |
|---|---|---|---|---|
| 2015-11-19 | [ERC-20](https://eips.ethereum.org/EIPS/eip-20) | Token Standard | Final | Baseline; one ERC-20 per tranche |
| 2018-06-17 | [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155) | Multi Token Standard | Final | Multiple token identifiers per contract |
| 2018-09-09 | [ERC-1400](https://github.com/ethereum/EIPs/issues/1411) | Security Token Standard (umbrella) | Issue; unofficial | Compliance umbrella |
| 2018-09-13 | [ERC-1410](https://github.com/SecurityTokenStandard/EIP-Spec/blob/master/eip/eip-1410.md) | Partially-Fungible Token (partitions) | Issue; unofficial | Tranche-as-partition model |
| 2021-04-05 | [ERC-3475](https://eips.ethereum.org/EIPS/eip-3475) | Abstract Storage Bonds | Final | Purpose-built tranche-token substrate |
| 2021-07-09 | [ERC-3643](https://eips.ethereum.org/EIPS/eip-3643) | T-REX (regulated tokens) | Final | Compliance and identity |
| 2021-12-22 | [ERC-4626](https://eips.ethereum.org/EIPS/eip-4626) | Tokenized Vaults | Final | Vault settlement base |
| 2022-05-01 | [EIP-5095](https://eips.ethereum.org/EIPS/eip-5095) | Principal Token | Stagnant | Principal leg of a cash-flow split |
| 2022-05-30 | [EIP-5115](https://eips.ethereum.org/EIPS/eip-5115) | SY / Standardized Yield | Draft | Yield-source wrapper |
| 2023-04-19 | [ERC-6909](https://eips.ethereum.org/EIPS/eip-6909) | Minimal Multi-Token | Final | Lightweight multi-token interface |
| 2023-06-20 | [ERC-7201](https://eips.ethereum.org/EIPS/eip-7201) | Namespaced Storage Layout | Final | Upgrade-safe storage substrate |
| 2023-09-14 | [ERC-7518](https://eips.ethereum.org/EIPS/eip-7518) | DyCIST | Review | Security token over ERC-1155 partitions |
| 2023-10-18 | [ERC-7540](https://eips.ethereum.org/EIPS/eip-7540) | Asynchronous Vaults | Final | Epoch and request-based settlement |
| 2023-12-11 | [ERC-7575](https://eips.ethereum.org/EIPS/eip-7575) | Multi-Asset Vaults | Final | Externalised share token |

## Two observations from the chronology

1. **Dependency inversion.** ERC-7540 (created 2023-10-18) depends on ERC-7575 (created 2023-12-11); ERC-7575 was separated from ERC-7540 after the fact. ERC-7575 is therefore a prerequisite for understanding ERC-7540 despite being the more recent document.

2. **Absence of a waterfall standard.** The chronology contains token standards, vault standards, and compliance standards, but no standard specifying payment priority, loss-allocation order, or coverage tests.

## Reading order

A dependency-ordered path is more instructive than strict chronology. Token substrate, then settlement base, then the cash-flow tokens, then storage and compliance:

`ERC-20 → ERC-1155 / ERC-6909 → ERC-3475` · `ERC-4626 → ERC-7540 → ERC-7575` · `EIP-5115 / EIP-5095 (cash-flow axis)` · `ERC-7201` · `ERC-3643 → ERC-7518 → ERC-1410 (compliance, where applicable)`

Further detail: [`token-substrate-layer.md`](./token-substrate-layer.md), [`vault-and-yield-layer.md`](./vault-and-yield-layer.md), [`storage-substrate.md`](./storage-substrate.md), [`security-token-branch.md`](./security-token-branch.md).
