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

<div align="center">

## ⚡ Start here

</div>

```text
1. Notion page
2. /embed
3. paste a URL from below
4. drag the block full-width   height ~220–320px
```

> First load after a push can be blank for a minute. Hard-refresh. GitHub Pages is slow once, then fine.

```mermaid
flowchart LR
  A["📄 HTML file"] --> B["🚀 GitHub Pages"]
  B --> C["📋 Copy URL"]
  C --> D["🧠 Notion /embed"]
  D --> E["✨ Widget on the page"]

  style A fill:#FFE08A,stroke:#C9A227,color:#1a1a1a
  style B fill:#9BDCFF,stroke:#2088FF,color:#1a1a1a
  style C fill:#FFB4A2,stroke:#E85D4C,color:#1a1a1a
  style D fill:#D4B5FF,stroke:#7C3AED,color:#1a1a1a
  style E fill:#B6F3C8,stroke:#16A34A,color:#1a1a1a
```

---

<div align="center">

## 🎨 Widget gallery

Pick a card. Copy the URL. That is the whole job.

</div>

<table>
<tr>
<td width="50%" valign="top">

### ⏱️ Flip clock
[![preview](https://img.shields.io/badge/live-open%20widget-111827?style=for-the-badge&labelColor=FF6B35)](https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html)

Split-flap **date + time + seconds**.
Always `America/Chicago`.
Label flips **CDT** ↔ **CST** by itself.

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html
```

| want this | stick this on the URL |
| :--- | :--- |
| 🕰️ 24-hour | `?format=24` |
| ☀️ light cards | `?theme=light` |
| 🪟 clear bg | `?bg=transparent` |
| ✨ both | `?theme=light&bg=transparent` |

```
.../flip-clock.html?format=24
.../flip-clock.html?theme=light&bg=transparent
```

</td>
<td width="50%" valign="top">

### 🌌 Orrery
[![preview](https://img.shields.io/badge/live-open%20widget-111827?style=for-the-badge&labelColor=7C3AED)](https://frankies2727.github.io/Digital-Brain-Notion-Widgets/orrery.html)

Live solar system. Planets sit where they actually are. No clock readout. Quieter starfield.

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/orrery.html
```

File: `orrery.html`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 💖 Days together
[![preview](https://img.shields.io/badge/live-open%20widget-111827?style=for-the-badge&labelColor=EC4899)](https://frankies2727.github.io/Digital-Brain-Notion-Widgets/index%20(6).html)

Live day count from the FIRE Conference start date.

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/index%20(6).html
```

File: `index (6).html`  
Filename has a space — use the encoded URL above.

</td>
<td width="50%" valign="top">

### ✨ Quotes — offline
[![preview](https://img.shields.io/badge/live-open%20widget-111827?style=for-the-badge&labelColor=22C55E)](https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithNoAPI.html)

Works with no quote API. Safer default.

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithNoAPI.html
```

File: `motivaitonalWithNoAPI.html`

</td>
</tr>
<tr>
<td width="50%" valign="top" colspan="2">

### 🌐 Quotes — with API
[![preview](https://img.shields.io/badge/live-open%20widget-111827?style=for-the-badge&labelColor=0EA5E9)](https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithAPI.html)

Same vibe, pulls quotes from an API. Use only if the offline one is not enough.

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithAPI.html
```

File: `motivaitonalWithAPI.html`

</td>
</tr>
</table>

---

<div align="center">

## 🧠 Edit a widget

</div>

```text
open the .html file  →  change it  →  push main  →  wait 30–60s  →  hard-refresh Notion
```

No build. No npm. Pages serves the files as-is.

---

<div align="center">

## 📁 Files

</div>

| color | file | what it is |
| :---: | :--- | :--- |
| 🟧 | `flip-clock.html` | Chicago flip clock |
| 🟪 | `orrery.html` | solar-system orrery |
| 🗬 | `index (6).html` | days together |
| 🟩 | `motivaitonalWithNoAPI.html` | quotes, offline |
| 🟦 | `motivaitonalWithAPI.html` | quotes, API |
| ⚪ | `.nojekyll` | tells Pages “just serve the files” |

---

<div align="center">

## 🔧 If something breaks

</div>

| symptom | fix |
| :--- | :--- |
| 🛑 **404 on a new file** | wait one minute, hard-refresh |
| 📎 **embed looks tiny** | stretch the Notion block — the widget fills the iframe |
| 🕒 **wrong time zone** | flip clock ignores the browser zone. It is Chicago-only |
| ⏸️ **want 24-hour** | add `?format=24` to the flip-clock URL |

<div align="center">

<br/>

`/embed` · paste · stretch · done

</div>
