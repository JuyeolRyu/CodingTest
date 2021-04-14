#https://programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    ans = [0]*len(prices)
    for idx in range(len(prices)):
        for j in range(idx+1,len(prices)):
            ans[idx] += 1
            if prices[idx] > prices[j]:
                break
    return ans