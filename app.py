import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Libera requisições do front-end

DATABASE = 'tarefas.db'

def get_db_connection():
    """Cria e retorna uma conexao com o banco de dados SQLite."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Retorna os resultados como dicionários
    return conn

def init_db():
    """Cria a tabela de tarefas caso ela ainda nao exista."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            status TEXT DEFAULT 'Pendente',
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Inicializa o banco de dados ao subir o servidor
init_db()


# ROTAS DA API REST
@app.route('/api/tarefas', methods=['GET'])
def listar_tarefas():
    """Retorna a lista de todas as tarefas cadastradas."""
    conn = get_db_connection()
    tarefas = conn.execute('SELECT * FROM tarefas ORDER BY id DESC').fetchall()
    conn.close()
    
    lista = [dict(t) for t in tarefas]
    return jsonify(lista), 200

@app.route('/api/tarefas', methods=['POST'])
def criar_tarefa():
    """Cria uma nova tarefa no banco de dados."""
    dados = request.get_json()
    titulo = dados.get('titulo')

    if not titulo:
        return jsonify({'erro': 'O titulo da tarefa eh obrigatorio!'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tarefas (titulo) VALUES (?)', (titulo,))
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    return jsonify({'id': novo_id, 'titulo': titulo, 'status': 'Pendente'}), 201

@app.route('/api/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    """Deleta uma tarefa específica pelo ID."""
    conn = get_db_connection()
    conn.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    return jsonify({'mensagem': 'Tarefa removida com sucesso!'}), 200

@app.route('/api/tarefas', methods=['DELETE'])
def limpar_tudo():
    """Deleta todas as tarefas."""
    conn = get_db_connection()
    conn.execute('DELETE FROM tarefas')
    conn.commit()
    conn.close()
    
    return jsonify({'mensagem': 'Todas as tarefas foram apagadas!'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)