#!/usr/bin/env python3
"""Pull Treadmill Utilization rows from Notion into treadmill-data.json."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

DATABASE_ID = os.environ.get("NOTION_DATABASE_ID", "c89f1d0ea6b382c8ac51811824457c0e")
TOKEN = os.environ.get("NOTION_TOKEN", "").strip()
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "treadmill-data.json"
PEOPLE = {
    "4a463c93-3bc7-49ef-b1b1-fb8c5fe0618e": "Frankie",
    "ce531e95-27f3-43be-8f40-8daecefe9c34": "Ceci",
}


def notion(path: str, payload: dict | None = None) -> dict:
    req = urllib.request.Request(
        "https://api.notion.com/v1/" + path,
        data=None if payload is None else json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        },
        method="GET" if payload is None else "POST",
    )
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.loads(res.read().decode())


def query_all() -> list[dict]:
    rows: list[dict] = []
    cursor = None
    while True:
        body: dict = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        data = notion(f"databases/{DATABASE_ID}/query", body)
        rows.extend(data.get("results") or [])
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return rows


def person_id(prop: dict) -> str:
    people = (prop or {}).get("people") or []
    if not people:
        return ""
    return people[0].get("id") or ""


def row_date(prop: dict) -> str:
    date = (prop or {}).get("date") or {}
    start = date.get("start") or ""
    return start[:10]


def row_steps(prop: dict) -> float:
    num = (prop or {}).get("number")
    return float(num or 0)


def row_name(prop: dict) -> str:
    bits = (prop or {}).get("title") or []
    return "".join(part.get("plain_text") or "" for part in bits).strip() or "Walking Steps"


def main() -> int:
    if not TOKEN:
        print("NOTION_TOKEN is missing", file=sys.stderr)
        return 1
    try:
        pages = query_all()
    except urllib.error.HTTPError as exc:
        print(exc.read().decode(), file=sys.stderr)
        return 1

    entries = []
    for page in pages:
        props = page.get("properties") or {}
        day = row_date(props.get("Day") or {})
        if not day:
            continue
        entries.append(
            {
                "date": day,
                "steps": row_steps(props.get("Steps") or {}),
                "who": person_id(props.get("Who") or {}),
                "name": row_name(props.get("Name") or {}),
            }
        )
    entries.sort(key=lambda r: (r["date"], r["who"]))

    payload = {
        "updated": datetime.now(ZoneInfo("America/Chicago")).isoformat(timespec="seconds"),
        "source": "Treadmill Utilization",
        "database_id": DATABASE_ID,
        "people": PEOPLE,
        "entries": entries,
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {len(entries)} rows to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
