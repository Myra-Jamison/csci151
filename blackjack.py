#----------------------
# Assignment 13 -- Blackjack
# ----------------------
# Myra Jamison
# CSCI 151
# May 2

import stdio
import random
import sys
import time

#this program simulates a game of blackjack where the dealer
#is the computer

# ==================================================================================================================

#-------------------------------------------------------------------------------------------------------------
# objects
#-------------------------------------------------------------------------------------------------------------

#create an object type for cards, containing an encoded attribute 'number' that represents it's value,
#and an attribute suit that represents the suit
class Card:
    def __init__(self, suit, number):
        self._suit = suit
        self._number = number
    
    def __str__(self):
        if self._number == 1:
            _cardValue = 'Ace'
        elif self._number == 11:
            _cardValue = 'Jack'
        elif self._number == 12:
            _cardValue = 'Queen'
        elif self._number == 13:
            _cardValue = 'King'
        else: _cardValue = str(self._number)
        return _cardValue + ' of ' + str(self._suit)

#create an object type for players, containing a variety of attributes related to scoring in blackjack,
#a players money, bet, and hand
#note! _gameScore is not used, but it could be to count the number of rounds a player has won
class Player:
    def __init__(self, name, funds):
        self._name = name
        self._softRoundCount = 0
        self._hardRoundCount = 0
        self._endRoundCount = 0
        self._gameScore = 0
        self._bet = 0.0
        self._funds = funds
        self._hand = []
        self._blackjackState = False
    
    def __str__(self):
        return (
            'Player Name: ' + str(self._name) + '\n' +
            'Count this round: ' + str(self._endRoundCount) + '\n' +
            'Bet: $' + str(self._bet) + '\n' +
            'Funds: $' + str(self._funds) + '\n' +
            'Total won rounds: ' + str(self._gameScore) + '\n' +
            '--------\n'
        )

#create an object type for the deck, consisting of card objects
class Deck:
    def __init__(self):
        self._shuffleState = False
        self._deckState = self.createDeck()
    
    def createDeck(self):
        _suit = ['Hearts','Diamonds','Spades','Clubs']
        cardList = []
        for i in _suit:
            for j in range(1,14):
                cardList.append(Card(i,j))
        return cardList
    
    #add a method for shuffling, this is the 'poke' method of shuffling, which is
    #a way to mathematically optmize shuffling a completely random deck. see the numberphile video
    #on card shuffling for more info. on average, this method requires ~250 steps)
    def shuffleDeck(self):
        count = 0
        while count < 52:
            pokePosition = random.randint(0,51)
            _topCard = self._deckState[0]
            self._deckState.pop(0)
            self._deckState.insert(pokePosition, _topCard)
            if pokePosition + count >= 51:
                count += 1
        self._shuffleState = True

    def __str__(self):
        _deckString = ''
        for i in self._deckState:
            _deckString = _deckString + " ".join([str(i), '\n'])
        return ('List of cards in deck:\n' +
                '------------\n' + 
                _deckString + 
                '----------\n' +
                'End of List'
        )

#------------------------------------------------------------------------------------------------
# game functions
#-----------------------------------------------------------------------------------------------------

#introduce a new game, and ask for player names and starting money. save to list called 'players'
def newGame():
    stdio.write('\n~~BlackJack Game~~\n' + 
                '===================\n'
    )      
    _playerList = [Player(name='Dealer',funds=float('inf'))]
    while True:
        stdio.write("Please enter a player name without spaces\n")
        _name = stdio.readString()
        stdio.write('Enter starting money for ' + str(_name) + ':\n')
        _funds = stdio.readFloat()
        player = Player(name=_name,funds=_funds)
        _playerList.append(player)
        stdio.write('Will another human be playing? [y/n]:')
        if stdio.readString() == 'y':
            continue
        else: break
    return _playerList

