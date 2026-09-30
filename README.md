# github-repo-stats-data

Long-term GitHub traffic stats (views, clones, referrers, stars) for my Chrome extensions, collected daily by [jgehrcke/github-repo-stats](https://github.com/jgehrcke/github-repo-stats). GitHub itself only keeps 14 days of traffic data.

- **Workflow:** [`.github/workflows/repostats.yml`](.github/workflows/repostats.yml) runs daily at 23:00 UTC (or manually from the Actions tab). Add a repo by adding it to the `statsRepo` list.
- **Reports:** on the [`github-repo-stats`](../../tree/github-repo-stats) branch, one folder per tracked repo (HTML + PDF).
- **Token:** repo secret `GHRS_GITHUB_API_TOKEN`, a fine-grained PAT with Administration (read) + Contents (read/write) on this repo and every tracked repo.
