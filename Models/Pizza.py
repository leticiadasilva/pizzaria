import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence, Float, TIMESTAMP
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData(schema="pizzaria")

Base = declarative_base(metadata=metadata)

class Pizza(Base):
    __tablename__ = 'tb_pizza'
    id = Column('id_pizza', Integer, primary_key=True)
    nome = Column('nome', String)
    descricao = Column('descricao', String)
    categoria = Column('categoria', String)
    preco = Column('preco', Float)

    def __repr__(self) -> str:
        return self.nome