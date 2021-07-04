################################################################################
#763. Partition Labels                                                         #
#https://leetcode.com/problems/partition-labels/                               #
################################################################################

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ans = []
        char_list = [] #중복되는 단어 체크 하기 위한 리스트
        char_idx = 0   #리스트를 나눠야 할 기준 인덱스를 저장(계속 갱신된다)
        idx = 0        #반복문에서 현재 인덱스를 저장
        lenS = len(S)

        reverse_S = ''.join(reversed(S)) #문자열 뒤집기
        
        
        #find first char idx
        char = S[0]
        char_list.append(char)
        char_idx = lenS - 1 - reverse_S.index(char)
        
        #기준 인덱스 까지 반복문을 돌면서 다른 단어가 현재 기준 인덱스보다 뒤쪽에 더 있으면 큰값으로 갱신
        while(idx < char_idx):
            if(S[idx] not in char_list):
                char_list.append(S[idx])
                #find last index
                tmp_idx = lenS - reverse_S.index(S[idx])-1
                if(tmp_idx > char_idx):
                    char_idx = tmp_idx
            idx+=1
    
        #문자열의 마지막일 경우 길이를 반환
        #그 외의 경우 재귀함수를 돌면서 계속 탐색
        if(char_idx == lenS-1):
            return ans + [lenS]
        else:
            ans.append(char_idx+1)
            return ans + self.partitionLabels( S[char_idx+1 : ] )