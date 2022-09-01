'''
https://www.codechef.com/submit/DIET
'''
T = int(input())
for _ in range(T):
    n, quantity = [int(x) for x in input().split()]
    in_list = [int(x) for x in input().split()]
    balance = 0
    flag = True
    for i in range(len(in_list)):
        if in_list[i]+balance < quantity:
            print('NO',i+1)
            flag = False
            break
        else:
            balance += in_list[i] - quantity
            
    if flag:
        print('YES')