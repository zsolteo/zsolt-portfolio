# HQ — vault instructions

This is Zsolt's (Csepecz Zsolt) Obsidian vault. Read this before touching any note.

## Folders
- `00 Inbox` — quick captures and raw ideas. `_archive` holds anything "deleted".
- `01 Daily` — one note per day, `YYYY-MM-DD.md`.
- `02 Sport` — underwater orienteering: training, competitions, judging, federation marketing, international contacts.
- `03 APEX` — APEX performance dashboard: specs, design/motion, WHOOP bridge, YAZIO, Render deploy.
- `04 Create` — content. `Reels/` one note per Reel, `Wise Time/` episodes of the "Wise time in my life" series, `Higgsfield/` prompts and the character sheet.
- `05 Brand & Clients` — @thechosenone, @reelworks.studio, wisetimezone webshop, `Clients/` one note per client.
- `06 Study` — Dunaújvárosi Egyetem courses and assignments.
- `07 AI Lab` — prompt library, n8n workflows, AI answers worth keeping.
- `90 Templates` — note templates. Always create notes from these.
- `99 Attachments` — images, PDFs, exports.

## Naming
- Dated notes: `YYYY-MM-DD Title`. Everything else: plain title.
- Wise Time episodes: `WT-01 Title`, `WT-02 Title`, …

## Front matter (every note)
```yaml
type:    # daily | reel | episode | project | client | competition | prompt | note
status:  # see the template
area:    # sport | apex | create | brand | study | ai
lang:    # en | hu | [en, hu]
```

## Content pipeline (Reels and episodes)
`status` moves: idea → script → visuals → edit → scheduled → posted.
- Captions always start with: "Get your Wise tee at wisetimezone, or in my bio." then one short line, then 5–6 hashtags.
- Visuals: use `04 Create/Higgsfield/Character sheet.md` for the animated self (PS2 cutscene style, holding The 48 Laws of Power where it fits).
- After scheduling on Buffer, write `buffer_link` and `post_date` back to the note.

## Rules
- Write in the language of the note; episodes need both EN and HU scripts.
- Never delete notes. Move them to `00 Inbox/_archive`.
- Link people, projects and episodes with `[[ ]]`.
- Raw video stays outside the vault (Edits `material` / `Exports` folders); only link to it.
