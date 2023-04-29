# Estudo de Aprendizado de Máquina

Este é meu repositório para estudar aprendizado de máquina na prática do zero, usando Python.

Estou seguindo o curso __Python Machine Learning__ do canal _Tech With Tim_
- [Acessar playlist](https://www.youtube.com/playlist?list=PLzMcBGfZo4-mP7qA9cagf68V06sko5otr)

## Ambiente de desenvolvimento

Para este projeto, está sendo usado os seguintes ambientes:
- [PyCharm](https://www.jetbrains.com/pycharm/): IDE para desenvolvimento em Python (usada no curso)
- [Anaconda3](https://www.anaconda.com/): pacote de ciência de dados (NumPy, Pandas, Matplotlib, etc) com IDE integrada (Jupyter, embora não seja usado neste projeto) e ambientes virtuais.

### Adicionar Anaconda no PATH do Windows

Para que o acesso ao Anaconda se torne mais fácil, é recomendável adiciona-lo ao PATH do Windows.
- Abra o terminal do Anaconda depois de instalado
- Use o comando ``where conda``
- Adicione os três caminhos no PATH, que são ``C:\...\anaconda3\Library``, ``C:\...\anaconda3\Scripts`` e ``C:\...\anaconda3``, sendo "..." o caminho do seu computador.
- Para verificar se foi adicionado corretamente, basta rodar no CMD o comando ``conda --version``.

## Criando o ambiente virtual

Depois de criado o ambiente de desenvolvimento, vamos criar um ambiente virtual. Este ambiente virtual serve para manter todas as dependências do repositório organizadas.

```conda create -n tensor python-3.11```

Este ambiente está sendo chamado de __tensor__ para fazer referência ao __TensorFlow__, que é uma plataforma de construção e treinamento de modelos de aprendizado de máquina e redes neurais mais usadas. É a base do projeto.

Lembre-se de verificar sua versão do Python e acessar o site do [TensorFlow](https://www.tensorflow.org/) e verificar em [releases](https://github.com/tensorflow/tensorflow/releases) qual é a versão suportada do Python (neste caso, estou usando o Python 3.11 e o TensorFlow tem suporte a ele).

Em seguida, para iniciar o ambiente virtual:

```activate tensor```

### Dependências

Ao usar o comando `activate` do Anaconda, todas as dependências serão adicionadas também.

Mas se for montar do zero o projeto sem usar esse repositório, será necessário usar o _PIP_ para instalar alguns pacotes, que são:
- [TensorFlow](https://www.tensorflow.org/) (`pip install tensorflow`): ambiente de desenvolvimento de aprendizado de máquina. A instalação desse pacote pode demorar.
- [Pandas](https://pandas.pydata.org/) (`pip install pandas`): pacote de análise da dados e DataFrames
- [scikit-learn](https://scikit-learn.org/stable/) (`pip install -U scikit-learn`): para importação dos algoritmos de aprendizado de máquina

Vale lembrar que no tutorial do _Tech With Tim_ e em outros tutoriais mais antigos, é instalado o _SKLearn_ invés do scikit-learn. Agora é usado o scikit-learn. Além disso, outros pacotes, como o _NumPy_ e _Keras_ já vem instalado por padrão e não precisa ser baixado.
\- _Lembre-se de instalar todos esses pacotes no ambiente virtual._

## Configurar ambiente virtual no PyCharm

Depois de criado o ambiente virtual e instalado as dependências, ainda é necessário vincular o editor do PyCharm ao ambiente virtual que foi criado.

File __>__ Settings __>__ Project:_nome do projeto_

- Em _Project Interpreter_, altere a versão do Python para a versão do seu TensorFlow se for necessário.
- Clicar ao lado direito em _Add Interpreter_ __>__ _Add Local Interpreter_
- No menu esquerdo, selecionar _Conda Environment_
- Selecionar a opção _Use existing environment_ e selecionar o ambiente virtual __tensor__
- Se o item anterior não funcionar, basta navegar pelas pastas até encontrar o ambiente virtual

Após fazer isso, basta escrever o seguinte script no arquivo _main.py_:

```
import tensorflow
import keras
```

Se não acontecer nenhum erro, quer dizer que o ambiente já está rodando e já está preparado.

## Base de dados

Para testar os algoritmos de aprendizado de máquina é necessário ter uma base de dados sólida que possamos trabalhar. Existem bases espalhadas na internet, mas o site [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) é uma boa opção para encontrar base de dados para trabalhar com aprendizado de máquina.

Neste repositório, estou usando o [Student Performance Data Set](https://archive.ics.uci.edu/ml/datasets/Student+Performance), uma base de dados que abordam o desempenho dos alunos no ensino secundário de duas escolas portuguesas, e que são bons para trabalhar treinando os modelos.