#ask for bets. don't allow for bets higher than the money a player has
def betting(players):
    for i in players[1:]:
        stdio.write('How much would ' + str(i._name) + ' like to bet? Enter number: \n')
        bet = stdio.readFloat()
        while bet > i._funds:
                stdio.write('Bet exceeds player funds. Please choose a bet lower than ' + str(i._funds) + '\n')
                bet = stdio.readFloat()
        i._bet = bet
        i._funds -= bet
    return

#deal 2 cards from our randomly shuffled deck to each player. dealer's second card is kept secret
def dealing(players):
    stdio.write('Shuffling cards...\n')
    shuffleAnimation()
    deck1 = Deck()
    deck1.shuffleDeck()
    for i in players:
        for j in range(2):
            _card = deck1._deckState[0]
            i._hand.append(_card)
            deck1._deckState.pop(0)
        if i._name == 'Dealer':
            stdio.write("\nDealer's cards:\n" + 
                        '----------\n' + 
                        str(i._hand[0]) + '\n' +
                        '~secret~\n' + 
                        '----------\n'
                    )
        else: stdio.write(str(i._name) + "'s cards:\n" +
                          '----------\n' + 
                        str(i._hand[0]) + '\n' + 
                        str(i._hand[1]) + '\n' +
                        '----------\n'
                    )
    return deck1

#create an animation to be used whenever the deck is shuffled. since the method for shuffling is so
#fast this gives the viewer more 'confidence' that the computer has shuffled the deck 'really well', even
#though each shuffle is already random as possible. 
def shuffleAnimation():
    frames = ['|','\\','-','/']
    animationCount = 0
    while animationCount < 4:
        for i in frames:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.2)
            sys.stdout.write('\b')
            animationCount += 1
    return

#update player object with scores from the cards in their hand
def checkCount(players):
    for i in players:
        i._hardRoundCount = 0
        i._softRoundCount = 0
        for j in i._hand:
            if j._number >= 10:
                i._hardRoundCount += 10
                i._softRoundCount += 10
            elif 2 <= j._number < 10:
                i._hardRoundCount += int(j._number)
                i._softRoundCount += int(j._number)
            elif 1 == j._number:
                i._hardRoundCount += 1
                i._softRoundCount += 11
    return 

#checks edge case of blackjacks being dealt on first round; ends game if this is the case
def checkBlackjacks(players):
    dealtBlackJack = False
    checkCount(players)
    for i in players:
        if i._softRoundCount == 21:
            stdio.write('\n' + str(i._name) + ' was dealt a blackjack!')
            i._blackjackState = True
            dealtBlackJack = True
        if i._blackjackState == True and i._name == 'Dealer':
            for k in players[1:]:
                if k._blackjackState == False:
                    i._funds += k._bet
        if i._blackjackState == True and players[0]._blackjackState == False:
            i._funds += i._bet + i._bet*1.5
            players[0]._funds -= i._bet*1.5
            i._bet = 0
            for j in players[1:]:
                if i == j:
                    continue
                else:
                    i._funds += j._bet
                    j._bet = 0
    return dealtBlackJack

#asks player to hit or stand, updates score according to card they get
def hitOrStand(players,deck):
    checkCount(players)
    for i in players[1:]:
        stdio.write('Would ' + str(i._name) + ' like to hit [y] or stand [n]?\n')
        while True:
            response = stdio.readString()
            if response == 'y':
                i._hand.append(deck._deckState[0])
                deck._deckState.pop(0)
                stdio.write(str(i._name) + "'s cards:\n" +
                            '----------\n')
                for j in i._hand:
                    stdio.write(str(j) + '\n')
                stdio.write('----------\n')
                checkCount(players)
                if i._hardRoundCount > 21:
                    stdio.writeln('Player has exceeded 21!\n')
                    break
                elif i._hardRoundCount < 21:
                    stdio.write('Would ' + str(i._name) + ' like to hit [y] or stand [n]?\n')
                    continue
                elif i._hardRoundCount == 21:
                    break
            if response == 'n':
                break
    return

