# """Example:
# Input: nums = [1,1,1,2,2,3], k = 2 → Output: [1, 2] 
# (1 appears 3 times, 2 appears twice, 3 appears once — 
# the top 2 most frequent are 1 and 2)
# """
# from collections import defaultdict,Counter

# def top_k_frequent(nums: list, k: int):
#     result=defaultdict(list)
#     for item in nums:
#         result[item].append(item)

#     final=defaultdict(list)
#     for key, value in result.items():
#         final[len(value)].append(key)

#     top=sorted(final.keys(),reverse=True)[:k]
#     print(top)
#     l=[]
#     for item in top:
#         for key in final[item]:
#            l.append(key)
#     print(l[:k])
#     return l[:k]


# counters=Counter([1,1,2,2,3,3,4])
# print(counters)
# result=defaultdict(list)
# for key,value in counters.items():
#     result[value].append(key)
# print(result)
# sorted_length=sorted(result.keys(),reverse=True)
# output=[]
# for item in sorted_length:
#     output.append(result[item])
# print(output)
# print(output[:2])
# #top_k_frequent([1,1,2,2,3,3,4],2)


from collections import Counter,defaultdict
nums = [1,1,1,2,2,3]
k=2

num_counts=Counter(nums)


counter_dict=defaultdict(list)
for key, value in num_counts.items():
    counter_dict[value].append(key)


sortedkeys=sorted(counter_dict.keys(),reverse=True)[:k]
print(sortedkeys)
result=[]
for key in sortedkeys:
    print(counter_dict[key])
    result.append(counter_dict[key])

print(result)
