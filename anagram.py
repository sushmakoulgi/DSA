""" Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]] """


from collections import defaultdict

input_array=["eat", "tea", "tan", "ate", "nat", "bat"]

result=defaultdict(list)
for item in input_array:
    print(item)
    sorted_item="".join(sorted(item))
    print(sorted_item,item)
    result[sorted_item].append(item)

final_array=[]
for key in result.keys():
    final_array.append(result[key])

print(list(result.values()))

