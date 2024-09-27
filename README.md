# Dice Game

This is a two-player dice game where players roll dice and accumulate points based on specific scoring rules. The first player to reach or exceed 5000 points wins!

## Features
- Roll six dice and display the result visually using ASCII art.
- Calculate points based on various dice combinations.
- Game continues until one player reaches 5000 points.
  
## Game Rules

- You roll six dice.
- Some combinations of dice will score points, while others won't.
- You take out the dice that have scored points and then decide whether to keep that score or re-roll the remaining dice to try to score more points.
- The goal is to reach 5000 points before your opponent!

### Dice Scoring

- **1** → 100 points
- **5** → 50 points
- **Three of a kind** → value * 100 (e.g., three 2's = 200 points)
- **Straight (1, 2, 3, 4, 5, 6)** → 1000 points
- **Three pairs** of any number → 1000 points
- **Six 1's** → 5000 points

## Requirements

- Python 3.x

## Example Gameplay
```
--- Welcome to the Dice Game! ---

        ==========================================
                         GAME RULES
        ==========================================
        You roll six dice.
        Some combinations of dice will score points, while others won't.
        You take out the dice that have scored points and then decide   
        whether to keep that score or re-roll the remaining dice        
        to try to score more points.
        
        GOAL: Reach 5000 points before your opponents!
        
        ------------------------------------------
        Possible Dice Combinations:
        
        - 1         ->  100 points
        - 5         ->  50 points
        - Three of a kind ->  value * 100 
                        (e.g. three 2's is 200 points)
        - A straight (1,2,3,4,5,6)  -> 1000 points
        - Three pairs of any number -> 1000 points
        - Six 1's   ->  5000 points
        ==========================================
        

Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││         ││  ●   ●  ││  ●      ││  ●      ││         │
│  ●   ●  ││    ●    ││    ●    ││         ││         ││    ●    │
│  ●   ●  ││         ││  ●   ●  ││      ●  ││      ●  ││         │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 250
Player 1's total score: 250


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││         ││  ●   ●  ││  ●      ││  ●      ││  ●   ●  │
│    ●    ││    ●    ││  ●   ●  ││         ││    ●    ││         │
│  ●   ●  ││         ││  ●   ●  ││      ●  ││      ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 1000
Player 2's total score: 1000


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●   ●  ││  ●   ●  ││  ●      ││  ●   ●  ││  ●   ●  │
│         ││         ││         ││         ││         ││    ●    │
│  ●   ●  ││  ●   ●  ││  ●   ●  ││      ●  ││  ●   ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 450
Player 1's total score: 700


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││         ││  ●   ●  ││  ●   ●  ││  ●   ●  ││  ●   ●  │
│    ●    ││    ●    ││         ││         ││         ││    ●    │
│  ●   ●  ││         ││  ●   ●  ││  ●   ●  ││  ●   ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 600
Player 2's total score: 1600


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●      ││  ●      ││         ││  ●      ││  ●   ●  ││         │
│         ││    ●    ││    ●    ││         ││  ●   ●  ││    ●    │
│      ●  ││      ●  ││         ││      ●  ││  ●   ●  ││         │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 200
Player 1's total score: 900


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●      ││  ●      ││  ●   ●  ││         ││  ●      ││         │
│    ●    ││         ││         ││    ●    ││    ●    ││    ●    │
│      ●  ││      ●  ││  ●   ●  ││         ││      ●  ││         │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 200
Player 2's total score: 1800


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││         ││         ││  ●   ●  ││         ││  ●      │
│    ●    ││    ●    ││    ●    ││    ●    ││    ●    ││         │
│  ●   ●  ││         ││         ││  ●   ●  ││         ││      ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 1100
Player 1's total score: 2000


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●      ││  ●   ●  ││  ●   ●  ││  ●      ││  ●      │
│         ││         ││    ●    ││    ●    ││         ││    ●    │
│  ●   ●  ││      ●  ││  ●   ●  ││  ●   ●  ││      ●  ││      ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 100
Player 2's total score: 1900


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●   ●  ││  ●   ●  ││  ●      ││  ●      ││  ●   ●  │
│  ●   ●  ││  ●   ●  ││  ●   ●  ││    ●    ││         ││         │
│  ●   ●  ││  ●   ●  ││  ●   ●  ││      ●  ││      ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 600
Player 1's total score: 2600


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●      ││  ●      ││  ●      ││  ●   ●  ││  ●   ●  ││  ●   ●  │
│         ││         ││    ●    ││  ●   ●  ││    ●    ││  ●   ●  │
│      ●  ││      ●  ││      ●  ││  ●   ●  ││  ●   ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 50
Player 2's total score: 1950


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●      ││  ●   ●  ││         ││  ●   ●  ││  ●      ││  ●   ●  │
│         ││         ││    ●    ││    ●    ││    ●    ││    ●    │
│      ●  ││  ●   ●  ││         ││  ●   ●  ││      ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 200
Player 1's total score: 2800


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●   ●  ││  ●      ││  ●   ●  ││  ●      ││  ●   ●  │
│  ●   ●  ││    ●    ││         ││  ●   ●  ││    ●    ││         │
│  ●   ●  ││  ●   ●  ││      ●  ││  ●   ●  ││      ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 50
Player 2's total score: 2000


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●      ││  ●      ││  ●      ││  ●   ●  ││  ●      │
│  ●   ●  ││         ││    ●    ││    ●    ││         ││         │
│  ●   ●  ││      ●  ││      ●  ││      ●  ││  ●   ●  ││      ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 0
Player 1's total score: 2800


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●      ││  ●   ●  ││         ││  ●   ●  ││  ●   ●  │
│  ●   ●  ││    ●    ││         ││    ●    ││  ●   ●  ││    ●    │
│  ●   ●  ││      ●  ││  ●   ●  ││         ││  ●   ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 150
Player 2's total score: 2150


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│         ││  ●   ●  ││  ●      ││  ●   ●  ││  ●   ●  ││  ●      │
│    ●    ││  ●   ●  ││    ●    ││    ●    ││         ││    ●    │
│         ││  ●   ●  ││      ●  ││  ●   ●  ││  ●   ●  ││      ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 150
Player 1's total score: 2950


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●      ││  ●   ●  ││         ││  ●      ││  ●      ││  ●   ●  │
│    ●    ││    ●    ││    ●    ││         ││    ●    ││    ●    │
│      ●  ││  ●   ●  ││         ││      ●  ││      ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 200
Player 2's total score: 2350


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●      ││  ●   ●  ││  ●   ●  ││  ●   ●  ││  ●   ●  ││         │
│         ││    ●    ││    ●    ││    ●    ││         ││    ●    │
│      ●  ││  ●   ●  ││  ●   ●  ││  ●   ●  ││  ●   ●  ││         │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 600
Player 1's total score: 3550


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●      ││         ││  ●      ││         ││         │
│    ●    ││         ││    ●    ││         ││    ●    ││    ●    │
│  ●   ●  ││      ●  ││         ││      ●  ││         ││         │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 1050
Player 2's total score: 3400


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│         ││         ││  ●   ●  ││  ●      ││  ●   ●  ││  ●      │
│    ●    ││    ●    ││    ●    ││         ││         ││    ●    │
│         ││         ││  ●   ●  ││      ●  ││  ●   ●  ││      ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 250
Player 1's total score: 3800


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●      ││  ●   ●  ││  ●      ││  ●      ││  ●   ●  │
│  ●   ●  ││    ●    ││    ●    ││         ││    ●    ││    ●    │
│  ●   ●  ││      ●  ││  ●   ●  ││      ●  ││      ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 100
Player 2's total score: 3500


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│         ││  ●   ●  ││  ●      ││  ●   ●  ││  ●      ││  ●   ●  │
│    ●    ││         ││    ●    ││         ││    ●    ││  ●   ●  │
│         ││  ●   ●  ││      ●  ││  ●   ●  ││      ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 100
Player 1's total score: 3900


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●      ││  ●   ●  ││  ●      ││  ●      ││  ●      ││  ●   ●  │
│         ││    ●    ││    ●    ││    ●    ││    ●    ││         │
│      ●  ││  ●   ●  ││      ●  ││      ●  ││      ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 350
Player 2's total score: 3850


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│         ││  ●      ││  ●   ●  ││         ││  ●   ●  ││  ●      │
│    ●    ││         ││         ││    ●    ││    ●    ││    ●    │
│         ││      ●  ││  ●   ●  ││         ││  ●   ●  ││      ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 250
Player 1's total score: 4150


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●      ││  ●   ●  ││         ││  ●   ●  ││  ●   ●  │
│         ││         ││  ●   ●  ││    ●    ││         ││  ●   ●  │
│  ●   ●  ││      ●  ││  ●   ●  ││         ││  ●   ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 100
Player 2's total score: 3950


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●   ●  ││  ●   ●  ││         ││  ●      ││  ●   ●  │
│         ││         ││    ●    ││    ●    ││         ││    ●    │
│  ●   ●  ││  ●   ●  ││  ●   ●  ││         ││      ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 200
Player 1's total score: 4350


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●   ●  ││         ││  ●   ●  ││  ●   ●  ││  ●      │
│    ●    ││         ││    ●    ││         ││         ││    ●    │
│  ●   ●  ││  ●   ●  ││         ││  ●   ●  ││  ●   ●  ││      ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 550
Player 2's total score: 4500


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││         ││  ●      ││  ●   ●  ││  ●   ●  ││  ●   ●  │
│         ││    ●    ││         ││    ●    ││         ││         │
│  ●   ●  ││         ││      ●  ││  ●   ●  ││  ●   ●  ││  ●   ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 550
Player 1's total score: 4900


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●      ││  ●      ││  ●      ││  ●      ││  ●   ●  ││  ●      │
│         ││         ││    ●    ││         ││         ││    ●    │
│      ●  ││      ●  ││      ●  ││      ●  ││  ●   ●  ││      ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 200
Player 2's total score: 4700


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●      ││  ●   ●  ││  ●      ││  ●   ●  ││  ●      │
│         ││         ││         ││    ●    ││    ●    ││         │
│  ●   ●  ││      ●  ││  ●   ●  ││      ●  ││  ●   ●  ││      ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 50
Player 1's total score: 4950


Player 2's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●   ●  ││  ●      ││  ●      ││  ●   ●  ││  ●      │
│    ●    ││  ●   ●  ││         ││         ││  ●   ●  ││         │
│  ●   ●  ││  ●   ●  ││      ●  ││      ●  ││  ●   ●  ││      ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 250
Player 2's total score: 4950


Player 1's turn:
┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│  ●   ●  ││  ●   ●  ││  ●   ●  ││  ●      ││         ││  ●      │
│    ●    ││  ●   ●  ││         ││    ●    ││    ●    ││    ●    │
│  ●   ●  ││  ●   ●  ││  ●   ●  ││      ●  ││         ││      ●  │
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
Points this round: 150
Player 1's total score: 5100

Player 1 wins!
Game over!
'''
