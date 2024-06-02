import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer((br.readLine()));
        int N = Integer.parseInt(st.nextToken());
        long[] arr = new long[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }
        Arrays.sort(arr);
        int result = 0;
        for (int t = 0; t < N; t++) {
            long num = arr[t];
            int i = 0, j = N - 1;

            while (i < j) {
                if (arr[i] + arr[j] == num) {
                    if (i != t && j != t) {
                        result++;
                        break;
                    }
                    else if (i == t) {
                        i++;
                    }
                    else if (j == t) {
                        j--;
                    }
                } else if (arr[i] + arr[j] < num) {
                    i++;
                }
                else {
                    j--;
                }
            }
        }
        System.out.println(result);
    }
}