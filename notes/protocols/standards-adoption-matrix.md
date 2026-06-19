# Standards Adoption Matrix

The standards each surveyed protocol adopts, drawn from the [protocol notes](./index.md).

| Protocol | Standards adopted | Note |
|---|---|---|
| Idle PYT | ERC-20 (AA/BB) and ERC-4626 | Two ERC-20 tokens; ERC-4626 accounting |
| BarnBridge | ERC-20 (jTokens) and ERC-721 (sBONDs) | Senior claim issued as a non-fungible bond |
| Centrifuge | ERC-20 (DROP/TIN); ERC-7540 in version 3 (over ERC-4626) | The only ERC-7540 adopter, which it co-authored |
| Goldfinch | ERC-20 (FIDU) and ERC-721 (PoolTokens) | Junior position issued as non-fungible |
| Maple | ERC-20 and ERC-4626 | Standard vault shares |
| Pendle | ERC-20 (PT/YT) and EIP-5115 (SY) | Principal token implements ERC-4626, not EIP-5095 |
| Saffron, Waterfall DeFi | ERC-20 | Plain fungible tokens |
| Untangled | ERC-20 (SOT/JOT), unverified | Likely plain ERC-20 |
| Galaxy, Tradable | Unverified; likely ERC-3643 or ERC-1400 | Permissioned real-world-asset wrappers |

## Observations

1. **ERC-20 predominates.** Each tranche is generally represented as a separate ERC-20 contract, the minimal representation with no shared accounting.
2. **ERC-3475 is not adopted.** The standard designed specifically to represent tranche-like instruments has minimal production adoption; protocols instead reconstruct the equivalent with ERC-20 pairs.
3. **ERC-1155 and ERC-6909 are not used for tranches.** Separate ERC-20 tokens are preferred for composability with decentralised exchanges and lending markets.
4. **ERC-4626 is the most widely adopted settlement base; ERC-7540 has a single adopter** (Centrifuge).
5. **Two standards outside the core sequence appear in practice:** ERC-721, for the dated or non-fungible tranche leg, and EIP-5115, as Pendle's yield wrapper.

## Implication

The standards best-suited to tranching (ERC-3475, ERC-1155/6909, ERC-7540, EIP-5095) are largely unused in this role; the prevailing practice combines ERC-20 with ERC-4626 and a bespoke engine. Both a tranche-token standard with practical adoption and a waterfall interface therefore remain unaddressed. The non-adoption of ERC-3475 and EIP-5095 informs the substrate selection in [`../synthesis/substrate-fork.md`](../synthesis/substrate-fork.md).
