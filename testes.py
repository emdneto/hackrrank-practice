'''
(a[i] <= a[j] e b[i] <= b[j]) e 

(a[i] < a[j] ou b[i] < b[j])
'''
import time
import timeit
import random

def main(p):
  n = len(p)
  lista = []
  
  for i in range(n):
    Ai = p[i][0]
    Bi = p[i][1]
    for j in range(i+1, n):
      Aj = p[j][0]
      Bj = p[j][1]
      Si = Ai + Bi
      Sj = Aj + Bj
      
      if not (((Ai <= Aj) and (Bi <= Bj)) and ((Ai < Aj) or (Bi < Bj))):
        print(f'{p[j]} não dominado por {p[i]}')
        lista.append(p[i])
      else: 
        print(f'{p[j]} dominado por {p[i]}')
      '''
      #print(p[i], p[j])
      if not ((Ai <= Aj) and (Bi <= Bj)) and ((Ai < Aj) or (Bi < Bj)):

        print(f'{p[j]} dominado por {p[i]}')
        
       # print(f'{p[i]} dominado por {p[j]}')
       # last = p[j]
       # if p[j] == last:
'''

  print(lista)


  
    

pares = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (8, 7), (15, 20), (20, 15)]


main(pares)
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False        
                #print(lista)
    return lista

def MetodoSort(lista):
  n = len(lista)

  if n == 1:
    return lista

  ctrl = True
  while ctrl: 
    ctrl = False
    for i in range(n-1):
      if lista[i] > lista[i+1]:
        print(lista)
        old = lista[i]
        new = lista[i+1]
        print(old, new)
        lista[i] = new
        lista[i+1] = old
        
        #lista[i], lista[i+1] = lista[i+1],lista[i]
        ctrl = True        
        
  
  return lista

  #print(lista)
  

  #while i < n and j < n:
  

''''
l = [5, 4, 3, 2, 1]
#l = list(reversed(range(50)))
n = len(l)

tic = time.perf_counter()
b = MetodoSort(l)
print(b)
toc = time.perf_counter()
print(f"DownloaTrue, ded the tutorial in {toc - tic:0.10f} seconds")

#a = bubbleSort(l)
#print(a)


tic = time.perf_counter()
a = bubble_sort(l)
print(a)
toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.10f} seconds")
'''
