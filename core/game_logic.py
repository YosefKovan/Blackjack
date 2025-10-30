from core.player_io import ask_player_action

#======================================
#            dealer play
#======================================

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    """this handles the dealers play"""

    dealer_count = calculate_hand_value(dealer["hand"])
    print("Dealers initial value is: ", dealer_count)

    #this loop will run as long as the dealer's count is less than 17
    while dealer_count < 17:
         dealer["hand"].append(deck.pop(0))
         dealer_count = calculate_hand_value(dealer["hand"])
         print(f"the dealers current hand is : {dealer_count}")


    if 17 <= dealer_count <= 21:
        print(f"the dealer is passing the current score is : {dealer_count}")
        return True

    print(f"Dealer Lost!!!!!!!")
    return False


#======================================
#        calculate_hand_value
#======================================

def calculate_hand_value(hand: list[dict]) -> int:
    """this function will calculate how many cards are in the players hand currently"""

    total_hand = 0
    for card in hand:
         total_hand += card["rank"]

    return total_hand


#======================================
#         pop_cards_from_deck
#======================================

def pop_cards_from_deck(deck, hand, amount):
    """this function will draw an amount of cards as passed to the amount variable"""
    for i in range(0, amount):
        hand.append(deck.pop(0))

#======================================
#           deal_two_each
#======================================

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    """this function will draw two cards for each"""

    pop_cards_from_deck(deck,  player["hand"], 2)
    pop_cards_from_deck(deck, dealer["hand"], 2)


#======================================
#           run_full_game
#======================================

def player_play(deck, player):
    """this function handles the players play"""

    print(f"Player initial card sum is : {calculate_hand_value(player["hand"])}")
    action = ask_player_action()

    while action != 'S':

        player["hand"].append(deck.pop(0))
        print(f"Players current hand is : {calculate_hand_value(player["hand"])}")

        if calculate_hand_value(player["hand"]) > 21:
            print("Player Lost")
            return False

        action = ask_player_action()

    print(f"Player asked to pass. players total in hand : {calculate_hand_value(player["hand"])}")
    return True

#===============================================
#          handle_check_winner_looser
#===============================================

def check_winner_looser(player, dealer):
    """this function prints the winner and the looser in the case in which both passed and didn't loose"""

    player_score = calculate_hand_value(player["hand"])
    dealer_score = calculate_hand_value(dealer["hand"])

    if player_score > dealer_score:
        print(f"Player won - dealer score : {dealer_score}, player score : {player_score}")
    elif player_score < dealer_score:
        print(f"Dealer won - dealer score : {dealer_score}, player score : {player_score}")
    else:
        print(f"Tie, both player and dealer scored : {player_score}")


#===============================================
#                run full game
#===============================================
def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    """this function runs the game"""

    #this will deal two cards for the player
    deal_two_each(deck, player, dealer)

    if player_play(deck, player) and dealer_play(deck, dealer):
        check_winner_looser(player, dealer)




