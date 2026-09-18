<div align="center">

# 🕯️ C+F Digital Brain
### Notion widgets · copy a URL · paste · done

[![GitHub Pages](https://img.shields.io/badge/hosted-GitHub%20Pages-2088FF?style=for-the-badge&logo=github&logoColor=white)](https://frankies2727.github.io/Digital-Brain-Notion-Widgets/)
[![Timezone](https://img.shields.io/badge/clock-America%2FChicago-FF6B35?style=for-the-badge&logo=clockify&logoColor=white)](https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html)
[![No build](https://img.shields.io/badge/build-none-22C55E?style=for-the-badge&logo=html5&logoColor=white)](#-edit-a-widget)
[![License](https://img.shields.io/badge/vibe-colorful-A855F7?style=for-the-badge)](#-widget-gallery)

**Base URL**

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/
```

Each file is one embed. Open Notion → type <kbd>/embed</kbd> → paste a link → stretch the block.

</div>

---

## ⚡ Start here

```text
1. Notion page
2. /embed
3. paste a URL from below
4. drag the block full-width   height ~220–320px
```

> First load after a push can be blank for a minute. Hard-refresh. GitHub Pages is slow once, then fine.

---

## 🎨 Widget gallery

### ⏱️ Flip clock

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html
```

| want this | stick this on the URL |
| :--- | :--- |
| 24-hour | `?format=24` |
| light cards | `?theme=light` |
| clear bg | `?bg=transparent` |

### 🟩 Treadmill heatmap

GitHub-style year grid for **Treadmill Utilization**. Color = steps that day. Reads `treadmill-data.json`.

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/treadmill-heatmap.html
```

| want this | stick this on the URL |
| :--- | :--- |
| light | `?theme=light` |
| clear bg | `?bg=transparent` |
| Frankie only | `?who=frankie` |
| Ceci only | `?who=ceci` |
| a year | `?year=2026` |

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/treadmill-heatmap.html?who=frankie
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/treadmill-heatmap.html?theme=light&bg=transparent
```

Stretch the embed wide (~220px tall, full width). Same-day walks are summed.

To keep it in sync with Notion: repo secrets `NOTION_TOKEN` + `NOTION_DATABASE_ID`, then **Actions → Sync treadmill heatmap**.

### 🌌 Orrery

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/orrery.html
```

### 💖 Days together

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/index%20(6).html
```

### ✨ Quotes — offline

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithNoAPI.html
```

### 🌐 Quotes — with API

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithAPI.html
```

---

## 🧠 Edit a widget

```text
open the .html file  →  change it  →  push main  →  wait 30–60s  →  hard-refresh Notion
```

No build. No npm. Pages serves the files as-is.

## 📁 Files

| file | what it is |
| :--- | :--- |
| `flip-clock.html` | Chicago flip clock |
| `treadmill-heatmap.html` | GitHub-style treadmill year grid |
| `treadmill-data.json` | steps pulled from Notion |
| `scripts/sync-treadmill.py` | Notion → JSON sync |
| `.github/workflows/sync-treadmill.yml` | daily / manual refresh |
| `orrery.html` | solar-system orrery |
| `index (6).html` | days together |
| `motivaitonalWithNoAPI.html` | quotes, offline |
| `motivaitonalWithAPI.html` | quotes, API |
| `.nojekyll` | tells Pages to serve files as-is |

## 🔧 If something breaks

| symptom | fix |
| :--- | :--- |
| 404 on a new file | wait one minute, hard-refresh |
| embed looks tiny | stretch the Notion block |
| heatmap is stale | run **Sync treadmill heatmap** or ask Grok to refresh `treadmill-data.json` |
