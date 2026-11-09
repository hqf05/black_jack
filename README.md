# Blackjack (Python Console Game)

A simple command-line Blackjack game where you play against the computer (the dealer).
Built as the Day 11 capstone project of the *100 Days of Code: The Complete Python Pro Bootcamp* course.

## How to Run

1. Make sure you have **Python 3** installed.
2. Keep `main.py` and `art.py` (which contains the logo) in the same folder.
3. Run:

```bash
python main.py
```

## How to Play

- The goal is to get a hand total **closer to 21 than the dealer**, without going over 21.
- You and the dealer each get **2 cards**. You see both of your cards but only the dealer's **first card**.
- On your turn, type:
  - `y` to draw another card (**Hit**)
  - `n` to stop (**Stand**)
- If your total goes over 21, you lose immediately (**Bust**).
- After you stand, the dealer draws cards until their total is **17 or more**.

## Card Values

| Card | Value |
|------|-------|
| 2 – 10 | Face value |
| J, Q, K | 10 |
| A (Ace) | 11, or 1 if 11 would make the total go over 21 |

## Winning Rules

The result is checked in this order:

1. Both have Blackjack → **Draw**
2. Dealer has Blackjack → **You lose**
3. You have Blackjack → **You win**
4. You went over 21 → **You lose**
5. Dealer went over 21 → **You win**
6. Equal scores → **Draw**
7. Otherwise, the higher score wins

> **Blackjack** = a total of 21 from the first two cards only (an Ace + a 10-value card).

## Simplified Rules

- The deck is infinite: a card can appear more than once.
- No betting, no splitting, no doubling down.

## Code Structure

| Function | What it does |
|----------|--------------|
| `deal_card()` | Returns one random card |
| `calculate_score(hand)` | Returns the hand's total and handles Aces |
| `is_blackjack(hand)` | Checks for 21 from the first two cards |
| `compare(user_hand, dealer_hand)` | Returns the result message |
| `play_game()` | Runs one full round of the game |

## Example

```
Your cards: ['K', '7'], current score: 17
Dealer's first card: 9
Type 'y' to get another card, type 'n' to pass: n

Your final hand: ['K', '7'], final score: 17
Dealer's final hand: ['9', '5', '6'], final score: 20
You lose.
```

## What I Learned

- Lists and dictionaries
- Functions with parameters and return values
- `while` loops and `if / elif / else` conditions
- The `random` module
