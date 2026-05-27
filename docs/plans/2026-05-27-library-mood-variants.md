# Library Mood Variants Implementation Plan

> **For agentic workers:** Implement this plan task-by-task.

**Goal:** Add 3 mood variants of the library background using Transform + matrixcolor, mapped to chapters by narrative arc.

**Architecture:** Define 3 new Ren'Py image statements in `characters.rpy` that apply `matrixcolor` transforms to the existing `bg library`. Update `scene` calls in chapter files and endings. Zero new assets.

**Tech Stack:** Ren'Py 8.5.3, `Transform`, `matrixcolor`, `TintMatrix`, `BrightnessMatrix`, `SaturationMatrix`

---

## File Structure

| File | Change |
|------|--------|
| `game/characters.rpy:59` | Insert 3 mood variant image definitions after `bg book_desk` |
| `game/chapter3.rpy:2` | `scene bg library` → `scene bg library_dim` |
| `game/chapter4.rpy:2` | `scene bg library` → `scene bg library_dim` |
| `game/chapter5.rpy:2` | `scene bg library` → `scene bg library_cool` |
| `game/chapter7.rpy:2` | `scene bg library` → `scene bg library_cool` |
| `game/script.rpy:61` | `scene bg library` → `scene bg library_warm` (secret ending) |
| `game/script.rpy:72` | `scene bg library` → `scene bg library_warm` (return ending) |

---

### Task 1: Add 3 mood variant images in characters.rpy

**Files:**
- Modify: `game/characters.rpy:58-59`

- [ ] **Insert 3 mood variant lines after `bg book_desk`**

Old:
```renpy
image bg book_desk = "images/Assets/bg/Book_desk.jpg"

image book_overlay = Transform("images/Assets/items/book.png", rotate=-10, align=(0.5, 0.5))
```

New:
```renpy
image bg book_desk = "images/Assets/bg/Book_desk.jpg"

image bg library_dim = Transform("bg library", matrixcolor=BrightnessMatrix(-0.10) * SaturationMatrix(0.7))
image bg library_cool = Transform("bg library", matrixcolor=TintMatrix((0.69, 0.77, 0.87, 1.0)) * BrightnessMatrix(-0.05))
image bg library_warm = Transform("bg library", matrixcolor=TintMatrix((1.0, 0.84, 0.0, 1.0)) * BrightnessMatrix(0.05))

image book_overlay = Transform("images/Assets/items/book.png", rotate=-10, align=(0.5, 0.5))
```

Note: `matrixcolor` requires Ren'Py 7.4+ / 8.0+. This project runs Ren'Py 8.5.3 — supported.

- [ ] **Commit**

```bash
git add game/characters.rpy
git commit -m "feat: add 3 library mood variants (dim, cool, warm)"
```

---

### Task 2: Update chapter3.rpy — dim variant

**Files:**
- Modify: `game/chapter3.rpy:2`

- [ ] **Replace `bg library` with `bg library_dim`**

Old:
```renpy
    scene bg library
```

New:
```renpy
    scene bg library_dim
```

- [ ] **Commit**

```bash
git add game/chapter3.rpy
git commit -m "feat: ch3 mirror man uses library_dim"
```

---

### Task 3: Update chapter4.rpy — dim variant

**Files:**
- Modify: `game/chapter4.rpy:2`

- [ ] **Replace `bg library` with `bg library_dim`**

Old:
```renpy
    scene bg library
```

New:
```renpy
    scene bg library_dim
```

- [ ] **Commit**

```bash
git add game/chapter4.rpy
git commit -m "feat: ch4 truth uses library_dim"
```

---

### Task 4: Update chapter5.rpy — cool variant

**Files:**
- Modify: `game/chapter5.rpy:2`

- [ ] **Replace `bg library` with `bg library_cool`**

Old:
```renpy
    scene bg library
```

New:
```renpy
    scene bg library_cool
```

- [ ] **Commit**

```bash
git add game/chapter5.rpy
git commit -m "feat: ch5 memory uses library_cool"
```

---

### Task 5: Update chapter7.rpy — cool variant

**Files:**
- Modify: `game/chapter7.rpy:2`

- [ ] **Replace `bg library` with `bg library_cool`**

Old:
```renpy
    scene bg library
```

New:
```renpy
    scene bg library_cool
```

- [ ] **Commit**

```bash
git add game/chapter7.rpy
git commit -m "feat: ch7 final uses library_cool"
```

---

### Task 6: Update endings in script.rpy — warm variant

**Files:**
- Modify: `game/script.rpy:61,72`

- [ ] **Replace `bg library` with `bg library_warm` in secret and return endings**

Line 61 (secret):
Old:
```renpy
    scene bg library
```
New:
```renpy
    scene bg library_warm
```

Line 72 (return):
Old:
```renpy
    scene bg library
```
New:
```renpy
    scene bg library_warm
```

- [ ] **Commit**

```bash
git add game/script.rpy
git commit -m "feat: secret/return endings use library_warm"
```

---

### Task 7: Lint verification

- [ ] **Ren'Py lint check**

```bash
/home/zndionisio/Downloads/Apps/Renpy/renpy-8.5.3-sdk/renpy.sh /home/zndionisio/Downloads/Apps/Renpy/renpy-8.5.3-sdk/games/The\ Alley\ of\ Light --lint
```

Expected: No errors or warnings. Delete any stale `.rpyc` files if lint complains about write permissions.

- [ ] **Update AGENTS.md if needed** — no changes expected.
