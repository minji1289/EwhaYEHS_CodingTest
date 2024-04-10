import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] nm = br.readLine().split(" ");
        
        int n= Integer.parseInt(nm[0]);
        int m= Integer.parseInt(nm[1]);
        

        String[] arr = new String[n]; //키워드 개수 = 배열 크기
      
        boolean[] visited = new boolean[n]; //키워드 사용 여부 저장 (false로 자동 초기화됨)

        HashSet<String> set = new HashSet<>();
       
        for (int i=0; i<n; i++)
        {
            set.add(br.readLine());
        }
        //여기까지 HashSet에 키워드 저장하는 로직!

        for (int j=0; j<m; j++){
            String[] temp = br.readLine().split(",");
            for(String tmp: temp)
            {
                set.remove(tmp);
            }
            bw.write(set.size()+"\n");
            bw.flush();
            // System.out.println(set.size());
        }
    }

}
