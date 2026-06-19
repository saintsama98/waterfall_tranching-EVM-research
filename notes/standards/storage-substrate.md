# Storage Substrate — ERC-7201

[ERC-7201, Namespaced Storage Layout](https://eips.ethereum.org/EIPS/eip-7201) (Final, 2023-06-20).

ERC-7201 is not a token standard. It specifies an upgrade-safe storage layout for contracts that maintain structured state, through the `@custom:storage-location erc7201:<id>` annotation and a formula that places a struct at a collision-resistant slot:

```
location = keccak256(abi.encode(uint256(keccak256(bytes(id))) - 1)) & ~bytes32(uint256(0xff))
```

```solidity
contract Example {
    /// @custom:storage-location erc7201:example.main
    struct MainStorage { uint256 x; uint256 y; }
    bytes32 private constant LOC = 0x183a6125c38840424c4a85fa12bab2ab606c4b6d0e7cc73c0c06ba5300eab500;
    function _get() private pure returns (MainStorage storage $) { assembly { $.slot := LOC } }
}
```

## Relevance

If the substrate selection (see [`../synthesis/substrate-fork.md`](../synthesis/substrate-fork.md)) favours ERC-6909 with implementer-defined semantics rather than ERC-3475, the per-tranche net asset value, seniority index, and coverage-test state require an upgrade-safe storage location keyed by tranche identifier. ERC-7201 provides exactly this layout, and is consistent with the diamond (EIP-2535) patterns used elsewhere in the broader workstream.
