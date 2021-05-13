import camelot  # camelot precisa de algumas coisas para seu uso, detalhes aqui -> https://camelot-py.readthedocs.io/en/master/user/install-deps.html#os-specific-instructions
from teste1 import downloadPDF
import pandas as pd
import zipfile, os, shutil


def gettables():
    pdf = downloadPDF(name=True)

    tables = camelot.read_pdf(pdf, pages='79,80,81,82,83,84,85')
    
    return tables


def getdataframes(ts=gettables()):
    df30 = ts[0].df

    df31 = ts[1].df

    for i in range(2,7):
        df31 = pd.concat([df31, ts[i].df], ignore_index=True)  # pula do 5 para o 18 mesmo

    df32 = ts[7].df

    return [df30,df31,df32]


def tocsv(dfs = getdataframes()):
    for i in range(len(dfs)):
        dfs[i].to_csv('quadro3{}.csv'.format(i))


def zipping():
    zippando = zipfile.ZipFile("Teste_Intuitive_Care_Gilmar_Junio_Macedo_Guedes.zip", 'w')

    for f in os.listdir():
        if f.endswith('.csv'):
            zippando.write(f, compress_type=zipfile.ZIP_DEFLATED)
    
    zippando.close()


def deletecsvs():
    for f in os.listdir():
        if f.endswith('.csv'):
            os.remove(f)


def main(delet=False):
    tocsv()
    zipping()

    if delet: deletecsvs()


if __name__=='__main__':
    main(delet=True)