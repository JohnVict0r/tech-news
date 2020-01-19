import logging
from abc import ABC, abstractmethod

from bs4 import BeautifulSoup
from datetime import datetime

from tech.utils import request_page
from tech.models import Post


logging.basicConfig(level=logging.INFO)


class PortalScrapper(ABC):
    def __init__(self, url=None):
        self.url = url
        self.response = None
        self.page = None
        self.load_soup()

    def load_soup(self):
        logging.info(f'{self.__class__.__name__} requisitando a página {self.url}...')
        self.response = request_page(self.url)
        self.page = BeautifulSoup(self.response.content, 'html.parser')

    @abstractmethod
    def process(self):
        raise NotImplementedError('Cannot call method from abstract class')


class TecmundoScrapper(PortalScrapper):
    def __init__(self):
        logging.info(f'{self.__class__.__name__} inicializando...')
        super(TecmundoScrapper, self).__init__('https://www.tecmundo.com.br/mais-lidas')

    def process(self):
        logging.info(f'{self.__class__.__name__} processando...')
        logging.info(f'{self.__class__.__name__} pegando os artigos mais lidos...')

        article_tags = self.page.find_all('article')
        logging.info(f'{self.__class__.__name__} {len(article_tags)} artigos identificados!')

        for article_tag in article_tags:
            a = article_tag.find('figure').find('a')
            str_published_date = article_tag.find_all("div", class_="tec--timestamp__item z--font-semibold")[0].text

            title = article_tag.find_all("a", class_="tec--card__title__link")[0].text.strip() 
            post_url = a['href']
            img_url = a.find('img')['data-src']
            published_date = datetime.strptime(str_published_date, '%d/%m/%Y').date()
            
            post, created = Post.objects.get_or_create(title=title, post_url=post_url, img_url=img_url, published_date=published_date)
            if created:
                logging.info(f'{self.__class__.__name__} artigo "{post.title}" cadastrado!')
            else:
                logging.info(f'{self.__class__.__name__} artigo "{post.title}" já estava cadastrado no sistema!')


class ScrappingManager(object):
    SCRAPPERS = [TecmundoScrapper]

    def __init__(self):
        logging.info(f'{self.__class__.__name__} inicializando...')
        self.scrappers = []
        self.initialize_scrappers()

    def initialize_scrappers(self):
        logging.info(f'{self.__class__.__name__} instanciando scrappers...')
        for scrapper_cls in self.SCRAPPERS:
            scrapper = scrapper_cls()
            self.scrappers.append(scrapper)

    def process(self):
        logging.info(f'{self.__class__.__name__} processando scrappers...')
        for scrapper in self.scrappers:
            scrapper.process()