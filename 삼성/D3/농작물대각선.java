package D3;

import java.util.Scanner;

public class 농작물대각선 {

	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int tc = 1; tc <= T; tc++) {
            int N = sc.nextInt();
            int [][]arr = new int[N][N];
            int ans = 0;

            for(int i = 0; i < N; i++) {
                String str = sc.next();
                for(int j = 0; j < str.length(); j++) {
                    arr[i][j] = str.charAt(j) - '0';
                }
            }

            int range = N / 2;
            for(int i = 0; i < N; i ++) {
                for(int j = 0; j < N; j++) {
                    int sum = i + j;
                    int diff = i > j ? i - j: j - i;
                    if(sum >= range && // 왼쪽 위 자르기 
                        sum < N + range && // 오른쪽 아래 자르기
                        diff <= range) { // 왼쪽 아래 오른쪽 위 자르기
                        ans += arr[i][j];
                    }
                }
            }

            System.out.printf("#%d %d\n",tc, ans);
        }
    }

}
