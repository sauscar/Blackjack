from utils import *


def userSequence(user, dealer, shuffled_deck):

    """
    The sequence for the user which asks or input, calculates hand value along the way and
    will return whether they busted or won. If not, this is followed by the dealerSequence.
    """
    while user.total < 21:

        ### NOW SHOULD ASK HIT OR STAND? Check for proper input from user
        response = getResponse()

        ### CHECK RESPONSE TYPE AND CONTINUE ACCORIDNGLY
        if response == "H":
            print("You chose to (H)it\n")
            card = shuffled_deck.pop()
            user.hand.append(card)
        else:
            print("You chose to (S)tand at", user.total, "\n")
            break

        ### CALCULATE HAND TOTALS AND DISPLAY HAND AND TOTAL
        userState(user)
        dealerHiddenState(dealer)

        ### CHECK IF TOTAL IS 21 AFTER HAVING HIT OR SURPASSED 21
        if user.total == 21:
            print("You win!")
            return
        elif user.total > 21:
            print("You lost since you passed 21")
            return


def dealerSequence(user, dealer, shuffled_deck):
    """
    Sequence for dealer, as long as they are below 17 they have to hit. If they go over will
    alert user. Determines win or loss of game.
    """
    while dealer.total < 17:
        card = shuffled_deck.pop()
        dealer.hand.append(card)
        dealerOpenState(dealer)

    if dealer.total > 21:
        print("The dealer busted! You win!")
        return

    if user.total > dealer.total:
        print("The dealer got to", dealer.total, "however your total is larger. You win!")
        return
    elif user.total == dealer.total:
        print("There was a tie. No one wins.")
        return
    else:
        print("You lost! Your total was less than dealer's")
        return


def game(user, dealer, deck):
    """
    Determine winner of the game, runs the actual game
    """
    ### SHUFFLE DECK ###
    shuffled_deck = shuffleDeck(deck)
    # shuffled_deck = deck
    ### DEAL INITIAL HANDS ###
    dealInitialHands(user, dealer, shuffled_deck)

    ### SHOW CURRENT STATE OF BOTH PLAYERS
    userState(user)
    dealerHiddenState(dealer)
    if user.total == 21:
        print("You won! Blackjack!")
    userSequence(user, dealer, shuffled_deck)
    if user.total >= 21:
        return

    print("It is the dealers turn now\n")

    dealerOpenState(dealer)

    if dealer.total >= 17:
        if user.total > dealer.total:
            print("You win! Your", user.total, "is greater than the dealers", dealer.total)
            return
        elif user.total == dealer.total:
            print("We have a tie at", user.total)
            return
        else:
            print(
                "You lost! Dealer didn't have to hit, they just had more than you right off the bat"
            )
            return

    dealerSequence(user, dealer, shuffled_deck)

    return
