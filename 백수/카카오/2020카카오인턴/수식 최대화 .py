from itertools import permutations
def solution(expression):
    answer = 0
    prios = ['*','+','-']
    num = ''
    exp = []
    for c in expression:
        if c.isdigit():
            num += c
        else:
            exp.append(num)
            exp.append(c)
            num = ''

    exp.append(num)

    
    for prio in list(map(list,permutations(prios))):
        tmp_exp = exp[:]
        for oper in prio:
            while oper in tmp_exp: 
                i = tmp_exp.index(oper)
                num = str(eval(tmp_exp.pop(i-1) + tmp_exp.pop(i-1) + tmp_exp.pop(i-1)))
                tmp_exp.insert(i-1,num)
        answer = max(answer,abs(int(tmp_exp[0])))

    return answer