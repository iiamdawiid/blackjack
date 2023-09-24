import random

class Blackjack():
    def __init__(self):
        self.in_progress = True

    def game_start(self):
        print("BLACKJACK".center(50, '-'))
        start = input("Press ENTER to Start: ")
        while start.isalnum():
            print("\n>>> INVALID INPUT <<<")
            start = input("Press ENTER to Start: ")
        self.shuffle_deck()

    def shuffle_deck(self):
        '''here we will create dictionary to hold cards and their values
           and shuffle the deck somehow'''
        self.cards = {
            'C1': 1, 'C2': 2, 'C3': 3, 'C4': 4, 'C5': 5, 'C6': 6, 'C7': 7, 'C8': 8, 'C9': 9, 'C10': 10, 'C11': 11, 'C12': 12, 'C13': 13,
            'D1': 1, 'D2': 2, 'D3': 3, 'D4': 4, 'D5': 5, 'D6': 6, 'D7': 7, 'D8': 8, 'D9': 9, 'D10': 10, 'D11': 11, 'D12': 12, 'D13': 13,
            'H1': 1, 'H2': 2, 'H3': 3, 'H4': 4, 'H5': 5, 'H6': 6, 'H7': 7, 'H8': 8, 'H9': 9, 'H10': 10, 'H11': 11, 'H12': 12, 'H13': 13,
            'S1': 1, 'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10, 'S11': 11, 'S12': 12, 'S13': 13
        }
        # store the cards in a list to shuffle - dictionary keys will be stored in the list
        self.card_list = list(self.cards.keys())
        random.shuffle(self.card_list)
        self.deal_cards()
        
    def deal_cards(self):
        '''deal the user 2 cards and deal the computer 2 cards. Player should be able to see their own cards
           but should only be able to see one of the dealers cards'''
        self.player_cards = []
        self.dealer_cards = []
        for i in range(0, 2):
            card = self.card_list.pop(i)
            self.player_cards.append(card)
        for i in range(0, 2):
            card = self.card_list.pop(i)
            self.dealer_cards.append(card)
        if self.cards[self.player_cards[0]] + self.cards[self.player_cards[1]] == 21:
            print("\nBLACKJACK -- YOU WIN !")
            self.end_game()
        elif self.cards[self.player_cards[0]] + self.cards[self.player_cards[1]] > 21:
            self.deal_cards()
        elif self.cards[self.dealer_cards[0]] + self.cards[self.dealer_cards[1]] > 21:
            self.deal_cards()
        else:
            print(f"\nDEALER: {self.dealer_cards[0]}, X")
            print(f"PLAYER: {', '.join(self.player_cards)}")
            self.running_game()

    def running_game(self):
        '''program will run till a player goes over 21, quits, or beats the dealer when choosing to stand'''
        while self.in_progress:
            self.card_total()
            if self.in_progress == False:
                break
            actions = {'H': self.hit, 'S': self.stand, 'Q': self.quit}
            player_choice = input("Hit, Stand, Or Quit?: (H/S/Q): ")
            player_choice = player_choice.upper()
            if player_choice not in {'H', 'S', 'Q'}:
                print("\n>>> INVALID INPUT <<<")
                player_choice = input("Hit, Stand, Or Quit?: (H/S/Q): ")
                player_choice == player_choice.upper()
            action = actions[player_choice]
            action()
        
    def card_total(self):
        '''will keep track of users card total and computer's card total'''
        self.player_total = 0
        self.dealer_total = 0
        for card in self.player_cards:
            self.player_total += self.cards[card]
        for card in self.dealer_cards:
            self.dealer_total += self.cards[card]
        if self.player_total == 21:
            self.print_score()
            print("\n!! YOU WON !")
            self.in_progress = False
            self.end_game()
        elif self.player_total > 21:
            self.print_score()
            print("!! YOU BUSTED !!")
            self.in_progress = False
            self.end_game()
        elif self.dealer_total == 21:
            # if dealer_total is 21 re-deal the cards
            self.card_total()
        else:
            pass

    def hit(self):
        '''will add additional card to user's deck if player decides to HIT'''
        if self.player_total > 21:
            self.print_score
            print("!! YOU BUSTED !!")
            self.end_game()
            self.in_progress = False
        else:
            card = self.card_list.pop()
            self.player_cards.append(card)
            print(f"\nDEALER: {self.dealer_cards[0]}, X")
            print(f"PLAYER: {', '.join(self.player_cards)}")

    def stand(self):
        ''' if user decides to stand, compare player_total to dealer_total and determine whether player or dealer won'''
        if self.player_total > self.dealer_total:
            self.print_score()
            print("!! YOU WON !!")
            self.end_game()
        elif self.player_total < self.dealer_total:
            self.print_score()
            print("!! YOU LOST !!")
            self.end_game()
        else:
            self.print_score()
            print("!! YOU TIED !!")
            self.end_game()
            
    def end_game(self):
        '''if player wants to play again, call running_game(), else set in_progress = False to terminate'''
        go_again = input("\nPlay Again?: (Y/N): ")
        go_again = go_again.upper()
        while go_again not in {'Y', 'N'}:
            print("\n>>> INVALID INPUT <<<")
            go_again = input("\nPlay Again?: (Y/N): ")
            go_again = go_again.upper()
        if go_again == 'Y':
            self.in_progress = True
            self.game_start()
        else:
            print("\nThank you for playing!")
            self.in_progress = False

    def quit(self):
        print("\nThank you for playing!")
        self.in_progress = False

    def print_score(self):
        print(f"\nDEALER SCORE: {self.dealer_total}\nPLAYER SCORE: {self.player_total}")



bj = Blackjack()
bj.game_start()