# Outstanding Questions and Research Direction

The following questions remain open before drafting the normative specification, in approximate priority order. The first two are the most consequential and the most concrete.

## 1. Loss recognition and net-asset-value oracle (component ②)

A waterfall has no effect until a loss is recognised and quantified, and no existing standard specifies this. Open questions: whether loss is recognised by mark-to-market, accrual, or a default event; who attests to net asset value and what mechanism (for example a dispute or challenge window) constrains that attestation. Many on-chain designs assume an honest net-asset-value feed; the credibility of the standard depends on this component.

## 2. Implementation review of hardcoded-waterfall protocols (component ③)

A comparison of how existing two-tranche, hardcoded engines compute the split identifies the common structure that the standard should generalise. Targets: Centrifuge version 3, Idle (`IdleCDO.sol`), Maple, Goldfinch, Notional, and Term Finance. For each: the location at which the per-tranche split is computed, the parameters that are configurable versus fixed, and the events emitted.

## 3. Traditional waterfall mechanics

The precise rules to be encoded: sequential versus pro-rata distribution, turbo and cash-trapping, excess-spread reserves, the formulae for diversion on a coverage breach, the separation of interest and principal waterfalls, and attachment and detachment points. Primary sources: collateralised-loan-obligation and residential-mortgage-backed-security indentures and rating-agency methodologies.

## 4. Economic security and demand

The principal cause of failure among prior protocols was insufficient demand for the junior tranche. Open questions: which participants hold first-loss capital and at what yield premium; procyclicality and redemption-run dynamics and the gating required to manage them; and the dependence of the senior layer's protection on assumed default correlation, which argues for governable parameters.

## 5. Failure post-mortems

The failure modes of BarnBridge (regulatory), Saffron, Waterfall DeFi, and Tranche Finance should be examined and translated into requirements for the Security Considerations and Rationale sections (liquidity, junior demand, complexity, and oracle trust).

## 6. Regulatory considerations (real-world-asset case)

The conditions under which a tranche constitutes a security, informed by the BarnBridge enforcement action, determine whether the [compliance branch](../standards/security-token-branch.md) (ERC-3643, ERC-7518) should be composed in.

## 7. Specification design

- A minimal interface — distribution events, an epoch or `distribute()` hook, per-tranche `coverageRatio()` and `nav()` views, and trigger-state queries — rather than a complete implementation.
- Composition with [ERC-4626 and ERC-7540](../standards/vault-and-yield-layer.md) beneath, and with the [substrate](./substrate-fork.md) above.
- Conformance vectors for `../test-vectors/`: for example, the senior tranche paid in full before the junior; the junior tranche exhausted before the senior incurs loss; and a coverage breach diverting cash flow.

## Pending decisions

- [ ] Token substrate: ERC-3475 versus ERC-6909 with ERC-7201 (currently favouring the latter; see [`substrate-fork.md`](./substrate-fork.md)).
- [ ] Axis scope: the risk axis first, the cash-flow axis subsequently, or a unified treatment.
- [ ] Verification of the token standards used by Untangled, Galaxy, and Tradable; see [`../protocols/standards-adoption-matrix.md`](../protocols/standards-adoption-matrix.md).
- [ ] A survey of the Ethereum Magicians forum and ERC repository pull requests for any in-progress tranche or waterfall proposal.
