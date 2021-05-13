import requests
from bs4 import BeautifulSoup
import os


def getpdfpagelink(debug=False):  # get the link to the page where the PDF is in
    link = 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar'
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')

    page_content = soup.find('div', class_='item-page')

    ahref = page_content.a['href']

    link_pdf_page = mountlink(ahref, link)  # the pdf link is in this page

    return link_pdf_page


def getpdflink():
    link = getpdfpagelink()
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')

    page_content = soup.find('div', class_='item-page')

    ahref = page_content.tbody.a['href']

    pdf_link = mountlink(ahref,link)

    return pdf_link


def mountlink(ahref,link):
    homelink = link[:link.find('.br') + 3]
    Link = f"{homelink}{ahref}"
    return Link


def downloadPDF(name=False):
    pdf_link = getpdflink()
    r = requests.get(pdf_link, stream=True)

    pdfname = pdf_link.split('/')[-1]
    if pdfname not in os.listdir():
        with open(f'{pdfname}', 'wb') as f:
            f.write(r.content)
        f.close
        print(f"\n{pdfname} was sucessfully downloaded\n")

    else:
        print(f'\n\nthere is a {pdfname} already\n\n')
        
    if name:
        return pdfname


if __name__=='__main__':
    downloadPDF()
