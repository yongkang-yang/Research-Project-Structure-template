from difflib import SequenceMatcher
from pathlib import Path


def read_lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8").splitlines()


def merge_lines(left: list[str], right: list[str]) -> list[str]:
    merged: list[str] = []
    matcher = SequenceMatcher(a=left, b=right)

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            merged.extend(left[i1:i2])
            continue

        if tag in {"replace", "delete"}:
            merged.extend(left[i1:i2])

        if tag in {"replace", "insert"}:
            for line in right[j1:j2]:
                if line not in merged[-max(len(merged), 1):]:
                    merged.append(line)

    return merged


def write_text(path: Path, lines: list[str]) -> None:
    content = "\n".join(lines).rstrip() + "\n"
    path.write_text(content, encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    agents_path = root / "AGENTS.md"
    claude_path = root / "CLAUDE.md"

    agents_lines = read_lines(agents_path)
    claude_lines = read_lines(claude_path)
    merged_lines = merge_lines(agents_lines, claude_lines)

    write_text(agents_path, merged_lines)
    write_text(claude_path, merged_lines)


if __name__ == "__main__":
    main()
