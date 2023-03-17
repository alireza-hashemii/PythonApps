import random 

SuitTuple = ("Spades","Hearts","Diamons","Clubs")
RankTuple = ("Ace","2","3","4","5","6","7","8","9","Jack","Queen","King")

NCARDS = 8
starting_deck_list = []

def getcard(DeckListIn:list):
    this_card = DeckListIn.pop()
    return this_card


def change_order(DeckListIn:list):
    DeckListOut = DeckListIn.copy()
    random.shuffle(DeckListOut)
    return DeckListOut


for suit in SuitTuple:
    for value,rank in enumerate(RankTuple,1):
        card_dict = {"suit":suit,"value":value,"rank":rank}
        starting_deck_list.append(card_dict)

score = 50

while True:
    gameDeckList = change_order(starting_deck_list)
    currentCardDict = getcard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is:', currentCardRank + ' of ' +currentCardSuit)
    print()

    for carditem in range(0,NCARDS):
        answer = input("would next card be greater or tinyer than currnt card l or h: ")
        answer = answer.casefold()
        nextCardDict = getcard(gameDeckList)
        nextCardSuit = nextCardDict["suit"]
        nextCardRank = nextCardDict["rank"]
        nextCardValue = nextCardDict["value"]

        if answer == "l":
            if currentCardValue > nextCardValue:
                print("You are right")
                score = score + 15
            else: 
                print("You lose")
                score = score - 15
        
        elif answer == "h":
            if currentCardValue < nextCardValue:
                print("You are right")
                score = score + 15
            else: 
                print("You lose")
                score = score - 15

        print(f"your score is {score}") 
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

    continue_or_not = input("y-n: ")
    if continue_or_not == "n":
        break


