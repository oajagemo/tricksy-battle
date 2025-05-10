import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = []

def create_deck():
    deck = []
    for suit in suits:
        for number in range(1, 13):  # 1 through 12, no Kingggsss
            deck.append((number, suit))
    random.shuffle(deck)
    return deck

def show_card(card):
    return str(card[0]) + " of " + card[1]

def show_hand(hand):
    for i in range(len(hand)):
        card = hand[i]
        print(str(i + 1) + ": " + str(card[0]) + " of " + card[1])

if __name__ == "__main__":
    deck = create_deck()
    print("Shuffled deck:")
    for card in deck:
        print(show_card(card))
