import numpy as np 
import math

#inner product is integral from 0,1 of f*g
def innerprod(x,y):
	f = np.polymul(x,y)
	f = np.polyint(f)
	return np.polyval(f, 1) - np.polyval(f, 0)

#projection of y onto x
def proj(x,y):
	n = np.poly1d([innerprod(y,x)/innerprod(x,x)])
	return np.polymul(x,n)

#gram schmidt process on a basis
def gram_schmidt(basis):
	x = []
	for i in range(len(basis)):
		tmp = basis[i]
		for j in x:
			proj_vec = proj(j, basis[i])
			tmp = np.polyadd(tmp, np.polymul(proj_vec, [-1]))
		x.append(tmp)
	return x

def normalize(x):
	for i in range(len(x)):
		norm = 1/math.sqrt(innerprod(x[i],x[i]))
		x[i] = np.polymul(x[i], [norm])

x = (gram_schmidt([[1],[1,0], [1,0,0],[1,0,0,0]]))

normalize(x)

print(x)
