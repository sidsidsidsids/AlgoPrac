import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer((br.readLine()));
        int N = Integer.parseInt(st.nextToken());
        int[][] arr = new int[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            arr[i][0] = w;
            arr[i][1] = h;
        }
        int[] ans = new int[N];

        for (int i = 0; i < N; i++) {
            int w = arr[i][0];
            int h = arr[i][1];
            int cnt = 1;
            for (int j = 0; j < N; j++) {
                if (i == j) {
                    continue;
                }
                if (w < arr[j][0] && h < arr[j][1]) {
                    cnt++;
                }
            }
            ans[i] = cnt;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(ans[i]);
            if (i < N - 1) {
                sb.append(" ");
            }
        }

        System.out.println(sb.toString());
    }
}