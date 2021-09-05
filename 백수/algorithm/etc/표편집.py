from collections import defaultdict
def solution(n, k, cmds):
    answer = ['O']*n
    delete = []
    pointer = k
    
    nodes=defaultdict(list)
    nodes[0],nodes[n-1] = [-1,1],[n-2,-1]
    for i in range(1,n-1):
        nodes[i]=[i-1,i+1]

    for cmd in cmds:
        cmd = cmd.split()
        if len(cmd)>1:
            if cmd[0] == 'U':
                for num in range(int(cmd[1])):
                    pointer = nodes[pointer][0]
            else:
                for num in range(int(cmd[1])):
                    pointer = nodes[pointer][1]

        else:
            if cmd[0] == 'C':
                a,b=nodes[pointer]
                delete.append([pointer,a,b])
                
                if a == -1:
                    nodes[b][0] = a
                elif b == -1:
                    nodes[a][1] = b
                else:
                    nodes[a][1] = b
                    nodes[b][0] = a

                if b == -1:
                    pointer = a
                else:
                    pointer = b
                
            else:
                cur,prev,ne = delete.pop()
                if prev == -1:
                    nodes[ne][0] = cur
                elif ne == -1:
                    nodes[prev][1] = cur
                else:
                    nodes[prev][1] = cur
                    nodes[ne][0] = cur

    for cur,prev,ne in delete:
        answer[cur] = 'X'
    return ''.join(answer)