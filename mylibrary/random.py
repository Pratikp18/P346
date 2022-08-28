import math

def prng(n, seed):
  a= 1103515245
  c= 12345
  m = 32768
  x= seed
  X=[]
  for i in range(1,n):
    x=(a*x+c)%m
    x = x/m
    X.append(x)
  return X