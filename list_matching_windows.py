"""TODO: module documentation"""

import pygetwindow as gw

print("Scanning all open window titles...")
matching = []
for title in gw.getAllTitles():
    if not title.strip():
        continue
    title_lower = title.lower()
    terms = [
        "maplestory",
        "photo viewer",
        "photos",
        "lie_capcha",
        "lie_click",
        "lie_violet",
        "lie_stars",
    ]
    matched_terms = [t for t in terms if t in title_lower]
    if matched_terms:
        # Pastikan bukan jendela browser, text editor, chat apps, dll.
        excludes = [
            "chrome",
            "firefox",
            "edge",
            "brave",
            "opera",
            "safari",
            "explorer",
            "discord",
            "vscode",
            "visual studio",
            "notepad",
            "sublime",
        ]
        if any(e in title_lower for e in excludes):
            continue

        w = gw.getWindowsWithTitle(title)[0]
        matching.append((title, matched_terms, w.isMinimized, w.left, w.top, w.width, w.height))

if not matching:
    print("No matching windows found at all.")
else:
    print(f"Found {len(matching)} matching window(s):")
    for idx, (title, terms, minimized, left, top, w, h) in enumerate(matching):
        print(f"[{idx}] Title: '{title}'")
        print(f"    Matched terms: {terms}")
        # pygetwindow properties: isMinimized
        print(f"    Minimized: {minimized} | Pos: ({left}, {top}) | Size: {w}x{h}")
