A = "abb"
B = "baz"

z="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

score=0
for i,j in zip(A,B):
        ii=z.index(i)
        jj=z.index(j)
        x=(z[ii::])
        x.index(j)
        y=(z[jj::]).index(i)
        # t=score
        if abs(score+x)<abs(score-y):
            score=score+x
        else:
            score=score-y
        # print(x,y,score)
print(abs(score))
# count = 0 

# for i in range(len(a)):
