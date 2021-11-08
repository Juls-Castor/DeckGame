import random, argparse

clubs = "\u2660"  # (♣)
diamonds = "\u2665"  # (♦)
hearts = "\u2666"  # (♥)
spades = "\u2663"  # (♠)


class Card:
    def __init__(self, symbol, number):
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return "[{} - {}]".format(self.symbol, self.number)


class Deck:
    def __init__(self, players):
        symbols = [clubs, diamonds, hearts, spades]
        numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.num_players = players      
        self.deck = []
        self.players = [[] for i in range(self.num_players)]

        for s in symbols:
            for n in numbers:
                card = Card(s, n)
                self.deck.append(card)

        print("> Init deck")
        self.print_deck(self.deck)

    def print_deck(self, deck):
        print()
        for num, card in enumerate(deck):
            if (num + 1) % 13 != 0:
                print(card, end="  ")
            else:
                print(card)
        print()

    def shuffled_deck(self):
        print("> Shuffled deck")
        random.shuffle(self.deck)
        self.print_deck(self.deck)

    def deal_deck(self, cards):
        print("> Players cards")

        for p in range(self.num_players):
            for c in range(cards):
                card = self.deck.pop(0)
                self.players[p].append(card)

            print()
            print("Player {}".format(p))
            self.print_deck(self.players[p])

        print()
        print("> Remaining cards in the deck")
        self.print_deck(self.deck)
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--players", help="Number of players to deal cards.", type=int)
    parser.add_argument("--cards", help="Number of cards to deal per player", type=int)
    args = parser.parse_args()

    if args.players * args.cards <= 52:
        deck = Deck(players=args.players)
        deck.shuffled_deck()
        deck.deal_deck(cards=args.cards)
        deck.deal_deck(cards=1) # Draw 1 card
    else:
        print("The number of players and cards exceed the deck limit.")
