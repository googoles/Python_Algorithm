num = int(input())
newnum = num

for i in range(1,num):
    print(' ' * (i-1) + '*' * ((2*(num-i)+1)))
for j in range(1, newnum+1):
    print(' '*(newnum-j) + '*'*(2*j-1))
