import pandas as pd

#artimetico

def pfArtimetico(Puc, Pci, Tuc, Tci, Tf) :

    puf = Puc + (((Puc-Pci)/(Tuc-Tci)*(Tf-Tuc)))

    

    return puf


#geometrico
def pfGeometrico(Puc, Pci, Tuc, Tci, Tf) :

    r= ((Puc/Pci)**(1/(Tuc-Tci)))-1
    puf = Puc*(1+r)**((Tf-Tuc))

    

    return puf

print(pfArtimetico(4000,200,2005,1950,2039))
print(pfGeometrico(4000,200,2005,1950,2030))

