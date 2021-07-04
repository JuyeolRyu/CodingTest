n = int(input())
people = []
ans = []
for _ in range(n):
  people.append(list(map(int,input().split())))

for cur_people in people: 
  tmp = 1
  for p in people:
    if p[0] > cur_people[0] and p[1] > cur_people[1]:
      tmp += 1
  ans.append(tmp)

for p in ans:
  print(p,end=' ')
print()