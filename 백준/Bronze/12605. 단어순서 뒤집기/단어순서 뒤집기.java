import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int N = Integer.parseInt(scanner.nextLine());
        
        for (int i = 1; i <= N; i++) {
            String line = scanner.nextLine();
            String[] words = line.split(" ");
            
            System.out.print("Case #" + i + ": ");
            
            for (int j = words.length - 1; j >= 0; j--) {
                System.out.print(words[j]);
                if (j != 0) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
        scanner.close();
    }
}
