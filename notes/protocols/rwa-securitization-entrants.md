# Real-World-Asset Securitisation Entrants (2025–2026)

Recent entrants closest in intent to a full waterfall. They treat loss recognition (component ②) as a first-class element, which most DeFi designs do not.

## Untangled Finance

```
credit pool and Credit Oracle → SOT (Senior Obligation Token) / JOT (Junior Obligation Token)
```

Untangled uses explicit securitisation terminology and a Credit Oracle, which represents a direct attempt to provide on-chain loss recognition. It is the most traditionally-structured of the on-chain models surveyed. The token standard is not yet verified and is likely ERC-20. Source: [documentation](https://docs.untangled.finance/docs/credio/Onchain-Private-Credit/Intro-Untangled-Pool/).

## Galaxy CLO 2025-1

A tokenised collateralised loan obligation (senior tranche at SOFR plus 570 basis points; initial 75M, expandable to 200M; on Avalanche). The waterfall operates off-chain within the traditional structure, and the token represents the claim. This is useful as a reference for the form of a real collateralised-loan-obligation tranche rather than as on-chain mechanics. Source: [PRNewswire](https://www.prnewswire.com/news-releases/galaxy-announces-initial-closing-of-debut-tokenized-clo-at-75-million-302662045.html).

## Tradable

Tokenised private credit on ZKsync, following the same wrapper pattern of an off-chain waterfall and an on-chain claim. Likely permissioned (ERC-3643 or ERC-1400 family); not verified. Source: [Chainlink analysis](https://chain.link/article/onchain-private-lending).

## Assessment

These wrappers demonstrate demand for tokenised tranches but retain the waterfall off-chain; they tokenise the output of a traditional structure rather than specifying the engine. Untangled is the exception in bringing loss recognition on-chain. The token standards used by Untangled, Galaxy, and Tradable remain to be confirmed; see [`standards-adoption-matrix.md`](./standards-adoption-matrix.md) and [`../synthesis/open-questions-and-next.md`](../synthesis/open-questions-and-next.md).
