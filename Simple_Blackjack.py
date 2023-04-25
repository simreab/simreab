import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
class Card:

    def __init__(self, suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.cash = 0

    def empty_hand(self):
        return self.all_cards.clear()

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
            
    def show_hand(self):
        print(f'{self.name} hand: ', end="")
        print (*self.all_cards, sep = ",  ")

    def hand_sum(self):
        card_sum = []
        for card in self.all_cards:
            card_sum.append(card.value)
        return sum(card_sum)
    def __str__(self):
        return f'{self.name} has ${self.cash}.'


def player_won():
    dealer.show_hand()
    player.show_hand()
    print(f'CONGRATULATIONS! You have Won {bet} this round.')
    return True

def player_lost():
    dealer.show_hand()
    player.show_hand()
    print(f'Sorry! You have lost {bet} this round.')
    return True


dealer = Player('dealer')
player = Player(input('What is your name? '))
initial_bet = int(input('How much money would you like to start with? '))
player.cash = initial_bet





game_on = True
new_round = True

#game logic
while game_on:
    
    new_deck = Deck()
    new_deck.shuffle()
    if player.cash == 0:
        print(player)
        print('Sorry, you have lost all your money. GOOD DAY!')
        new_round = False
        break
    bet = int(input('How much would you like to bet? Enter "0" to stop playing. '))

    if (bet <= player.cash) and (bet != 0):
        new_round = True
        dealer.empty_hand()
        player.empty_hand()
        dealer.add_cards(new_deck.deal_one())
        player.add_cards(new_deck.deal_one())
        player.add_cards(new_deck.deal_one())
        
        while new_round:    
            new_deck.shuffle()
            dealer.show_hand()
            player.show_hand()
            print(f"your hand sum is {player.hand_sum()}")

            pd_input = int(input('Enter 1 to Hit or 2 to Stay. ')) 
            if pd_input in [1,2]:
                pd = pd_input
            else:
                print("Invalid Input.")
                continue

            if player.hand_sum() == 21:
                player.cash += bet
                player_won()
                break
            elif pd == 1:
                player.add_cards(new_deck.deal_one())
                if player.hand_sum() > 21:
                    player.cash -= bet
                    player_lost()
                    break
                elif player.hand_sum() < 21:
                    continue
                else:
                    player.cash += bet
                    player_won()
                    break
            elif pd == 2:
                dealer.add_cards(new_deck.deal_one())
                dealer.show_hand()
                while (dealer.hand_sum() <= player.hand_sum()) and (dealer.hand_sum() <=  21):
                    if dealer.hand_sum() > 21:
                        player.cash += bet
                        player_won()
                        break
                    elif (dealer.hand_sum() <= 21) and (dealer.hand_sum() > player.hand_sum()):
                        player.cash -= bet
                        player_lost()
                        break
                    while (dealer.hand_sum() <= player.hand_sum()):
                        dealer.add_cards(new_deck.deal_one())
                        dealer.show_hand()
                        continue
                if ((dealer.hand_sum() <= 21) and (dealer.hand_sum() > player.hand_sum())):
                    player.cash -= bet
                    player_lost()
                else:
                    player.cash += bet
                    player_won()
                break
            break

    elif bet == 0:
        new_round = False
        if player.cash > initial_bet:
            print(player)
            print(f'CONGRATULATIONS! You have Won {player.cash - initial_bet}.')
            break
        elif player.cash < initial_bet:
            print(player)
            print(f'Sorry, you have lost {initial_bet - player.cash}.')
            break
        else:
            print(player)
            print(f'You have broke even and leaving with {player.cash}. Not bad!')
            break
    else:
        print(f'you have insufficient balance. you can only bet upto ${player.cash}.')   
        new_round = True
    print("You have $" + str(player.cash) + ' left.')
