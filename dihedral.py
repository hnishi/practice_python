
# coding: utf-8

# In[2]:

import math
import numpy


# In[3]:

def dihedral_4(r1,r2,r3,r4):#四点が構成する二面角（0度が重なり、-180度、180度が最もずれ）
    r12,r23,r34 = [r2-r1,r3-r2,r4-r3]
    #print(numpy.cross(r23,r34))
    sin = numpy.dot(r12,numpy.cross(r23,r34)) * numpy.linalg.norm(r12)     / numpy.linalg.norm(numpy.cross(r12,r23)) / numpy.linalg.norm(numpy.cross(r23,r34))#torsion角tのsin
    #print(sin)
    cos = numpy.dot(numpy.cross(r12,r23),numpy.cross(r23,r34))     / numpy.linalg.norm(numpy.cross(r12,r23)) / numpy.linalg.norm(numpy.cross(r23,r34))#torsion角tのcos
    sign = sin / math.fabs(sin)#sinの符号
    t = sign * math.acos(cos)#torsion角t(rad)
    t = math.degrees(t)#t;rad->degree
    return t


# In[4]:

r1 = numpy.array([12.875,1.334,-17.762]) 
r2 = numpy.array([11.472,1.216,-15.718]) 
r3 = numpy.array([10.363,0.806,-14.818]) 
r4 = numpy.array([8.968,1.319,-15.257])

dih = dihedral_4(r1,r2,r3,r4)
#dih = 0
print(dih)


# In[66]:




# In[67]:

0*0


# In[67]:




# In[67]:




# In[67]:




# In[67]:




# In[ ]:



