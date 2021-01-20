from itertools import combinations
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return round(nums[0],4) == 24
        #print(list(enumerate(nums)))
        else:
            for (i, m),(j, n) in combinations(enumerate(nums), 2):
                new_nums = [x for t, x in enumerate(nums) if i != t != j]
                lst = [m+n,m*n,abs(m-n)]
                if m != 0:
                    lst.append(n/m)
                if n != 0:
                    lst.append(m/n)

                for x in lst:
                    if self.judgePoint24(new_nums +[x]):
                        return True
                #print(new_nums,m,n)
            return False