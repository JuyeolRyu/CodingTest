from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    for i in range(len(orders)):
        orders[i] = sorted(list(orders[i]))
    
    for c in course:
        dic = defaultdict(int)
        for order in orders:
            if len(order) < c:
                continue
            for i in combinations(order,c):
                dic["".join(i)]+=1

        dic = sorted(dic.items(), key=lambda x:-x[1])
        
        if not dic or dic[0][1] == 1:
            continue
        max_num = dic[0][1]
        for d in dic:
            if d[1] == max_num:
                answer.append(d[0])
            else:
                break

    return sorted(answer)


'''javascript
function combinations(arr,num){
    const result = [];
    if(num === 1){
        return arr.map((v)=>[v])
    }
    arr.forEach((v,idx,arr)=> {
        const fixed = v;
        const restArr = arr.slice(idx+1);
        const combinationArr = combinations(restArr, num-1);
        const combineFix = combinationArr.map((v)=> [fixed, ...v]);
        result.push(...combineFix);
    });
    return result;
}
function solution(orders, course) {
    var answer = [];
    
    for(var i=0;i<orders.length;i++){
        orders[i] = orders[i].split("")
        orders[i].sort();
    }
    for(var c of course){
        var dic = {};
        
        for(var order of orders){
            if(order.length < c){
                continue;
            }
            for(var i of combinations(order,c)){
                var string = i.join("");
                if(string in dic){
                    dic[string]+=1;
                }else{
                    dic[string]=1;
                }
            }
        }
        var sorted_arr = [];
        for(var key in dic){
            sorted_arr.push([key,dic[key]]);
        }
        sorted_arr.sort((a,b)=>{
            return b[1]-a[1];
        })

        if(sorted_arr.length === 0 || sorted_arr[0][1] == 1){
            continue;
        }

        var max_num = sorted_arr[0][1];
        for(var x of sorted_arr){
            if(x[1] == max_num){
                answer.push(x[0]);
            }else{
                break;
            }
        }
    }
    answer.sort();
    return answer;
}
'''