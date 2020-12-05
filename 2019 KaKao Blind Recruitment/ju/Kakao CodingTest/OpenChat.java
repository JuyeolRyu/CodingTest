import java.util.HashMap;

public class OpenChat {
    public String[] solution(String[] record) {
    	//���� �α��� ����, ���Դ� ������ ����, ����� ����
        int logCount = record.length;
        int ioCount = 0;
        int num = 0;
        //�ؽ� ��
        HashMap<String, String> hs = new HashMap<String, String>();

        for(int i=0; i<logCount;i++){			//������ ���� �� ���
            String[] tmp = spl(record[i]);      //�α׸� ��ūȭ

            if(tmp[0].equals("Enter")){         
                if(hs.containsKey(tmp[1])){     //�ٽ� ���� ���
                    hs.remove(tmp[1]);
                    hs.put(tmp[1],tmp[2]);
                }else{                          //ó�� ���� ���
                    hs.put(tmp[1],tmp[2]);
                }
                ioCount++;
            }else if(tmp[0].equals("Change")){  //�г��� ����
                hs.remove(tmp[1]);
                hs.put(tmp[1],tmp[2]);
            }else if(tmp[0].equals("Leave")){   //������ ���
                ioCount++;
            }

        }

        String[] answer = new String[ioCount];   //��� �Է� ����

        for(int i=0; i<logCount;i++){
            String[] tmp = spl(record[i]);

            if(tmp[0].equals("Enter"))           //���� ��� �ؽ�Ʈ
                answer[num++] = hs.get(tmp[1]) + "���� ���Խ��ϴ�.";
            else if(tmp[0].equals("Leave"))
                answer[num++] = hs.get(tmp[1]) + "���� �������ϴ�.";

        }
        return answer;
    }
    public String[] spl(String prev){            //split
        String[] result = prev.split(" ");
        return result;
    }
}