def sockMerchant(n, ar):


    set_sock = set(ar)
    set_sock = list(set_sock)
    # for i in range(n):
    count = 0
    # print(set_sock)

    for i in range(len(set_sock)):
        pair_socks = ar.count(set_sock[i])
        a = pair_socks // 2
        count += a

    return count









n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n,ar))
'''
9
10 20 20 10 10 30 50 10 20


3
'''