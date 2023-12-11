# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint
# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
def print_card_name(card1_rank):
    # Implement card_name function here
    if card1_rank == 1:
    # A 1 stands for an ace.
        card1_name = "Ace"
    elif card1_rank == 11:
    # An 11 stands for a jack.
        card1_name = "Jack"
    elif card1_rank == 12:
    # A 12 stands for a queen.
        card1_name = "Queen"
    elif card1_rank == 13:
    # A 13 stands for a king.
        card1_name = "King"
    else:
    # All other cards are named by their number, or rank.
        card1_name = str(card1_rank)

    if card1_rank == 1 or card1_rank == 8:
        print('Drew an ' + card1_name)
    else:
        print('Drew a ' + card1_name)


# Draws a new random card, prints its name, and returns its value.
# 
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
def draw_card():
    # Implement draw_card function here
    card1_rank = randint(1,13)
    print_card_name(card1_rank)
    if card1_rank == 11 or card1_rank == 12 or card1_rank == 13:
    # Jacks, Queens, and Kings are worth 10.
        card1_value = 10
    elif card1_rank == 1:
    # Aces are worth 11.
        card1_value = 11
    else:
    # All other cards are worth the same as their rank.
        card1_value = card1_rank
    return card1_value

# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
# 
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
def print_header(message):
    # Implement print_header function here
    str(message)
    print("-----------\n" + message + "\n-----------")

# Prints turn header and draws a starting hand, which is two cards.
# 
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
    # Implement draw_starting_hand function here
    print_header(name + " TURN")
    card1_value = draw_card()
    card2_value = draw_card()
    hand_value = card1_value + card2_value
    return hand_value

# Prints the hand total and status at the end of a player's turn.
# 
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none
def print_end_turn_status(hand_value):
    # Implement print_end_turn_status function here
    print("Final hand: " + str(hand_value) + ".")
    if hand_value == 21:
        print("BLACKJACK!")
    elif hand_value > 21:
        print("BUST.")
    user_hand = hand_value
    
# Prints the end game banner and the winner based on the final hands.
# 



# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none
def print_end_game_status(user_hand, dealer_hand):
    print_header("GAME RESULT")
    if user_hand <= 21 and user_hand == dealer_hand:
        print("Push.")
    elif user_hand <= 21  and user_hand > dealer_hand:
        print("You win!")
    elif user_hand == 21 and dealer_hand > 21:
        print("You win!")
    elif user_hand < 21 and user_hand < dealer_hand:
        print("Dealer wins!")
    elif user_hand < 21 and dealer_hand > 21:
        print("You win!")
    else:
        if user_hand > 21:
            print("Dealer wins!")
    # Implement print_end_game_status function here
