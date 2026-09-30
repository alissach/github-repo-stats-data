"""Add plain-language explanations under each chart heading in the
github-repo-stats HTML reports.

The action regenerates report.html from scratch on every run, so this runs
after it (see .github/workflows/repostats.yml) and re-adds the text each time.

Usage: python add_explanations.py <data-branch-checkout-dir>
"""

import pathlib
import re
import sys

MARKER = "ghrs-explainer"

# Keyed by the heading id the report generates
EXPLANATIONS = {
    "views": (
        "How often people opened this repo's pages on GitHub: the main page, "
        "README, individual files, issues, and so on. Each bar is one day."
    ),
    "unique-visitors": (
        "Different people who viewed the repo that day. Someone who visits "
        "10 times in a day counts once. <em>Cumulative</em> adds up the daily "
        "counts, so the same person visiting on two different days counts twice."
    ),
    "total-views": (
        "Every page load, including repeat visits and refreshes. Much higher "
        "than unique visitors usually means a few people browsed around a lot."
    ),
    "clones": (
        "How often someone downloaded a full copy of the code with Git (for "
        "example to install the extension from source or to contribute). "
        "\u201cDownload ZIP\u201d is not counted. Automated tools and bots clone "
        "repos too, so clones without matching views are often not real people."
    ),
    "unique-cloners": "Different people (or machines) who cloned the repo that day.",
    "total-clones": "Every clone, including the same person cloning more than once.",
    "stargazers": "People who starred the repo, over time. A rough measure of interest.",
    "forks": "People who made their own copy of the repo on GitHub to change it.",
    "top-referrers-and-paths": (
        "Where visitors came from and what they looked at, for the most "
        "common entries."
    ),
    "top-referrers": (
        "The websites that sent visitors here, e.g. <code>google.com</code>, "
        "<code>linkedin.com</code>, or <code>github.com</code> (from inside "
        "GitHub, like your profile page or search). Direct visits from a typed "
        "or bookmarked link are not listed."
    ),
    "top-paths": (
        "The specific pages inside the repo that got the most visitors. "
        "<code>/alissach/&lt;repo&gt;</code> is the main page with the README; "
        "paths with <code>/tree/</code> are folders, <code>/blob/</code> are "
        "individual files, and <code>/issues</code> or <code>/releases</code> "
        "are those tabs. Tells you what people are most curious about."
    ),
}

STYLE = f"""<style>
.{MARKER} {{
  background: #f3f4f6;
  color: #374151;
  border-left: 3px solid #9ca3af;
  padding: 0.5em 0.8em;
  font-size: 0.9em;
  line-height: 1.45;
  margin: 0.4em 0 1em;
}}
.{MARKER} code {{ font-size: 0.95em; }}
</style>
"""


def annotate(html: str) -> str:
    if MARKER in html:
        return html
    for heading_id, text in EXPLANATIONS.items():
        html = re.sub(
            rf'(<h[1-6] id="{heading_id}">.*?</h[1-6]>)',
            rf'\1\n<p class="{MARKER}">{text}</p>',
            html,
            count=1,
        )
    return html.replace("</head>", STYLE + "</head>", 1)


def main() -> None:
    root = pathlib.Path(sys.argv[1])
    for report in root.glob("*/*/latest-report/report.html"):
        original = report.read_text(encoding="utf-8")
        updated = annotate(original)
        if updated != original:
            report.write_text(updated, encoding="utf-8")
            print(f"annotated {report}")


if __name__ == "__main__":
    main()
