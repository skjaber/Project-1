#Python List Comprehension

squares = [x**2 for x in range(5)]
print(squares)


listn= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
evenlist = [x for x in listn if x%2==0]
print(evenlist)

l2=list(range(1,20))
evenlist2 = [x for x in l2 if x%2==0]
print(evenlist2)
