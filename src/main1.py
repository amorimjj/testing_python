import psycopg
from fastapi import FastAPI

app = FastAPI()

DB_CONFIG = {
    "dbname": "develop",
    "user": "postgres.tgedywzwadfwiixclsdm",
    "password": "rowFy4wCaoh54RvB",
    "host": "aws-0-us-west-1.pooler.supabase.com",
    "port": 5432
}

def get_data():
    try:
        # Conecta ao banco
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                # Executa o SELECT
                cur.execute("SELECT name FROM clients ORDER BY name;")
                
                # Pega as colunas e linhas
                columns = [desc[0] for desc in cur.description]
                rows = cur.fetchall()
                
                # Converte para lista de dicionários
                users = [dict(zip(columns, row)) for row in rows]
                
                return users  # Retorna os dados para quem chamou!
                
    except psycopg.Error as e:
        raise psycopg.Error(f"Erro no banco de dados: {e}")  # Propaga o erro para o chamador
    except Exception as e:
        raise Exception(f"Erro genérico: {e}")

@app.get("/")
def do_GET():
    data = get_data()
    return data