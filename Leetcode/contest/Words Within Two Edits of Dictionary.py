queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]

res=[]
N=len(queries)
for query in queries:
            for word in dictionary:
                delta=0
                
                for i in range(N):
                    if query[i]!=word[i]:
                        delta+=1
                        
                if delta<=2:
                    res.append(query)
                    break
print(res)
# ans = []
        
# for query_word in queries:        
#             for dictionary_word in dictionary:
                
#                 edits = 0
#                 for letter1, letter2 in zip(query_word, dictionary_word):
                    
#                     if letter1 != letter2:
#                         edits += 1
                        
#                     if edits > 2:
#                         break
#                 else:
#                     ans.append(query_word) 
#                     break
        
# print(ans)


# res = []

# for q in range(len(queries)):
#     for d in range(len(dictionary)):
#                 c = 0
#                 for i in range(len(queries[q])):
#                     if queries[q][i] != dictionary[d][i]:
#                         c += 1
#                 if c <= 2:
#                     res.append(queries[q])
#                     break
# print(res)