const API_URL = 'http://127.0.0.1:5000/api/tarefas';

// Carrega as tarefas assim que a página é aberta
document.addEventListener('DOMContentLoaded', carregarTarefas);

// 1. LISTAR TAREFAS (GET)
async function carregarTarefas() {
    try {
        const resposta = await fetch(API_URL);
        const tarefas = await resposta.json();

        const lista = document.getElementById('listaTarefas');
        lista.innerHTML = '';

        tarefas.forEach(tarefa => {
            const li = document.createElement('li');
            li.innerHTML = `
                <span>${tarefa.titulo}</span>
                <button onclick="deletarTarefa(${tarefa.id})">❌</button>
            `;
            lista.appendChild(li);
        });
    } catch (erro) {
        console.error('Erro ao carregar tarefas:', erro);
    }
}

// 2. CRIAR TAREFA (POST)
async function adicionarTarefa() {
    const input = document.getElementById('campoTarefa');
    const titulo = input.value.trim();

    if (!titulo) {
        alert('Por favor, digite o título da tarefa!');
        return;
    }

    try {
        const resposta = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ titulo: titulo })
        });

        if (resposta.ok) {
            input.value = '';
            carregarTarefas(); // Recarrega a lista com a nova tarefa vinda do banco
        }
    } catch (erro) {
        console.error('Erro ao adicionar tarefa:', erro);
    }
}

// 3. DELETAR UMA TAREFA (DELETE)
async function deletarTarefa(id) {
    try {
        const resposta = await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
        });

        if (resposta.ok) {
            carregarTarefas(); // Atualiza a lista após deletar
        }
    } catch (erro) {
        console.error('Erro ao deletar tarefa:', erro);
    }
}

// 4. LIMPAR TODAS AS TAREFAS (DELETE ALL)
async function limparTodasTarefas() {
    if (!confirm('Tem certeza que deseja apagar todas as tarefas?')) {
        return;
    }

    try {
        const resposta = await fetch(API_URL, {
            method: 'DELETE'
        });

        if (resposta.ok) {
            carregarTarefas(); // Esvazia a lista na tela
        }
    } catch (erro) {
        console.error('Erro ao limpar tarefas:', erro);
    }
}