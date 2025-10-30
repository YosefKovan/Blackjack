
#======================================
#         ask_player_action
#======================================
def ask_player_action() -> str:
    """this function will ask the player for a action H or S"""

    while True:
        try:
            user_input = input("Please enter H - Hit , or S - Stand ")
            user_input = user_input.lower()

            if user_input == 'h' or user_input == 's':
                return user_input.upper()

            print("make sure to input H or S only!!!")

        except:
            print("make sure to input letter H or S only!")
