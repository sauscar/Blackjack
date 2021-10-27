import random


def deck_initialization():
    """
    Creates card dictionary and deck for the game
    """
    card_dict = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": [1, 11],
    }
    deck = []
    for key in card_dict:
        temp = [key] * 4
        for val in temp:
            deck.append(val)
    print("Deck created")
    return card_dict, deck


def dealInitialHands(user, dealer, deck):
    """
    Deals initial hands for both players. 2 to each.
    """
    for i in range(4):
        if i % 2 == 0:
            user.hand.append(deck.pop())
        else:
            dealer.hand.append(deck.pop())


def shuffleDeck(deck):
    """
    Input: deck | [List]
    Output: deck | [List] (shuffled)
    Shuffle the deck and return it
    """
    random.shuffle(deck)
    deck.reverse()  ## to treat the deck as a stack the top or the last value will be popped and used
    print("Deck has been shuffled\n")
    return deck


def userState(user):
    """
    Input: user and dealer | Player
    Calculate hand totals and show the hand of user. Doesn't return anything
    """
    ###
    user.totalHandValue()
    user.showUserHand()


def dealerHiddenState(dealer):
    """
    Input: user and dealer | Player
    Calculate hand totals and show the hand of dealer (hidden). Doesn't return anything
    """
    ###
    dealer.totalHandValue()
    dealer.showDealerHand(hidden=True)


def dealerOpenState(dealer):
    """
    Input: user and dealer | Player
    Calculate hand totals and show the hand of dealer (open). Doesn't return anything
    """
    ###
    dealer.totalHandValue()
    dealer.showDealerHand(hidden=False)


def getResponse():
    """
    Ask user for input and check for proper input. Returns response from user.
    """
    while True:
        response = str(input("Would you like to (H)it or (S)tand?: ")).upper()
        if response == "H" or response == "S":
            print("Thank you for your choice")
            break
        else:
            print("Please make sure you are entering H to hit or S to stand")
            continue
    return response
