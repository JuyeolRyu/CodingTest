def solution(s):
    answer = []
    tuple_list = []

    for sub_s in s.split('}')[:-2]:
        num = ''
        nums = []
        for c in sub_s[2:]:
            if c.isdigit():
                num += c
            elif c == ',':
                nums.append(int(num))
                num = ''
        nums.append(int(num))
        tuple_list.append(nums)

    tuple_list = sorted(tuple_list, key=lambda x:(len(x)))
    for t in tuple_list:
        for num in t:
            if num not in answer:
                answer.append(num)
    return answer