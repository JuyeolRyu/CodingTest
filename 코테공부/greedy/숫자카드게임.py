#값입력 받기 및 수정
n, m = map(int,input.split())
arr = []
res_arr = []
for i in range(n):
    tmp = lit(map(int, input().split()))
    arr.append(tmp)

#sub_arr에서 가장 작은수 찾기
for sub_arr in arr:
    res_arr.append(min(sub_arr))

print(max(res_arr))
