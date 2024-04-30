import sys
input = sys.stdin.readline

#dict에 읽어들이는 문자 d[value]+=1
#if d[value]+=3, 다음 인덱스에 오는 애는 같은 문자여야함
#if not, 바로 FAKE.
# FAKE가 아니면 OK

num = int(input())

for i in range(num):
    d = {}
    s = input()
    for i in range(len(s)):
        if s[i] not in d: #딕셔너리에 키 없으면 추가
            d[s[i]]=1
        else:
            d[s[i]]+=1
        
        if (d[s[i]]==3 and i!=(len(s)-1)):
            if (s[i+1]!=s[i]): #글자가 한번 더 추가되지 않으면
                print('FAKE')
                break
            else: #한번 더 추가되면
                d[s[i]]=-1 #d[i] 초기화: -1로 해줘야함!(한 글자는 무조건 추가되어야함)
        if (d[s[i]]==3 and (i==len(s)-1)):
            print('FAKE')
            break
        if (i==len(s)-1): #마지막 글자인데 위의 예외조건에 안걸리면,
            print('OK') #진짜 메시지
