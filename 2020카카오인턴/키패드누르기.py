from collections import deque

def solution(numbers, hand):
    ans = ''
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left_start = [3, 0]
    right_start = [3, 2]

    def bfs(row, col, target):
        visited = [[False for _ in range(3)] for i in range(4)]
        queue = deque()
        queue.append([row, col])
        visited[row][col] = True
        cnt = 0
        while queue:
            tmp_queue = deque()

            while queue:
                c_row, c_col = queue.popleft()
                if grid[c_row][c_col] == target:
                    return cnt,[c_row,c_col]

                d_row = [-1, 1, 0, 0]
                d_col = [0, 0, -1, 1]

                for i in range(4):
                    n_row = c_row + d_row[i]
                    n_col = c_col + d_col[i]
                    if 0 <= n_row < 4 and 0 <= n_col < 3 and not visited[n_row][n_col]:
                        tmp_queue.append([n_row, n_col])

            queue = tmp_queue
            cnt += 1

    for number in numbers:
        if number in [1,4,7]:
            ans += 'L'
            left_start = [number//3,0]
        elif number in [3,6,9]:
            ans += 'R'
            right_start = [number//3-1,2]
        else:
            left,tmp_left = bfs(left_start[0],left_start[1],number)
            right,tmp_right = bfs(right_start[0],right_start[1],number)

            if left > right:
                ans += 'R'
                right_start = tmp_right
            elif left < right:
                ans += 'L'
                left_start = tmp_left
            elif left == right:
                if hand == 'left':
                    ans += 'L'
                    left_start = tmp_left
                else:
                    ans += 'R'
                    right_start = tmp_right
        
    return ans