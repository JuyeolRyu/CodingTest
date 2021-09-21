from collections import defaultdict
def dfs(graph,node,answer,pay):
    if node == '-' or pay==0:
        return;
    tax = pay//10
    if tax != 0:
        answer[node] += (pay-tax)
    else:
        answer[node] += pay
    dfs(graph,graph[node],answer,tax)

    return;
def solution(enroll, referral, seller, amount):
    ans = []
    answer = defaultdict(int)
    graph = defaultdict(str)
    for node in enroll:
        answer[node]=0
    for idx,child in enumerate(referral):
        graph[enroll[idx]] = child

    for idx,node in enumerate(seller):
        pay = amount[idx]*100
        dfs(graph,node,answer,pay)

    return list(answer.values())