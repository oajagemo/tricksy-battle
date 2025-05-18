import random


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = []
player_hand = []
computer_hand = []
player_points = 0
computer_points = 0

# Create deck
def create_deck():
    new_deck = []
    for suit in suits:
        for number in range(1, 13):  # 1-12, no King
            new_deck.append((number, suit))
    random.shuffle(new_deck)
    return new_deck


def deal_cards(deck, hand, count=8):
    for i in range(count):
        hand.append(deck.pop())


def show_card(card):
    return str(card[0]) + " of " + card[1]

# Show all cards 
def show_hand(hand):
    for i in range(len(hand)):
        card = hand[i]
        print(str(i + 1) + ": " + show_card(card))

# Let the player choose a card
def player_choose_card(hand, lead_suit=None):
    while True:
        print("\nYour hand:")
        show_hand(hand)

        try:
            choice = int(input("Choose a card to play: ")) - 1
            chosen = hand[choice]

            
            if lead_suit is not None:
                has_same_suit = False
                for card in hand:
                    if card[1] == lead_suit:
                        has_same_suit = True

                if has_same_suit and chosen[1] != lead_suit:
                    print("You must follow the lead suit!")
                    continue

            hand.pop(choice)
            return chosen
        except:
            print("Invalid choice. Try again.")


def computer_play_card(hand, lead_suit=None):
    for card in hand:
        if lead_suit is not None and card[1] == lead_suit:
            hand.remove(card)
            return card
    return hand.pop(0)


def determine_winner(card1, card2, lead_suit):
    if card2[1] != lead_suit:
        return "player"
    elif card1[0] > card2[0]:
        return "player"
    else:
        return "computer"


def play_game():
    global deck, player_points, computer_points

    deck = create_deck()
    deal_cards(deck, player_hand)
    deal_cards(deck, computer_hand)
    leader = "player"

    print("=== Welcome to Tricksy Battle ===")

    while len(player_hand) > 0 and len(computer_hand) > 0:
        print("\n--- New Round ---")

        if leader == "player":
            lead_card = player_choose_card(player_hand)
            follow_card = computer_play_card(computer_hand, lead_card[1])
            print("You played:", show_card(lead_card))
            print("Computer played:", show_card(follow_card))
        else:
            lead_card = computer_play_card(computer_hand)
            follow_card = player_choose_card(player_hand, lead_card[1])
            print("Computer played:", show_card(lead_card))
            print("You played:", show_card(follow_card))

        winner = determine_winner(lead_card, follow_card, lead_card[1])

        if winner == "player":
            player_points += 1
            leader = "player"
            print("You win the round!")
        else:
            computer_points += 1
            leader = "computer"
            print("Computer wins the round!")

        print("Score:")
        print("You:", player_points)
        print("Computer:", computer_points)

    print("\n=== Game Over ===")
    if player_points > computer_points:
        print("You win the game!")
    elif computer_points > player_points:
        print("Computer wins the game!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    play_game()