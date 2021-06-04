import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence, Float, TIMESTAMP
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from ..Models.Pizza import Pizza

engine = create_engine(
    "postgresql://postgres:postgres@localhost/pizzaria",
)


class PizzaController():
    def buscar_pizzas(self):
        with Session(engine) as session:
            print(session.query(Pizza).all())