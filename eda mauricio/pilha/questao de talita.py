class Element:
    def __init__(self, value):
        self.value = value 
        self.prox = None

    def showNode(self):
        return (self.value)

class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def insert(self, no):
        node = Element(no)
        if self.top is None:
            self.top = node
            self.size += 1
        else:
            node.prox = self.top
            self.top = node
            self.size += 1
    def remove(self):
        if self.top is None:
            print("pilha vazia")
        else:
            self.top = self.top.prox
    

    def show(self):
        if self.top is not None:
            temp = self.top
            print('**LISTA**')
            while temp is not None:
                print(temp.showNode())
                temp = temp.prox

    def expValidator(self, expression):
    #args as a list w the symbols going this way -->
        for i in expression:
            if (i == "(") or (i == "[") or (i == "{"):
                self.insert(i)  
            else:
                if (i == ")") and (self.top.value == "("):
                    self.remove()
                elif (i == "]") and (self.top.value == "["): 
                    self.remove()
                elif (i == "}") and (self.top.value == "{"): 
                    self.remove()           
        if self.top is None:
            print("expressão válida")
        else:
            print("expressão inválida")

    
   

def main():
    List = Stack()
    List.expValidator(["[", "]", "(", "]"])
    List.show()

if __name__ == '__main__':
    main()