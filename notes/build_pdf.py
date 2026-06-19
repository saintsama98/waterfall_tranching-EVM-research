#!/usr/bin/env python3
"""Build a single consolidated PDF of the research garden, in index order.

Flattens the interlinked notes into one document for reading/distribution.
Internal relative .md links are neutralised to plain text (they have no target
in a flattened document); external links are preserved. Run from notes/:

    python3 build_pdf.py
"""
import re
from pathlib import Path

import markdown
from weasyprint import HTML

HERE = Path(__file__).resolve().parent
OUT = HERE / "tranches-waterfall-research.pdf"

# Reading order — mirrors index.md. The top-level index.md and README.md are
# navigation aids and are intentionally excluded from the flattened document.
ORDER = [
    "00-thesis-and-direction.md",
    "standards/index.md",
    "standards/timeline-and-reading-order.md",
    "standards/token-substrate-layer.md",
    "standards/vault-and-yield-layer.md",
    "standards/storage-substrate.md",
    "standards/security-token-branch.md",
    "mechanics/index.md",
    "mechanics/waterfall-tranching-primer.md",
    "mechanics/oc-ic-coverage-tests.md",
    "mechanics/heuristics-vs-plumbing.md",
    "protocols/index.md",
    "protocols/reference-architecture.md",
    "protocols/loss-tranching-protocols.md",
    "protocols/cashflow-tranching-protocols.md",
    "protocols/rwa-securitization-entrants.md",
    "protocols/standards-adoption-matrix.md",
    "synthesis/index.md",
    "synthesis/substrate-fork.md",
    "synthesis/open-questions-and-next.md",
]

LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def neutralise_internal_links(text: str) -> str:
    def repl(m):
        label, url = m.group(1), m.group(2)
        if url.startswith("http"):
            return m.group(0)
        return label  # internal/relative link -> plain text
    return LINK.sub(repl, text)


def main() -> None:
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    sections = []
    for rel in ORDER:
        raw = (HERE / rel).read_text(encoding="utf-8")
        html = md.convert(neutralise_internal_links(raw))
        md.reset()
        sections.append(f'<section class="note">{html}</section>')

    cover = (
        '<section class="cover">'
        "<h1>Waterfall Tranching Standard</h1>"
        "<p class=\"sub\">Directional Research</p>"
        "<p class=\"meta\">Consolidated 2026-06-19 &middot; status: in progress</p>"
        "</section>"
    )

    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<style>
@page {{ size: A4; margin: 22mm 20mm;
  @bottom-center {{ content: counter(page); font-family: Georgia, serif; font-size: 9pt; color: #888; }} }}
html {{ font-family: Georgia, 'Times New Roman', serif; font-size: 10.5pt; line-height: 1.5; color: #1a1a1a; }}
.cover {{ text-align: center; margin-top: 38%; }}
.cover h1 {{ font-size: 26pt; border: none; margin-bottom: 4pt; }}
.cover .sub {{ font-size: 14pt; color: #555; letter-spacing: 0.5pt; }}
.cover .meta {{ font-size: 10pt; color: #999; margin-top: 18pt; }}
section.note {{ page-break-before: always; }}
h1, h2, h3 {{ font-family: 'Helvetica Neue', Arial, sans-serif; color: #111; line-height: 1.25; }}
h1 {{ font-size: 17pt; border-bottom: 1.5px solid #222; padding-bottom: 4pt; margin-top: 0; }}
h2 {{ font-size: 12.5pt; margin-top: 16pt; }}
h3 {{ font-size: 11pt; color: #333; }}
p {{ margin: 6pt 0; }}
a {{ color: #1a4d7a; text-decoration: none; }}
code {{ font-family: 'DejaVu Sans Mono', monospace; font-size: 8.6pt; background: #f3f3f3; padding: 1px 3px; border-radius: 2px; }}
pre {{ background: #f6f8fa; border: 1px solid #e1e4e8; border-radius: 4px; padding: 9pt 11pt;
  font-family: 'DejaVu Sans Mono', monospace; font-size: 8.2pt; line-height: 1.32; white-space: pre; overflow-x: hidden; }}
pre code {{ background: none; padding: 0; font-size: 8.2pt; }}
table {{ border-collapse: collapse; width: 100%; margin: 9pt 0; font-size: 9pt; }}
th, td {{ border: 1px solid #d0d0d0; padding: 4pt 7pt; text-align: left; vertical-align: top; }}
th {{ background: #f0f0f0; font-family: 'Helvetica Neue', Arial, sans-serif; }}
blockquote {{ border-left: 3px solid #ccc; margin: 8pt 0; padding: 2pt 12pt; color: #444; }}
hr {{ border: none; border-top: 1px solid #ddd; margin: 14pt 0; }}
</style></head><body>{cover}{''.join(sections)}</body></html>"""

    HTML(string=doc, base_url=str(HERE)).write_pdf(str(OUT))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
