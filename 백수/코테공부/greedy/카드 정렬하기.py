#https://www.acmicpc.net/problem/1715
#1715카드 정렬하기
import heapq

n = int(input())
cards = []
for i in range(n):
  cards.append(int(input()))

heapq.heapify(cards)

if n == 1:
  print(0)
elif n == 2:
  print(cards[0]+cards[1])
else:
  ans = 0
  while len(cards) > 1:
    tmp = heapq.heappop(cards)+heapq.heappop(cards)
    ans += tmp
    heapq.heappush(cards,tmp)

  print(ans)