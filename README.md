# 🏆 Rastreador de Platinas (Trophy Tracker)

Bem-vindo ao **Rastreador de Platinas**! Este é um projeto em Python desenvolvido para auxiliar jogadores a gerenciar seu progresso em busca da completude total (100% ou "Platina") de seus jogos favoritos.

O sistema permite marcar conquistas realizadas, salvar o progresso automaticamente e calcular exatamente quais troféus ainda faltam para finalizar o jogo.

## 📋 Funcionalidades

* **Catálogo de Jogos:** Biblioteca pré-definida com jogos populares (Hollow Knight, Elden Ring, Dark Souls, etc.).
* **Persistência de Dados:** O progresso é salvo automaticamente em um arquivo `JSON`, garantindo que você não perca seus dados ao fechar o programa.
* **Comparação Inteligente:** Utiliza lógica de conjuntos para filtrar e exibir apenas as conquistas que o usuário **ainda não** desbloqueou.
* **Sistema de Sugestões:** Permite que o usuário sugira novos jogos, salvando o feedback em um arquivo de texto.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Bibliotecas Padrão:**
    * `json`: Para serialização e persistência dos dados do usuário.
    * `os`: Para verificação e manipulação de arquivos do sistema.
* **Estruturas de Dados:** Uso de Dicionários Aninhados e Conjuntos (Sets) para otimização de busca e comparação.

## 🚀 Como Executar o Projeto

### Pré-requisitos
Você precisa ter o **Python 3.x** instalado em sua máquina. Nenhuma biblioteca externa (`pip install`) é necessária.

### Passo a Passo

1. Clone este repositório ou baixe o arquivo do código.
2. Abra o terminal (ou CMD) na pasta do arquivo.
3. Execute o comando:

```bash
python main.py
