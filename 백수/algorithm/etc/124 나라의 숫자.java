class Solution {
    public String solution(int n) {
        String answer = "";
        String[] s = {"4","1","2"};
        while(n>0){
            int mod=n%3;
            n/=3;
            answer = s[mod]+answer;
            if(mod==0){
                n-=1;
            }
        }
        return answer;
    }
}