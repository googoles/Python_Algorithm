#U => 9
#N => 7
#U => 9
#C => 3
#I => 5
# C=> 3

#ABC => 3
#DEF 4
#GHI 5
#JKL 6
#MNO 7
#PQRS 8
#TUV 9
#WXYZ 10

# a = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# import sys
# a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# b = sys.stdin.readline()
# cnt = 0
# for i in range(b):
#     if b[i] == a[:2]:
#         cnt += 3
#     if b[i] == a[3:5]:
#         cnt += 4
w = input()
a = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
t = 0
for i in range(len(w)):
    for j in a:
        if(w[i] in j):
            t += a.index(j) + 3

# [ t += a.index(j) + 3 if (w[i] in j) for j in a for i in range(len(w))]

print(t)
