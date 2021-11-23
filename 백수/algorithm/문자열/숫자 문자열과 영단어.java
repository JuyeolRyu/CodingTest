import java.util.*;
class Solution {
    public int solution(String s) {
        String answer = "";
        Map<String,String> dic=new HashMap<String,String>();
        String[] wordArray=s.split("");
        String stack="";
        char c;

        dic.put("zero","0");
        dic.put("one","1");
        dic.put("two","2");
        dic.put("three","3");
        dic.put("four","4");
        dic.put("five","5");
        dic.put("six","6");
        dic.put("seven","7");
        dic.put("eight","8");
        dic.put("nine","9");
        Set<String> keys=dic.keySet();
        
        for(int i=0;i<s.length();i++){
            c=s.charAt(i);
            
            if(Character.isDigit(c)==true){
                answer+=c;
            }else{
                stack+=c;
                if(dic.containsKey(stack)){
                    answer+=dic.get(stack);
                    stack="";
                }
            }
        }
//         for(String c:wordArray){
//             if(Character.isDigit(c)==true){
//                 System.out.println(c);
//             }
            
//         }


        return Integer.valueOf(answer);
    }
}