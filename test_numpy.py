import numpy as np

a = np.array([1,2,3,4,5])
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b)

c = np.zeros((2,3), np.uint8)
print(c)

d = np.ones((2,3), np.uint8)
print(d)

e = np.full((2,3), 5)
print(e)

f = np.eye(3, 5, 2, np.uint8)
print(f)

g = np.random.random((6,8))
print(g)
print(g[5,6])