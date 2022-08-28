import mylibrary.random as r
import matplotlib.pyplot as plt
def random_walk(n,seed1,seed2):
#taking two random number generator as a,b
  a = r.prng(n,seed1)
  b = r.prng(n,seed2)
  q=list()
  n= len(a)
  A=[]
  B=[]
  d=0.0
  #fixing intial coordinate (x1,y1)=(0,0)
  x1=0.0
  y1=0.0
  #for loop to continue the steps of the random walk
  for i in range(0,n-1):
    x=(2*a[i]-1)+x1
    A.append(x)
    y=(2*b[i+1]-1)+y1
    B.append(y)
    d+=((x-x1)**2+(y-y1)**2)
    x1=x
    y1=y
  
  rms= (d/n)**0.5
  dis=(x1**2+y1**2)**0.5
  output('Net displacement = '+str(dis))
  output('Net rms value = '+str(rms))
  plt.plot(A,B)
  plt.pause(1)
  plt.show()



#Function to write output to a file
def output(s):
    with open("C:\\Users\\manor\\Desktop\\P346 labs\\Assignment-1\\Output(Q3).txt",'a') as file:
        file.write(s)
        file.close()
    return

#Function to create a output file
with open("C:\\Users\\manor\\Desktop\\P346 labs\\Assignment-2\\Output(Q3).txt",'w') as file:

  file.write("OUTPUT : \n")
  file.close()  
  

random_walk(300,15,12)
random_walk(600,11,17)
random_walk(900,13,9)