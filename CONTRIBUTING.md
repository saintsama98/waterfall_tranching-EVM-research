# Contributing

This is an open research repository. Contributions — corrections, sources, implementation work, review of the draft spec — are welcome, and **anyone is welcome to comment on an issue or pick one up entirely**.

## Ways to contribute

- **Open an issue** — report an error, raise a design question, or propose a change. Issues are the open work-thread for this repo; feel free to claim one.
- **Discuss the design** — substantive standard-level discussion belongs on the forum thread linked from the [README](./README.md), so the conversation stays with the canonical `discussions-to` venue.
- **Open a pull request** — for spec edits, reference-implementation code, test vectors, or notes.

## Pull-request workflow

1. **Fork** this repository and clone your fork.
2. Create a topic branch (`git checkout -b <short-description>`).
3. Make your change. Keep the change focused; one concern per PR.
4. For **spec changes**, update [`CHANGELOG.md`](./CHANGELOG.md) and bump the spec version where appropriate.
5. For **code changes**, ensure the reference project builds and tests pass.
6. Open the PR against `main` with a clear description of *what* changed and *why*.

## What goes where

| Change type | Location |
|-------------|----------|
| The standard / spec text | [`spec/`](./spec/) |
| Reference implementation + tests | [`reference/`](./reference/) |
| Conformance vectors | [`test-vectors/`](./test-vectors/) |
| Research notes, exploration, sources | [`notes/`](./notes/) |
| Ecosystem/process research | [`external/`](./external/) |

## Licensing of contributions

By contributing you agree that your contributions are licensed under the repository's dual scheme: **CC-BY-4.0** for spec/prose content and **MIT** for code (see [`LICENSE`](./LICENSE) and [`LICENSE-SPEC`](./LICENSE-SPEC)).
