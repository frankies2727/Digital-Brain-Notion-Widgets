# Digital-Brain-Notion-Widgets

C+F Digital Brain Notion Widgets

Hosted on GitHub Pages:
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/

## Flip clock (date + time + seconds, Chicago / CDT)

Mechanical split-flap clock locked to `America/Chicago`. DST is automatic (CDT in summer, CST in winter). Seconds flip every tick.

**Embed this URL in Notion** (`/embed`):

```
https://frankies2727.github.io/Digital-Brain-Notion-Widgets/flip-clock.html
```

Optional query params:

| Param | Values | Default |
| --- | --- | --- |
| `format` | `12` or `24` | `12` |
| `theme` | `dark` or `light` | `dark` |
| `bg` | `solid` or `transparent` | `solid` |

Examples:

- 24-hour dark: `.../flip-clock.html?format=24`
- Light + transparent for a white Notion page: `.../flip-clock.html?theme=light&bg=transparent`

Suggested Notion embed size: full column width, about 220–280px tall.

## Other widgets

- Days together: `index (6).html`
- Motivational quotes (API): `motivaitonalWithAPI.html`
- Motivational quotes (offline): `motivaitonalWithNoAPI.html`
- Orrery: `orrery-5.html`
