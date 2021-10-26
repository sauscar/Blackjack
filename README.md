# Blackjack
Play blackjack with computer! Standard 21 bust, stand on 17.

# Files

There are a total of 4 files. They are:
1. main.py: this file is what you run and it calls all the appropriate main modules
2. player.py: contains the player class which both user and dealer are part of. Runs necessary computations and stores relevant information like player's hand.
3. blackjack.py: here you will find the actual game and this is where input from user is requested and winning conditions are met and visualized
4. utils.py: supplementary modules make up this file. Some of these modules are called often and others aren't. They aren't really the core of the game mechanics, however they are vital for the playability of the game.

# Dependencies

Only two libraries are used: itertools and random, and they are both part of the the standard python library. So if you have python you should have these two libraries.
If needed here is where to download python: http://www.python.org/download/

# Run program

Open up your terminal interface. Make sure you have directed into the folder "FreenomeCodingChallenge". Then from there just type "python main.py" and it will run the program.

# Play game

The cards will be shuffled and dealt. The program will show your hand and the dealers (with the dealers first card being hidden). You could win immediately which is called blackjack. If not, then you will be prompted to hit or stand. The value of your hand will be calculated for you. Once you make your decision, you will either be at or above 21 or below 21. If you "bust" (above 21) the program will tell you that you lost and you will have to run the program again if you'd like to play again (follow instructions above).

If you are at 21 exactly you will win. Otherwise, you will be below 21, at which point you must decide if you'd like to hit or stand again, and so on and so forth.

If lets say you stand at a value below 21, the dealer's turn starts. There is a chance that their starting 2 cards are greater than where you are standing at which point the dealer will win. If that doesn't happen the dealer will then hit until they are at least at 17 if they are below 17. This could result in the dealer hitting at a value above yours which dealer will win. If not, they could hit above 21 meaning they bust and you win.

# Assumptions

There weren't many that I had to make outside of the instructions. One assumption that comes to mind was in the beginning of the game. The user is dealt a card first and then the dealer then back to user and finally ends with dealer receiving the last card.

# Positives

I think I did a really good job in organizing the files and code in general. Modules are expalined within the code so you know what each is doing. The code is maintainable as it is compartmentalized and each module has a specific task.

# Rationale and Approach

One big decision I made was making the player class. I thought it made sense to represent the user and dealer as both players since they both have their own data specific to them. With this class I was also able to make the modules to run the calculations necessary for their respsective hand and show their hands. It was a very elegant and proper solution instead of having loose variables which would have been the alternative.

I also had to handle the trickiness of the aces. I came up with a really solid solution using itertools. Essentially itertools gathers the number of combinations depending on how many aces are in hand of 1 and 11. So if I have 3 aces it looks for all combinations of 3 aces in which the aces can have value 1 or 11. Before this, I created a temporary total which has the total of all non-ace cards. Continuing, these ace combinations were summed and added to the temporary total. If any of these summations were over 21 they were added to the bad combinations list if not they were appended to the possible combos list. The reason for this being, if all of the summations between temporary total and ace sums are over 21 I have to return the least of the bad combos, in which case the player will bust. Given there are totals in the possible combinations list, I return the max of them.

Core to my approach was writing maintainable, readable code. I wanted to make sure anyone taking a look at my code would easily understand what each module is doing. Also makes debugging easier, as I have a better idea where a problem is occuring. The way I have it now is better than all those lines of code in one file, it is much neater.

# Tradeoffs



# Improvements

Definitely would improve the way the deck is created. Right now it runs at O(n^2). I believe there is a faster way to do this. Also maybe there is a better way to run the different combinations for the aces. One that runs faster I would think. I could probably remove some modules like dealerHiddenState, dealerOpenState, and userState only because all they do is call two other modules. I don't think they're really necessary. It would just help in maybe some confusing if tracing code back, remove a layer of depth and help in understanding what my code is doing. I would lastly implemnent testing into the code so that one may test certain modules and make sure they are running smoothly.

# Testing

I didn't have to time to implement testing, however I will present a few ideas for tests. I'd create a test that checks that the deck has been shuffled. Another test for the calculations of the hand values, to make sure that the right values are being outputted. Very important test as this is what the whole game revolves around. I'd create a test for checking whether the hidden hand is shown when its the users turn. Also very important because that is an advantage that should be preserved for the dealer.
