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
    
def calculate_score(dice):
    dice_count = {i: dice.count(i) for i in range(1,7)}
    score = 0

    # Check for special combinations
    if sorted(dice) == [1, 2, 3, 4, 5, 6]:
        return 1000  # Straight
    
    if list(dice_count.values()).count(2) == 3:
        return 1000  # Three pairs

    if dice_count[1] == 6:
        return 5000  # Six 1's
    
    # Calculate score for triples and individual 1's and 5's
    for num, count in dice_count.items():
        if count >= 3:
            score += num * 100 if num != 1 else 1000  # Triple of other numbers or triple 1's
            count -= 3  # Remove the counted three

        if num == 1:
            score += count * 100  # Each additional 1 is 100 points
        elif num == 5:
            score += count * 50  # Each additional 5 is 50 points

    return score

def roll_dice(num_of_dice):
    # Function to roll dice and print the result
    dice = [random.randint(1, 6) for _ in range(num_of_dice)]

    '''
    # vertically
    for die in range(num_of_dice):
        for line in dice_art.get(dice[die]):
            print(line)
    '''
    # horizontally
    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()

    # Calculate score for this roll
    round_score = calculate_score(dice)
    print(f"Points this round: {round_score}")
    return round_score

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
    target_score = 5000  # Winning score

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