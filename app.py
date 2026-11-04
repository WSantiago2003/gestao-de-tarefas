import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATABASE = 'tarefas.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            categoria TEXT DEFAULT 'Geral',
            concluida INTEGER DEFAULT 0,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/api/tarefas', methods=['GET'])
def listar_tarefas():
    conn = get_db_connection()
    tarefas = conn.execute('SELECT * FROM tarefas ORDER BY id DESC').fetchall()
    conn.close()
    return jsonify([dict(t) for t in tarefas]), 200

@app.route('/api/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    titulo = dados.get('titulo')
    categoria = dados.get('categoria', 'Geral')

    if not titulo:
        return jsonify({'erro': 'O título é obrigatório!'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tarefas (titulo, categoria) VALUES (?, ?)', (titulo, categoria))
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    return jsonify({'id': novo_id, 'titulo': titulo, 'categoria': categoria, 'concluida': 0}), 201

@app.route('/api/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    dados = request.get_json()
    concluida = dados.get('concluida')

    conn = get_db_connection()
    conn.execute('UPDATE tarefas SET concluida = ? WHERE id = ?', (concluida, id))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Tarefa atualizada!'}), 200

@app.route('/api/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Tarefa removida!'}), 200

@app.route('/api/tarefas', methods=['DELETE'])
def limpar_tudo():
    conn = get_db_connection()
    conn.execute('DELETE FROM tarefas')
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Todas as tarefas foram apagadas!'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)