---
type: note
area: create
---
# Content pipeline

idea → script → visuals → edit → scheduled → posted

## In progress
```dataview
TABLE status, account, lang, post_date, buffer_link
FROM "04 Create"
WHERE (type = "reel" OR type = "episode") AND status != "posted"
SORT choice(status = "scheduled", 1, choice(status = "edit", 2, choice(status = "visuals", 3, choice(status = "script", 4, 5)))) ASC
```

## Posted (last 20)
```dataview
TABLE account, post_date
FROM "04 Create"
WHERE (type = "reel" OR type = "episode") AND status = "posted"
SORT post_date DESC
LIMIT 20
```
