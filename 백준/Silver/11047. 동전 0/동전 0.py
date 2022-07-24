import sys

n, k = map(int,input().split())

count = 0
balance = k

coins = list()
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

for coin in reversed(coins):
    if balance > 0:
        if balance >= coin:
            count += balance // coin
            balance %= coin

print(count)
