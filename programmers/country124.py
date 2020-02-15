#country 124

oddnumbers = {'1' : '1', '2' : '2', '3' : '4',
           '4' : '11', '5' : '12', '6' : '14',
           '7' : '21', '8' : '22', '9' : '24',
           '10' : '41'}

n = list(map(str, input()))
print(n)
newnumber = []
for i in range(len(n)):
    if n[i] == oddnumbers['1']:
        newnumber += oddnumbers['1']
    elif n[i] == oddnumbers['2']:
        newnumber += oddnumbers['2']
    elif n[i] == oddnumbers['3']:
        newnumber += oddnumbers['3']
    elif n[i] == oddnumbers['4']:
        newnumber += oddnumbers['4']
    elif n[i] == oddnumbers['5']:
        newnumber += oddnumbers['5']
    elif n[i] == oddnumbers['6']:
        newnumber += oddnumbers['6']
    elif n[i] == oddnumbers['7']:
        newnumber += oddnumbers['7']
    elif n[i] == oddnumbers['8']:
        newnumber += oddnumbers['8']
    elif n[i] == oddnumbers['9']:
        newnumber += oddnumbers['9']
    elif n[i] == oddnumbers['10']:
        newnumber += oddnumbers['41']
    else n[i] 


print(newnumber)
# print(oddnumbers['3'])