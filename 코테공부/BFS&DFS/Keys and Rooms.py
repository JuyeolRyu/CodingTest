############################################################################
#841. Keys and Rooms                                                       #
#https://leetcode.com/problems/keys-and-rooms/                             #
############################################################################

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #방문한 room 확인
        visited = [False for _ in range(len(rooms))]
        
        def dfs(idx):
            #현재 인덱스의 방 키를 저장
            #현재 room 방문처리
            room = rooms[idx]
            visited[idx] = True
            #빈방일 경우
            if not room:
                return;
            #방에 있는 키를 순차적으로 dfs
            for key in room:
                #키가 이미 갔던 방의 키이면 가지 않는다
                if visited[key]:
                    continue
                else:
                    dfs(key)
                
            return;
        #0번 방부터 탐색 시작
        dfs(0)
        #못간 방이 있으면 false
        if False in visited:
            return False
        return True