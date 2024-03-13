

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]




user_cards = []
dealer_cards = []
flag = True

play_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")




def draw_card():
    next_card_user = random.choice(cards)
    user_cards.append(next_card_user)
    next_card_dealer = random.choice(cards)
    dealer_cards.append(next_card_dealer)
    user_score = sum(user_cards)
    dealer_score = sum(dealer_cards)
    if 11 in user_cards and user_score > 21:
        user_cards.remove(11)
        user_cards.append(1)
        user_score = sum(user_cards)
    if 11 in dealer_cards and dealer_score > 21:
        dealer_cards.remove(11)
        dealer_cards.append(1)
        dealer_score = sum(dealer_cards)

    print(f"You cards: {user_cards}, current score: {user_score}")
    print(f"Dealer's first card: {first_draw_dealer}")
    if sum(user_cards) > 21:
        global flag
        flag = False
        print(f"You cards: {user_cards}, score: {sum(user_cards)}")
        print(f"Dealer's cards: {dealer_cards}, score: {sum(dealer_cards)}")
        print("You Lose!")


if play_or_not == 'y':
    first_draw_user = random.choice(cards)
    user_cards.append(first_draw_user)
    first_draw_dealer = random.choice(cards)
    dealer_cards.append(first_draw_dealer)
    play_or_not == 'n'
    draw_card()


   
while flag == True:
    play_again = input("Type 'y' to get another card, type 'n' to pass: ")

    if play_again == 'y':
        draw_card()

    if play_again == 'n':
       flag = False
       print(f"You cards: {user_cards}, score: {sum(user_cards)}")
       print(f"Dealer's cards: {dealer_cards}, score: {sum(dealer_cards)}")

       if sum(user_cards) == sum(dealer_cards):
           print("Draw!")
       elif sum(user_cards) <= 21 and sum(user_cards) > sum(dealer_cards):
           print("You win!")
       elif sum(user_cards) <= 21 and sum(dealer_cards) > 21 :
           print("You win!")
       else:
           print("You Lose!")
