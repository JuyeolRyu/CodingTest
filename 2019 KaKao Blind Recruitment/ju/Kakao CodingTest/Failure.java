class Solution {
    public int[] solution(int N, int[] stages) {
    	//���п� index����,������ ������ ����
        int[] answer = new int[N];
        double[] answerVal = new double[N];
        int stageLen = stages.length;
        int index = 0;

        for(int i=1;i<=N;i++){
        	//�ش� �������� ����or������ ����� ��, �������� ����� ��
            int manCount = 0;
            int failCount = 0;
            
            for(int j=0;j<stageLen;j++){
                if(stages[j] >= i){
                    manCount++;
                    if(stages[j] == i){
                        failCount++;
                    }
                }
            }
            double result = (double)failCount/manCount; //������ ����
            //�ϴ� �׳� ������� ���� �־��ش�.
            answer[index] = i;
            answerVal[index++] = result;
        }

        //selection sort ����ؼ� ����ū���� �տ� ������ ���� ���� ��� index �������� �տ� �����Ѵ�.
        for(int i=0; i<index-1; i++){
            int maxIndex = i;

            for(int j=i+1; j<index; j++){
                if(answerVal[j] > answerVal[maxIndex])       //�������� �� ���� ���
                    maxIndex = j;
                else if(answerVal[j] == answerVal[maxIndex]){//�������� ���� ���
                     if(answer[j] < answer[maxIndex])		 //�������� ���� �ε����� ���� ��� �ٲ���
                         maxIndex = j;
                }
            }
            swap(answer,maxIndex,i);
            swap(answerVal,maxIndex,i);    //����
        }

        return answer;
    }
    //���� �޼ҵ�
    int[] swap(int[] arr,int a,int b){
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
        return arr;
    }
    double[] swap(double[] arr,int a,int b){
        double tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
        return arr;
    }
}