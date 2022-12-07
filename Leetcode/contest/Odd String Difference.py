from collections import defaultdict
words = ["adc","wzy","abc"]

hashmap = defaultdict(list)
hashmap = {}
for w in words:
            difference = []
            for i in range(1,len(w)):
                difference.append(ord(w[i])-ord(w[i-1]))
            for i in difference:
                hashmap[i].append(w)
            # hashmap[tuple(difference)].append(w)
            # hashmap[difference].append((w))
for k,a in hashmap.items():
            if len(a) == 1:
                print(a[0])