#https://www.acmicpc.net/problem/1043
#1043 거짓말
n,m = map(int,input().split())
people = list(map(int,input().split()))[1:]
ans = 0
party_list = []
graph = dict()
visited = [False for i in range(n)]

#graph search
def search(p):
  if visited[p-1]:
    return;
  visited[p-1] = True

  for person in graph[p]:
    search(person)
  return;
#graph input
for _ in range(m):
  scanner = list(map(int,input().split()))[1:]
  party_list.append(scanner)
  for s in scanner:
    for s2 in scanner:
      if s == s2:
        continue
      
      if s in graph:
        graph[s].add(s2)
      else:
        graph[s] = set([s2])
#search
for p in people:
  if p in graph:
    search(p)
#check valid party
for party in party_list:
  check = False
  for p in party:
    if visited[p-1] or p in people:
      check = True
      break
  if not check:
    ans += 1
print(ans)