# test-vectors/

**Machine-checkable conformance vectors**: known inputs paired with expected outputs, so
*any* implementation — not just the one in [`../reference/`](../reference/) — can prove it
conforms to the standard.

## Convention

- One file per scenario, named `NNNN-short-description.json`.
- Each vector is self-describing: inputs, expected outputs/events, and a short rationale.
- Keep vectors implementation-agnostic (no Solidity-specific assumptions beyond the ABI).

## Example shape

```json
{
  "name": "0001-basic-waterfall-distribution",
  "description": "Senior tranche paid in full before junior receives anything.",
  "given": { },
  "when":  { },
  "then":  { }
}
```

> Spec/data here is licensed under CC-BY-4.0; any tooling is MIT.
