##########################################################################################
#1029. Two City Scheduling                                                               #
#https://leetcode.com/problems/two-city-scheduling/                                      #
##########################################################################################

#combination으로 모든 조합 == 완전 탐색 ==> 실패
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        idx = [i for i in range(len(costs))]
        idx_sets = list(itertools.combinations(idx,len(costs)//2))
        ans = math.inf
        
        for idx_set in idx_sets:
            tmp = 0
            for index in range(len(costs)):
                if(index in idx_set):
                    tmp += costs[index][0]
                else:
                    tmp += costs[index][1]
            
            if(tmp < ans):
                ans = tmp
        return ans

#차이가 가장 큰 순서대로 나열해서 순서대로 작은 값을 먼저 넣어준다.
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        dif_set = []
        a_cnt = len(costs) // 2
        b_cnt = a_cnt
        
        for cost in costs:
            dif_set.append( [abs(cost[0] - cost[1]), costs.index(cost)] )
        
        dif_set = sorted(dif_set,key = lambda x : -x[0])
        
        for dif,idx in dif_set:
            min_num = min(costs[idx])
            max_num = max(costs[idx])
            if( costs[idx].index( min_num ) == 0 ):
                if(a_cnt > 0):
                    ans += min_num
                    a_cnt -= 1
                else:
                    ans += max_num
                    b_cnt -= 1
            else:
                if(b_cnt > 0):
                    ans += min_num
                    b_cnt -= 1
                else:
                    ans += max_num
                    a_cnt -= 1
        
        return ans