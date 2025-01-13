from sqlalchemy import create_engine

# Conectando ao SQLite com caminho relativo
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão com o SQLite usando caminho relativo estabelecida")

