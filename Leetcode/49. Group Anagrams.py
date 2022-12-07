strs = ["eat","tea","tan","ate","nat","bat"]



# dict = {}
#         #loop thru words in strs
# for word in strs:
#             #sort the word(all anagrams will be the same sorted)
#             key = tuple(sorted(word))
#             #if key exists, get existing words (as a list), add word to it, if not, create it
#             dict[key]=dict.get(key, []) +[word]
#         #return the values (which comes out as a list anyway)
# print(dict.values())


# strs_table = {}

# for string in strs:
#             sorted_string = ''.join(sorted(string))

#             if sorted_string not in strs_table:
#                 strs_table[sorted_string] = []

#             strs_table[sorted_string].append(string)

# print(list(strs_table.values()))


# hashmap = {}
# tmp = []

# for i in strs:
#     j = ''.join(sorted(i))
#     if j in hashmap:
#         hashmap[j].append(i)
#     else:
#         hashmap[j]=[i]

# for i in hashmap:
#             tmp.append(hashmap[i])
# print(tmp)

