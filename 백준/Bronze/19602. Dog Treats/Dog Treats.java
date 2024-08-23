import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        int S = Integer.parseInt(st.nextToken());
//        int M = Integer.parseInt(st.nextToken());
//        int L = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        int L = Integer.parseInt(br.readLine());
        System.out.println(solution(S, M, L));
    }

    public static String solution(int S, int M, int L) {
        String answer;
        if ((S + 2 * M + 3 * L) >= 10) {
            answer = "happy";
        } else {
            answer = "sad";
        }
        return answer;
    }
}
