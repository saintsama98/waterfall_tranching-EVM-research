# Deterministic Logic versus Parameterised Calibration

A waterfall comprises two layers. Conflating them is a design error.

## Deterministic layer

The priority of payments — pay the senior tranche, distribute the remainder to the junior tranche, and divert distributions to cure a breach — is arithmetic and ordering. For a given set of inputs the result is exact and reproducible. This layer is the appropriate subject of a normative on-chain specification, because any party can verify that distributions followed the stated rules.

## Calibration layer

Every threshold and parameter that feeds the deterministic layer is a modelling judgement rather than a determinable constant:

- The overcollateralisation trigger (for example 1.10) and the interest-coverage trigger (for example 1.20).
- The attachment and detachment points that set the senior-to-junior division.
- The assumed default correlation that underlies the senior layer's protection.

These parameters are conditional estimates: the senior layer is protected only while losses remain within the junior cushion and defaults do not correlate more strongly than assumed. The 2008 failure of the Gaussian-copula approach illustrates the consequence — a correlation assumption that held in calm conditions and failed when defaults correlated, causing senior tranches rated as low-risk to incur losses. The failure was one of opaque calibration, not of the payment mechanism.

## Governing rule

Specify the deterministic layer precisely. Expose every calibration value as an explicit, governable, and auditable parameter, rather than embedding it as a fixed constant. The advantage available on-chain, relative to traditional practice, is that the calibration becomes public and inspectable rather than embedded in a rating and a private indenture.

## Mapping to the specification

- **Specification** — the deterministic engine and the coverage-test interface.
- **Rationale and Security Considerations** — the treatment of calibration as parameterised judgement, with reference to the prior-art failure modes in [`../synthesis/open-questions-and-next.md`](../synthesis/open-questions-and-next.md).
- **Conformance vectors** — deterministic scenarios; calibration is left to the deployer.
