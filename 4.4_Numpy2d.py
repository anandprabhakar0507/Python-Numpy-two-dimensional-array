
# coding: utf-8

#  <a href="http://cocl.us/topNotebooksPython101Coursera"><img src = "https://ibm.box.com/shared/static/yfe6h4az47ktg2mm9h05wby2n7e8kei3.png" width = 750, align = "center"></a>
# 
# 

# <a href="https://www.bigdatauniversity.com"><img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 300, align = "center"></a>
# 
# 
# 
# <h1 align=center><font size = 5>numpy in Python</font></h1>

# In[4]:


import numpy as np 
import matplotlib.pyplot as plt


#  Consider the list **a **, the list contains three nested lists **each of equal size**. 

# In[37]:

a=[[11,12,13],[21,22,23],[31,32,33]]
a


#  We can cast the list to a numpy array  as follow

# In[38]:

#every elment if of the same type 
A=np.array(a)
A


# We can use the attribute **ndim** to obtain the number of axes or dimensions referred to as the rank. 

# In[10]:

A.ndim


#  Attribute **shape** returns a tuple corresponding to the size or number of each dimension.

# In[11]:

A.shape


# The total number of elements in the array is given by the attribute **size**.

# In[12]:

A.size


# ### Accessing different elements of an Numpy Array 

#  We can use rectangular brackets to access the different elements of the array,The correspondence  between the rectangular brackets and the list and the rectangular representation is shown in the following figure for a 3x3 array:  

#  <a><img src = "https://ibm.box.com/shared/static/dsa3nfspbvarlwikt2nuva4ka8ez7stm.png" width = 500, align = "center"></a>
# 

# We can access the 2nd-row 3rd column as shown in the following figure:

#  <a><img src="https://ibm.box.com/shared/static/7ezznbkz63cvd39wn6yidqojdqbh9v0u.png" , width=500,align="center"> </a>

#  We simply use the square brackets and the indices corresponding to the element we would like:

# In[43]:

A[1,2]


#  We can also use the following notation to obtain the elements: 

# In[44]:

A[1][2]


#  Consider the elements shown in the following figure 

#  <a><img src="https://ibm.box.com/shared/static/178texrln4qv2figweqtmgliwwikncnd.png", width=500,align="center"> </a>

#  we can access the element as follows 

# In[45]:

A[0][0]


#  We can also use slicing in numpy arrays,consider the following figure; we would like to obtain the first two columns in the first row  

#  <a><img src="https://ibm.box.com/shared/static/mjmlvk9d9p1fokh5e1ka51bayw8qnv1e.png", width=500,align="center"> </a>

#  This can be done with the following syntax 

# In[15]:

A[0][0:2]


# Similarly, we can obtain the first two rows of the 3rd column as follows:

# In[16]:

A[0:2,2]


# Corresponding to the following figure: 

# <a><img src="https://ibm.box.com/shared/static/p9y7q111sq4epvkn2vtvkda5667gyiho.png", width=500,align="center" ></a>

# # Basic Operations 

#  We can also add arrays; the process is identical to matrix addition. Matrix addition of **X** and **Y** is shown in the following figure:

#  <a><img src="https://ibm.box.com/shared/static/6fiwxq3nsnpk3ae82t0vbxv8qtz1c1gs.png", width=500,align="center"> </a>

#  The numpy array is given by **X** and **Y**

# In[6]:

X=np.array([[1,0],[0,1]]) 
X


# In[7]:

Y=np.array([[2,1],[1,2]]) 
Y


#  We can add the numpy arrays as follows.

# In[8]:

Z=X+Y
Z


#  Multiplying a numpy array by a scaler is identical to multiplying a matrix by a scaler. If we multiply the matrix **Y** by the scaler 2, we simply multiply every element in the matrix by 2 as shown in the figure.

#  <a><img src="https://ibm.box.com/shared/static/b942bzigx47l3bfkielh0d36ghurrma8.png", width=500,align="center"> </a>

#  We can perform the same operation in numpy as follows 

# In[21]:

Y=np.array([[2,1],[1,2]]) 
Y


# In[22]:

Z=2*Y
Z


#  Multiplication of two arrays corresponds to an element-wise product or  Hadamard product.  Consider matrix  **X** and **Y**. The Hadamard product corresponds to multiplying each of the elements in the same position, i.e. multiplying elements contained in the same colour boxes together. The result is a new matrix that is the same size as matrix **Y** or **X**, as shown in the following figure.

#  <a><img src="https://ibm.box.com/shared/static/7yha01bj0orozx9vicpf32p6p4t3f3ii.png", width=500,align="center"> </a>
# 

# We can perform element-wise product of the array **X** and **Y** as follows:

# In[12]:

Y=np.array([[2,1],[1,2]]) 
Y


# In[13]:

X=np.array([[1,0],[0,1]]) 
X


# In[14]:

Z=X*Y
Z


#  We can also perform matrix multiplication with the numpy arrays **A** and **B** as follows:

#  First, we define matrix **A** and **B**:

# In[15]:

A=np.array([[0,1,1],[1,0,1]])
A


# In[27]:

B=np.array([[1,1],[1,1],[-1,1]])
B


# We use the numpy function **dot** to multiply the arrays together.

# In[28]:

Z=np.dot(A,B)
Z


# In[17]:

np.sin(Z)


# In[20]:

C=np.array([[1,1],[2,2],[3,3]])
C


# In[21]:

C.T


# <a href="http://cocl.us/bottemNotebooksPython101Coursera"><img src = "https://ibm.box.com/shared/static/irypdxea2q4th88zu1o1tsd06dya10go.png" width = 750, align = "center"></a>

# ### About the Authors:  
# 
#  [Joseph Santarcangelo]( https://www.linkedin.com/in/joseph-s-50398b136/) has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 

# Copyright &copy; 2017 [cognitiveclass.ai](https:cognitiveclass.ai). This notebook and its source code are released under the terms of the [MIT License](cognitiveclass.ai).
