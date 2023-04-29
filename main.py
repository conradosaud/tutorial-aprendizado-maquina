import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model

# Lê o arquivo CSV contendo os dados do estudante
data = pd.read_csv("student-mat.csv", sep=";")

# Seleciona as colunas relevantes para o modelo
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

# Define a variável alvo a ser prevista
predict = "G3"

# Separa os dados de entrada e de saída em duas variáveis distintas
X = np.array( data.drop([predict], axis=1 ) )
y = np.array( data[predict] )

# Separa os dados em conjuntos de treinamento e teste
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

# Cria um modelo de regressão linear
linear = linear_model.LinearRegression()

# Treina o modelo com os dados de treinamento
linear.fit( x_train, y_train )

# Calcula a acurácia do modelo com os dados de teste
acc = linear.score( x_test, y_test )
print(acc)

print("Coeficiente: ", linear.coef_)
print("Interceptação: ", linear.intercept_)

# Printa os resultados e a previsão em tempo real
predictions = linear.predict(x_test)
for i in range(len(predictions)):
    print(predictions[i], x_test[i], y_test[i])