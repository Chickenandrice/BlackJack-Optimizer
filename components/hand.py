import dealing_cards.dealer as dd

# dealing for player hands
class Hand: 
    def __init__(self):
        self.hand = []

    def draw_card(self): 
        self.hand.append(dd.Dealer.deal_card()) 

    def final_hand(self):
        return self.hand 
    
    def pair(self):
        return len(self.hand) == 2 and self.hand[0][0] == self.hand[1][0]
