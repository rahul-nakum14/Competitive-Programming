tmp=[]
for i in range(0, int(input())):
    j = input().split()
    m=0
    
    if j.count('1') >= 2:
        m+=1
        tmp.append(m)
print(sum(tmp))