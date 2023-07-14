from .Node import Node

class Tree:
    def __init__(self):
        self.root = None
        
    def set_root(self, node:Node):
        self.root = node
        
    def add(self, node:Node, parent:int):
        if self.root != None:
            queue = [self.root]
            while len (queue) >0:
                queue = queue + queue[0].children
                tmp=queue[0]
                queue= queue[1:]
                if tmp.id == parent:
                    tmp.children.append(node)
        else:
            self.set_root(node)
      
    '''        
    usado apenas para printar a árvore para 
    utiliza método de busca em largura para para printar   
    def print (self):
        if self.root != None:
            queue = [self.root]
            while len (queue) > 0:
                queue = queue + queue[0].children
                tmp = queue[0]
                queue = queue[1:]
                print (str(tmp.id)+" - "+str([x.id for x in tmp.children]))
                
    #chamar add
    '''