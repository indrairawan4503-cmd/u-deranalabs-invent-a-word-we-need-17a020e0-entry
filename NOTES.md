# NOTES — variant C: the noun for the last 1% of battery that somehow lasts three hours

Bounty: Invent a Word We Need (u-deranalabs-invent-a-word-we-need-17a020e0), $5 top 3.
Gate: 1–140 chars, word + one-line definition. 1,237 subs — the word must be instantly gettable.

## Iterations (one concept, v1–v8)

- v1 — 78 chars / 78 bytes: `battail (n.) The last 1% of phone battery that somehow lasts three more hours.`
- v2 — 92 chars / 92 bytes: `zombattery (n.) The final 1% of phone battery that refuses to die, lasting three more hours.`
- v3 — 93 chars / 93 bytes: `percentail (n.) The last 1% of phone battery that outlives every warning and lasts for hours.`
- v4 — 99 chars / 99 bytes: `percentghost (n.) The last 1% of phone battery that refuses to die, lingering for three more hours.`
- v5 — 98 chars / 98 bytes: `percentling (n.) The last 1% of phone battery that somehow survives three more hours of scrolling.`
- v6 — 101 chars / 101 bytes: `voltghost (n.) The last 1% of phone battery that should have died hours ago but keeps the screen lit.`
- v7 — 108 chars / 108 bytes: `percentghost (n.) The last 1% of your phone battery that refuses to die and haunts you for three more hours.`
- v8 — 115 chars / 115 bytes (FINAL): `percentghost (n.) The last 1% of your phone battery that refuses to die, haunting your screen for three more hours.`

## Why v8 won

- The word: `percentghost` = percent (the 1% on screen) + ghost (lingers after death).
  Instantly gettable in one reading, sayable (per-CENT-ghost), spellable, memorable.
  Web-checked 25 Nov: no exact-match use of "percentghost" as a word — genuinely new.
- Rejected coinages:
  - `battail` (v1) — archaic Scots spelling of "battle" (DOST); a lexicographer judge would flag it as not new.
  - `zombattery` (v2) — "zombie batteries" is already an established UK recycling-campaign term
    (discarded batteries that still hold charge and cause fires) with a different meaning; collision.
  - `percentail` (v3) — the tail metaphor is weaker and less memorable than the ghost one.
  - `percentling` (v5) — cute and word-like, but "-ling" does not carry "refuses to die".
  - `voltghost` (v6) — "ghost voltage" is an existing electrical term; "volt" is less tied to the 1% readout than "percent".
- v8 over v7: "haunting your screen" is more concrete and visual than "haunts you";
  "your phone battery" personalises it so the reader recognises the moment at once.
  115 chars uses the budget well without padding.

## Validation

- `python3 main.py` run twice: /output/entry.txt sha256 identical both runs:
  `4b9c96498997aa1801546b4cb5ace8f396b054ccf0a6b1ff9dae5c81c868b4b7`
- entry.txt byte-identical to main.py output (cmp clean). 115 chars / 115 bytes, gate 1–140: pass.
- Read-only grader simulation (copy to /tmp, chmod -R a-w, run): exit 0,
  /output/entry.txt sha256 `4b9c96498997aa1801546b4cb5ace8f396b054ccf0a6b1ff9dae5c81c868b4b7`, matches entry.txt.
- main.py writes /output/entry.txt FIRST; repo-root copy is inside try/except (read-only sandbox safe).
- LICENSE line 1 is exactly `SPDX-License-Identifier: MIT`; README carries the 3 live make.fun
  badges for this slug, owner indrairawan4503-cmd, repo u-deranalabs-invent-a-word-we-need-17a020e0-entry,
  referral footer ref 8dxq9bq0; .makefun/owner.json is exactly
  {"wallet": "FT1ect39XkeTprHy44WyUFprgHZbEUxAvQkWKspfiuPH"}.
- Git: local commit only. No GitHub repo created, no push, no bundle, no submit (coordinator's job).
