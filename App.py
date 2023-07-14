import numpy as np
import random
from .Tree import self

#gerador de tabela
'''
  0 - empty
 -1 - o
  1 - x
'''
mat = np.array([0 for x in range(9)]).reshape((3,3))
aux = mat.tolist()
aux[0] + aux [1] + aux[2]


#percorre a árvore
def generate(mat, player, lvl):
    for i in range(mat.size):
        aux = mat.tolist()
        aux = aux[0] + aux [1] + aux[2]
        if aux[i] == 0:
            aux[i]=player
            tmp=np.array(aux).reshape((3,3))
            #print(tmp)
            #print(aux[5])
            #print("-----")
            #input()
            generate(tmp, -player, lvl+1)        
               
#gerar_tb=generate(np.array([0 for x in range(9)]).reshape((3,3)), 1, 1)


#chamar add
#busca em largura
def bfs(self, parent):
  visitados, fila = set(), [parent]
  while fila:
    vertice = self.queue.pop(0)
    if vertice not in visitados:
      visitados.add(vertice)
      fila.extend(self[vertice] - visitados)    
      return visitados 
  input()
busca=bfs(self)

buscar_larg=generate.busca

#desenhar a board
def draw_board(tab, aux):
  print('Escolha onde você jogará:')
  print("-------------")
  print('| 0 | 1 | 2 |')
  print("-------------")
  print('| 3 | 4 | 5 |')
  print("-------------")
  print('| 6 | 7 | 8 |')
  print("-------------")
  
  print('Tabela do jogo: ')
  for i in range(tab.shape[0]):
    for j in range(tab.shape[1]):
      match tab[i,j]:
        case 1:
          aux = 'x'
        case -1:
          aux = 'o'
        case 0:
          aux = ('_') if i<2 else ''
      print( aux + ('|' if j<2 else' '), end="")
    print()
      
#tab = np.matrix([(0,1,2), (3,4,5), (6,7,8)])  
#tab.shape  
#draw_board(aux, tab)

#verificação
def check(aux):
  #verificar quem ganhou
  #linha
  if   (aux[0] == aux[1] and aux[0] == aux[2] == 1):
    return 1
  elif(aux[0] == aux[1] and aux[0] == aux[2] == -1):
    return 2
  elif (aux[3] == aux[4] and aux[3] == aux[5] == 1):
    return 1
  elif(aux[3] == aux[4] and aux[3] == aux[4] == -1):
    return 2
  elif (aux[6] == aux[7] and aux[6] == aux[8] == 1):
    return 1
  elif (aux[6] == aux[7] and aux[6] == aux[8] == -1):
    return 2
  #coluna
  elif (aux[0] == aux[3] and aux[0] == aux[6] == 1):
    return 1
  elif (aux[0] == aux[3] and aux[0] == aux[6] == -1):
    return 2
  elif (aux[1] == aux[4] and aux[1] == aux[7] == 1):
    return 1
  elif (aux[1] == aux[4] and aux[1] == aux[7] == -1):
    return 2
  elif (aux[2] == aux[5] and aux[2] == aux[8] == 1):
    return 1
  elif (aux[2] == aux[5] and aux[2] == aux[8] == -1):
    return 2
  #diagonal
  elif (aux[0] == aux[4] and aux[0] == aux[8] == 1):
    return 1
  elif (aux[0] == aux[4] and aux[0] == aux[8] == -1):
    return 2
  elif (aux[2] == aux[4] and aux[0] == aux[6] == 1):
    return 1 
  elif (aux[2] == aux[4] and aux[0] == aux[6] == -1):
    return 2
  #verificar se não acabou
  elif (aux[0]==0) or (aux[1]==0) or (aux[2]==0) or (aux[3]==0) or (aux[4]==0) or (aux[5]==0) or (aux[6]==0) or (aux[7]==0) or (aux[8]==0):
    return None
  #verificar se empatou
  else:
    return 3

#quando o jogo começa
def play_game():
  #chamar o metodo para gerar a tabela de arvore para percorrer (nao sei fazer esse carai)
  generate.busca
  #ordem aleatoria
  # x - primeiro
  # o - segundo
  order=random.randint(0,1)
  control = 0
  tab = None
  while True:
    if control == order:
      print("player")
      draw_board(tab, aux)
      a=(int(input()))
      #ver moviemento valido
      while (a!=0 or a!=1 or a!=2 or a!=3 or a!=4 or a!=5 or a!=6 or a!=7 or a!=8):
        print('Movimento invalido, jogue novamente:')
        a=(int(input()))
      b=a 
      #adicionar a jogada do player dentro da draw board
      #comparar a draw board com o nó da árvore que é igual
      #fazer a busca
    else:
      print("pc")
      #fazer um metodo para saber qual foi a jogada do player para que a ia saiba escolher onde jogar
              
    control += 1
    if control>1:
      control=0   
    match check(tab):
      #case 0:
       # check(aux)     
      case 1:
        print("player win")
        break
      case 2:
        print("pc win")
        break
      case 3:
        print("empate, fck")    
    input()

#menu do usuário
def menu():
  while True:
    # perguntar para o Edison a diferença de '' e ""
    print('Bem-vindo ao "Jogo da Velha VS IA"...')
    print('Quem começará jogando será sorteado em ordem aleatótia... \n'
          'Deseja começar a partida ?')
    opc=input('[s/n]').strip()      
    while opc!='n' and opc!='s':
      opc=input('Opção inválida, digite sua opção novamente').strip()   
    if opc == 's':
      play_game()
    else:
      print('Ué?')
menu()
