> #!/usr/bin/python
> import numpy as np
> import matplotlib.pyplot as plt
> from random import randint, random
> 
> class Grid:
>       def __init__(self,n,p):
>               self.n=n
>               self.p=p
>               
>       def gr(self):
>               gr=np.zeros((self.n,self.n))
>               all=self.n*self.n
>               thresh=(self.p*all)/100
>               nr=0
>               #Ading new density counters untill threshold 
>               while nr<thresh:
>                       x=randint(0,self.n-1)
>                       y=randint(0,self.n-1)
>                       gr[x,y]=1
>                       nr=np.sum(gr)
>               return gr
> 
>       def perc(self,n,p):
>               ifis=0
>               n=self.n
>               p=self.p
>               x=Grid(n,p)
>               m=x.gr()
>               #Exchanging empty (0) blocks for 'path' (2) to start from it
>               for i in xrange(n):
>                       if m[0,i]==0:
>                               m[0,i]=2
>               tn=m.sum()
>               to=m.sum()-1    
>               #I am checking if from my 'path' cells there are free cells left, right, and downsite and marking them for every row
>               while tn!=to: #this line is checking condition if any new available free blocks found if percolation was not found
>                       to=m.sum()
>                       for i in range(n-1):
>                               for o in range(n):
>                                       if m[i,o]==2:
>                                               if o==0:
>                                                       if m[i+1,o]==0:
>                                                               m[i+1,o]=2
>                                                       if m[i,o+1]==0:
>                                                               m[i,o+1]=2
>                                               elif o==(n-1):
>                                                       if m[i+1,o]==0:
>                                                               m[i+1,o]=2
>                                                       if m[i,o-1]==0:
>                                                               m[i,o-1]=2              
>                                               else:
>                                                       if m[i+1,o]==0:
>                                                               m[i+1,o]=2
>                                                       if m[i,o-1]==0:
>                                                               m[i,o-1]=2      
>                                                       if m[i,o+1]==0:
>                                                               m[i,o+1]=2
>                       #if percolation accured, returns path and percolation (ifis 1 for percolation)                                  
>                       for u in xrange(n):
>                               if  m[n-1,u]==2:
>                                       ifis=1
>                                       return m, ifis  
>                               
>                       for i in reversed(xrange(n-1)):
>                               i+=1
>                               for o in reversed(xrange(n)):
>                                       if m[i,o]==2:
>                                               if o==0:
>                                                       if m[i-1,o]==0:
>                                                               m[i-1,o]=2
>                                                       if m[i,o+1]==0:
>                                                               m[i,o+1]=2
>                                               elif o==(n-1):
>                                                       if m[i-1,o]==0:
>                                                               m[i-1,o]=2
>                                                       if m[i,o-1]==0:
>                                                               m[i,o-1]=2              
>                                               else:
>                                                       if m[i-1,o]==0:
>                                                               m[i-1,o]=2
>                                                       if m[i,o-1]==0:
>                                                               m[i,o-1]=2      
>                                                       if m[i,o+1]==0:
>                                                               m[i,o+1]=2
>                       tn=m.sum()      
>               #after finding all possible connections, returns path and for no percolation 0  
>               return m, ifis          
>               
>       def image(self):
>               a=Grid(self.n,self.p)
>               pa=a.perc()
>               plt.imshow(pa[0])
>               plt.show()
>               
>       def pro(self):
>               n=self.n
>               p=self.p
>               p=[18]
>               pro=[]
>               for i in xrange(31):
>                       isper=0.0
>                       p.append(p[i]+2)
>                       num=randint(50,200)
>                       for o in xrange(num):
>                               a=Grid(n,p[i])
>                               x=a.perc(n,p[i])
>                               if x[1]==1:
>                                       isper+=1.0
>                       pro.append((isper/num)*100)                     
>                       print 'For density', p[i+1], '% and grid size', n, 'the probability of percolation is', pro[i], '%'
>               x=np.array(p)
>               y=np.array(pro)
>               x=np.delete(x,0)
>               return x,y
> 
> #calculating and plotting for given values
> #I think it would be good to assume that when percolation reaches 0 for some density value, it will be 0 for highter to safe calculation time
> r=[10,20,40,80]
> for i in r:
>       a=Grid(i,0)
>       u=a.pro()
>       plotting=plt.plot(u[0],u[1])
>       plt.show()
> 
> print 'Percolation threshold is between 40 and 50 percent'


