import pandas as pd
import numpy as np

#artimetico

def pfArtimetico(Puc, Pci, Tuc, Tci, Tf) :

    pf = Puc + (((Puc-Pci)/(Tuc-Tci)*(Tf-Tuc)))

    

    return pf


#geometrico
def pfGeometrico(Puc, Pci, Tuc, Tci, Tf) :

    r= ((Puc/Pci)**(1/(Tuc-Tci)))-1
    pf = Puc*(1+r)**((Tf-Tuc))

    

    return pf

#exponecial
def pfExponecial(Puc, Pca, Tuc, Tca, Tf,Pci, Tci):
    k=(np.log(Puc)-np.log(Pca))/(Tuc-Tca)
    pf= Pci * np.exp(k*(Tf-Tci))
    return pf

#print(pfArtimetico(4000,200,2005,1950,2039))
print(pfArtimetico(2806,1067,2005,1938,2022))
print(pfGeometrico(2806,1067,2005,1938,2022))
print(pfExponecial(2806,2440,2005,1993,2022,1067,1938))

