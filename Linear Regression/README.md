# Linear Regression (Regressão Linear)

O algoritmo de regressão linear é um dos algoritmos de aprendizado de máquina mais simples e básicos.
Ele é usado para modelar a relação entre uma __variável dependente__ (também chamada de variável de resposta ou target) e uma ou mais __variáveis independentes__ (também chamadas de recursos ou features).

O objetivo do algoritmo de regressão linear é encontrar a melhor linha reta que se ajuste aos dados. A linha reta é representada pela equação `y = mx + b` onde `y` é a variável dependente, `x` é a(s) variável(is) independente(s), `m` é a inclinação da linha e `b` é a intercepção no eixo `y`.

O processo de treinamento do modelo de regressão linear envolve o ajuste dos valores de `m` e `b` para minimizar a diferença entre as previsões do modelo e os valores reais da variável dependente nos dados de treinamento. Isso é feito usando o método dos _mínimos quadrados_.

O algoritmo de regressão linear é usado principalmente para problemas de regressão, ou seja, problemas em que a variável dependente é contínua e não discreta. Ele pode ser usado para prever valores futuros de uma variável, encontrar a relação entre as variáveis independentes e dependentes, e também para identificar a importância relativa de cada variável independente no resultado final.

## Base de dados

Para testar este algoritmo, estou usando o [Student Performance Data Set](https://archive.ics.uci.edu/ml/datasets/Student+Performance), uma base de dados que abordam o desempenho dos alunos no ensino secundário de duas escolas portuguesas, e que são bons para trabalhar treinando os modelos.

## Aplicação prática

Na prática, o algoritmo de regressão linear neste repositório foi usado para __prever o desempenho final de um aluno__, (que no caso, é a _variável dependente_ `G3`) com base em variáveis como as notas nos dois primeiros períodos (variáveis `G1` e `G2`), tempo de estudo semanal (variável `studytime`), número de reprovações (variável `failures`) e número de faltas (variável `absences`), sendo essas últimas citadas, as _variáveis independentes_.

A regressão linear funciona criando uma linha reta que melhor se ajusta aos dados de entrada `X` e saída `y`. Essa linha é então usada para fazer previsões em novos dados. No caso do código, a função `linear.fit(x_train, y_train)` treina o modelo com os dados de treinamento, ajustando a linha de regressão linear aos dados. A acurácia do modelo é então avaliada nos dados de teste usando a função `linear.score(x_test, y_test)`.

Depois de treinado, o modelo é usado para prever o desempenho final de um aluno com base nos valores de entrada de suas notas nos dois primeiros períodos, tempo de estudo semanal, número de reprovações e número de faltas. A linha de regressão linear é usada para calcular a saída prevista para cada conjunto de valores de entrada. A precisão dessas previsões pode ser verificada comparando as previsões com os valores reais usando a função `print(predictions[i], x_test[i], y_test[i])`.