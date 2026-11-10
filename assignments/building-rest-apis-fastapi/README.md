# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI, organizando recursos em endpoints e usando métodos HTTP, validação de dados e códigos de status. Ao final, você terá uma API para cadastrar e gerenciar tarefas em memória.

## 📝 Tarefas

### 🛠️ Implementar Rotas de Leitura

#### Descrição
Prepare o ambiente e complete em `main.py` as rotas que permitem consultar as tarefas cadastradas.

#### Requisitos
O programa concluído deve:

- Instalar as dependências listadas em `requirements.txt` e iniciar a aplicação com `uvicorn main:app --reload`.
- Implementar `GET /tasks` para retornar a lista de tarefas.
- Implementar `GET /tasks/{task_id}` para retornar uma tarefa pelo identificador ou responder com o código `404` se ela não existir.
- Permitir consultar a documentação interativa da API em `/docs`.

### 🛠️ Criar e Atualizar Tarefas

#### Descrição
Implemente os endpoints para cadastrar uma tarefa e substituir seus dados, usando os modelos Pydantic definidos no código inicial.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para criar uma tarefa com identificador único e responder com o código `201`.
- Validar os dados de entrada com os modelos Pydantic; cada tarefa deve ter título, descrição e estado de conclusão.
- Implementar `PUT /tasks/{task_id}` para substituir os dados de uma tarefa existente e responder com `404` quando o identificador não existir.
- Retornar a tarefa criada ou atualizada no corpo da resposta.

### 🛠️ Remover e Verificar Tarefas

#### Descrição
Complete a operação de remoção e verifique os endpoints usando a documentação interativa do FastAPI.

#### Requisitos
O programa concluído deve:

- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa existente e responder com o código `204`, sem conteúdo na resposta.
- Responder com `404` ao tentar remover uma tarefa inexistente.
- Usar `/docs` para testar os fluxos de criação, consulta, atualização e remoção, incluindo os códigos de status e a validação de dados.
- Manter os dados em memória durante a execução do servidor; não é necessário usar um banco de dados.
