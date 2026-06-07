#!/usr/bin/env python3
"""
Privacy scan for skill repos.

Walks the repo, applies regex-based redaction rules, and produces a report.
CRITICAL: NEVER modifies files. Only reports. The human reviews and decides
what to apply.

Usage:
    python3 privacy_scan.py <repo-root> [--out <report.md>]
"""

import argparse
import re
import sys
from pathlib import Path
from datetime import datetime

# (category, regex, suggested_replacement, severity)
# Severity: 1 = must-redact, 2 = should-redact, 3 = can-keep
RULES = [
    # --- Tier 1: MUST redact (data leaks) ---
    ("machine_user_path", re.compile(r"/Users/joy(/|\b)"), "/Users/<USER>/", 1),
    ("machine_user_tilde", re.compile(r"~/Documents/skills"), "~/<REPO_ROOT>", 1),
    ("anthropic_api_key", re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}"), "<YOUR_API_KEY>", 1),
    ("minimax_api_key", re.compile(r"\bsk-cp-[A-Za-z0-9_-]{20,}"), "<YOUR_API_KEY>", 1),
    ("github_pat", re.compile(r"\bghp_[A-Za-z0-9]{30,}\b"), "<YOUR_GITHUB_TOKEN>", 1),
    ("github_pat_new", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{50,}\b"), "<YOUR_GITHUB_TOKEN>", 1),
    ("openai_key", re.compile(r"\bsk-[A-Za-z0-9]{20,}T3BlbkFJ[A-Za-z0-9]{20,}"), "<YOUR_OPENAI_KEY>", 1),
    ("google_api_key", re.compile(r"\bAIza[A-Za-z0-9_-]{30,}"), "<YOUR_GOOGLE_KEY>", 1),
    ("feishu_token", re.compile(r"\bt-[A-Za-z0-9_-]{20,}"), "<YOUR_FEISHU_TOKEN>", 1),
    ("feishu_app", re.compile(r"\bcli_[A-Za-z0-9]{10,}\b"), "<YOUR_FEISHU_APP_ID>", 1),
    ("email_personal", re.compile(r"\b[A-Za-z0-9._%+-]+@(gmail|qq|163|outlook|hotmail|yahoo|icloud)\.com\b"), "<YOUR_EMAIL>", 1),
    ("lan_ip", re.compile(r"\b(?:192\.168|10\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b"), "<LAN_IP>", 1),
    ("github_username_in_url", re.compile(r"github\.com/Joy917/"), "github.com/<YOUR_GH_USER>/", 1),
    # Hex/base64 long strings (likely tokens/hashes) — only if they look like secrets
    ("long_b64", re.compile(r"\b[A-Za-z0-9+/=_-]{40,}\b"), "<POSSIBLE_SECRET>", 2),

    # --- Tier 2: SHOULD redact (PII / context leak) ---
    ("personal_pub_name", re.compile(r"「左一说」"), "<YOUR_PUBLICATION>", 2),
    ("personal_pub_handle", re.compile(r"@coderjoy666"), "<YOUR_HANDLE>", 2),
    ("weixin_openid", re.compile(r"\bou_[A-Za-z0-9_-]{20,}\b"), "<YOUR_USER_ID>", 2),
    ("feishu_openid", re.compile(r"\b[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\b"), "<UUID_USER_ID>", 2),
    ("weixin_account_id", re.compile(r"\b857fc3c4[A-Za-z0-9_]*\b"), "<ACCOUNT_ID>", 2),
    ("feishu_app_id_14digit", re.compile(r"\bcli_[a-z0-9]{14}\b"), "<FEISHU_APP_ID>", 2),
    ("specific_zhuanlan_url", re.compile(r"https://wx\.zsxq\.com/group/\d+"), "<PRIVATE_GROUP_URL>", 2),
    ("specific_podcast", re.compile(r"左一说\s*·\s*每周聊几个AI话题"), "<YOUR_TAGLINE>", 2),

    # --- Tier 3: keep (general / not identifying) ---
    # These are NOT redacted but logged as "considered and kept":
    # - General platform names: GitHub, Claude, Hermes
    # - Skill names, framework names
    # - Public example URLs (github.com/anthropics/...)
    # - AI product names (Notion, Linear, etc.)
]

# Files to skip
SKIP_PATTERNS = [
    ".git/",
    "__pycache__/",
    "node_modules/",
    ".DS_Store",
    "*.pyc",
    ".venv/",
    "venv/",
    "privacy_scan.py",  # the scanner itself
]


def should_skip(path: Path) -> bool:
    s = str(path)
    return any(pat in s for pat in SKIP_PATTERNS)


def scan(root: Path) -> list:
    """Returns list of (file, line_no, rule_category, match_text, severity, replacement)"""
    hits = []
    for p in root.rglob("*"):
        if not p.is_file() or should_skip(p):
            continue
        # Only text-ish files
        if p.suffix not in {".md", ".txt", ".py", ".js", ".ts", ".json", ".yaml", ".yml", ".sh", ".toml", ".html", ".css", ".csv", ""}:
            continue
        try:
            content = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for line_no, line in enumerate(content.splitlines(), start=1):
            for cat, regex, repl, sev in RULES:
                for m in regex.finditer(line):
                    hits.append({
                        "file": str(p.relative_to(root)),
                        "line": line_no,
                        "rule": cat,
                        "match": m.group(0),
                        "replacement": repl,
                        "severity": sev,
                        "context": line.strip()[:200],
                    })
    return hits


def render_report(root: Path, hits: list) -> str:
    out = []
    out.append(f"# Privacy Scan Report")
    out.append("")
    out.append(f"**Repo:** `{root}`")
    out.append(f"**Scanned at:** {datetime.now().isoformat(timespec='seconds')}")
    out.append(f"**Total hits:** {len(hits)}")
    out.append("")
    out.append("---")
    out.append("")

    if not hits:
        out.append("✅ No hits. Safe to push.")
        return "\n".join(out)

    # Group by severity
    by_sev = {1: [], 2: [], 3: []}
    for h in hits:
        by_sev[h["severity"]].append(h)

    severity_labels = {
        1: "🔴 Tier 1 — MUST REDACT (data leak risk)",
        2: "🟡 Tier 2 — SHOULD REDACT (PII / context leak)",
        3: "🟢 Tier 3 — keep but acknowledged",
    }

    for sev in (1, 2, 3):
        group = by_sev[sev]
        if not group:
            continue
        out.append(f"## {severity_labels[sev]}")
        out.append(f"**Count:** {len(group)}")
        out.append("")
        # Group by file
        by_file = {}
        for h in group:
            by_file.setdefault(h["file"], []).append(h)
        for f, file_hits in sorted(by_file.items()):
            out.append(f"### `{f}`")
            out.append("")
            out.append("| Line | Rule | Match | Suggested replacement | Context |")
            out.append("|---|---|---|---|---|")
            for h in file_hits:
                # Truncate match for display
                m_disp = h["match"]
                if len(m_disp) > 40:
                    m_disp = m_disp[:20] + "..." + m_disp[-10:]
                ctx = h["context"].replace("|", "\\|")
                if len(ctx) > 120:
                    ctx = ctx[:120] + "..."
                out.append(f"| {h['line']} | `{h['rule']}` | `{m_disp}` | `{h['replacement']}` | {ctx} |")
            out.append("")

    out.append("---")
    out.append("")
    out.append("## Next steps")
    out.append("")
    out.append("1. **Review Tier 1 hits** — these MUST be fixed before pushing. Apply mechanically, no judgment needed.")
    out.append("2. **Review Tier 2 hits** — these depend on whether you want the repo to be anonymous or personally branded. Decide per hit.")
    out.append("3. **Tier 3 hits** — none in this report (Tier 3 is for things considered and kept; not currently flagged).")
    out.append("")
    out.append("Once you've decided, run a separate apply script to actually rewrite the files. The scanner does NOT modify files.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path, help="Repo root to scan")
    ap.add_argument("--out", type=Path, default=None, help="Output report path (default: stdout)")
    args = ap.parse_args()

    if not args.root.exists():
        print(f"ERROR: {args.root} does not exist", file=sys.stderr)
        sys.exit(1)

    hits = scan(args.root)
    report = render_report(args.root, hits)

    if args.out:
        args.out.write_text(report)
        print(f"Report written to {args.out}")
        print(f"Hits: {len(hits)}")
    else:
        print(report)


if __name__ == "__main__":
    main()
