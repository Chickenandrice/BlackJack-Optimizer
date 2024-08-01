import random

class Dealer():
    """
    A Dealer class that mimics the tasks a BlackJack Dealer would have. 

    Attributes:
        hand (list): A list of tuple[str, str], which represent cards in a hand
        total (int): The total of the card values in a dealer's hand.

    Methods:
        deal_card(self, deck: list[tuple[str, str]]):
            deals a card, which is represented by a tuple[str,str], and it is taken from a deck, which is a list of cards 

        deal_self(self, deck: list[tuple[str, str]]):
            uses the deal_card method to deal the dealer as a tradition dealer would 

        dealer_hand_values(self): 
            returns the dealer's hand values in the form of a list 

        upcard(self): 
            returns the first upcard of the dealer's hand 

        reset(self): 
            resets the dealer's hand and dealer's total hand value 
    """

    def __init__(self):
        """
            This is the constructor for the Dealer class 

        """
        self.hand = []
        self.total = 0

    def deal_card(self, deck: list[tuple[str, str]]) -> tuple[str,str]: 
        """ 
        This method randomly deals cards from a deck. 

        Parameters: 

        deck (list[tuple[str, str]]): A list of tuples that have two string values, which represent a card's value and suit 

        Returns: 

        A tuple that represents a card's value and suit in the format tuple[str, str] 
        """
        return deck.pop(random.randint(0, len(deck)-1))

    def deal_self(self, deck: list[tuple[str, str]]) -> tuple[list[tuple[str,str]], int]:
        """
        This method mimics a dealer dealing cards to their own hand

        Parameters:

        deck (list[tuple[str, str]]): A list of tuples that have two string values, which represent a card's value and suit 

        Returns: 
        
        tuple[list[tuple[str,str]], int]: the first value is the dealer's hand, the second value is the total of the dealer's hand 


        """
        aces = 0
        print("dealer cards:")
        while self.total < 17:

            # if there exists an ace that changes from 11 -> 1, is less than 17, and total < 21
            card = self.deal_card(deck)
            self.hand.append(card)  
          

            if card[0] in ["2","3", "4", "5", "6", "7", "8", "9", "10"]:
                self.total += int(card[0])
            elif card[0] in ["Jack", "Queen", "King"]:
                self.total += 10
            else:
                aces += 1
                self.total += 11

            if aces > 0 and self.total > 21: 
                if self.total - 10 <= 21:
                     # Ace is 1, above 16, less 22
                    if self.total - 10 >= 17:
                        self.total -= 10
                        print(self.hand)
                        return self.hand, self.total
                        
                    # Ace is 1, less 17 
                    else: 
                        self.total -= 10
                        aces -= 1
                else: 
                    # case where Ace is 1, above 21 
                    self.total -= 10
                    print(self.hand)
                    return self.hand, self.total
        
        print(self.hand)
        return self.hand, self.total 
    
    def dealer_hand_values(self) -> list[str]:
        """ 
        This method returns the card values of all cards in a dealer's hand. 

        Returns: 

        list of string values of the dealer's hand values 
        """

        vals = []
        for value in self.hand: 
            vals.append(value[0])
        return vals 
    
    def upcard(self) -> tuple[str,str]:
        """ 
        This method returns the upcard in a dealer's hand.

        Returns: 
        a tuple[str,str] that represents the dealer's first upcard
        """

        return self.hand[0]
    
    def reset(self) -> None:
        """ This method resets a dealer's hand and total by setting it to an empty list and 0 total. """

        self.hand = []
        self.total = 0
