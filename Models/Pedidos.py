import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence, Float, TIMESTAMP
from sqlalchemy.orm import Session
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP

metadata = MetaData(schema="pizzaria")

Base = declarative_base(metadata=metadata)

class Pedidos(Base):
    __tablename__ = 'tb_pedidos'
    id = Column('id_pedido', Integer, primary_key=True)
    id_cliente = Column('id_cliente', Integer, ForeignKey(tb_cliente.id_cliente))
    observacao = Column('observacao', String)
    tipo_entrega = Column('tipo_entrega', String)
    preco = Column('preco', Float)
    data_pedido = Column('data_pedido', TIMESTAMP)

    def __repr__(self) -> str:
        return self.nome