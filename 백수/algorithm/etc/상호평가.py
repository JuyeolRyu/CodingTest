def solution(scores):
    answer = ''
    for c in range(len(scores[0])):
        tmp = []
        for r in range(len(scores)):
            tmp.append([scores[r][c],r])
            
        tmp.sort(key=lambda x:x[0])
        if tmp[0][1] == c and tmp[0][0] != tmp[1][0]:
            tmp.pop(0)
        elif tmp[-1][1] == c and tmp[-1][0] != tmp[-2][0]:
            tmp.pop(-1)
        s = 0
        for i in range(len(tmp)):
            s+=tmp[i][0]
        avg = s//len(tmp)
        
        if avg>=90:
            answer+='A'
        elif avg>=80:
            answer+='B'
        elif avg>=70:
            answer+='C'
        elif avg>=50:
            answer+='D'
        else:
            answer+='F'
    return answer

'''javascript
function solution(scores) {
    var answer = '';
    for(var c=0;c<scores.length;c++){
        var tmp = [];
        for(var r=0;r<scores.length;r++){
            tmp.push([scores[r][c],r]);
        }
        tmp.sort((a,b,c) => {
            return a[0]-b[0];
        });
        
        if(tmp[0][1] === c && tmp[0][0]!=tmp[1][0]){
            tmp.shift()
        }else if(tmp[tmp.length-1][1] === c && tmp[tmp.length-1][0]!=tmp[tmp.length-2][0]){
            tmp.pop()
        }
        var sum = 0;
        for(var i=0;i<tmp.length;i++){
            sum += tmp[i][0];
        }
        var avg = sum/tmp.length;
        if(avg>=90)
            answer+='A'
        else if(avg>=80)
            answer+='B'
        else if( avg>=70)
            answer+='C'
        else if( avg>=50)
            answer+='D'
        else
            answer+='F'
    }
    return answer;
}
'''