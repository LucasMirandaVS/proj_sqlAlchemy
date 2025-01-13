from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError  # Importa exceções do SQLAlchemy

Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    fornecedor = relationship("Fornecedor")  # Relação entre Produto e Fornecedor

engine = create_engine('sqlite:///desafio.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# Inserindo fornecedores
try:
    with Session() as session:  # Usando a sessão corretamente com o gerenciador de contexto
        fornecedores = [
            Fornecedor(nome="Mirassol", telefone="777", email="contato@a.com", endereco="Endereço A"),
            Fornecedor(nome="Sport", telefone="876543", email="contato@b.com", endereco="Endereço B"),
            Fornecedor(nome="Nautico", telefone="123", email="contato@c.com", endereco="Endereço C"),
            Fornecedor(nome="Santa Cruz", telefone="5678", email="contato@d.com", endereco="Endereço D"),
            Fornecedor(nome="Retro FC", telefone="432175", email="contato@e.com", endereco="Endereço E")
        ]
        session.add_all(fornecedores)
        session.commit()
except SQLAlchemyError as e:  # Capturando exceções do SQLAlchemy
    print(f"Erro ao inserir fornecedores: {e}")

# Inserindo produtos
try:
    with Session() as session:  # Corrigindo a utilização da sessão
        produtos = [
            Produto(nome="Reserva de Magrão", descricao="Descrição do Magrão", preco=100, fornecedor_id=1),
            Produto(nome="Carlinhos Bala", descricao="Descrição da bala", preco=200, fornecedor_id=2),
            Produto(nome="Caça Rato", descricao="Descrição do rato", preco=300, fornecedor_id=3),
            Produto(nome="Abreu e Lima", descricao="Descrição do bairro", preco=400, fornecedor_id=4),
            Produto(nome="Ibura", descricao="Descrição do bairro", preco=500, fornecedor_id=5)
        ]
        session.add_all(produtos)
        session.commit()
except SQLAlchemyError as e:
    print(f"Erro ao inserir produtos: {e}")

from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
# Supondo que engine já foi definido anteriormente e os modelos Produto e Fornecedor foram definidos conforme o exemplo anterior.

Session = sessionmaker(bind=engine)
session = Session()

resultado = session.query(
    Fornecedor.nome,
    func.sum(Produto.preco).label('total_preco')
).join(Produto, Fornecedor.id == Produto.fornecedor_id
).group_by(Fornecedor.nome).all()

for nome, total_preco in resultado:
    print(f"Fornecedor: {nome}, Total Preço: {total_preco}")