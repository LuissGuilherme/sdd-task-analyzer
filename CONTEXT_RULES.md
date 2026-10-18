Diretrizes Arquiteturais (Obrigatórias)
Linguagem e Versão: O código deve ser implementado obrigatoriamente utilizando Python 3.11 ou versão superior.
Tipagem: É imperativo o uso de type hints (anotações de tipo) nativas do Python em todas as assinaturas de funções, métodos e variáveis complexas.
Boas Práticas e Clean Code: O desenvolvimento deve seguir o padrão PEP 8. As funções devem ser concebidas sob o princípio da Responsabilidade Única (SRP): pequenas, altamente coesas e focadas num objetivo estrito.
Documentação: Obrigatoriedade do uso de docstrings sob o padrão Google Style para todos os módulos, classes, métodos e funções geradas.
Tratamento de Exceções: Exceções devem ser capturadas ou levantadas de forma específica (evitar except Exception: genérico), com mensagens de erro autoexplicativas.
Logs: A rastreabilidade deve ser feita utilizando o módulo nativo logging do Python, estruturado adequadamente (INFO, WARNING, ERROR).

Proibições Explícitas (Regras Restritivas)
NÃO utilizar ou importar bibliotecas e pacotes externos (ex: Pandas, Numpy) não autorizados expressamente (preferir a biblioteca padrão do Python).
NÃO alterar, adaptar ou ignorar os cenários de teste pré-definidos no documento de Especificação.
NÃO modificar a estrutura e a nomenclatura das pastas e arquivos definida para a árvore do repositório.
NÃO inserir lógicas para persistência de dados em arquivos físicos (CSV, JSON, TXT) ou em bancos de dados relacionais/NoSQL. O processamento deve ocorrer em memória.
NÃO alterar a assinatura (nome, ordem ou tipo de parâmetros) das funções e métodos públicos descritos no contrato de interface.
NÃO gerar implementações de novas funcionalidades sem que existam testes automatizados correspondentes cobrindo-as.
NÃO introduzir trechos de código duplicado, inalcançável ou desnecessário.
NÃO assumir, inferir ou "alucinar" comportamentos lógicos que não estejam explicitamente documentados no contrato de negócio.
