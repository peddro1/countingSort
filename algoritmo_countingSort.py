from random import shuffle
from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
  
def desenhaGrafico(x,y, xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()


def geraLista(tam):
    
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista
    
    
    
x2 = [100000,200000,300000,400000,500000,1000000,2000000]
y = []


def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m                
    
    for a in array1:
    
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1


for a in range(len(x2)):
 
    array = geraLista(x2[a])
  
    inicio = timeit.default_timer()
    counting_sort(array,x2[a])
    fim = timeit.default_timer()
     
    y.append('%f' %(fim - inicio))
   
    print(y)
    
    
    
desenhaGrafico(x2,y)
    
