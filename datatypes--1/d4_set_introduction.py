# set {}
# set has no index function--3
# tuples are faster than list and consume less memory.

# set1 = {<immutable1>,<immutable2>,<immutable3>,<immutable14>,}
# empty_set2 = set()----------- empty set
# new_set1 = ([<immutable1>,<immutable2>,<immutable3>,<immutable14>])

set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9}
print("set1 =", set1)
print("set2 =", set2)

# # add = add element at given sequence
set1.add(11)
set1.add(21)
set1.add(31)
set1.add(41)
print("set1 after addition of element",set1)

# # remove ------remove fix element use remove (gives error if assign element is not present i.e set1.remove(123) )
set1.remove(11)
set1.remove(21)
set1.remove(31)
print("set1 after remove=", set1)

# # discard = discard the given element form set (do not give error if assign element is not present)
set1.discard(41)
print("*****", set1)

# # pop ----------- remove any random element then use pop and pop define element which was pop
# d = set1.pop()
# print("set1 after pop=", set1)
# print("pop element=", d)        # this line show which element was remove.
#
# # clear = remove all element i.e clear the set.
# set1.clear()
# print("clear set1 =", set1)

# set operation--2 --- above codes are comments for next set operation--2

# union = gives union of the given two set.
union_set = set1.union(set2)
print("union set =", union_set)

# intersection = gives common element of given set.
intersection_set = set1.intersection(set2)
print("intersection of set1 and set2 =", intersection_set)

# intersection_update = set1.intersection_update(set2)
# print('intersection update =', intersection_update)

# difference
diffa_b = set1.difference(set2)
print("a-b =", diffa_b)

diffb_a = set2.difference(set1)
print("b-a =", diffb_a)

# symmetric difference  = union of a-b and b-a     -- {(s1 u s2)- (s1 n s2)}
symm_diff = set1.symmetric_difference(set2)
print("symmetric differnce =", symm_diff)

symm_diffupdate = set1.symmetric_difference_update(set2)
print("symm diff update =", symm_diffupdate)

# issubset(set) = return true if given set is subset of passed set
# issuperset(set) = return true if given set is superset of passed set

st1 = {1, 2, 3}
print(st1.issubset(set1))
st2 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
print(st2.issuperset(set2))

# disjoint = to know both set is differ than each other i.e no common element
print(set1.isdisjoint(set2))

set3 = {1, 2, 3, 4}
print(set2.isdisjoint(set3))
