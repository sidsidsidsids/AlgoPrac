import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer((br.readLine()));
        int A = Integer.parseInt(st.nextToken());
        int result = 0;
        for (int i = 0; i < 7; i++) {
            if((A&(1<<i)) > 0) result++;
        }
        System.out.println(result);
    }
}