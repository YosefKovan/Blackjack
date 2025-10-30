

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