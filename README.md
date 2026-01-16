# 🚀 SQLite to Excel - Automação de Relatórios

Este projeto nasceu de uma necessidade real do meu dia a dia de trabalho.

Antes, o controle de abastecimentos era feito de forma **manual**, criando e atualizando planilhas no Excel para acompanhar:
- Veículos
- Setores
- Datas
- Valores de abastecimento

Esse processo, além de **demorado**, estava sujeito a **erros humanos** e retrabalho.

## 💡 A Solução

Criei este projeto em Python para **automatizar completamente** esse processo:

- O sistema:
  - Conecta em um banco de dados SQLite
  - Executa consultas SQL
  - Organiza os dados usando Pandas
  - Gera automaticamente planilhas Excel prontas para uso

Agora, em vez de montar relatórios manualmente, basta **executar o script** e os arquivos são gerados em segundos.

---

## ⚙️ Tecnologias utilizadas

- Python
- SQLite
- Pandas
- OpenPyXL
- Pytest (para testes automatizados)
- GitHub Actions (CI)

---

## 📊 O que este projeto faz hoje

- ✅ Gera relatório de abastecimentos por data
- ✅ Gera lista de veículos abastecidos
- ✅ Exporta os dados automaticamente para Excel (`.xlsx`)
- ✅ Possui testes automatizados
- ✅ Possui pipeline de Integração Contínua (CI) com GitHub Actions

---

## 🗂️ Estrutura do projeto

