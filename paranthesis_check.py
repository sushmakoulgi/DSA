

def is_valid(s):
    is_valid=False
    matching_list={
        "[":"]",
        "{":"}",
        "(":")"
    }
    print(matching_list.values())
    closint_list="}])"
    stack=[]
    for item in s:
        print(item)
        if item not in matching_list.values():
            print("adding item")
            stack.append(item)
        else:
            top_element=stack.pop()
            print("popping ",top_element,item)
            if matching_list[top_element]==item:
                continue
            else:
                return False

    return True

s="{{[])"
print(is_valid(s))
