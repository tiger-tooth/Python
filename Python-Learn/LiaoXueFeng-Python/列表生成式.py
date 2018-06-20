L=[x*x for x in range(1,12) if x%2==0]
print(L)

M=[m+n for m in 'ABC' for n in 'XYZ']
print(M)

import os
N=[d for d in os.listdir('.')]
print(N)