############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from replit import clear
from art import logo

def deal_card():
  """returns a random card from deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """take a list of cards and returns the score calculated from cards"""
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    
  return sum(cards)
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over, you lose!"
  elif computer_score > 21:
    return "Opponent went over, you win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def playgame():

  print(logo)
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  your cards: {user_cards}, current score: {user_score} ")
    print(f"  computer's first hand: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_should_deal == "y":
      user_cards.append(deal_card())
    else:
      is_game_over = True
  
  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  
  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"Your final hand: {user_cards}, final score: {user_score} ")
  print(f"computer's final hand: {computer_cards}, final score: {computer_score} ")
  print(compare(user_score, computer_score))
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  playgame()




# import random
# from replit import clear
# from art import logo
# def compare_score(f_card1, f_card2):
#   f_score1 = sum(f_card1)
#   f_score2 = sum(f_card2)
#   if f_score1 > f_score2:
#     print("You won")
#   elif f_score1 < f_score1:
#     print("You loose")
#   elif f_score1 == f_score1:
#     print("You draw")
# def compare_score(f_card1, f_card2):
#   if your_score > comp_score:
#     print("You won")
#   elif your_score < comp_score:
#     print("You loose")
#   elif your_score == comp_score:
#     print("You draw")
# def add_card(f_card):
#   card = random.choice(cards)
#   f_card.append(card)
# def display_card(f_card1, f_card2):
#   print(f"Your cards: {f_card1}, current score: {sum(f_card1)}")
#   print(f"Computer's first card: {f_card2[0]}")
# def display_hand(f_card1, f_card2):
#   print(f"Your final hand: {f_card1}, final score: {sum(f_card1)} ")
#   print(f"computer's final hand: {f_card2}, final score: {sum(f_card2)} ")
# game_status = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
# while game_status != 'y' and game_status != 'n':
#   print("bsdk backchodi mt pel")
#   game_status = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# while game_status == 'y':
#   clear()
#   print(logo)
#   your_card = random.choices(cards, k=2)
#   comp_card = random.choices(cards, k=2)
#   your_c_score = sum(your_card)
#   display_card(your_card,comp_card)
#   comp_c_score = sum(comp_card)
#   if your_c_score == 21 or comp_c_score == 21:
#     display_hand(your_card, comp_card)
#     print("BLACKJACK!")
#     compare_score(your_card, comp_card)
#     game_status = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
#   else:
#     your_score = your_c_score
#     while your_score < 21:
#       stay_draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#       if stay_draw == 'y':
#         add_card(your_card)
#         your_score = sum(your_card)
#         if your_score < 21:
#           display_card(your_card, comp_card)
#       elif stay_draw == 'n':
#         break
#       else:
#         print("invalid input")
#     if your_score > 21 :
#       display_hand(your_card, comp_card)
#       print("You went over. You lose 😭")
#     elif your_score == 21:
#       display_hand(your_card, comp_card)
#       print("BLACKJACK!, You won ")
#     else:
#       comp_score = comp_c_score
#       comp_draw = random.randint(0,19)
#       for r in range(0,comp_draw):
#         if comp_score < 21:
#           add_card(comp_card)
#           comp_score = sum(comp_card)
#         elif comp_score > 21:
#           display_hand(your_card, comp_card)
#           print("Computer went over. You won ")
#           game_status = 'n'
#           break
#         elif comp_score == 21:
#           display_hand(your_card, comp_card)
#           print("BLACKJACK!, Computer won ")
#           game_status = 'n'
#           break
    
#   game_status = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
# print("Bye")
