a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

A = set(a)
B = set(b)

print(A.difference(B))
print(A.union(B))
print(A.symmetric_difference(B))
print(A.intersection(B))