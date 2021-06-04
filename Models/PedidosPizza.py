import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence, Float, TIMESTAMP
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

metadata = MetaData(schema="pizzaria")

Base = declarative_base(metadata=metadata)

class PedidosPizza(Base):
    __tablename__ = 'tb_pedido_pizza'
    id_pedido = Column('id_pedido', Integer, ForeignKey(tb_pedido.id_pedido))
    id_pizza = Column('id_pizza', Integer, ForeignKey(tb_pizza.id_pizza))
    quantidade = Column('quantidade', String)

    def __repr__(self) -> str:
        return self.nome