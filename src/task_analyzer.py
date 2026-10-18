from typing import List, Dict, Any
from datetime import datetime

class TaskValidationError(Exception):
    """Exceção customizada levantada para dados de tarefas inconsistentes."""
    pass

def analyze_tasks(tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    total_tarefas = len(tasks)
    
    # Prevenção para casos de entradas vazias
    if total_tarefas == 0:
        return {
            "total_tarefas": 0,
            "total_concluidas": 0,
            "total_pendentes": 0,
            "tempo_medio_conclusao_horas": 0.0,
            "taxa_atraso_percentual": 0.0,
            "tempo_medio_por_prioridade": {}
        }
        
    total_concluidas = 0
    total_pendentes = 0
    tarefas_atrasadas = 0
    tempo_total_horas = 0.0
    
    tempos_prioridade: Dict[str, List[float]] = {"Alta": [], "Média": [], "Baixa": []}
    
    for task in tasks:
        # Validação de datas inconsistentes
        if task.get("data_conclusao"):
            criacao = datetime.fromisoformat(task["data_criacao"])
            conclusao = datetime.fromisoformat(task["data_conclusao"])
            
            if conclusao < criacao:
                raise TaskValidationError("A data de conclusão não pode ser anterior à data de criação.")
                
            total_concluidas += 1
            horas_decorridas = (conclusao - criacao).total_seconds() / 3600
            tempo_total_horas += horas_decorridas
            
            prioridade = task.get("prioridade", "Média")
            if prioridade in tempos_prioridade:
                tempos_prioridade[prioridade].append(horas_decorridas)
                
        else:
            total_pendentes += 1
            if task.get("prazo"):
                prazo = datetime.fromisoformat(task["prazo"])
                if datetime.now() > prazo:
                    tarefas_atrasadas += 1

    # Cálculos com prevenção de divisão por zero
    tempo_medio_conclusao_horas = (tempo_total_horas / total_concluidas) if total_concluidas > 0 else 0.0
    taxa_atraso_percentual = (tarefas_atrasadas / total_tarefas) * 100 if total_tarefas > 0 else 0.0
    
    tempo_medio_por_prioridade = {
        prioridade: (sum(tempos) / len(tempos)) if tempos else 0.0
        for prioridade, tempos in tempos_prioridade.items()
    }

    return {
        "total_tarefas": total_tarefas,
        "total_concluidas": total_concluidas,
        "total_pendentes": total_pendentes,
        "tempo_medio_conclusao_horas": tempo_medio_conclusao_horas,
        "taxa_atraso_percentual": taxa_atraso_percentual,
        "tempo_medio_por_prioridade": tempo_medio_por_prioridade
    }
