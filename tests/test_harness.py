import os

# 1. Criar a estrutura de diretórios
os.makedirs('src', exist_ok=True)
os.makedirs('tests', exist_ok=True)

# 2. Criar o ficheiro __init__.py para o Python reconhecer a pasta src como um pacote
with open('src/__init__.py', 'w') as f:
    f.write('')

# 3. Criar o código principal (task_analyzer.py)
task_analyzer_code = """from typing import List, Dict, Any
from datetime import datetime

class TaskValidationError(Exception):
    pass

def analyze_tasks(tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    total_tarefas = len(tasks)
    if total_tarefas == 0:
        return {
            "total_tarefas": 0, "total_concluidas": 0, "total_pendentes": 0,
            "tempo_medio_conclusao_horas": 0.0, "taxa_atraso_percentual": 0.0,
            "tempo_medio_por_prioridade": {}
        }
        
    total_concluidas = 0
    total_pendentes = 0
    tarefas_atrasadas = 0
    tempo_total_horas = 0.0
    tempos_prioridade: Dict[str, List[float]] = {"Alta": [], "Média": [], "Baixa": []}
    
    for task in tasks:
        if task.get("data_conclusao"):
            criacao = datetime.fromisoformat(task["data_criacao"])
            conclusao = datetime.fromisoformat(task["data_conclusao"])
            if conclusao < criacao:
                raise TaskValidationError("A data de conclusão não pode ser anterior à data de criação.")
            total_concluidas += 1
            horas = (conclusao - criacao).total_seconds() / 3600
            tempo_total_horas += horas
            prioridade = task.get("prioridade", "Média")
            if prioridade in tempos_prioridade:
                tempos_prioridade[prioridade].append(horas)
        else:
            total_pendentes += 1
            if task.get("prazo"):
                prazo = datetime.fromisoformat(task["prazo"])
                if datetime.now() > prazo:
                    tarefas_atrasadas += 1

    tempo_medio_conclusao_horas = (tempo_total_horas / total_concluidas) if total_concluidas > 0 else 0.0
    taxa_atraso_percentual = (tarefas_atrasadas / total_tarefas) * 100 if total_tarefas > 0 else 0.0
    tempo_medio_por_prioridade = {
        p: (sum(t) / len(t)) if t else 0.0 for p, t in tempos_prioridade.items()
    }

    return {
        "total_tarefas": total_tarefas, "total_concluidas": total_concluidas,
        "total_pendentes": total_pendentes, "tempo_medio_conclusao_horas": tempo_medio_conclusao_horas,
        "taxa_atraso_percentual": taxa_atraso_percentual, "tempo_medio_por_prioridade": tempo_medio_por_prioridade
    }
"""
with open('src/task_analyzer.py', 'w', encoding='utf-8') as f:
    f.write(task_analyzer_code)

# 4. Criar o ficheiro do Test Harness (test_harness.py)
test_harness_code = """import pytest
from src.task_analyzer import analyze_tasks, TaskValidationError

def test_cenario_1_sucesso_calculos():
    tasks = [
        {"id": 1, "data_criacao": "2023-10-01T10:00:00", "data_conclusao": "2023-10-01T12:00:00", "prioridade": "Alta"},
        {"id": 2, "data_criacao": "2023-10-02T10:00:00", "data_conclusao": "2023-10-02T14:00:00", "prioridade": "Baixa"},
        {"id": 3, "data_criacao": "2023-10-01T10:00:00", "prazo": "2023-10-02T10:00:00"},
        {"id": 4, "data_criacao": "2030-10-01T10:00:00", "prazo": "2030-10-02T10:00:00"}
    ]
    resultado = analyze_tasks(tasks)
    assert resultado["total_tarefas"] == 4
    assert resultado["total_concluidas"] == 2
    assert resultado["total_pendentes"] == 2
    assert resultado["tempo_medio_conclusao_horas"] == 3.0
    assert resultado["tempo_medio_por_prioridade"]["Alta"] == 2.0
    assert resultado["tempo_medio_por_prioridade"]["Baixa"] == 4.0
    assert resultado["taxa_atraso_percentual"] == 25.0

def test_cenario_2_excecao_datas_inconsistentes():
    tasks = [
        {"id": 1, "data_criacao": "2023-10-02T10:00:00", "data_conclusao": "2023-10-01T10:00:00"}
    ]
    with pytest.raises(TaskValidationError):
        analyze_tasks(tasks)

def test_casos_de_borda_entradas_vazias():
    resultado = analyze_tasks([])
    assert resultado["total_tarefas"] == 0
    assert resultado["tempo_medio_conclusao_horas"] == 0.0

def test_casos_de_borda_apenas_pendentes():
    tasks = [{"id": 1, "data_criacao": "2030-10-01T10:00:00", "prazo": "2030-10-02T10:00:00"}]
    resultado = analyze_tasks(tasks)
    assert resultado["tempo_medio_conclusao_horas"] == 0.0
"""
with open('tests/test_harness.py', 'w', encoding='utf-8') as f:
    f.write(test_harness_code)

# 5. Executar os testes forçando o reconhecimento do diretório atual
!python -m pytest tests/test_harness.py -v
