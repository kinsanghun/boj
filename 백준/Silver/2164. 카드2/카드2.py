from collections import deque

cnt = int(input())
cards = deque()

for i in range(1, cnt+1):
    cards.append(i)
    
while len(cards)>1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])    
