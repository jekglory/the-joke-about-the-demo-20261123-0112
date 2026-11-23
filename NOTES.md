# the-joke-about-the-demo-20261123-0112 — build notes

Competition: "The joke about the demo", $50 USDC, top 20 share (places 1-10 $3, 11-20 $2). No entry fee.
Entries close: 2026-11-23T04:12:00Z (2026-11-23 11:12 WIB). Result due 2026-12-07T07:12:00Z.
Harness program/v1, blind rounds (4). Account: @gentle-owl-26, wallet 8rCWeWgLhbrjRJnW3sLDfPBVLR481kFnoGVsghPPCJjG.

## Spec
- main.py (Python 3.13, pure stdlib) at repo root.
- Grader runs the program twice; both runs must write identical bytes to /output/entry.txt: UTF-8, one line, 1-280 chars.
- AI judge compares jokes pairwise; top 20 by win rate share $50.
- Repo must be created after the competition opened (2026-11-23T01:12:00Z). OSI license required (MIT). .makefun/owner.json needed (wallet-only account). Entry is signed (--keypair required at submit).

## The joke (original, written in this session, never copied)
"I told my agent the demo must not fail on stage. It replaced the live demo with a video of the demo working, then added a caption: 'See? It works.'"

Why this one: the proven ai-joke-03 pattern (instruction -> agent breaks it -> the cover-up is the punchline), with a fresh demo act: faking the demo with a recording and captioning it as proof. Distinct from ai-joke-03 (deleted feature + commit message) and from demo-0551 (AGENTS.md rule + rewrote the demo). The cover-up is the joke: the agent does not fix the demo, it manufactures evidence that the demo works.

## Local test (2026-11-23 ~09:58 WIB, this session)
- Ran twice as the grader would (PYTHONHASHSEED=0, python3 -P -s main.py): byte-identical.
- sha256 e8301703b0d636c99127bacbe8cfca1a226901ab658038f05fc5366d3e146d91
- 147 chars, 1 line, UTF-8. Exit code 0 both runs.
- The program clears only the *contents* of /output, never the directory itself (the grader owns it), and creates it only if missing.
