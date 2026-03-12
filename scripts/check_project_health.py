#!/usr/bin/env python3
"""
Project Health Check Script

Checks:
1. Required files exist
2. Document last update times
3. AGENTS.md and CLAUDE.md synchronization
4. File naming conventions
"""

import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.resolve()

REQUIRED_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "PROJECT_REPORT.md",
    "MEASURES.md",
    "README.md",
]

REQUIRED_DIRS = [
    "data",
    "scripts",
    "compliance",
    "submission",
    "writing",
    "presentation",
]

WARNING_DAYS = 30

NAMING_PATTERNS = {
    "analysis": r"^\d{4}-\d{2}-\d{2}_study\d+_.+_v\d+\.\w+$",
    "draft": r"^\d{4}-\d{2}-\d{2}_.+_draft_v\d+\.\w+$",
    "meeting": r"^\d{4}-\d{2}-\d{2}_meeting_.*\.md$",
    "log": r"^\d{4}-\d{2}-\d{2}_.*\.md$",
}


class Colors:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    END = "\033[0m"


def check_required_files():
    """Check if all required root files exist."""
    print(f"\n{Colors.BLUE}=== Checking Required Files ==={Colors.END}")
    all_exist = True
    for filename in REQUIRED_FILES:
        filepath = PROJECT_ROOT / filename
        if filepath.exists():
            print(f"  {Colors.GREEN}✓{Colors.END} {filename}")
        else:
            print(f"  {Colors.RED}✗{Colors.END} {filename} (MISSING)")
            all_exist = False
    return all_exist


def check_required_dirs():
    """Check if all required directories exist."""
    print(f"\n{Colors.BLUE}=== Checking Required Directories ==={Colors.END}")
    all_exist = True
    for dirname in REQUIRED_DIRS:
        dirpath = PROJECT_ROOT / dirname
        if dirpath.exists() and dirpath.is_dir():
            print(f"  {Colors.GREEN}✓{Colors.END} {dirname}/")
        else:
            print(f"  {Colors.RED}✗{Colors.END} {dirname}/ (MISSING)")
            all_exist = False
    return all_exist


def check_document_updates():
    """Check if documents have been updated recently."""
    print(f"\n{Colors.BLUE}=== Checking Document Update Times ==={Colors.END}")
    docs = ["PROJECT_REPORT.md", "MEASURES.md", "AGENTS.md", "CLAUDE.md", "README.md"]
    stale = []
    for doc in docs:
        filepath = PROJECT_ROOT / doc
        if filepath.exists():
            mtime = datetime.fromtimestamp(filepath.stat().st_mtime)
            age = (datetime.now() - mtime).days
            if age > WARNING_DAYS:
                print(
                    f"  {Colors.YELLOW}⚠{Colors.END} {doc} (last updated {age} days ago)"
                )
                stale.append(doc)
            else:
                print(f"  {Colors.GREEN}✓{Colors.END} {doc} (updated {age} days ago)")
    return len(stale) == 0


def check_ai_docs_sync():
    """Check if AGENTS.md and CLAUDE.md are synchronized."""
    print(f"\n{Colors.BLUE}=== Checking AI Docs Synchronization ==={Colors.END}")
    agents = PROJECT_ROOT / "AGENTS.md"
    claude = PROJECT_ROOT / "CLAUDE.md"

    if not agents.exists() or not claude.exists():
        print(f"  {Colors.RED}✗{Colors.END} One or both files missing")
        return False

    agents_content = agents.read_text()
    claude_content = claude.read_text()

    if agents_content == claude_content:
        print(f"  {Colors.GREEN}✓{Colors.END} AGENTS.md and CLAUDE.md are synchronized")
        return True
    else:
        print(f"  {Colors.RED}✗{Colors.END} AGENTS.md and CLAUDE.md are OUT OF SYNC")
        return False


def check_naming_conventions():
    """Check file naming conventions."""
    print(f"\n{Colors.BLUE}=== Checking File Naming Conventions ==={Colors.END}")
    import re

    violations = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        if ".git" in root:
            continue
        for f in files:
            if f.startswith(".") or f.endswith(".pyc"):
                continue
            filepath = Path(root) / f
            rel_path = filepath.relative_to(PROJECT_ROOT)

            matched = False
            for pattern_name, pattern in NAMING_PATTERNS.items():
                if re.match(pattern, f):
                    matched = True
                    break

            if not matched:
                violations.append(str(rel_path))

    if violations:
        print(f"  {Colors.YELLOW}⚠{Colors.END} Files not following naming conventions:")
        for v in violations[:10]:
            print(f"      {v}")
        if len(violations) > 10:
            print(f"      ... and {len(violations) - 10} more")
        return False
    else:
        print(f"  {Colors.GREEN}✓{Colors.END} All files follow naming conventions")
        return True


def main():
    print(f"{Colors.BLUE}Research Project Health Check{Colors.END}")
    print(f"Project: {PROJECT_ROOT}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    results = {
        "files": check_required_files(),
        "dirs": check_required_dirs(),
        "updates": check_document_updates(),
        "sync": check_ai_docs_sync(),
        "naming": check_naming_conventions(),
    }

    print(f"\n{Colors.BLUE}=== Summary ==={Colors.END}")
    all_passed = all(results.values())

    if all_passed:
        print(f"{Colors.GREEN}All checks passed!{Colors.END}")
        return 0
    else:
        print(f"{Colors.RED}Some checks failed. Please review above.{Colors.END}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
