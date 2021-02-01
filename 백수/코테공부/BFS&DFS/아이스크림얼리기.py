def find_ice(present_node,arr):
  row, col = present_node
  #리스트 밖으로 나간 경우 False 리턴
  if row <0 or row >= len(arr) or col < 0 or col >= len(arr[0]):
      return False
  #주변 노드 탐색
  if arr[row][col] == 0:
    arr[row][col] = 1
    
    find_ice([row-1,col],arr)
    find_ice([row+1,col],arr)
    find_ice([row,col-1],arr)
    find_ice([row,col+1],arr)

    return True

  return False
############################################################################
ans = 0
#입력 받기
n, m = map(int,input().split())
arr = []

#입력 받아서 배열 만들기
for i in range(n):
  arr.append(list(map(int,input())))

for row in range(n):
  for col in range(m):
    if find_ice([row,col], arr):
      ans += 1
print(ans)    