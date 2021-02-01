################################################################################
#1657. Determine if Two Strings Are Close                                      #
#https://leetcode.com/problems/determine-if-two-strings-are-close/             #
################################################################################

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #문자열들을 set으로 만들어 준다.
        set1 = set(word1)
        set2 = set(word2)
        list1 = []
        list2 = []
        #두개의 문자열의 요소들이 같은지 확인한다.
        #다르면 같은 문자열로 바꿀수 없으므로 False
        for word in set1:
            if word not in set2:
                return False
            
        #각 단어의 개수를 전부 센다
        for word in set1:
            list1.append(word1.count(word))
            
        for word in set2:
            list2.append(word2.count(word))
        
        #단어의 개수 정렬
        list1 = sorted(list1)
        list2 = sorted(list2)
        #단어의 개수가 하나라도 다르면 False
        for num in list1:
            if list1 != list2:
                return False
            
        return True