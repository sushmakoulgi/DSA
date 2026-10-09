""" find the common characters in 2 strings
solution("aabcc","adcaa")"""

a1="aabcc"
a2="adcaa"

from collections import Counter

a1_counts=Counter(a1)
print(a1_counts)
a2_counts=Counter(a2)
print(a2_counts)

resul=[]
for key , value in a1_counts.items():
    if key in a2_counts.keys():
        min_count=min(a1_counts[key],a2_counts[key])
        for i in range(min_count):
            resul.append(key)


print(resul)