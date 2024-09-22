import random #rolling random num <1,6>

# print("\u25CF \u250C \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

def print_game_rules(): 
    # Function to print the game rules
    print("""
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
        """)
    
def roll_dice(num_of_dice):
    # Function to roll dice and print the result
    dice = []
    round = 0

    for die in range(num_of_dice):
        dice.append(random.randint(1, 6))

    for die in range(num_of_dice):
        for line in dice_art.get(dice[die]):
            print(line)

    for die in dice:
        round += die
    
    print(f"Points this round: {round}")
    return round

def player_turn(player_name, num_of_dice):
    #Single turn for a player
    print(f"\n{player_name}'s turn:")
    return roll_dice(num_of_dice)

if __name__ == "__main__":
    print("--- Welcome to the Dice Game! ---")

    print_game_rules()

    # Initialize scores for both players
    player1_score = 0
    player2_score = 0
    target_score = 3000  # Winning score

    # Number of dice to roll
    num_of_dice = 6

    # Main game loop
    while player1_score < target_score and player2_score < target_score:
        # Player 1's turn
        player1_score += player_turn("Player 1", num_of_dice)
        print(f"Player 1's total score: {player1_score}\n")
        if player1_score >= target_score:
            print("Player 1 wins!")
            break
        
        # Player 2's turn
        player2_score += player_turn("Player 2", num_of_dice)
        print(f"Player 2's total score: {player2_score}\n")
        if player2_score >= target_score:
            print("Player 2 wins!")
            break
    
    print("Game over!")