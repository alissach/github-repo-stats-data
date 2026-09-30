# github-repo-stats-data

Long-term GitHub traffic stats (views, clones, referrers, stars) for my Chrome extensions, collected daily by [jgehrcke/github-repo-stats](https://github.com/jgehrcke/github-repo-stats). GitHub itself only keeps 14 days of traffic data.

- **Workflow:** [`.github/workflows/repostats.yml`](.github/workflows/repostats.yml) runs daily at 23:00 UTC (or manually from the Actions tab). Add a repo by adding it to the `statsRepo` list.
- **Reports:** on the [`github-repo-stats`](../../tree/github-repo-stats) branch, one folder per tracked repo (HTML + PDF), served via GitHub Pages:
  - [job-scraper-to-airtable](https://alissach.github.io/github-repo-stats-data/alissach/job-scraper-to-airtable/latest-report/report.html)
  - [chrome-url-redirect](https://alissach.github.io/github-repo-stats-data/alissach/chrome-url-redirect/latest-report/report.html)
  - [browser-disable-ctrl-scroll-zoom](https://alissach.github.io/github-repo-stats-data/alissach/browser-disable-ctrl-scroll-zoom/latest-report/report.html)
- **Chart explanations:** [`scripts/add_explanations.py`](scripts/add_explanations.py) adds a short explanation under each chart heading in the HTML reports after every run (the PDFs are left as the action generates them). Edit the `EXPLANATIONS` text there to change them.
- **Token:** repo secret `GHRS_GITHUB_API_TOKEN`, a fine-grained PAT with Administration (read) + Contents (read/write) on this repo and every tracked repo.
