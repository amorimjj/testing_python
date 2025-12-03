import psycopg
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

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

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = get_data()
        #print('Dados retornados')
        #print(json.dumps(data, ensure_ascii=False, indent=2).encode('utf-8'))
        json_data = json.dumps(data, ensure_ascii=False, indent=2).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(json_data)


server_address = ("", 8000)
httpd = HTTPServer(server_address, HelloHandler)

print('Running. Press Ctrl+C to stop.')
httpd.serve_forever()