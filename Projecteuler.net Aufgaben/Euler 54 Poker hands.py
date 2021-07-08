cards = []
with open("C:/Users/Jim/Desktop/Euler_54_Poker_hands.txt","r") as f:
    file = f.readlines()
for line in file:
    card = line.split()
    cards.append(card)
#print(words)

hands = []
for x in range(0,100):
    hands.append([cards[x]])
print(hands)

alltime_winner = "null"
winner = "null"
while alltim_winner == "null":
    while winner == "null":
        
    
#for match in range(1, 1001):
    
    
