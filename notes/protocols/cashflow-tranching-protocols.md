# Cash-Flow-Tranching Protocols (Cash-Flow Axis)

Protocols that split a yield asset into a principal component and a yield component, rather than into senior and junior risk layers. The structure parallels the risk axis. The relevant token standards are described in [`../standards/vault-and-yield-layer.md`](../standards/vault-and-yield-layer.md).

## Pendle

```
yield asset → SY (EIP-5115, an ERC-4626 superset wrapper)
            → split → PT (principal, redeems 1:1 at maturity)
                      YT (variable yield to maturity)
```

The principal token (PT) and yield token (YT) are both ERC-20. SY normalises the underlying yield source, and the split operates only against the SY `exchangeRate()`. The internal pyIndex is designed not to decrease, so yield volatility is absorbed by the YT first and the PT is ring-fenced; the PT therefore occupies a position analogous to the senior tranche and the YT a position analogous to a first-loss claim on yield. The structure has a fixed maturity, and the PT/YT oracle takes the maximum of the SY and PY indices to resist downward manipulation. Pendle's principal tokens implement ERC-4626 rather than EIP-5095. Sources: [Pendle documentation](https://docs.pendle.finance/pendle-v2/Introduction), [Minting](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/YieldTokenization/Minting), [mixbytes analysis](https://mixbytes.io/blog/yield-tokenization-protocols-how-they-re-made-pendle).

## Spectra

The same principal-and-yield split applied to interest-bearing tokens: the principal token provides a fixed return at maturity and the yield token supports speculation on or hedging of future yield. Source: [spectra-core](https://github.com/perspectivefi/spectra-core).

## Relevance

The non-decreasing index is a net-asset-value technique applicable to the proposed standard, and the normalise-then-split architecture supports the use of a uniform yield adapter beneath the engine (see [`../standards/vault-and-yield-layer.md`](../standards/vault-and-yield-layer.md)). As on the risk axis, the split engine itself is unspecified, while only the token legs received standards; see [`../00-thesis-and-direction.md`](../00-thesis-and-direction.md).
