ans = 1
direction_set = \{0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]\}
check =[False,False,False,False]

n, m = map(int, input().split())
x,y,direction = map(int, input().split())

for i in range(n):
  tmp = []
  for j in map(int,input().split()):
    tmp.append(j)
  field.append(tmp)


while(True):
  direction = (direction + 3)%4
  left = direction_set[ direction ]

  if( field[x + left[0]][y + left[1]] == 0):
    check =[False,False,False,False]
    field[x][y] = -1
    x += left[0]
    y += left[1]
    ans += 1
  else:
    check[direction] = True

  if False not in check:
    direction = (direction + 2)%4
    back = direction_set[direction]
    if(field[x + back[0]][y+ back[1]] == 1):
      print(ans)
      break
    else:
      x += back[0]
      y += back[1]
}
 
