
# SDD Task Analyzer - Bootcamp III

## Visão Geral
O **TaskAnalyzer** é um módulo em Python desenvolvido para analisar métricas de produtividade com base numa lista de tarefas. Este projeto faz parte do Desafio da Entrega Intermediária (Fase 2) da disciplina Bootcamp III. 

A aplicação foi construída seguindo um ciclo de desenvolvimento assistido por Inteligência Artificial, guiado estritamente por um Contrato de Negócio (SDD) e Regras de Contexto (Context Rules), garantindo um código limpo, validado e com 100% de cobertura de testes.

## Estrutura do Repositório
- `src/` - Contém o código-fonte da aplicação (`task_analyzer.py`), com tipagem forte e tratamento de exceções.
- `tests/` - Contém a suíte de testes automatizados (`test_harness.py`) implementada com `pytest`.
- `specs/` - Contém a especificação original do contrato SDD e os cenários de aceite (BDD).
- `CONTEXT_RULES.md` - Diretrizes de governança arquitetural e restrições aplicadas ao assistente de IA.

## Requisitos
Para executar este projeto localmente, precisas de ter instalado:
- Python 3.11 ou superior
- `pytest` (>= 7.0.0)

## Instruções de Execução

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/SEU-USUARIO/sdd-task-analyzer.git
   cd sdd-task-analyzer
   ```

2. **Criar um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows utiliza: venv\Scripts\activate
   ```

3. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Executar a Suíte de Testes (Test Harness):**
   A validação do sistema é feita através de testes automatizados que cobrem cenários de sucesso, exceções (datas inconsistentes) e casos de borda (prevenção de divisão por zero).
   Para executar, utiliza o comando:
   ```bash
   python -m pytest tests/test_harness.py -v
   ```

## Status do Build
- **Testes Automatizados:** 100% Passed :white_check_mark:
- **Homologação:** Revisão humana concluída via Pull Request documentado.
