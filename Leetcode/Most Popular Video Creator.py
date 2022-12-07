from collections import defaultdict

creators = ["alice","bob","alice","chris"]
ids = ["one","two","three","four"]
views = [5,10,5,4]
hmap=defaultdict(list)

hmap_view=defaultdict(int)
n=len(ids)
for i in range(n):
            hmap[creators[i]].append([ids[i],views[i]])
            hmap_view[creators[i]]+=views[i]
c=[]
mx=max(hmap_view.values())
for i,j in hmap_view.items():
            if j==mx:
                c.append(i)
ans=[]
for cr in c:
            tmp=[cr]
            tmp.append(sorted(hmap[cr],key=lambda x:(-x[1],x[0]))[0][0])
            ans.append(tmp)
print(ans)

# hashmap = {}

# Output: [["alice","one"],["bob","two"]]

# for i,j,k in zip(creators,ids,views):
#     if i not in hashmap:
#         hashmap[i].append[([j,k])]
# print(hashmap)































# d = collections.defaultdict(dict)
# c = collections.defaultdict(int)
# res = list()
        
# for i in range(len(creators)):
#             d[creators[i]][ids[i]] = views[i]
                
# for i in range(len(creators)):
#             c[creators[i]] += views[i]
            
# max_viewers= max(c.values())
# max_creators = [k for k, v in c.items() if v == max_viewers]
        
# for creator in max_creators:
#             t = [creator]
            
#             max_v = max(d[creator].values())
#             t.append(min([k for k, v in d[creator].items() if v == max_v]))

#             res.append(t)

# print(res)