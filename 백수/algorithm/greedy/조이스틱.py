def solution(name):
    ans = 0
    for n in name:
        ans += min(abs(ord(n)-ord('A')),abs(ord(n)-ord('Z'))+1)
    if 'A' not in name:
        ans += len(name)-1
    elif name == 'A'*len(name):
        return ans
    else:
        left,mid,right = 0,0,0
        for i,c in enumerate(reversed(name)):
            if c != 'A':
                right = len(name)-i-1
                break
        for i in range(1,len(name)):
            if  name[i] == 'A' and name[i-1] != 'A':
                left = i-1
                break
        for i in range(left+1,len(name)):
            if name[i] != 'A':
                mid = i
                break
        ans += min(right, left*2 + 1 + (len(name)-1-mid))
    return ans

'''javascript
function solution(name) {
    var ans = 0;
    var tmp = 'A'.repeat(name.length);
    for(var n of name){
        ans += Math.min(Math.abs(n.charCodeAt(0)-'A'.charCodeAt(0)), Math.abs(n.charCodeAt(0)-'Z'.charCodeAt(0))+1);
    }
    if(!name.includes('A'))
        ans += name.length-1
    else if(name === tmp)
        return ans
    else{
        var left=0;
        var mid=0;
        var right=0;
        for(var i=name.length-1;i>=0;i--){
            if(name[i] != 'A'){
                right = i
                break
            }
        }
        for(var i=1;i<name.length;i++){
            if(name[i] == 'A' && name[i-1] != 'A'){
                left = i-1
                break
            }
        }
        for(var i=left+1;i<name.length;i++){
            if(name[i] != 'A'){
                mid = i
                break
            }
        }
        ans += Math.min(right, left*2+1+(name.length-1-mid))
    }
    return ans;
}
'''