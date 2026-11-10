# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Pratique o uso de strings, listas, loops, condicionais e entrada de dados ao criar uma versão em Python do jogo da Forca.

## 📝 Tarefas

### 🛠️ Preparar e Exibir a Palavra

#### Descrição
Complete o código inicial em `starter-code.py` para selecionar uma palavra secreta e exibir o progresso da palavra enquanto o jogador tenta adivinhá-la.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista predefinida em `words`.
- Inicializar as variáveis necessárias para registrar as letras adivinhadas e o limite de tentativas incorretas.
- Exibir cada letra já adivinhada na posição correspondente e um sublinhado para cada letra ainda não descoberta, por exemplo: `_ _ _`.

### 🛠️ Processar Palpites e Concluir a Partida

#### Descrição
Implemente o loop principal do jogo para receber palpites, atualizar o estado da partida e informar o resultado ao jogador.

#### Requisitos
O programa concluído deve:

- Solicitar ao jogador um palpite de letra e verificar se ela aparece na palavra secreta.
- Atualizar e exibir o progresso quando o palpite estiver correto.
- Reduzir e exibir o número de tentativas incorretas restantes quando o palpite estiver incorreto.
- Encerrar a partida quando o jogador adivinhar a palavra ou esgotar as tentativas.
- Exibir uma mensagem de vitória ou derrota e, em caso de derrota, revelar a palavra secreta.
