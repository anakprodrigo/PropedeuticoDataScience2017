
# coding: utf-8

# In[1]:

#ANA KAREN PRISCILA RODRIGO FLORES
import numpy as np


# In[2]:

x = [1,2,3]
y = [4,5,6]
x + y


# In[3]:

B = np.array([[1,2,3], [4,5,6]]) # habiendo corrido import numpy as np


# In[4]:

B + 2*B 


# In[5]:

np.matmul(B.transpose(), B) # B^t*B


# In[6]:

B[1,1]


# In[7]:

B[1,:]


# In[8]:

B[:,2]


# In[9]:

B[0:2,0:2]


# In[10]:

B.shape


# In[11]:

vec = np.array([1,2,3])
print(vec)


# In[12]:

class Array:
    "Una clase minima para algebra lineal"    
    def __init__(self, list_of_rows): 
        "Constructor"
        self.data = list_of_rows
        self.shape = (len(list_of_rows), len(list_of_rows[0]))


# In[13]:

A = Array([[1,2,3], [4,5,6]])
A.__dict__ 


# In[14]:

A.data


# In[15]:

A.shape


# In[16]:

Array([[1,2,3], [4,5,6]])


# In[17]:

print(Array([[1,2,3], [4,5,6]]))


# In[18]:

np.array([[1,2,3], [4,5,6]])


# In[19]:

print(np.array([[1,2,3], [4,5,6]]))


# In[20]:

class TestClass:
    def __init__(self):
        pass # this means do nothing in Python
    def say_hi(self):
        print("Hey, I am just a normal method saying hi!")
    def __repr__(self):
        return "I am the special class method REPRESENTING a TestClass without printing"
    def __str__(self):
        return "I am the special class method for explicitly PRINTING a TestClass object"


# In[21]:

x = TestClass()


# In[22]:

x.say_hi()


# In[23]:

x


# In[24]:

print(x)


# In[28]:

# EJERCICIO 1
np.array_repr(np.array([1,2]))


# In[29]:

np.array_str(np.arange(3))


# In[30]:

some_list = [1,2,3, 4, 5, 6]
[i**2 for i in some_list]


# In[31]:

class Array:
    "Una clase minima para algebra lineal"    
    def __init__(self, list_of_rows): 
        "Constructor y validador"
        # obtener dimensiones
        self.data = list_of_rows
        nrow = len(list_of_rows)
        #  ___caso vector: redimensionar correctamente
        if not isinstance(list_of_rows[0], list):
            nrow = 1
            self.data = [[x] for x in list_of_rows]
        # ahora las columnas deben estar bien aunque sea un vector
        ncol = len(self.data[0])
        self.shape = (nrow, ncol)
        # validar tamano correcto de filas
        if any([len(r) != ncol for r in self.data]):
            raise Exception("Las filas deben ser del mismo tamano")
            
    def __repr__(self):
        "Ejercicio"
        pass
    
    def __str__(self):
        "Ejercicio"
        pass


# In[32]:

Array([[1,2,3], [4,5]])


# In[33]:

vec = Array([1,2,3])
vec.data


# In[34]:

A = Array([[1,2], [3,4]])
A[0,0]


# In[35]:

A[0,0] = 8


# In[53]:

class Array:
    "Una clase minima para algebra lineal"    
    def __init__(self, list_of_rows): 
        "Constructor y validador"
        # obtener dimensiones
        self.data = list_of_rows
        nrow = len(list_of_rows)
        #  ___caso vector: redimensionar correctamente
        if not isinstance(list_of_rows[0], list):
            nrow = 1
            self.data = [[x] for x in list_of_rows]
        # ahora las columnas deben estar bien aunque sea un vector
        ncol = len(self.data[0])
        self.shape = (nrow, ncol)
        # validar tamano correcto de filas
        if any([len(r) != ncol for r in self.data]):
            raise Exception("Las filas deben ser del mismo tamano")
    
    def __getitem__(self, idx):
        return self.data[idx[0]][idx[1]]
    
    #EJERCICIO 2
    def __setitem__(self, idx, new_value):
        self.vector[idx] = new_value


# In[54]:

A = Array([[1,2],[3,4]])
A[0,1]


# In[59]:

np.zeros((3,6))


# In[61]:

#EJERCICIO 3
a=np.zeros((3,6))
np.zeros_like(a)  


# In[62]:

np.identity(5)


# In[63]:

np.array([[1,2], [3,4]]).transpose()


# In[83]:

#EJERCICIO 4
def transpose(matrix):
   x=0
   trans=[]
   b=len(matrix[0])
   while b!=0:
       trans.append([])
       b-=1
   for list in matrix:
       for element in list:
          trans[x].append(element)
          x+=1
       x=0
   return trans


