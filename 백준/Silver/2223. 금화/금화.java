import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Monster {
    int d, s;

    Monster(int d, int s) {
        this.d = d;
        this.s = s;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Monster[] monsters = new Monster[m];
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            monsters[i] = new Monster(d, s);
        }

        int maxima = t + 1;
        for(Monster mon : monsters){
            int d = mon.d;
            int s = mon.s;
            int divisor = Math.floorDiv(d, s);
            if (d % s == 0){
                divisor -= 1;
            }
            maxima = Math.min(maxima, divisor);
        }
        if (maxima >= t | m == 0) {
            System.out.println(t * x);
        } else if (maxima == 0) {
            System.out.println(0);
        } else {
            int r = Math.floorDiv(t - maxima, 2);
            System.out.println((maxima + r) * x);
        }
        }
    }
