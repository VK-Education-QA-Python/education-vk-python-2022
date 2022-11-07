from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, CHAR, VARCHAR

Base = declarative_base()


class BannerModel(Base):

    __tablename__ = 'banner'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'Banner id={self.id}, name={self.name}, url={self.url}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(CHAR(50), nullable=False)
    url = Column(VARCHAR(50), nullable=False)
