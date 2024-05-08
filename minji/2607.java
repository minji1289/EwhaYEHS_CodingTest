import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        HashMap<String, Integer> map = new HashMap<>();

        int count = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine()); //br.readLine() -> 기본적으로 string 타입으로 입력받는 메소드
        String s = br.readLine();

        //s를 HashMap에 넣는 과정
        for (int i=0; i<s.length(); i++)
            {
            if (!map.containsKey(String.valueOf(s.charAt(i))))
            {
                map.put(String.valueOf(s.charAt(i)), 1);
            }
            else
            {
                int value = map.get(String.valueOf(s.charAt(i))) + 1;
                map.replace(String.valueOf(s.charAt(i)), value);
            }
        }

        //1. 하나의 문자를 더하기
        //2. 하나의 문자를 빼기
        //3. 하나의 문자를 바꾸기

        HashMap<String, Integer> temp = new HashMap<>();
        for (int j=0; j<n-1; j++)
        {
            //두번째 단어 이후 각 단어 temp Map에 저장하는 과정
            String str = br.readLine();
            for (int i=0; i<str.length(); i++)
            {
                if (!temp.containsKey(String.valueOf(str.charAt(i))))
                {
                    temp.put(String.valueOf(str.charAt(i)), 1);
                }
                else
                {
                    int value = temp.get(String.valueOf(str.charAt(i))) + 1;
                    temp.replace(String.valueOf(str.charAt(i)), value);
                }
            }

            //s와 temp 비교
            for (int i=0; i<s.length(); i++)
            {
              //s와 temp가 같으면 ㄱㅊ
              if (temp.containsKey(String.valueOf(s.charAt(i))) && (temp.get(String.valueOf(s.charAt(i)))==map.get(String.valueOf(s.charAt(i)))))
              {
                continue;
              }
              else{ //다르면
                //한 단어 더하거나 빼서 같거나
                if (temp.containsKey(String.valueOf(s.charAt(i))) && ((temp.get(String.valueOf(s.charAt(i)))-map.get(String.valueOf(s.charAt(i))))==-1 || (temp.get(String.valueOf(s.charAt(i)))-map.get(String.valueOf(s.charAt(i))))==1))
                {count++;
                  break;}
                //한 단어 바꾸거나..
                else if(!(!temp.containsKey(String.valueOf(s.charAt(i))) && map.get(String.valueOf(s.charAt(i)))>1)) 
                {count++;
                  break;}
                else
                  continue;
              }
            }
        }
      System.out.println(count);

    }
}
