#importa las librerias de pandas y numpy
import pandas as pd
import numpy as np

#leer el archivo .csv y guardarlo como un dataframe en una variable
dfPob= pd.read_csv('censo3.csv',sep=';')

#generar las funciones 

#metodo aritmetico
def pfArtimetico(df, Tf) :
    k=0
    for i in range(df.index.size - 1):
            iPob= df.iloc[i]
            fPob=df.iloc[i+1]
            k+=(((fPob.iloc[1])-(iPob.iloc[1]))/((fPob.iloc[0])-(iPob.iloc[0])))
    k=(k/(df.index.size -1))
    fnPob=df.iloc[-1]
    pf = round(fnPob.iloc[1] + (k*(Tf-fnPob.iloc[0])))

    return pf

#metodo geometrico
def pfGometrico(df, Tf):
    r=0
    for i in range(df.index.size - 1):
        iPob=df.iloc[i]
        fPob=df.iloc[i+1]
        r+=(((fPob.iloc[1]/iPob.iloc[1])**(1/(fPob.iloc[0]-iPob.iloc[0])))-1)
    r= r/(df.index.size -1)
    fnPob=df.iloc[-1]
    pf=round(fnPob.iloc[1]*((1+r)**(Tf-fnPob.iloc[0])))

    return pf

#metodo exponencial
def pfExponencial(df, Tf):
    k=0
    for i in range(df.index.size -1):
       iPob=df.iloc[i]
       fPob=df.iloc[i+1]
       k+=(np.log(fPob.iloc[1])-np.log(iPob.iloc[1]))/(fPob.iloc[0]-iPob.iloc[0])
    k=(k/(df.index.size -1))
    inPob=df.iloc[0]
    pf=round(inPob.iloc[1]*np.exp(k*(Tf-inPob.iloc[0])))
    return pf

# metodo wappus    
def pfWappus(df, Tf):
     pf=0
     i=0
     for j in range(df.index.size -1):
         iPob=df.iloc[j]
         fPob=df.iloc[j+1]
         i+=200*(fPob.iloc[1]-iPob.iloc[1])/((fPob.iloc[0]-iPob.iloc[0])*(iPob.iloc[1]+fPob.iloc[1]))
     i=i/(df.index.size -1)
     inPob=df.iloc[0]
     if((i*(Tf-inPob.iloc[0]))<200):
          pf=inPob.iloc[1]*((200+(i*(Tf-inPob.iloc[0])))/(200-(i*(Tf-inPob.iloc[0]))))
     else:
        pf="no se puede aplicar este metodo"
     return pf
     

print(pfArtimetico(dfPob,2022))
print(pfGometrico(dfPob,2022))
print(pfExponencial(dfPob,2022)) 
print(pfWappus(dfPob,2022))
