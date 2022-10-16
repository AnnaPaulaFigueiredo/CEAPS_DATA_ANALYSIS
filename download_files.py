import logging
from urllib import request
from logging import basicConfig, INFO

basicConfig(level=INFO, filename='download_logger.log', filemode='a',
            format="%(levelname)s- %(asctime)s: %(message)s")


def main():

    file_urls = ['https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2022.csv', 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2021.csv',
                 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2020.csv', 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2019.csv',
                 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2018.csv', 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2017.csv',
                 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2016.csv', 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2015.csv',
                 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2014.csv', 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2013.csv',
                 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2012.csv', 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2011.csv',
                 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2010.csv', 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2009.csv',
                 'https://www.senado.gov.br/transparencia/LAI/verba/despesa_ceaps_2008.csv', ]

    files = ['./data/despesa_ceaps_2022.csv', './data/despesa_ceaps_2019.csv', './data/despesa_ceaps_2018.csv', './data/despesa_ceaps_2017.csv', './data/despesa_ceaps_2016.csv',
             './data/despesa_ceaps_2015.csv', './data/despesa_ceaps_2014.csv', './data/despesa_ceaps_2013.csv', './data/despesa_ceaps_2012.csv', './data/despesa_ceaps_2012.csv',
             './data/despesa_ceaps_2010.csv', './data/despesa_ceaps_2009.csv', './data/despesa_ceaps_2008.csv']

    for url, file in zip(file_urls, files):

        try:
            request.urlretrieve(url, file)
            logging.info(f"Download complete: {url}.")

        except Exception as e:
            logging.info(f"Falha no download {url}: {e}")

if __name__ == "__main__":
    main()
