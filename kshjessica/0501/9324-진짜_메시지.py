import sys

input = sys.stdin.readline

test_case = int(input())

for i in range(test_case):
    dic = {}
    message = input()

    for i in range(len(message)):
        if message[i] not in dic:
            dic[message[i]] = 1
        else:
            dic[message[i]] += 1
        
        if (dic[message[i]] == 3 and i != (len(message)-1)):
            if (message[i+1] != message[i]):
                print('FAKE')
                break
            else:
                dic[message[i]] =- 1

        if (dic[message[i]] == 3 and (i == len(message) - 1)):
            print('FAKE')
            break
        
        if (i == len(message)-1):
            print('OK')