from collections import Counter

def is_subset(sub_list, main_list):
    """
    Return True if every element in sub_list appears in main_list
    with at least the same multiplicity (order doesn't matter).
    Requires elements to be hashable.
    """
    # Quick outs
    if not sub_list:
        return True
    if len(sub_list) > len(main_list):
        return False

    sub_counts = Counter(sub_list)
    main_counts = Counter(main_list)
    return all(main_counts.get(x, 0) >= cnt for x, cnt in sub_counts.items())


# Examples (correct argument order: is_subset(sub, main))
a = [2, 4, 3, 5, 7]
b = [4, -3]
c = [3, 7]
d = []
e = [2, 4, 7, 3, 5]
f = [2, 4, 7, 3, 5, 1]
g = ['apple', 'banana', 'orange']
h = ['apple']

print(is_subset(b, a))  # False  (-3 not in a)
print(is_subset(c, a))  # True
print(is_subset(d, a))  # True   (empty sub is always subset)
print(is_subset(e, a))  # True   (same multiset)
print(is_subset(f, a))  # False  (1 not in a)
print(is_subset(h, g))  # True
