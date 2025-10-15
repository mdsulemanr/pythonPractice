# Define a procedure, deep_reverse, that takes as input a list,
# and returns a new list that is the deep reverse of the input list.
# This means it reverses all the elements in the list, and if any
# of those elements are lists themselves, reverses all the elements
# in the inner list, all the way down.

# Note: The procedure must not change the input list.

# The procedure is_list below returns True if
# p is a list and False if it is not.

def deep_reverse(parameter):
    if not isinstance(parameter, list):
        raise TypeError("Input must be a list")

    result = []
    for i in reversed(parameter):
        result.append(deep_reverse(i) if isinstance(i, list) else i)
    return result

#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print (deep_reverse(p))
#>>> [[[[6, 5], 4], 3, 2], 1]
print (p)
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print (deep_reverse(q))
#>>> [ [6,5], 4, [3, 2], 1]
print (q)
#>>> [1, [2,3], 4, [5,6]]

r =  [1, 2, 3, 4]
print (deep_reverse(r))
#>>> [4, 3, 2, 1]
print(r)