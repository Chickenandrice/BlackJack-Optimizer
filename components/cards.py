
def new_deck(num_decks: int) -> list[tuple[str, str]]:
    """
    gets a list of tuples that represents card in a playing deck. 

    Parameters: 

    num_decks (int): The number of decks that should be in a game

    Returns:

    list[tuple[str,str]]: a list of tuples, which represent playing cards
    """
    play_cards = []
    for card in deck: 
        play_cards.append(card)

    return play_cards*num_decks

# list of tuples that represent cards in a standard 52 card deck 
deck = [
("2","Clubs"), 
("2","Diamonds"),
("2","Hearts"),
("2","Spades"),
("3","Clubs"),
("3","Diamonds"),
("3","Hearts"),
("3","Spades"),
("4","Clubs"),
("4","Diamonds"),
("4","Hearts"),
("4","Spades"),
("5","Clubs"),
("5","Diamonds"),
("5","Hearts"),
("5","Spades"),
("6","Clubs"),
("6","Diamonds"),
("6","Hearts"),
("6","Spades"),
("7","Clubs"),
("7","Diamonds"),
("7","Hearts"),
("7","Spades"),
("8","Clubs"),
("8","Diamonds"),
("8","Hearts"),
("8","Spades"),
("9","Clubs"),
("9","Diamonds"),
("9","Hearts"),
("9","Spades"),
("10","Clubs"),
("10","Diamonds"),
("10","Hearts"),
("10","Spades"),
("Jack","Clubs"),
("Jack","Diamonds"),
("Jack","Hearts"),
("Jack","Spades"),
("Queen","Clubs"),
("Queen","Diamonds"),
("Queen","Hearts"),
("Queen","Spades"),
("King","Clubs"),
("King","Diamonds"),
("King","Hearts"),
("King","Spades"),
("Ace","Clubs"),
("Ace","Diamonds"),
("Ace","Hearts"),
("Ace","Spades"),
]


"""
test cases 

def new_deck2(num_decks, decks):
    play_cards = []
    for card in decks: 
        play_cards.append(card)

    return play_cards*num_decks

deck2 = [("Ace","Clubs"),("7","Diamonds")]
deck3 = [("7","Diamonds"),("Ace","Clubs")]
deck4 = [("4","Diamonds"),("Ace","Clubs"),("7", "Clubs")]
deck5 = [('4', 'Hearts'), ('Ace', 'Diamonds'), ('6', 'Hearts')]
deck6 = [('Ace', 'Diamonds'), ('10', 'Diamonds'), ('9', 'Diamonds')]
deck7 = [('10', 'Hearts'), ('3', 'Hearts'), ('3', 'Spades'), ('Ace', 'Hearts')]
deck8 = [('Ace', 'Spades'), ('3', 'Clubs'), ('9', 'Spades'), ('Jack', 'Diamonds'), ('King', 'Spades'), ('8', 'Spades')]

"""