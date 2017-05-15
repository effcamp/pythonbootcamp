import random
i = 0

class Dealer(object):
    suits = ("of Hearts", "of Spades", "of Clubs", "of Diamonds")
    ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace")
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    
    def __init__(self):
        self.hand = []
        

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, hand, n=1):
        global i
        for n in range(n):
            hand.append(self.deck[i])
            i += 1
        if i % 51 == 0:
            i = 0
            self.shuffle()
            
    def clear(self):
        self.hand.clear()

    def value(self):
        val = 0
        for card in self.hand:
            if card[0] == "Jack" or card[0] == "Queen" or card[0] == "King":
                val += 10
            elif card[0] in range(2, 11):
                val += card[0]
            #Dealing with aces as the dealer, pun intended!
            else:
                if val + 11 < 21:
                    val += 11
                else:
                    val += 1
        return val

class Player(Dealer):
    def __init_(self):
        self.hand = []

    def value(self):
        val = 0
        for card in self.hand:
            if card[0] == "Jack" or card[0] == "Queen" or card[0] == "King":
                val += 10
            elif card[0] in range(2, 11):
                val += card[0]
            elif card[0] == "Ace":
                while True:
                    try:
                        ace = int(input("\nYou got an ACE! (Current value {}). \nAce as 1 or 11: ".format(val)))
                    except:
                        print("Wrong input")
                        continue
                    if ace == 1 or ace == 11:
                        val += ace
                        break
                    else:
                        print("Wrong number!")
                        continue 
        return val

def main():
    print("Welcome to BlackJack!")
    #print("You have a starting balance of 100 dollars.")
    #print("Would you like to add more? Y/N")
    #TODO add blance check

    print("Let's play!")
    wins = 0
    loss = 0
    draw = 0
    balance = 100

    #Game loop + deal initial cards
    Dealer().shuffle()
    while True:
        track = 0
        dealertrack = 0
        p_bust = False
        d_bust = False
        player = Player()
        dealer = Dealer()
        print("You have ${}.".format(balance),end="")
        while True:
            try:
                bet = int(input(" What is your bet: "))
            except:
                continue
            if 0 < bet <= balance:
                break
            else:
                print("Please enter a valid amount from 1 to {}:".format(balance))
                continue
            
        Dealer().deal(player.hand, 2)
        Dealer().deal(dealer.hand, 1)
        print("Dealer's cards are:\n{} - Worth: {}".format(dealer.hand, dealer.value()))
        print()

        print("Your cards are:\n{}".format(player.hand), end="")
        track = player.value()
        print(" - Worth: {}".format(track))
        #Hit loop        
        while True:
            try:
                hit = str(input("Hit? Y/N: "))
            except ValueError:
                continue
            if hit.upper() == "N":
                print()
                break
            elif hit.upper() == "Y":
                Dealer().deal(player.hand)                
                print("Your Cards: {}".format(player.hand))
                track = player.value()
                print("Worth: {}".format(track))
                if track > 21:
                    print("\t\t>>>>BUST!<<<<<")
                    p_bust = True
                    break
        #print()  
        while True:
            dealertrack = dealer.value()
            if dealertrack <= 16 and p_bust == False:
                Dealer().deal(dealer.hand)
                continue
            elif dealertrack > 21:
                print("\t\t>>>>>>Dealer bust!<<<<<<<<")
                d_bust = True
                break
            else:
                break
            
        #print()
        if p_bust == False and track > dealertrack or d_bust:
            print("\n\t\t*******YOU WIN!********: \n Dealer's cards were {}. \nValue was {}.".format(dealer.hand, dealertrack))
            print("You had {}.".format(track))
            wins += 1
            balance += bet
        elif track == dealertrack and (p_bust == False and d_bust == False):
            print("\n\t\t*******PUSH!*********: \n Dealer's cards were {}. \nValue was {}.".format(dealer.hand, dealertrack))
            print("You had {}.".format(track))
        else:
            print("\n\t\t*********YOU LOSE!*********: \n Dealer's cards were {}. \nValue was {}.".format(dealer.hand, dealertrack))
            print("You had {}.".format(track))
            loss += 1
            balance -= bet

        play = input("You have ${}. Play again? Y/N: ".format(balance))
        
        if play.upper() == "Y":
            continue
        elif play.upper() == "N":
            print("Your total winnings: ${}".format(balance))
            break
        else:
            print("Unknown input, closing")
            break
            
if __name__ == "__main__":
    main()
