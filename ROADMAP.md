# 🧩 PlugOS Roadmap

> A living lesson checklist for building **PlugOS** from a simple Python terminal prototype into a cleaner, expandable game project.

![Status](https://img.shields.io/badge/status-prototype-orange)
![Language](https://img.shields.io/badge/language-python-blue)
![Roadmap](https://img.shields.io/badge/roadmap-active-brightgreen)

## 🗺️ Roadmap Overview

| Phase | Focus | Status |
|---:|---|---|
| 1 | Core Python Control | ⬜ Planned |
| 2 | Player State | ⬜ Planned |
| 3 | Trading System | ⬜ Planned |
| 4 | Game Loop Design | ⬜ Planned |
| 5 | Code Structure Upgrade | ⬜ Planned |
| 6 | Multiple Products | ⬜ Planned |
| 7 | Risk Systems | ⬜ Planned |
| 8 | Reputation System | ⬜ Planned |
| 9 | Events | ⬜ Planned |
| 10 | Saving and Loading | ⬜ Planned |
| 11 | Project Files | ⬜ Planned |
| 12 | Polish | ⬜ Planned |
| 13 | Git Discipline | ⬜ Planned |

---

# Phase 1 — Core Python Control

> **Goal:** Understand how a Python terminal game runs from top to bottom.

<details>
<summary><strong>Lesson 1 — Program Flow</strong></summary>

- [x] Understand that Python runs from top to bottom
- [ ] Understand why imports come first
- [ ] Understand why variables are created before functions use them
- [ ] Understand why the game loop sits at the bottom
- [ ] Understand how `while running:` keeps the game alive

</details>

<details>
<summary><strong>Lesson 2 — Menu Systems</strong></summary>

- [ ] Understand how a printed menu gives the player choices
- [ ] Understand how `input()` stores a player choice
- [ ] Understand how `if / elif / else` routes the choice
- [ ] Add new menu options without breaking old ones
- [ ] Keep menu text readable and consistent

</details>

<details>
<summary><strong>Lesson 3 — Functions</strong></summary>

- [ ] Understand what a function is
- [ ] Understand why functions stop code becoming one massive swamp
- [ ] Know when to create a new function
- [ ] Know how to call a function
- [ ] Keep each function focused on one job

</details>

<details>
<summary><strong>Lesson 4 — Basic Validation</strong></summary>

- [ ] Understand why raw player input cannot be trusted
- [ ] Convert text input into numbers safely
- [ ] Handle bad input without crashing
- [ ] Reject negative numbers
- [ ] Reject zero where zero makes no sense

</details>

---

# Phase 2 — Player State

> **Goal:** Make the player’s data easier to manage.

<details>
<summary><strong>Lesson 5 — Player Stats</strong></summary>

- [ ] Track cash
- [ ] Track reputation
- [ ] Track inventory
- [ ] Track current day
- [ ] Display stats clearly

</details>

<details>
<summary><strong>Lesson 6 — State Changes</strong></summary>

- [ ] Understand what changes cash
- [ ] Understand what changes reputation
- [ ] Understand what changes inventory
- [ ] Understand what advances the day
- [ ] Make sure actions update the right values

</details>

<details>
<summary><strong>Lesson 7 — Globals</strong></summary>

- [ ] Understand what a global variable is
- [ ] Understand why globals are simple at first
- [ ] Understand why globals become messy later
- [ ] Learn what `global` does
- [ ] Prepare to move state into cleaner structures later

</details>

---

# Phase 3 — Trading System

> **Goal:** Turn buying and selling into the central gameplay system.

<details>
<summary><strong>Lesson 8 — Product Basics</strong></summary>

- [ ] Understand product stock
- [ ] Understand buy price
- [ ] Understand sell price
- [ ] Understand profit
- [ ] Understand risk when buying at bad prices

</details>

<details>
<summary><strong>Lesson 9 — Buying</strong></summary>

- [ ] Ask the player how much they want to buy
- [ ] Check the amount is valid
- [ ] Check the player has enough cash
- [ ] Subtract cash
- [ ] Add inventory
- [ ] Advance the day

</details>

<details>
<summary><strong>Lesson 10 — Selling</strong></summary>

- [ ] Ask the player how much they want to sell
- [ ] Check the amount is valid
- [ ] Check the player has enough stock
- [ ] Remove inventory
- [ ] Add cash
- [ ] Advance the day

</details>

<details>
<summary><strong>Lesson 11 — Market Prices</strong></summary>

- [ ] Understand random price generation
- [ ] Update prices after actions
- [ ] Display current market prices
- [ ] Notice when prices create profit opportunities
- [ ] Avoid making randomness feel completely pointless

</details>

---

# Phase 4 — Game Loop Design

> **Goal:** Make each turn feel like part of a game, not just a menu calculator.

<details>
<summary><strong>Lesson 12 — Days and Turns</strong></summary>

- [ ] Understand that each meaningful action should cost time
- [ ] Decide which actions advance the day
- [ ] Decide which actions should not advance the day
- [ ] Display the current day clearly
- [ ] Use the day system for future events

</details>

<details>
<summary><strong>Lesson 13 — Jobs</strong></summary>

- [ ] Add safe ways to earn small money
- [ ] Make jobs affect reputation
- [ ] Make jobs advance the day
- [ ] Decide whether jobs should have risk
- [ ] Decide whether jobs should become less useful over time

</details>

<details>
<summary><strong>Lesson 14 — Win and Lose Conditions</strong></summary>

- [ ] Create a cash goal
- [ ] Check the goal after each action
- [ ] End the game cleanly when the goal is reached
- [ ] Add a loss condition later
- [ ] Make the player understand what they are working toward

</details>

---

# Phase 5 — Code Structure Upgrade

> **Goal:** Move from beginner script to cleaner project structure.

<details>
<summary><strong>Lesson 15 — Dictionaries</strong></summary>

- [ ] Learn what a dictionary is
- [ ] Store player stats in a dictionary
- [ ] Store product data in a dictionary
- [ ] Read values from dictionaries
- [ ] Update values inside dictionaries

</details>

<details>
<summary><strong>Lesson 16 — Reusable Functions</strong></summary>

- [ ] Replace repeated code with helper functions
- [ ] Pass values into functions using parameters
- [ ] Return values from functions
- [ ] Avoid copy-pasting similar functions
- [ ] Make functions reusable for more than one product

</details>

<details>
<summary><strong>Lesson 17 — Data-Driven Design</strong></summary>

- [ ] Understand that products should be data
- [ ] Add new products without writing whole new systems
- [ ] Store product names, prices, and stock together
- [ ] Loop through products to show the market
- [ ] Build systems that scale

</details>

---

# Phase 6 — Multiple Products

> **Goal:** Expand the game beyond one trade item.

<details>
<summary><strong>Lesson 18 — Product Expansion</strong></summary>

- [ ] Add a second product
- [ ] Give each product separate prices
- [ ] Give each product separate inventory
- [ ] Let the player choose which product to buy
- [ ] Let the player choose which product to sell

</details>

<details>
<summary><strong>Lesson 19 — Product Balance</strong></summary>

- [ ] Give cheap products lower profit
- [ ] Give expensive products higher risk
- [ ] Make rare products harder to buy
- [ ] Make some products reputation-locked
- [ ] Make market changes matter

</details>

---

# Phase 7 — Risk Systems

> **Goal:** Make the game more interesting by adding danger and consequence.

<details>
<summary><strong>Lesson 20 — Heat</strong></summary>

- [ ] Add a heat/wanted level
- [ ] Increase heat after risky actions
- [ ] Lower heat through resting or bribes
- [ ] Display heat to the player
- [ ] Use heat to trigger danger

</details>

<details>
<summary><strong>Lesson 21 — Police Events</strong></summary>

- [ ] Create random police checks
- [ ] Make risk depend on heat
- [ ] Add consequences for getting caught
- [ ] Remove cash, inventory, or reputation as punishment
- [ ] Make risk understandable, not random nonsense

</details>

<details>
<summary><strong>Lesson 22 — Debt or Rent</strong></summary>

- [ ] Add regular costs
- [ ] Charge rent every set number of days
- [ ] Add debt as pressure
- [ ] Penalize missed payments
- [ ] Use pressure to stop infinite safe grinding

</details>

---

# Phase 8 — Reputation System

> **Goal:** Make reputation affect the game instead of just being a number.

<details>
<summary><strong>Lesson 23 — Reputation Meaning</strong></summary>

- [ ] Define what reputation represents
- [ ] Increase reputation through jobs or successful deals
- [ ] Decrease reputation through failure
- [ ] Use reputation to unlock products
- [ ] Use reputation to unlock better jobs

</details>

<details>
<summary><strong>Lesson 24 — Reputation Effects</strong></summary>

- [ ] Better prices at higher reputation
- [ ] Bigger deals at higher reputation
- [ ] Riskier attention at higher reputation
- [ ] New contacts at higher reputation
- [ ] Reputation becomes both useful and dangerous

</details>

---

# Phase 9 — Events

> **Goal:** Make days feel different from each other.

<details>
<summary><strong>Lesson 25 — Random Events</strong></summary>

- [ ] Create a list of possible events
- [ ] Trigger events when a day passes
- [ ] Make events affect prices
- [ ] Make events affect risk
- [ ] Make events affect player stats

</details>

<details>
<summary><strong>Lesson 26 — Event Design</strong></summary>

- [ ] Some events should help the player
- [ ] Some events should hurt the player
- [ ] Some events should create choices
- [ ] Events should be readable
- [ ] Events should not feel unfair

</details>

---

# Phase 10 — Saving and Loading

> **Goal:** Let the player keep progress between sessions.

<details>
<summary><strong>Lesson 27 — File Saving</strong></summary>

- [ ] Understand what a save file is
- [ ] Store game state in a dictionary
- [ ] Save the dictionary to a file
- [ ] Load the dictionary from a file
- [ ] Handle missing save files safely

</details>

<details>
<summary><strong>Lesson 28 — JSON</strong></summary>

- [ ] Understand what JSON is
- [ ] Convert Python data to JSON
- [ ] Convert JSON back to Python data
- [ ] Save player stats
- [ ] Save market stats

</details>

---

# Phase 11 — Project Files

> **Goal:** Stop keeping everything in one file forever.

<details>
<summary><strong>Lesson 29 — Splitting Files</strong></summary>

- [ ] Keep `main.py` for the game loop
- [ ] Move player logic into another file
- [ ] Move market logic into another file
- [ ] Move event logic into another file
- [ ] Import your own code between files

</details>

<details>
<summary><strong>Lesson 30 — Project Structure</strong></summary>

Target structure later:

```text
PlugOS/
├── main.py
├── player.py
├── market.py
├── events.py
├── save_system.py
├── README.md
└── ROADMAP.md
```

Checklist:

- [ ] Understand what each file is responsible for
- [ ] Avoid circular imports
- [ ] Keep file names simple
- [ ] Keep related code together
- [ ] Make the project easier to navigate

</details>

---

# Phase 12 — Polish

> **Goal:** Make the game feel better to play.

<details>
<summary><strong>Lesson 31 — Text Output</strong></summary>

- [ ] Improve menu readability
- [ ] Improve stat display
- [ ] Add clearer action results
- [ ] Add spacing consistently
- [ ] Avoid walls of messy text

</details>

<details>
<summary><strong>Lesson 32 — Player Feedback</strong></summary>

- [ ] Show what changed after each action
- [ ] Show profit after selling
- [ ] Warn when cash is low
- [ ] Warn when heat is high
- [ ] Show progress toward the goal

</details>

<details>
<summary><strong>Lesson 33 — Balancing</strong></summary>

- [ ] Test how long it takes to win
- [ ] Adjust starting cash
- [ ] Adjust product prices
- [ ] Adjust job rewards
- [ ] Adjust goal cash

</details>

---

# Phase 13 — Git Discipline

> **Goal:** Track progress properly instead of randomly smashing code into existence.

<details>
<summary><strong>Lesson 34 — Commits</strong></summary>

- [ ] Commit after each working lesson
- [ ] Use clear commit names
- [ ] Do not commit broken code unless it is intentional
- [ ] Keep commits focused
- [ ] Push regularly

</details>

<details>
<summary><strong>Lesson 35 — README</strong></summary>

- [ ] Add a short project description
- [ ] Explain how to run the game
- [ ] List current features
- [ ] List planned features
- [ ] Keep it updated as the project grows

</details>

---

## ✅ How To Use This Roadmap

Use this file as a **living checklist**.

Recommended workflow:

1. Pick one lesson.
2. Complete one small coding task from that lesson.
3. Test the game.
4. Tick the box.
5. Commit the change.
6. Move to the next lesson.

Do not try to do five lessons at once. That is not speed. That is just making future-you hate current-you.

---

## 🧠 Development Rule

> Build one small thing, understand it, test it, commit it.

That is the loop.

Not glamorous. Very effective.
