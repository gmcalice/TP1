import statistics
import math
import numpy as np

#recebe os pontos
pontos = np.array()
def arvorekd(pontos, depth):

dim = #quantidade de dimensoes do ponto
#Se o conjunto de pontos só tem 1 ponto restante, retorna a folha que contém esse ponto (nó raiz)
  if(pontos.len == 1):
    return lista[1]

#Vai fazendo a mediana dependendo de qual iteração está (o que muda é a dimensão em que está fazendo a mediana)
#Nos nós serão armazenados as medianas e nas folhas esse ponto que restou 
#Cada iteração indica em qual profundidade está (depth)
#Fazer o mod pra saber em qual dimensão fazer a mediana
  elif(depth % dim == 0):
    #faz a mediana. Ordena o vector pela dimensão que vai fazer a mediana, se tiver um número par de pontos, faz a media dos dois do meio, se tivr um número ímpar, pega o do meio
 #Depois de fazer a mediana, vão ser criados dois grupos, da esquerda e da direita, por exemplo e chama a função novamente para agora fazer a mediana de um desses grupos, até que reste apenas um ponto.
 #Chama a função para o outro grupo (para chamar um dos lados, usar a classe que representa cada nó - ver a seguir) e faz isso até que todos os pontos tenham sido adicionados na árvore.


#Vai ter uma classe que represente cada nó, com o seu valor e nó que está a direita e a esquerda. Para chamar os grupos mencionados anteriormente, basta chamar a função para esse nó da esquerda ou direita.
