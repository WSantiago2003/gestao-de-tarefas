const API_URL = 'http://127.0.0.1:5000/api/tarefas';

document.addEventListener('DOMContentLoaded', carregarTarefas);

async function carregarTarefas() {
    try {
        const resposta = await fetch(API_URL);
        const tarefas = await resposta.json();

        const lista = document.getElementById('listaTarefas');
        lista.innerHTML = '';

        tarefas.forEach(tarefa => {
            const li = document.createElement('li');
            
            const estaConcluida = tarefa.concluida === 1;

            li.innerHTML = `
                <div class="tarefa-conteudo">
                    <input type="checkbox" ${estaConcluida ? 'checked' : ''} onchange="alternarStatus(${tarefa.id}, this.checked)">
                    <span class="${estaConcluida ? 'concluida' : ''}">${tarefa.titulo}</span>
                    <span class="categoria-tag">${tarefa.categoria || '📚 Estudos'}</span>
                </div>
                <button onclick="deletarTarefa(${tarefa.id})">❌</button>
            `;
            lista.appendChild(li);
        });
    } catch (erro) {
        console.error('Erro ao carregar tarefas:', erro);
    }
}

async function adicionarTarefa() {
    const input = document.getElementById('campoTarefa');
    const select = document.getElementById('selectCategoria');
    
    const titulo = input.value.trim();
    const categoria = select.value;

    if (!titulo) {
        alert('Por favor, digite o título da tarefa!');
        return;
    }

    try {
        const resposta = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ titulo: titulo, categoria: categoria })
        });

        if (resposta.ok) {
            input.value = '';
            carregarTarefas();
        }
    } catch (erro) {
        console.error('Erro ao adicionar tarefa:', erro);
    }
}

async function alternarStatus(id, concluida) {
    try {
        await fetch(`${API_URL}/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ concluida: concluida ? 1 : 0 })
        });
        carregarTarefas();
    } catch (erro) {
        console.error('Erro ao atualizar status:', erro);
    }
}

async function deletarTarefa(id) {
    try {
        const resposta = await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
        if (resposta.ok) carregarTarefas();
    } catch (erro) {
        console.error('Erro ao deletar tarefa:', erro);
    }
}

async function limparTodasTarefas() {
    if (!confirm('Tem certeza que deseja apagar todas as tarefas?')) return;

    try {
        const resposta = await fetch(API_URL, { method: 'DELETE' });
        if (resposta.ok) carregarTarefas();
    } catch (erro) {
        console.error('Erro ao limpar tarefas:', erro);
    }
}