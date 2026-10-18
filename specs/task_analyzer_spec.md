# Especificação TaskAnalyzer - Contrato de Negócio (SDD)

## 1. Visão Geral e Propósito
O TaskAnalyzer é um módulo avançado focado na análise de métricas e produtividade[cite: 8]. Ele tem como propósito principal processar listas de tarefas executadas para gerar indicadores valiosos de desempenho[cite: 8]. O sistema será responsável pelo cálculo exato do tempo médio de conclusão das tarefas, determinação da taxa de atraso (tarefas finalizadas após o prazo estipulado) e a consolidação de todos esses indicadores segmentados por prioridade (baixa, média e alta)[cite: 8].

## 2. Contrato Executável de Interface

### Entradas (Inputs)
- **id:** Inteiro (int) ou String. Identificador único da tarefa[cite: 8].
- **titulo:** String. Nome ou descrição curta da tarefa[cite: 8].
- **prioridade:** String. Nível de importância: "baixa", "média" ou "alta"[cite: 8].
- **data_criacao:** Datetime / String. Data e hora de registro da tarefa[cite: 8, 9].
- **data_conclusao:** Datetime / String. Data e hora em que a tarefa foi finalizada[cite: 9].
- **prazo_limite:** Datetime / String. Data limite estipulada para a entrega[cite: 9].
- **status:** String. Estado atual da tarefa (ex: "concluída", "pendente")[cite: 9].

### Saídas (Outputs)
- **tempo_medio_conclusao:** Float (Horas/Dias). Tempo médio geral gasto nas tarefas concluídas[cite: 9].
- **taxa_atraso_geral:** Float (Porcentagem). Percentual de tarefas concluídas após o prazo limite[cite: 9].
- **metricas_por_prioridade:** Dicionário (Dict). Agrupamento contendo tempo médio e taxa de atraso específicos para prioridades "baixa", "média" e "alta"[cite: 9].

## 3. Regras de Negócio e Restrições
- O processamento deve considerar apenas tarefas com status "concluída"[cite: 10]. Tarefas pendentes devem ser ignoradas no cálculo das métricas[cite: 10].
- A data de conclusão não pode ser cronologicamente anterior à data de criação (datas inconsistentes invalidam a entrada)[cite: 10].
- O sistema deve implementar proteções para evitar divisão por zero em cenários onde não haja tarefas concluídas no conjunto de dados[cite: 10].

## 4. Cenários de Aceite (BDD)

### Cenário 1 (Sucesso - Métricas Corretas)
**Dado** um conjunto válido de tarefas com diferentes níveis de prioridade, prazos definidos e status mistos (concluídas e pendentes)[cite: 10].
**Quando** o analisador de tarefas for executado sobre este conjunto[cite: 10].
**Então** o sistema deve retornar as métricas exatas, englobando o tempo médio de conclusão geral e por prioridade, a correta taxa de atraso e o volume adequado de tarefas processadas para cada prioridade[cite: 10].

### Cenário 2 (Exceção/Erro - Entradas Inválidas)
**Dado** uma entrada de dados contendo anomalias, como tarefas cuja data de conclusão seja anterior à data de criação, ou um conjunto sem nenhuma tarefa concluída (risco de divisão por zero)[cite: 10].
**Quando** o analisador de tarefas for executado[cite: 10].
**Então** o sistema deve interceptar o erro e disparar uma exceção específica e tratada, acompanhada de uma mensagem de erro clara direcionada ao usuário ou aos logs do sistema[cite: 10].
