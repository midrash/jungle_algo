import java.util.Scanner;
import java.lang.Math;

public class Main {
	public static int answer=0;
	public static int[] arr;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		arr = new int[N];
		dps(0,N);
		System.out.println(answer);
	}
	
	public static void dps(int depth,int n) {
		if(depth == n) {
			answer++;
			return;
		}
		for (int i = 0; i < n; i++) {
			arr[depth] = i;
			if (cando(depth)) {
				dps(depth+1,n);
			}
		}
		
	}
	public static boolean cando(int depth) {
		for (int i = 0; i < depth; i++) {
			if (arr[depth] == arr[i]) {
				return false;
			}
			else if (Math.abs(depth - i)==Math.abs(arr[depth]-arr[i])) {
				return false;
			}
		}
		
		
		return true;
	}

}