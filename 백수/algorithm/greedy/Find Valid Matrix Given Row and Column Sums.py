class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans = []
        row_len = len(rowSum)
        col_len = len(colSum)
        r_idx , c_idx = 0,0
        for i in range(len(rowSum)):
            tmp = []
            for j in range(len(colSum)):
                tmp.append(0)
            ans.append(tmp)
            
        #작은수 먼저 채우고 나머지 채우면서 idx 올리기
        while(r_idx < row_len and c_idx < col_len):
            min_num = min(rowSum[r_idx] , colSum[c_idx])
            ans[r_idx][c_idx] = min_num
            
            rowSum[r_idx] -= min_num
            colSum[c_idx] -= min_num
            
            if(rowSum[r_idx] == 0):
                r_idx += 1
            
            if(colSum[c_idx] == 0):
                c_idx += 1
                
        return ans