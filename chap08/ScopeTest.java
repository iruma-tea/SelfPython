package chap08;

public class ScopeTest {
    public static void main(String[] args) {
        if (true) {
            int i = 13;
            System.out.println(i);
        }
        // System.out.println(i); // エラー
    }
}