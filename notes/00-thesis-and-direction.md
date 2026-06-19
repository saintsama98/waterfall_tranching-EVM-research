# Thesis and Direction

## Summary

The Ethereum standards ecosystem has specified the tokens that represent tranches and the vault interfaces on which they settle, but it has not specified the logic that allocates cash flow and loss between tranches: the priority-of-payments waterfall (senior versus junior) and the yield-split engine (principal versus yield). This unspecified layer defines the scope of the proposed standard.

## The two-axis observation

Tranching occurs along two distinct axes, and the same structural gap is present on both.

| Axis | Token representation | Active engine |
|---|---|---|
| Risk (senior versus junior subordination) | ERC-3475 (Final, minimal adoption); otherwise ad-hoc ERC-20 pairs | Priority-of-payments waterfall — unspecified |
| Cash flow (principal versus yield) | EIP-5095 (principal leg, Stagnant); EIP-5115 SY (wrapper, Draft); yield leg absent | Split engine — unspecified |

On both axes, the token representations received partial, stalled, or unadopted standards, while the logic that allocates cash flow and loss remains specific to each protocol. Detail in [`synthesis/substrate-fork.md`](./synthesis/substrate-fork.md) and [`standards/timeline-and-reading-order.md`](./standards/timeline-and-reading-order.md).

## The behaviour the standard introduces

The defining mechanic of traditional securitisation — coverage tests (overcollateralisation and interest-coverage) that actively re-route cash flow upon breach, diverting junior distributions to de-lever the senior tranche and trapping excess spread in a reserve — is not implemented by any surveyed on-chain protocol. Existing protocols either absorb loss passively (Idle, Maple) or halt new issuance on breach without redirecting cash flow (Centrifuge). See [`mechanics/oc-ic-coverage-tests.md`](./mechanics/oc-ic-coverage-tests.md) and [`protocols/reference-architecture.md`](./protocols/reference-architecture.md).

## Design principle

A waterfall comprises two layers, only one of which is deterministic.

1. **Plumbing — deterministic.** The priority of payments (pay the senior tranche, distribute the remainder to the junior tranche, and divert distributions to cure a breach) is arithmetic and ordering. For a given set of inputs the result is exact and reproducible. This layer is the candidate for normative on-chain specification, since any party can verify that distributions followed the rules.

2. **Calibration — heuristic.** Every threshold (the overcollateralisation trigger, the interest-coverage trigger, attachment and detachment points, and the assumed default correlation) is a modelling judgement rather than a determinable constant. The 2008 failure of the Gaussian-copula approach was a failure of opaque calibration, not of the payment mechanism.

The governing rule follows: specify the plumbing precisely, and expose every calibration value as an explicit, governable, auditable parameter rather than embedding it as a fixed constant. Discussion in [`mechanics/heuristics-vs-plumbing.md`](./mechanics/heuristics-vs-plumbing.md).

## Mapping to the specification

- **Specification** — the deterministic engine, its events, and a coverage-test interface.
- **Rationale and Security Considerations** — the treatment of calibration as parameterised judgement, and the failure modes observed in prior art.
- **Conformance vectors** (`test-vectors/`) — deterministic scenarios such as the diversion of junior distributions to de-lever the senior tranche on a coverage breach.

## Scope

The proposed standard specifies an interface and a behaviour rather than a complete implementation. It is asset-agnostic, composes with ERC-4626 and ERC-7540 for settlement, and sits above a tranche-token substrate (see [`synthesis/substrate-fork.md`](./synthesis/substrate-fork.md)).
