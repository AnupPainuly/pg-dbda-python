A={1,2,3,4,5}
B={4,5,6,7,8}
print(A,B)
print("union of A and B",A|B)
print("intersection of A and B",A&B)
print("difference of A and B",A-B)
print("symmetric_difference of A and B",A^B)
print("difference_update of A and B")
A=A-B
print(A)
print("symmetric_difference_update of A and B")
A={1,2,3,4,5}
B={4,5,6,7,8}
A=A^B
print(A)

A={10,20,30,40}
B={10,20}
print(A,B)
print("A.issuperset(B)",A.issuperset(B))
print("B.issubset(A)",B.issubset(A))

A={"a","b","c"}
B={1,2}
print(A.isdisjoint(B))