#follow rules for whether dealer must hit or stand
def dealerHits(players,deck):
    stdio.write("\nDealer's cards:\n" + 
                        '----------\n' + 
                        str(players[0]._hand[0]) + '\n' +
                        str(players[0]._hand[1]) + '\n'
                    )
    if players[0]._softRoundCount < 17:
        _card = deck._deckState[0]
        players[0]._hand.append(_card)
        deck._deckState.pop(0)
        stdio.write(str(_card) + '\n')
        checkCount(players)
        if players[0]._hardRoundCount > 21:
            players[0]._endRoundCount = 0
        elif players[0]._softRoundCount > 21 and players[0]._hardRoundCount < 22:
            players[0]._endRoundCount = players[0]._hardRoundCount
        else: players[0]._endRoundCount = players[0]._softRoundCount
    stdio.write('----------\n')

#calculate highest total score from the two possible scores a 
#player could have (counting aces as 1's or 11's)
def scoring(players):
    for i in players[1:]:
        if i._hardRoundCount > 22:
            i._endRoundCount = 0
        elif 22 < i._softRoundCount:
            i._endRoundCount = i._hardRoundCount
        elif 22 > i._softRoundCount:
            i._endRoundCount = i._softRoundCount
    return

#find the winner, payouts
def winner(players):
    winner = players[0]
    for i in range(1,len(players)):
        if players[i]._endRoundCount > winner._endRoundCount:
            winner = players[i]
        elif players[i]._endRoundCount == winner._endRoundCount:
            #tie
            stdio.writeln('There was a tie. No payouts')
            for i in players:
                i._funds += i._bet
                i._bet = 0
            return winner == None
    winner._funds += winner._bet
    for i in players:
        winner._funds += i._bet
        i._bet = 0
    return winner

    
#-----------------------------------------------------------------------------------------
# game client
#--------------------------------------------------------------------------------------------

#start a new round, use above functions to perform various operations
def gameRun(players):
    for i in players:
        i._softRoundCount = 0
        i._hardRoundCount = 0
        i._endRoundCount = 0
        i._hand = []
        i._blackjackState = False
    betting(players)
    deck = dealing(players)
    if checkBlackjacks(players) == True:
        stdio.write("\nThe game has ended. A Blackjack was dealt. Breakdown: \n")
        for i in players:
            stdio.write(str(i) + '_________________\n')
        stdio.write('Play again? [y/n]')  
        if stdio.readString() == 'y':
            return gameRun(players)
        else: return stdio.write("Thanks for playing!")
    hitOrStand(players, deck)
    dealerHits(players,deck)
    scoring(players)
    winningPlayer = winner(players)
    if winningPlayer != None:
        stdio.write('~~~~~~\nWINNER: ' + str(winningPlayer._name) + '\n~~~~~~~\n' +
            'Breakdown:\n___________\n')
        for i in players:
            stdio.write(str(i) + '_________________\n')  
        stdio.write('The winner was ' + str(winningPlayer._name) + '. Play again? [y/n]')
        if stdio.readString() == 'y':
            return gameRun(players)
        else: return stdio.write("Thanks for playing!\n----------------\n")
    else: 
        stdio.write('There was a tie. No payouts were made. Play again? [y/n]')
        if stdio.readString() == 'y':
            return gameRun(players)
        else: return stdio.write("Thanks for playing!\n----------------\n")


#HERE IS THE ACTUAL CLIENT. making the 'players' variable global allows for multiple rounds.
def main():
    players = newGame()
    gameRun(players)

if __name__ == "__main__":
    main()

#THERE IS A PROBLEM WITH THIS SCRIPT IF A PLAYER HOLDS MORE THAN ONE ACE. UH OH, OH WELL. WE WILL
# TAKE WHATEVER LOSS IN POINTS OCCURS DUE TO THAT.





        



