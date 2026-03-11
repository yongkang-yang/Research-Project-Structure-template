from pathlib import Path


BEGIN_MARKER = "<!-- BEGIN DIRECTORY TREE -->"
END_MARKER = "<!-- END DIRECTORY TREE -->"
MAX_DEPTH = 3
SKIP_DIRS = {".git", "__pycache__"}
ROOT_FILES = {"AGENTS.md", "CLAUDE.md", "MEASURES.md", "PROJECT_REPORT.md", "README.md"}


def iter_children(path: Path):
    children = []
    for child in sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower())):
        if child.name in SKIP_DIRS:
            continue
        if path == ROOT and child.name in ROOT_FILES:
            continue
        if child.name.startswith(".") and child.name != ".gitkeep":
            continue
        children.append(child)
    return children


def format_name(path: Path) -> str:
    return f"{path.name}/" if path.is_dir() else path.name


def build_lines(path: Path, prefix: str = "", depth: int = 0) -> list[str]:
    lines: list[str] = []
    children = iter_children(path)
    if depth >= MAX_DEPTH:
        return lines

    for index, child in enumerate(children):
        is_last = index == len(children) - 1
        connector = "`-- " if is_last else "|-- "
        lines.append(f"{prefix}{connector}{format_name(child)}")
        if child.is_dir() and depth + 1 < MAX_DEPTH:
            extension = "    " if is_last else "|   "
            lines.extend(build_lines(child, prefix + extension, depth + 1))
    return lines


def render_tree() -> str:
    lines = ["."] + build_lines(ROOT)
    return "\n".join(lines)


def replace_block(readme_text: str, replacement: str) -> str:
    start = readme_text.index(BEGIN_MARKER)
    end = readme_text.index(END_MARKER) + len(END_MARKER)
    block = (
        f"{BEGIN_MARKER}\n"
        "```text\n"
        f"{replacement}\n"
        "```\n"
        f"{END_MARKER}"
    )
    return readme_text[:start] + block + readme_text[end:]


def main() -> None:
    readme_path = ROOT / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8")
    updated = replace_block(readme_text, render_tree())
    readme_path.write_text(updated, encoding="utf-8")


ROOT = Path(__file__).resolve().parent.parent


if __name__ == "__main__":
    main()
