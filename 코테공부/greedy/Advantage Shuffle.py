############################################################################
#870. Advantage Shuffle                                                    #
#https://leetcode.com/problems/advantage-shuffle/                          #
############################################################################

#시간초과
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        #b[i]보다 큰 값 중 최솟값 찾기
        #b[i]보다 큰 값이 없으면 최솟값 삽입
        ans = []
        for b in B:
            tmp = []
            check = False
            
            if len(A) == 1:
                ans.append(A[-1])
                break
            for a in A:
                if a > b:
                    tmp.append(a)
                    check = True
            if not check:
                ans.append(min(A))
            else:
                ans.append(min(tmp))
            A.pop(A.index(ans[-1]))
        return ans

#
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        #A 정렬, B
        A = sorted(A)
        #B의 정렬된 인덱스 배열 생성
        idx = sorted(range(len(B)), key=lambda x:B[x], reverse=True)
        ans = [0 for _ in range(len(B))]
        
        tmp = []
        for a in A:
            #a값이 B의 최대값보다 클경우 ans 해당 인덱스에 추가
            #그 외의 경우 tmp에 저장
            if a>B[idx[-1]]:
                ans[idx.pop()] = a
            else:
                tmp.append(a)

        #두 변수 묶어주는 zip함수
        for b,a in zip(idx,tmp):
            ans[b] = a
        return ans