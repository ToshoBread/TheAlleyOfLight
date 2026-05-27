# Background & Asset Integration Design

## Scope

Replace all `Placeholder("bg")` with downloaded PNG/JPG assets. Add book overlay composite for book-opening scenes. Set Main Menu + Settings backdrop to `Dark_street.jpg`.

## Asset Mapping

| Scene / Screen | Asset | Notes |
|---|---|---|
| Main Menu | `Dark_street.jpg` | Background behind title + glow |
| Settings / Save / Load | `Dark_street.jpg` | Via `gui.main_menu_background` |
| Prologue (start) | `Dark_street.jpg` | Waking up in the alley |
| Prologue (door opens) | `Library.jpg` | Transition to library interior |
| enter_library | `Library.jpg` | First library scene |
| Chapters 1-6 | `Library.jpg` | All standard library scenes |
| Chapter 7 | `Library.jpg` | "Library stays light" — no night variant |
| Endings (secret/return/stay) | `Library.jpg` | Same library interior |
| Book-opening scenes | `Book_desk.jpg` + `book.png` rotated -10° | Composite scene |

## Book-Opening Scenes (use bg book_desk + book overlay)

- **ch_intro**: MC picks up glowing book → cut to book_desk
- **ch4 (truth path)**: MC finds ancient ledger → cut to book_desk
- **ch5 (memory path)**: MC touches flickering book → cut to book_desk
- **ch6**: MC opens flickering book, memories flood → cut to book_desk
- **ch7**: Final book materializes, MC reads own story → cut to book_desk

## Changes by File

### characters.rpy
- Remove 3 `Placeholder("bg")` lines
- Add: `bg dark_street`, `bg library`, `bg book_desk`
- Add: `book_overlay` image (book.png, rotate=-10, centered)
- Remove: `bg library_night` (replaced by `bg library`)

### script.rpy
- `prologue_alley`: `scene bg dark_street` (was `bg alley`), transition to `bg library` at door
- Endings: `bg library_int` → `bg library`
- Update `bg alley` refs

### chapter_intro.rpy
- `bg library_int` → `bg library`
- Book scene: `scene bg book_desk` + `show book_overlay`

### chapters 1-7
- `bg library_int` → `bg library`
- `bg library_night` → `bg library` (ch7)
- Add book_desk + book_overlay for designated book scenes

### screens.rpy
- `screen main_menu()`: add `"images/Assets/bg/Dark_street.jpg"` as background layer
- `gui.rpy`: set `gui.main_menu_background = "images/Assets/bg/Dark_street.jpg"`

## Mood Variants (Transform + matrixcolor)

3 named variants defined in `characters.rpy` using `Transform` with `matrixcolor`:

```renpy
image bg library_dim = Transform("bg library", matrixcolor=BrightnessMatrix(-0.10) * SaturationMatrix(0.7))
image bg library_cool = Transform("bg library", matrixcolor=TintMatrix((0.69, 0.77, 0.87, 1.0)) * BrightnessMatrix(-0.05))
image bg library_warm = Transform("bg library", matrixcolor=TintMatrix((1.0, 0.84, 0.0, 1.0)) * BrightnessMatrix(0.05))
```

### Mood → Chapter Mapping

| Chapter | Variant | Rationale |
|---------|---------|-----------|
| ch1 (Writer) | `bg library` (default) | Establish warmth, safety |
| ch2 (Mother) | `bg library` (default) | Maintain familiarity |
| ch3 (Mirror Man) | `bg library_dim` | Unease, first crack in reality |
| ch4 (Truth) | `bg library_dim` | Still off-balance, liminal |
| ch5 (Memory) | `bg library_cool` | Cold dread before flashback |
| ch6 | — (book_desk only) | N/A |
| ch7 (Final) | `bg library_cool` | Solemn, detached |
| secret ending | `bg library_warm` | Peaceful acceptance |
| return ending | `bg library_warm` | Hopeful return |
| stay ending | `bg library` (default) | Neutral continuation |

### Transition behavior
- Chapter breaks: hard cut (standard `scene` command)
- ch5 memory path returning from book_desk → library: `with dissolve`

## Files Not Changed

- `stats.rpy`, `options.rpy` — no visual elements
