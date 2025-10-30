import random



#=============================== shuffling ================================

#======================================
#          satisfies condition
#======================================
def satisfies_condition(deck, index2, suit):
    """this check if the index satisfies the condition"""

    match suit:
        case 'H':
            return True if index2 % 5 == 0 else False
        case 'C':
            return True if index2 % 3 == 0 else False
        case 'D':
            return True if index2 % 2 == 0 else False
        case 'S':
            return True if index2 % 7 == 0 else False

    return False

#======================================
#        get second swap index
#======================================
def get_second_swap_index(deck, index1, suit):
    """this function will return the second index according to the condition"""
    print("in the get_second_swap_index")
    while True:
        index2 = random.randrange(0, 52)

        #satisfies_condition(deck, index2, deck[index2]["suit"])

        #this will check if the indexes equal
        if index2 != index1:
            return index2


#======================================
#           shuffle by suit
#======================================
def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    """this function is in charge of shuffling the deck"""
    print("in the shuffle_by_suit")
    shuffle_count = 0

    while shuffle_count < swaps:
        index1 = random.randrange(0, 52)
        first_card = deck[index1]

        index2 = get_second_swap_index(deck, index1, first_card["suit"])

        #this will swap between the two indexes
        deck[index1], deck[index2] = deck[index2], deck[index1]
        print(shuffle_count)
        shuffle_count += 1

    return deck


#=============================== init deck ================================

#======================================
#             create card
#======================================
def create_card(number, suit):
    """checks and creates the correct card"""

    if str(number).isdigit():
        return {"number": str(number), "rank": number, "suit": suit}
    elif number == 'A':
        return {"number": 'A', "rank": 1, "suit": suit}
    else:
        return {"number": number, "rank" : 10, "suit": suit}


#======================================
#         build standard deck
#======================================
def build_standard_deck() -> list[dict]:
    """this function will return a full deck"""

    suits = ['H', 'C', 'D', 'S']
    numbers = list(range(2,11)) + ['J', 'Q', 'K', 'A']
    deck = []

    for suit in suits:
        for number in numbers:
            deck.append(create_card(number, suit))


    return deck