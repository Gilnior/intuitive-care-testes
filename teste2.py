import camelot  # camelot precisa de algumas coisas para seu uso, detalhes aqui -> https://camelot-py.readthedocs.io/en/master/user/install-deps.html#os-specific-instructions
from teste1 import downloadPDF
import pandas as pd

def gettables():
    pdf = downloadPDF(name=True)

    tables = camelot.read_pdf(pdf, pages='79,80,81,82,83,84,85')
    
    return tables

pdf = 'Padrão_TISS_Componente_Organizacional_202103.pdf'
ts = camelot.read_pdf(pdf, pages='79,80,81,82,83,84,85')

df30 = ts[0].df

df31 = ts[1].df

for i in range(2,7):
    df31 = pd.concat([df31, ts[i].df], ignore_index=True)

df32 = ts[7].df

print(df30,df31,df32,sep='\n\n')
