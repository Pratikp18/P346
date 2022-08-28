import mylibrary.random as r
a = r.prng(10000000,0)
q=list()
n= len(a)
for i in range(0,n-2):
  x=a[i]
  y=a[i+1]
  z=a[i+2]
  v=(x**2+y**2+z**2)**0.5
  if v<1 :
    q.append(v)

volume= len(q)/n
#Function to write output to a file
def output(s):
  with open("C:\\Users\\manor\\Desktop\\P346 codes\\Assignment-2\\Output(Q2).txt",'a') as file:
    file.write(s)
    file.close()
  return

#Function to create a output file
with open("Users\\pratikpatra\\Desktop\\p346 lab\\assignment 2\\Output(Q2).txt",'w') as file:
    file.write("OUTPUT : \n")
    file.close()
output('The volume of the first octant is : '+str(volume))
