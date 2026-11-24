"""Unpack the editor's inline source files or rebuild the standalone page."""

import argparse
import re
from pathlib import Path


STYLES = (
    "fonts.css", "base.css", "paper-proofs.css", "archive.css",
    "art-surface.css", "emoji-picker.css", "photo-credits.css", "paper-finish.css",
)
SCRIPTS = (
    "materials.js", "translations.js", "emoji-catalog.js", "emoji-picker.js",
    "renderer.js", "gif-encoder.js", "editor.js",
)
INLINE = re.compile(rb"<(style|script)>(.*?)</\1>", re.DOTALL)


def marker(name):
    return f"<!-- inline {name} -->".encode("ascii")


def unpack(page, folder):
    html = page.read_bytes()
    matches = list(INLINE.finditer(html))
    tags = [match[1] for match in matches]
    if tags != [b"style"] * len(STYLES) + [b"script"] * len(SCRIPTS):
        raise ValueError("Unrecognized editor layout. Check the style and script block list.")
    folder.mkdir(parents=True, exist_ok=False)
    chunks = []
    start = 0
    for name, match in zip((*STYLES, *SCRIPTS), matches):
        (folder / name).write_bytes(match[2])
        chunks.extend((html[start:match.start()], marker(name)))
        start = match.end()
    chunks.append(html[start:])
    (folder / "page.html").write_bytes(b"".join(chunks))


def pack(folder, output):
    html = (folder / "page.html").read_bytes()
    for name in (*STYLES, *SCRIPTS):
        key = marker(name)
        if html.count(key) != 1:
            raise ValueError(f"Expected a single marker for {name} in page.html")
        tag = b"style" if name in STYLES else b"script"
        body = (folder / name).read_bytes()
        if b"</" + tag in body.lower():
            raise ValueError(f"Escape the closing {tag.decode()} tag literal in {name}")
        html = html.replace(key, b"<" + tag + b">" + body + b"</" + tag + b">")
    with output.open("xb") as target:
        target.write(html)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    extract = commands.add_parser("unpack", help="write the editable files into a new folder")
    extract.add_argument("page", type=Path)
    extract.add_argument("folder", type=Path)
    assemble = commands.add_parser("pack", help="build a new, self-contained HTML file")
    assemble.add_argument("folder", type=Path)
    assemble.add_argument("page", type=Path)
    args = parser.parse_args()
    if args.command == "unpack":
        unpack(args.page, args.folder)
    else:
        pack(args.folder, args.page)


if __name__ == "__main__":
    main()
