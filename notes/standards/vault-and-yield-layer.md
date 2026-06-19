# Vault and Yield Layer

These standards specify the settlement rails and yield wrappers beneath a tranche structure. Each defines a single share class and provides no concept of seniority or splitting.

## ERC-4626 — [specification](https://eips.ethereum.org/EIPS/eip-4626) (Final; requires ERC-20, ERC-2612)

A tokenized vault interface comprising `deposit`, `mint`, `withdraw`, and `redeem`, together with `convertTo*`, `preview*`, and `max*` views. ERC-4626 defines a single share class and is pari-passu by construction. A common senior-and-junior implementation deploys two ERC-4626 vaults over one strategy, as in the Idle Perpetual Yield Tranches. The `totalAssets()` and `convertToAssets()` functions are the points at which a waterfall would override the proportional net-asset-value split. Reference implementations: [Solmate](https://github.com/transmissions11/solmate/blob/main/src/tokens/ERC4626.sol) and OpenZeppelin.

## ERC-7540 — [specification](https://eips.ethereum.org/EIPS/eip-7540) (Final; requires ERC-20, ERC-165, ERC-4626, ERC-7575)

An asynchronous extension of ERC-4626 providing `requestDeposit` and `requestRedeem` followed by later fulfilment. The request-to-fulfilment boundary corresponds to an epoch boundary, at which a waterfall would compute the per-tranche split before fulfilling claims. ERC-7540 is used by Centrifuge, Ondo, and Backed for real-world-asset settlement.

## ERC-7575 — [specification](https://eips.ethereum.org/EIPS/eip-7575) (Final; vault interface `0x2f0a18c5`, share interface `0xf815c03d`)

Externalises the share token from the vault through a `share()` accessor, allowing multiple asset entry points to share one token (with optional "Pipes" for conversion). This is the inverse of a tranche structure: it maps many assets to one share, whereas a tranche maps one asset to many share classes. It confirms that the vault standards do not address seniority. Note the [dependency inversion](./timeline-and-reading-order.md): ERC-7540 requires ERC-7575 although ERC-7540 is the earlier document.

## Cash-flow-split tokens

The following standards represent the output of a yield split (principal versus yield) rather than a risk tranche.

### EIP-5115 — SY / Standardized Yield — [specification](https://eips.ethereum.org/EIPS/eip-5115) (Draft; requires ERC-20)

A yield-wrapper interface more general than ERC-4626, authored by the Pendle team. It relaxes three ERC-4626 assumptions: it permits multiple input and output tokens (`getTokensIn`, `getTokensOut`), it permits accounting in units that are not themselves depositable (for example AMM liquidity units), and it provides for reward-token handling. Its model is a generic yield-generating pool with `exchangeRate() = totalAssets / totalShares`. Pendle wraps an arbitrary yield source as SY and then splits it into principal and yield tokens. The architectural consequence is that a uniform yield-source adapter beneath the engine allows the engine to reason about a single normalised net asset value irrespective of source.

### EIP-5095 — Principal Token — [specification](https://eips.ethereum.org/EIPS/eip-5095) (Stagnant; requires ERC-20, ERC-2612)

Specifies the principal-token leg only — ownership of an underlying ERC-20 at a future `maturity()`, redeemable at that maturity — using an ERC-4626-shaped redemption interface. It does not specify the yield token or the act of splitting. The proposal is Stagnant, and Pendle's principal tokens implement ERC-4626 rather than EIP-5095 ([discussion](https://ethereum-magicians.org/t/eip-5095-principal-token-standard/9259)).

## Relevance

The cash-flow axis mirrors the risk axis: the token legs received partial or stalled standards (EIP-5095 and EIP-5115), while the split engine is unspecified — the same gap as the waterfall. See [`../00-thesis-and-direction.md`](../00-thesis-and-direction.md) and [`../protocols/cashflow-tranching-protocols.md`](../protocols/cashflow-tranching-protocols.md).
