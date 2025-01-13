from sqlalchemy import create_engine

# Conectando ao SQLite com caminho relativo
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão com o SQLite usando caminho relativo estabelecida")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)