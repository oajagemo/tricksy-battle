import random


player_hand = [] 
computer_hand = []
player_points = 0
computer_points = 0
deck = []
revealed_cards = []
suit_lead = None

def create_card(number,suit):
    card = (number, suit)
    return card

def make_deck():
    new_deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    for suit in suits:
        for number in range(1, 13):  # 1-12
            if number != 13:
                new_card = create_card(number,suit)
                new_deck.append(new_card)
    
    return new_deck

def shuffle_deck(deck):
    random.shuffle(deck)

def play_game():
    print('WELCOME TO THE GAME')

deck = make_deck()
print(deck)
print(shuffle_deck(deck))