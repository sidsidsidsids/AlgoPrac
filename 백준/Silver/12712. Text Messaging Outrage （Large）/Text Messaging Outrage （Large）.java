import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        for (int n = 0; n < N; n++) {
            st = new StringTokenizer(br.readLine());
            int P = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            int L = Integer.parseInt(st.nextToken());

            int[] records = new int[L];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < L; i++) {
                records[i] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(records);
            long answer = 0;
            int value = 1;
            int chk = K;
            int l = L - 1;
            while (l >= 0) {
                long record = records[l];
                answer += record * value;
                chk--;
                if (chk == 0) {
                    value++;
                    chk = K;
                }
                l--;
            }

            System.out.println("Case #" + (n + 1) + ": " + answer);
        }
    }
}
