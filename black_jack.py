
import random
import art
 
cards = {
    "A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10,
}
 
 
def deal_card():
    """Return one random card name."""
    return random.choice(list(cards))
 
 
def calculate_score(hand):
    """Return the total of a hand. Aces count as 1 instead of 11 when needed."""
    score = 0
    for card in hand:
        score += cards[card]
 
    aces = hand.count("A")
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score
 
 
def is_blackjack(hand):
    """Blackjack = 21 from the first two cards only."""
    return len(hand) == 2 and calculate_score(hand) == 21
 
 
def compare(user_hand, dealer_hand):
    """Return the result message of the game."""
    user_score = calculate_score(user_hand)
    dealer_score = calculate_score(dealer_hand)
 
    if is_blackjack(user_hand) and is_blackjack(dealer_hand):
        return "Both have Blackjack. It's a draw."
    elif is_blackjack(dealer_hand):
        return "Dealer has Blackjack. You lose."
    elif is_blackjack(user_hand):
        return "Blackjack! You win."
    elif user_score > 21:
        return "You went over 21. You lose."
    elif dealer_score > 21:
        return "Dealer went over 21. You win."
    elif user_score == dealer_score:
        return "It's a draw."
    elif user_score > dealer_score:
        return "You win."
    else:
        return "You lose."
 
 
def play_game():
    print(art.logo)
 
    user_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
 
    # Player's turn
    while True:
        user_score = calculate_score(user_hand)
        print(f"\nYour cards: {user_hand}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")
 
        if is_blackjack(user_hand) or is_blackjack(dealer_hand) or user_score > 21:
            break
 
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == "y":
            user_hand.append(deal_card())
        else:
            break
 
    # Dealer's turn: draws until 17 or more (only if the player didn't go over 21)
    while calculate_score(dealer_hand) < 17 and calculate_score(user_hand) <= 21:
        dealer_hand.append(deal_card())
 
    print(f"\nYour final hand: {user_hand}, final score: {calculate_score(user_hand)}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {calculate_score(dealer_hand)}")
    print(compare(user_hand, dealer_hand))
 
 
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_game()
 
print("Goodbye!")
 

