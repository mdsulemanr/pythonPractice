import itertools


def one_list(p):
    q=[]
    for i in (p):
        if isinstance(i, list):
            q.extend(one_list(i))
        else:
            q.append(i)
    return q


original_list = [[2,4,3,['a',['Alhumdulillah']]],[1,5,6], [9], [7,9,0],1,['a',['b',['c',['d']]]]]
print(one_list(original_list))
