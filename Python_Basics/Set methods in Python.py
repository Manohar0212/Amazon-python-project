# add(Element)
# remove(Element)
# discard(Element)
# pop(Element)
# clear(Element)
#
# joining two sets
# union()
# update()
#
# Keep only duplicates
# intersection
# intersection_update
#
# Keep all excluding dupliates
# symetric_difference()
# symetric_differnce update()
#
# Returns set containing difference between two or more sets
# differnce()
# differnce_update()
#
# issubset()
# issuperset()
#
demo_set1={"Delhi","Kolkata","Mumbai","Lucknow","Kashmir","New york"}
demo_set2={"Delhi","Kolkata","Mumbai","Lucknow","Kashmir","New york", "Melborne","Sydney"}
# print(demo_set1)
# demo_set1.add("Bangalore")
# print(demo_set1)

# print(demo_set1)
# demo_set1.remove("Kolkata")
# print(demo_set1)

# print(demo_set1)
# demo_set1.discard("Delhi")
# print(demo_set1)

# print(demo_set1)
# demo_set1.pop()
# print(demo_set1)
# #
# print(demo_set1)
# demo_set1.clear()
# print(demo_set1)
#
# demo_set3= demo_set1.union(demo_set2)
# print(demo_set3)
# demo_set1.update(demo_set2)
# print(demo_set1)

# demo_set3= demo_set1.intersection(demo_set2)
# print(demo_set3)
# demo_set1.intersection_update(demo_set2)
# print(demo_set1)

# demo_set3= demo_set1.symmetric_difference(demo_set2)
# print(demo_set3)
# demo_set1.symmetric_difference_update(demo_set2)
# print(demo_set1)
#
# demo_set3= demo_set2.difference(demo_set1)
# print(demo_set3)
# demo_set1.difference_update(demo_set2)
# print(demo_set1)

demo_set3= demo_set1.issubset(demo_set2)
print(demo_set3)
demo_set3= demo_set2.issuperset(demo_set1)
print(demo_set3)
#
#
