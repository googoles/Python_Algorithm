import sys

num = int(input())
check = num
new_num = 0
temp = 0
count = 0

while True:
    temp = num//10 + num%10
    new_num = (num%10)*10 + temp%10
    count += 1
    num = new_num
    if new_num == check:
        break
print(count)

    # 10보다 작다면? 9 => 09 => 99 => 9 + 9 => 18 => 98 => 9 + 8 => 17 -> 87
    # if 26 => 2 + 6 => 8 => 68, 6 + 8 => 14 => 84, 8 + 4 => 12 => 42,  4 + 2 = 6 => 26
