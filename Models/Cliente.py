import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence, Float, TIMESTAMP
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData(schema="pizzaria")

Base = declarative_base(metadata=metadata)

class Cliente(Base):
    __tablename__ = 'tb_cliente'
    id = Column('id_cliente', Integer, primary_key=True)
    nome = Column('nome', String)
    email = Column('email', String)
    endereco = Column('endereco', String)

    def __repr__(self) -> str:
        return self.nome