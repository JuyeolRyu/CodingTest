def solution(lottos, win_nums):
    ans = []
    cnt = [0,0]
    dic = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    lottos.sort(reverse=True)
    
    for l in lottos:
        if l != 0 and l in win_nums:
            cnt[0]+=1
            cnt[1]+=1
            win_nums.remove(l)
        elif l == 0 and win_nums:
            cnt[1]+=1
            win_nums.pop(0)
    cnt = list(reversed(cnt))
    for c in cnt:
        ans.append(dic[c])
    return ans