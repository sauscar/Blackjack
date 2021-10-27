from itertools import combinations_with_replacement


class Player:
    def __init__(self, card_dict, deck):
        self.hand = []
        self.total = 0
        self.card_dict = card_dict
        self.deck = deck  # Might not need deck in the class

    def totalHandValue(self):
        """
        Calculates hand value for either user or dealer. Takes into account the various options
        with aces.
        """
        ace_count = 0
        total = 0
        for card in self.hand:
            if card == "A":
                ace_count += 1
            else:
                val = self.card_dict[card]
                total += val
        if ace_count > 0:
            ace_values = [1, 11]
            ace_combos = list(combinations_with_replacement(ace_values, ace_count))

            potential_combos = []
            bad_combos = []
            for combo in ace_combos:
                temp_sum = total + sum(combo)
                if temp_sum <= 21:
                    potential_combos.append(temp_sum)
                else:
                    bad_combos.append(temp_sum)
            if potential_combos:
                self.total = max(potential_combos)
            else:
                self.total = min(bad_combos)
        else:
            self.total = total

    def showDealerHand(self, hidden):
        """
        Shows the dealers hand, conditioned on whether we are showing a hidden version (the first card is hidden)
        or whether it all to be seen (occurs when user has elected to stand)
        """
        hand_string = ""
        if hidden:
            print("Dealer's Hidden Hand:", self.hand[0] + " ?", "Value: ?", "\n")
        else:
            for card in self.hand:
                hand_string += card + " "
            print("Dealer's Open Hand: " + hand_string, "Value: ", self.total)

    def showUserHand(self):
        """
        Shows users hand
        """
        hand_string = ""
        for card in self.hand:
            hand_string += card + " "
        print("Your Hand: " + hand_string, "Value: ", self.total)
