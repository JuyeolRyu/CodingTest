############################################################################################
#1591. Strange Printer II                                                                  #
#https://leetcode.com/problems/strange-printer-ii/                                         #
############################################################################################
class Solution:
    def isPrintable(self, grid: List[List[int]]) -> bool:
        m,n = len(grid),len(grid[0])
        pos = [[m,n,0,0]for i in range(61)]
        #색들의 조합
        colors = set()
        for i in range(m):
            for j in range(n):
                #현재 그리디의 색 추출
                color = grid[i][j]
                colors.add(color)
                #색의 좌상단,우하단 좌표를 저장
                pos[color][0] = min(pos[color][0],i)
                pos[color][1] = min(pos[color][1],j)
                pos[color][2] = max(pos[color][2],i)
                pos[color][3] = max(pos[color][3],j)
        
        def isRect(color):
            #직사각형 범위 탐색
            for i in range(pos[color][0],pos[color][2]+1):
                for j in range(pos[color][1],pos[color][3]+1):
                    #0인경우 같은색으로 간주
                    if grid[i][j] != 0:
                        #직사각형의 색과 다를 경우 False 반환
                        if grid[i][j] != color:
                            return False
                    
            for i in range(pos[color][0],pos[color][2]+1):
                for j in range(pos[color][1],pos[color][3]+1):
                    #직사각형이 되는것을 확인했으므로 0으로 초기화
                    grid[i][j] = 0
            return True
        
        while colors:
            colors2 = set()
            for color in colors:
                #직사각형이 안되는 경우
                if not isRect(color):
                    colors2.add(color)
                
            #더이상 직사각형이 나오지 않는 경우
            if len(colors) == len(colors2):
                return False
            
            colors = colors2
            
        return True
                