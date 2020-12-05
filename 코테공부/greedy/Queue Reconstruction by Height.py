################################################################################
#406. Queue Reconstruction by Height                                           #
#https://leetcode.com/problems/queue-reconstruction-by-height/                 #
################################################################################

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        #리스트를 정렬
        #key = lambda 배열 : 기준
        #첫번째 height를 기준으로 내림차순 정렬후 k를 기준으로 오름차순 정렬
        people = sorted(people,key = lambda people:(people[0]*-1, people[1]))
        #반복문 돌면서 k값에 대응되는 인덱스에 값을 삽입
        for person in people:
            ans.insert(person[1],person)
        
        return ans