#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from random import randint, random

class Grid:
	def __init__(self,n,p):
		self.n=n
		self.p=p
		
	def gr(self):
		gr=np.zeros((self.n,self.n))
		all=self.n*self.n
		thresh=(self.p*all)/100
		nr=0
		#Ading new density counters untill threshold 
		while nr<thresh:
			x=randint(0,self.n-1)
			y=randint(0,self.n-1)
			gr[x,y]=1
			nr=np.sum(gr)
		return gr

	def perc(self,n,p):
		ifis=0
		n=self.n
		p=self.p
		x=Grid(n,p)
		m=x.gr()
		#Exchanging empty (0) blocks for 'path' (2) to start from it
		for i in xrange(n):
			if m[0,i]==0:
				m[0,i]=2
		tn=m.sum()
		to=m.sum()-1	
		#I am checking if from my 'path' cells there are free cells left, right, and downsite and marking them for every row
		while tn!=to: #this line is checking condition if any new available free blocks found if percolation was not found
			to=m.sum()
			for i in range(n-1):
				for o in range(n):
					if m[i,o]==2:
						if o==0:
							if m[i+1,o]==0:
								m[i+1,o]=2
							if m[i,o+1]==0:
								m[i,o+1]=2
						elif o==(n-1):
							if m[i+1,o]==0:
								m[i+1,o]=2
							if m[i,o-1]==0:
								m[i,o-1]=2		
						else:
							if m[i+1,o]==0:
								m[i+1,o]=2
							if m[i,o-1]==0:
								m[i,o-1]=2	
							if m[i,o+1]==0:
								m[i,o+1]=2
			#if percolation accured, returns path and percolation (ifis 1 for percolation)					
			for u in xrange(n):
				if  m[n-1,u]==2:
					ifis=1
					return m, ifis	
				
			for i in reversed(xrange(n-1)):
				i+=1
				for o in reversed(xrange(n)):
					if m[i,o]==2:
						if o==0:
							if m[i-1,o]==0:
								m[i-1,o]=2
							if m[i,o+1]==0:
								m[i,o+1]=2
						elif o==(n-1):
							if m[i-1,o]==0:
								m[i-1,o]=2
							if m[i,o-1]==0:
								m[i,o-1]=2		
						else:
							if m[i-1,o]==0:
								m[i-1,o]=2
							if m[i,o-1]==0:
								m[i,o-1]=2	
							if m[i,o+1]==0:
								m[i,o+1]=2
			tn=m.sum()	
		#after finding all possible connections, returns path and for no percolation 0	
		return m, ifis		
		
	def image(self):
		a=Grid(self.n,self.p)
		pa=a.perc()
		plt.imshow(pa[0])
		plt.show()
		
	def pro(self):
		n=self.n
		p=self.p
		p=[18]
		pro=[]
		for i in xrange(31):
			isper=0.0
			p.append(p[i]+2)
			num=randint(50,200)
			for o in xrange(num):
				a=Grid(n,p[i])
				x=a.perc(n,p[i])
				if x[1]==1:
					isper+=1.0
			pro.append((isper/num)*100)			
			print 'For density', p[i+1], '% and grid size', n, 'the probability of percolation is', pro[i], '%'
		x=np.array(p)
		y=np.array(pro)
		x=np.delete(x,0)
		return x,y

#calculating and plotting for given values
#I think it would be good to assume that when percolation reaches 0 for some density value, it will be 0 for highter to safe calculation time
r=[10,20,40,80]
for i in r:
	a=Grid(i,0)
	u=a.pro()
	plotting=plt.plot(u[0],u[1])
	plt.show()

print 'Percolation threshold is between 40 and 50 percent'
