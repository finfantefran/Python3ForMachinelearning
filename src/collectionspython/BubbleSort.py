'''
@author: finfantefran
'''


def bubleSort(lista1):
    print("Estado inicial lista: ",lista1)
    
    for i in range(0,len(lista1)-1):
        for j in range(i+1,len(lista1)):
            print(j)
            if(lista1[i]>lista1[j]):
                temp=lista1[i]
                lista1[i]=lista1[j]
                lista1[j]=temp
                
                
    print("Lista ordendada: ",lista1)
    
    
if __name__=="__main__":
    
    lista1=[1,5,3,4]
    print(len(lista1))
    bubleSort(lista1)