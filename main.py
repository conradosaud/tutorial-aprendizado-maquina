import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

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
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

# Treina o modelo e salva o melhor resultado
# defineMelhorModelo()

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

print("Acurácia: ", linear.score(x_train, y_train))
print("Coeficiente: ", linear.coef_)
print("Interceptação: ", linear.intercept_)

# Printa os resultados e a previsão em tempo real
#predictions = linear.predict(x_test)
#for i in range(len(predictions)):
#    print(predictions[i], x_test[i], y_test[i])

# mostraGrafico()

def mostraGrafico():
    p = "G1"
    style.use("ggplot")
    pyplot.scatter(data[p], data["G3"])
    pyplot.xlabel(p)
    pyplot.ylabel("Final Grade")
    pyplot.show()

def defineMelhorModelo():
    best_acc = 0
    for _ in range(30):

        # Separa os dados em conjuntos de treinamento e teste
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

        # Cria um modelo de regressão linear
        linear = linear_model.LinearRegression()

        # Treina o modelo com os dados de treinamento
        linear.fit(x_train, y_train)

        # Calcula a acurácia do modelo com os dados de teste
        acc = linear.score(x_test, y_test)
        print(acc)

        if acc > best_acc:
            best_acc = acc
            with open("studentmodel.pickle", "wb") as f:
                pickle.dump(linear, f)

    print("Melhor acurácia: ", best_acc)