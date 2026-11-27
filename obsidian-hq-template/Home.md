---
type: note
area: hq
---
# HQ

## Today
- Today's note: click the calendar icon in the left ribbon (core Daily notes)
- [[00 Inbox]] — empty it every Sunday

## Content pipeline
[[04 Create/Pipeline|Pipeline table]]

```dataview
TABLE status, account, post_date
FROM "04 Create"
WHERE (type = "reel" OR type = "episode") AND status != "posted"
SORT post_date ASC
```

## Active projects
```dataview
TABLE area, deadline
WHERE type = "project" AND status = "active"
SORT deadline ASC
```

## Areas
- [[02 Sport]] · [[03 APEX]] · [[04 Create]] · [[05 Brand & Clients]] · [[06 Study]] · [[07 AI Lab]]
