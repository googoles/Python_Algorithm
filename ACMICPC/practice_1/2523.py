num = int(input())
new_num = num
for i in range(1,new_num+1):
    print('*'*i)
for k in range(1,num):
    print('*'*(new_num-k))
