from utils import deck_initialization
from player import Player
from blackjack import game


def main():
    """
    Runs the program, calls all necessary modules
    """
    ### Create deck and card dictionary ###
    card_dict, deck = deck_initialization()
    user = Player(card_dict, deck)
    dealer = Player(card_dict, deck)
    game(user, dealer, deck)


if __name__ == "__main__":
    main()
