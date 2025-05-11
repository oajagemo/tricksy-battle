import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = []
player_hand = []
computer_hand = []

def create_deck():
    deck = []
    for suit in suits:
        for number in range(1, 13):
            deck.append((number, suit))
    random.shuffle(deck)
    return deck

def deal_cards(deck, hand, count=8):
    for _ in range(count):
        hand.append(deck.pop())

def show_card(card):
    return str(card[0]) + " of " + card[1]

def show_hand(hand):
    for i in range(len(hand)):
        card = hand[i]
        print(str(i + 1) + ": " + str(card[0]) + " of " + card[1])

def play_card(hand, lead_suit=None):
    for card in hand:
        if lead_suit and card[1] == lead_suit:
            hand.remove(card)
            return card
    return hand.pop(0)

def determine_winner(card1, card2, lead_suit):
    if card2[1] != lead_suit:
        return "player"
    return "player" if card1[0] > card2[0] else "computer"

def play_game():
    global deck
    deck = create_deck()
    deal_cards(deck, player_hand)
    deal_cards(deck, computer_hand)
    leader = "player"

    while player_hand and computer_hand:
        if leader == "player":
            lead = play_card(player_hand)
            follow = play_card(computer_hand, lead[1])
        else:
            lead = play_card(computer_hand)
            follow = play_card(player_hand, lead[1])

        print("Player played:", show_card(lead))
        print("Computer played:", show_card(follow))

        winner = determine_winner(lead, follow, lead[1])
        if winner == "player":
            leader = "player"
            print("Player wins the round!")
        else:
            leader = "computer"
            print("Computer wins the round!")

if __name__ == "__main__":
    play_game()