# In[86]:

C = np.array([[1,2], [3,4]])
transpose(C)


# In[87]:

"hola " + "tu"


# In[88]:

[1,2,3] + [2,3,4]


# In[89]:

np.array([1,2,3]) + np.array([2,3,4])


# In[90]:

np.array([1,2,3]) + 10 


# In[91]:

class Array:
    "Una clase minima para algebra lineal"    
    def __init__(self, list_of_rows): 
        "Constructor y validador"
        # obtener dimensiones
        self.data = list_of_rows
        nrow = len(list_of_rows)
        #  ___caso vector: redimensionar correctamente
        if not isinstance(list_of_rows[0], list):
            nrow = 1
            self.data = [[x] for x in list_of_rows]
        # ahora las columnas deben estar bien aunque sea un vector
        ncol = len(self.data[0])
        self.shape = (nrow, ncol)
        # validar tamano correcto de filas
        if any([len(r) != ncol for r in self.data]):
            raise Exception("Las filas deben ser del mismo tamano")
        
    def __add__(self, other):
        "Hora de sumar"
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise Exception("Las dimensiones son distintas!")
            rows, cols = self.shape
            newArray = Array([[0. for c in range(cols)] for r in range(rows)])
            for r in range(rows):
                for c in range(cols):
                    newArray.data[r][c] = self.data[r][c] + other.data[r][c]
            return newArray
        elif isinstance(2, (int, float, complex)): # en caso de que el lado derecho sea solo un numero
            rows, cols = self.shape
            newArray = Array([[0. for c in range(cols)] for r in range(rows)])
            for r in range(rows):
                for c in range(cols):
                    newArray.data[r][c] = self.data[r][c] + other
            return newArray
        else:
            return NotImplemented # es un tipo de error particular usado en estos metodos


# In[92]:

A = Array([[1,2], [3,4]])
B = Array([[5,6], [7,8]])
C = A + B
C.data


# In[93]:

D = A + 10


# In[94]:

D.data


# In[95]:

Array([[1,2], [3,4]]) + Array([[5,6, 5], [7,8,3]])


# In[104]:

#EJERCICIO 5
class Array:
    def __init__(self, list_of_rows): 
        "Constructor y validador"
        # obtener dimensiones
        self.data = list_of_rows
        nrow = len(list_of_rows)
        #  ___caso vector: redimensionar correctamente
        if not isinstance(list_of_rows[0], list):
            nrow = 1
            self.data = [[x] for x in list_of_rows]
        # ahora las columnas deben estar bien aunque sea un vector
        ncol = len(self.data[0])
        self.shape = (nrow, ncol)
        # validar tamano correcto de filas
        if any([len(r) != ncol for r in self.data]):
            raise Exception("Las filas deben ser del mismo tamano")
    def __radd__(self,other):
        newArray = Array([[0. for c in range(cols)] for r in range(rows)])        
        newArray= Array(self.list_of_rows+other.list_of_rows)
        return newArray


# In[110]:

E = Array([2, [3,4]])
E.data


# In[123]:

#EJERCICIO 6


class Multip(object):
    
    aarg = 0

    def __init__(self):
        self.aarg = 1
    
    def __rmul__(self,A):
        print(A)
        return 0

    def __mul__(self,A):
        print(A)
        return 0
    
    
A = [[i*j for i in np.arange(2)  ] for j in np.arange(3)]
A = np.array(A)
R = Multip()
C =  A * R


# In[133]:

#EJERCICIO 7 al 10
class Vector(Array): # declara que Vector es un tipo de Array
    def __init__(self, list_of_numbers):
        self.vdata = list_of_numbers
        list_of_rows = [[x] for x in list_of_numbers]
        return Array.__init__(self, list_of_rows)
    def __repr__(self):
        return "Vector(" + str(self.vdata) + ")"
    def __str__(self):
        return str(self.vdata)
    def __add__(self, other):
        new_arr = Array.__add__(self, other)
        return Vector([x[0] for x in new_arr.data])


# In[134]:

Vector([1,2,3]).__dict__


# In[135]:

Vector([1,2,3])


# In[142]:

tri = np.zeros((67, 67))
tri[np.triu_indices(67, 1)]


# In[143]:

a = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[144]:

tri_upper_diag = np.triu(a, k=0)


# In[145]:

print (tri_upper_diag)


# In[146]:

tri_upper_no_diag = np.triu(a, k=1)


# In[147]:

print (tri_upper_no_diag)


# In[148]:

tri_lower_diag = np.tril(a, k=0)
print (tri_lower_diag)


# In[149]:

tri_lower_no_diag = np.tril(a, k=-1)
print (tri_lower_no_diag)


# In[ ]:



