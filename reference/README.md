# reference/

A runnable **reference implementation** of the standard in [`../spec/`](../spec/) — the
"research-as-open-tooling" artifact that proves the spec is implementable.

## Planned layout (Foundry)

```
reference/
├── foundry.toml
├── src/        # contracts implementing the spec interface
├── test/       # unit/invariant tests
└── script/     # deployment / example scripts
```

## Getting started (once code is added)

```bash
cd reference
forge build
forge test
```

> Code here is licensed under MIT (see [`../LICENSE`](../LICENSE)).
