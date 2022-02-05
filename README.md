# Machine Learning Project in Python Step-By-Step
Projeto simples de aprendizado de máquina em Python - passo a passo 

____
O projeto foi totalmente reproduzido e traduzido a partir do site:
[https://machinelearningmastery.com/machine-learning-in-python-step-by-step/](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)

O desenvolvimento deste projeto é apenas para motivos de estudo.
____

Neste tutorial passo a passo você irá:

1. Baixar e instalar o Python SciPy e obter o pacote mais útil para aprendizado de máquina em Python.
2. Carregar um conjunto de dados e entender sua estrutura usando resumos estatísticos e visualização de dados.
3. Criar 6 modelos de aprendizado de máquina, escolhendo o melhor e criando confiança de que a precisão é confiável. 

Se você é um iniciante em aprendizado de máquina e deseja finalmente começar a usar o Python, este tutorial foi projetado para você 
____

Para instalar as dependências necessários você pode rodar o comando 
```
pip install -r requirements.txt
```
Na pasta root deste projeto
____

Um projeto de aprendizado de máquina pode não ser linear, mas possui várias etapas bem conhecidas:

- Defina Problema.
- Preparar Dados.
- Avaliar Algoritmos.
- Melhore os Resultados.
- Resultados atuais.

Este é um bom e conhecido projeto para se iniciar

1. Os atributos são numéricos, então você precisa descobrir como carregar e manipular dados.
2. É um problema de classificação, permitindo que você pratique com talvez um tipo mais fácil de algoritmo de aprendizado supervisionado.
3. É um problema de classificação multi-classe (multi-nominal) que pode exigir algum tratamento especializado.
4. Possui apenas 4 atributos e 150 linhas, o que significa que é pequeno e cabe facilmente na memória (e em uma tela ou página A4).
5. Todos os atributos numéricos estão nas mesmas unidades e na mesma escala, não exigindo nenhuma escala ou transformação especial para começar.
____
### Carregar conjunto de dados

Podemos carregar os dados diretamente do repositório UCI Machine Learning.

Estamos usando pandas para carregar os dados. Também usaremos pandas a seguir para explorar os dados com estatísticas descritivas e visualização de dados.

Observe que estamos especificando os nomes de cada coluna ao carregar os dados. Isso ajudará mais tarde, quando explorarmos os dados. 

Toda essa parte de carregamento de dados é feita através da função ```returnsDataSet()```
____
###  Resuma o conjunto de dados

Agora é hora de dar uma olhada nos dados.

Nesta etapa, vamos dar uma olhada nos dados de algumas maneiras diferentes:

- Dimensões do conjunto de dados.
- Espreite os dados em si.
- Resumo estatístico de todos os atributos.
- Detalhamento dos dados pela variável de classe.

Não se preocupe, cada olhar para os dados é um comando. Estes são comandos úteis que você pode usar repetidamente em projetos futuros. 

O summarize pode ser visualizado no arquivo sumarrize_dataset.py
____
#### Visualização de dados

Agora temos uma ideia básica sobre os dados. Precisamos estender isso com algumas visualizações.

Veremos dois tipos de gráficos:

- Gráficos univariados para entender melhor cada atributo.
- Gráficos multivariados para entender melhor as relações entre os atributos. 

As funções de visualização dos gráficos podem ser visualizadas no arquivo show_graphs.py
____
### Avalie alguns algoritmos

Agora é hora de criar alguns modelos de dados e estimar sua precisão em dados não vistos.

Aqui está o que vamos abordar nesta etapa:

- Separe um conjunto de dados de validação.
- Configure o equipamento de teste para usar a validação cruzada de 10 vezes.
- Construa vários modelos diferentes para prever espécies a partir de medições de flores
- Selecione o melhor modelo. 

A avaliação pode ser acessada no arquivo evaluate_algorithms.py
____
### Fazer previsões

Devemos escolher um algoritmo para usar para fazer previsões.

Os resultados da seção anterior sugerem que o SVM foi talvez o modelo mais preciso. Usaremos este modelo como nosso modelo final.

Agora queremos ter uma ideia da precisão do modelo em nosso conjunto de validação.

Isso nos dará uma verificação final independente sobre a precisão do melhor modelo. É importante manter um conjunto de validação para o caso de você cometer um deslize durante o treinamento, como um ajuste excessivo ao conjunto de treinamento ou um vazamento de dados. Ambas as questões resultarão em um resultado excessivamente otimista. 
____

Cada arquivo pode ser executado individualmente através do comando
```
python nome_arquivo.py
```

Se quiser ver a execução completa, execute:
```
python main.py
```
____
Você não precisa saber como os algoritmos funcionam. É importante conhecer as limitações e como configurar algoritmos de aprendizado de máquina. Mas aprender sobre algoritmos pode vir mais tarde. Você precisa construir esse conhecimento de algoritmo lentamente por um longo período de tempo. Hoje, comece por se familiarizar com a plataforma.

O exercício implementado nesse repositório foi retirado do:
[https://machinelearningmastery.com/machine-learning-in-python-step-by-step/](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
