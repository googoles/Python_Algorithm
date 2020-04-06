a = ['č','ć','dž','đ','lj','nj','š','ž']
b = ['c=','c-','dz=','d-','lj','nj','s=','z=']
c = str(input())
for t in b:
    c = c.replace(t,'*')
print(len(c))