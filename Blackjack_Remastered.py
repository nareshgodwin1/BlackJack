#Blackjack
import random
import time

def welcome():
    print("~~~~~~~~~~~~~~~~~~~~~\nWELCOME TO BLACKJACK!\n~~~~~~~~~~~~~~~~~~~~~")

def reset_variables():
    global deck, player_hand, player_values, dealer_hand, dealer_values, hit, dealer_move, player_stand, bust, insta_blackjack
    deck = ["A♦", "A♠", "A♣", "A♥", "2♦", "2♠", "2♣", "2♥", "3♦", "3♠", "3♣", "3♥", "4♦", "4♠", "4♣", "4♥", "5♦", "5♠", "5♣", "5♥",  "6♦", "6♠", "6♣", "6♥", "7♦", "7♠", "7♣", "7♥", "8♦", "8♠", "8♣", "8♥", "9♦", "9♠", "9♣", "9♥", "10♦", "10♠", "10♣", "10♥", "J♦", "J♠", "J♣", "J♥","Q♦", "Q♠", "Q♣", "Q♥","K♦", "K♠", "K♣", "K♥"]
    player_hand = []
    player_values = []
    dealer_hand = []
    dealer_values = []
    hit = False
    dealer_move = False
    player_stand = False
    bust = False
    insta_blackjack = False

def generate_card():
    card = random.choice(deck)
    deck.remove(card)
    return card

def card_value(card):
    card_value = 0
    if "10" in card or "J" in card or "Q" in card or "K" in card:
        card_value = 10
    elif "A" in card:
        card_value = 11
    else:
        card_value = int(card[0])
    return card_value

def generate_player_hand():
    global player_hand, player_values
    
    if hit == False:
        for num in range(0, 2):
            player_hand.append(generate_card())
            player_values.append(card_value(player_hand[num]))
    if hit == True:
            player_hand.append(generate_card())
            player_values.append(card_value(player_hand[-1]))

def calculate_player_sum():        
    global player_sum
    player_sum = sum(player_values)
    index = 0
    while player_sum > 21 and index < len(player_values):
        if player_values[index] == 11:
            player_values[index] = 1
            player_sum -= 10
        else:
            index+=1
    return player_sum

def generate_dealer_hand():
    global dealer_hand, dealer_values
    
    if dealer_move == False:
        for num in range(0, 2):
            dealer_hand.append(generate_card())
            dealer_values.append(card_value(dealer_hand[num]))
    if dealer_move == True:
            dealer_hand.append(generate_card())
            dealer_values.append(card_value(dealer_hand[-1]))

def calculate_dealer_sum():
    global dealer_sum
    dealer_sum = sum(dealer_values)
    index = 0
    while dealer_sum > 21 and index < len(dealer_values):
        if dealer_values[index] == 11:
            dealer_values[index] = 1
            dealer_sum -= 10
        else:
            index+=1
    return dealer_sum

def instant_blackjack():
    global insta_blackjack, player_stand
    if player_sum == 21:
        insta_blackjack = True
        player_stand = False
        win_conditions()

def hit_or_stand():
    global hit, player_stand, bust, dealer_move
    
    #When the player sum is less than 21, ask if they want to hit or stand
    while player_sum < 21 and player_stand == False:
        #Input
        while True:
            hit_or_stand = str(input("\nHit or Stand? ")).lower()
            if hit_or_stand == "hit" or hit_or_stand == "h" or hit_or_stand == "stand" or hit_or_stand == "s":
                break
            else:
                print("Please enter a valid response")

        #if hit | generate new card and new value
        if hit_or_stand == "hit" or hit_or_stand == "h":
            hit = True
            generate_player_hand()
            calculate_player_sum()

            print("\nPlayer:", " ".join(player_hand))
            print(f"Player sum is {player_sum}")

            if player_sum > 21:
                bust = True
                dealer_move = False
                break

        #if stand | break loop
        elif hit_or_stand == "stand" or hit_or_stand == "s":
            player_stand = True
            dealer_move = True
            break

def dealer_moves():
    global dealer_move
    if dealer_move == True:
        time.sleep(1) 
        print("\nDealer Reveals")
        time.sleep(1)
        print("\nDealer:", " ".join(dealer_hand))
        time.sleep(1)
        print("Dealer sum is", dealer_sum)
        while dealer_sum < 17 and dealer_sum < player_sum:
            generate_dealer_hand()
            calculate_dealer_sum()
            time.sleep(1) 
            print("\nDealer hits\n")
            time.sleep(1) 
            print("Dealer:", " ".join(dealer_hand))
            time.sleep(1) 
            print("Dealer sum is", dealer_sum)
            time.sleep(1) 

def win_conditions():
    global player_stand, bust, insta_blackjack
    if bust == True:
        print("Bust! Dealer wins!\n")
        player_stand = False
    
    if insta_blackjack == True:
        print("Blackjack! Player wins!")
        player_stand = False
        insta_blackjack = False

    if player_stand == True:
        if player_sum == 21 and dealer_sum == 21 and len(player_values) == len(dealer_values):
            print("Tie! Split the pot\n")
            player_stand == False
           
        elif player_sum == 21 and len(player_values) <= len(dealer_values):
            print("Blackjack! Player Wins!\n")
            player_stand == False

        elif dealer_sum == 21 and len(dealer_values) <= len(player_values):
            print("\nDealer Blackjack! Dealer Wins!\n")
            player_stand == False
           
        elif player_sum == dealer_sum and dealer_sum != 21 and player_sum != 21:
            print("\nDealer Stands")
            time.sleep(1)
            print("Tie! Split the pot\n")
            player_stand == False
        
        elif dealer_sum > 21:
            print("Dealer Busted! Player wins!\n")
            player_stand == False
       
        elif player_sum > dealer_sum and dealer_sum < 21 and player_sum < 21:
            print("\nDealer Stands")
            time.sleep(1)
            print("Player Wins!\n")
            player_stand == False
           
        elif player_sum < dealer_sum and dealer_sum < 21 and player_sum < 21:
            print("\nDealer Stands")
            print("Dealer Wins!\n")
            player_stand == False

    if player_stand == False:
        pass

def play_again():
    game()
    while True:
        again = input("Would you like to play again? (Y)es or (N)o: ")
        if again == "y" or again == "n" or again == "no" or again == "yes":
            game()
            break
        else:
            print("Please enter (Y)es or (N)o")

def game():
    welcome()
    reset_variables()
    generate_player_hand()
    generate_dealer_hand()
    calculate_player_sum()
    calculate_dealer_sum()

    print(f"Player:", " ".join(player_hand))
    print(f"Player sum is {player_sum}")
    print(f"Dealer: {dealer_hand[0]} ？")

    instant_blackjack()
    win_conditions()
    hit_or_stand()

    dealer_moves()
    win_conditions()

play_again()