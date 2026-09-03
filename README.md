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

<p>
  <a href="https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html">
    <img src="https://image.thum.io/get/width/1400/crop/720/noanimate/https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html" alt="Flip clock widget" width="820">
  </a>
</p>

<sub>GitHub blocks live HTML in READMEs. These are pictures of the real widgets. Click any image to open the live one.</sub>

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

Pictures first. URL under each one.

</div>

### ⏱️ Flip clock

<div align="center">

[![Flip clock](https://image.thum.io/get/width/1400/crop/720/noanimate/https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html)](https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html)

</div>

Split-flap **date + time + seconds**. Always `America/Chicago`. Label flips **CDT** ↔ **CST** by itself.

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
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html?format=24
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html?theme=light&bg=transparent
```

---

### 🌌 Orrery

<div align="center">

[![Orrery](https://image.thum.io/get/width/1400/crop/800/noanimate/https://frankies2727.github.io/Digital-Brain-Notion-Widgets/orrery.html)](https://frankies2727.github.io/Digital-Brain-Notion-Widgets/orrery.html)

</div>

Live solar system. Planets sit where they actually are. No clock readout.

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/orrery.html
```

---

### 💖 Days together

<div align="center">

[![Days together](https://image.thum.io/get/width/1400/crop/720/noanimate/https://frankies2727.github.io/Digital-Brain-Notion-Widgets/index%20(6).html)](https://frankies2727.github.io/Digital-Brain-Notion-Widgets/index%20(6).html)

</div>

Live day count from the FIRE Conference start date.

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/index%20(6).html
```

File: `index (6).html` — filename has a space, so use the encoded URL above.

---

### ✨ Quotes — offline

<div align="center">

[![Quotes offline](https://image.thum.io/get/width/1400/crop/720/noanimate/https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithNoAPI.html)](https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithNoAPI.html)

</div>

Works with no quote API. Safer default.

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithNoAPI.html
```

---

### 🌐 Quotes — with API

<div align="center">

[![Quotes API](https://image.thum.io/get/width/1400/crop/720/noanimate/https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithAPI.html)](https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithAPI.html)

</div>

Same vibe, pulls quotes from an API. Use only if the offline one is not enough.

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/motivaitonalWithAPI.html
```

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
| 🖼️ **README image is blank** | wait a few seconds and refresh — the screenshot service is catching up |

<div align="center">

<br/>

`/embed` · paste · stretch · done

</div>
