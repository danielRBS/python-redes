#importa la libreria de pandas
import pandas as pd

#leer el archivo .csv y guardarlo como un dataframe en una variable
dfPob= pd.read_csv('censo.csv',sep=';')

#generar las funciones 
def pfArtimetico(df, Tf) :
    k=0
    for i in range(df.index.size - 1):
            iPob= df.iloc[i]
            fPob=df.iloc[i+1]
            k+=(((fPob.iloc[1])-(iPob.iloc[1]))/((fPob.iloc[0])-(iPob.iloc[0])))
    k=(k/(df.index.size -1))
    fPob=df.iloc[-1]

    puf = round(fPob.iloc[1] + (k*(Tf-fPob.iloc[0])))

    return puf


def pfGometrico(df, Tf):
    r=0
    for i in range(df.index.size - 1):
        iPob=df.iloc[i]
        fPob=df.iloc[i+1]
        r+=(((fPob.iloc[1]/iPob.iloc[1])**(1/(fPob.iloc[0]-iPob.iloc[0])))-1)
    r= r/(df.index.size -1)
    fPob=df.iloc[-1]
    puf=round(fPob.iloc[1]*((1+r)**(Tf-fPob.iloc[0])))
    return puf


print(pfArtimetico(dfPob,2034))
print(pfGometrico(dfPob,2034)) 