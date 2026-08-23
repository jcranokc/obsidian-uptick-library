# `library.json` schema

The registry is an **index, not a host**. Every entry points at a repository you
own and control. Nothing you write is copied into this repo, and removing your
entry is a one-line pull request.

## An entry

```json
{
  "id": "salesforce-admin-fundamentals",
  "name": "Salesforce Administrator — Fundamentals",
  "description": "Core admin concepts written from the public exam guide.",
  "type": "flashcards",
  "topic": "Salesforce",
  "certification": "Salesforce Certified Administrator",
  "author": "your-github-username",
  "repo": "https://github.com/your-github-username/your-repo",
  "branch": "main",
  "files": ["decks/fundamentals.md"],
  "cards": 120,
  "license": "CC-BY-4.0",
  "original": true,
  "tags": ["salesforce", "admin", "beginner"],
  "added": "2026-08-23"
}
```

| Field | Required | Notes |
|---|---|---|
| `id` | yes | Unique, lowercase, hyphens. Becomes the folder name on install. |
| `name` | yes | What a person sees. |
| `description` | yes | One sentence. What it covers and who it is for. |
| `type` | yes | `flashcards` or `exam`. |
| `topic` | yes | Broad subject, e.g. `Salesforce`, `AWS`, `Languages`. |
| `certification` | no | Exact credential name, if it targets one. |
| `author` | yes | Your GitHub username. |
| `repo` | yes | **Must be `https://github.com/...`** — nothing else is fetched. |
| `branch` | no | Defaults to `main`. |
| `files` | yes | Paths inside your repo. Markdown only. No `..`, no absolute paths. |
| `cards` | yes | Roughly how many. Honesty is the whole point. |
| `license` | yes | An SPDX id, or `CC-BY-4.0`. **No entry is merged without one.** |
| `original` | yes | `true` asserts this is your own work — see below. |
| `tags` | no | Lowercase, for filtering. |
| `added` | yes | `YYYY-MM-DD`. |

## The `original` field is the point

Setting `"original": true` asserts that **you wrote this content**, or that it
is derived from material you have the right to redistribute under the licence
you named.

It is not a formality. The most common way a study library like this dies is
people uploading questions copied from paid exam banks — Udemy courses, K2,
Whizlabs, official practice tests. That is infringement, it exposes the person
who uploaded it, and it makes the whole library untrustworthy because nobody
can tell the copied material from the real work.

**Content written from public exam guides, official documentation, or your own
notes is fine and welcome.** Content lifted from a paid question bank is not,
and will be removed on report.

## Review

A pull request is checked for: valid JSON, a licence, an `original` attestation,
a reachable `repo`, and `files` that exist and are Markdown. Content is not
reviewed for correctness — that is what `author` and `license` are for.
