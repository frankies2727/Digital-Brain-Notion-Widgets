# C+F Digital Brain — Notion widgets

Short version: each file is one embeddable widget. Copy a URL. Paste it in Notion with `/embed`. Done.

**Base URL**

`https://frankies2727.github.io/Digital-Brain-Notion-Widgets/`

---

## Start here

1. Open a Notion page.
2. Type `/embed` and pick **Embed**.
3. Paste one of the links below.
4. Drag the block to about **full column width**. Height ~**220–320px**.

If the embed is blank for a minute after a new push, refresh. GitHub Pages is slow the first time.

---

## Widget list

Pick one. Copy the whole line.

### Flip clock — date + time + seconds (Chicago)

`https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html`

- Split-flap date and time
- Seconds included
- Timezone is always `America/Chicago`
- Label shows **CDT** in summer and **CST** in winter. You do not change anything.

**Optional add-ons** (stick these on the end of the URL)

| Want this | Add this |
| --- | --- |
| 24-hour, no AM/PM | `?format=24` |
| Light cards | `?theme=light` |
| Clear background | `?bg=transparent` |
| Light + clear | `?theme=light&bg=transparent` |

Examples

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html?format=24
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html?theme=light&bg=transparent
```

File: `flip-clock.html`

---

### Days together

`https://frankies2727.github.io/Digital-Brain-Notion-Widgets/index%20(6).html`

Live day count from the FIRE Conference start date.

File: `index (6).html`  
Note: the filename has a space. Use the encoded URL above.

---

### Quotes — offline

`https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithNoAPI.html`

Works with no internet API. Safer default.

File: `motivaitonalWithNoAPI.html`

---

### Quotes — with API

`https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithAPI.html`

Same idea, pulls quotes from an API. Use this only if the offline one is not enough.

File: `motivaitonalWithAPI.html`

---

### Orrery / planet clock

`https://frankies2727.github.io/Digital-Brain-Notion-Widgets/orrery-5.html`

Orbit-style clock.

File: `orrery-5.html`

---

## Edit a widget

1. Open the `.html` file in this repo.
2. Change the page.
3. Push to `main`.
4. Wait ~30–60 seconds.
5. Hard-refresh the Notion page.

No build step. No npm. GitHub Pages serves the files as-is.

---

## Files in this repo

| File | What it is |
| --- | --- |
| `flip-clock.html` | Chicago flip clock |
| `index (6).html` | Days together |
| `motivaitonalWithNoAPI.html` | Quotes, offline |
| `motivaitonalWithAPI.html` | Quotes, API |
| `orrery-5.html` | Planet clock |
| `.nojekyll` | Tells Pages “just serve the files” |

---

## If something breaks

- **404 on a new file** → wait one minute, then hard-refresh.
- **Embed looks tiny** → stretch the Notion block. The widget scales to the iframe.
- **Wrong time zone** → flip clock ignores the browser zone on purpose. It is Chicago-only.
- **Want 24-hour** → add `?format=24` to the flip-clock URL.
