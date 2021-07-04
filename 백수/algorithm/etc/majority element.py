from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num]+=1
        dic = sorted(dic.items(), key=lambda x:x[1],reverse=True)
        return dic[0][0]