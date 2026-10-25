import pytest
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
