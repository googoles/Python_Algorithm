# a = ['a','b','c']
import time
start = time.time()

import sys
st = list(map(str, sys.stdin.readline().split()))
cnt = 0
# save = []
# st.sort()
print(st)
for i in range(len(st)):
    if st[i] == st[i-1]:
        continue
    else:
        cnt += 1
print(cnt)
# for i in range(len(st)):
#     print(st)
    # if st[i] in st[:i]:
    #     continue
    # else:
    #     cnt += 1
# print(cnt)
#         # save.append(st[i])
# # print(len(save))
# print(cnt)

print("time :", time.time() - start)
