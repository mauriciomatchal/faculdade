class Node:
    def __init__(self, value):
        self.value = value
        self.prox = None
    def show_node(self):
        return f'{self.value}'
class LinkedList:
    def __init__(self):
        self.head = None
    def append_last(self, node):
        if self.head is not None:  # checks if the list is not empty
            temp = self.head  # creates a pointer to the first element called "temp"
            while True:
                if temp.prox is None:  # if the list has only one element
                    temp.prox = node  # the next element is "node"
                    break
                temp = temp.prox
                # if there is another element after 1 the temp now points to this number
        else:
            self.head = node
            # if the list is empty the first is x
    def show(self):
        if self.head is not None:
            temp = self.head
            print('*** Lista ***')
            while temp is not None:
                print(f'{temp.show_node()}')
                temp = temp.prox
    def create_cycle(self):
        if self.head is not None:
            temp = self.head
            temp2 = self.head.prox
            while temp is not None:
                if temp.prox is None:
                    temp.prox = temp2
                    break
                temp = temp.prox
    def set_prox(self, pos):
        if self.head is not None:
            temp = self.head
            temp_pos = self.head
            for _ in range(pos-1):
                temp_pos = temp_pos.prox
            while temp is not None:
                if temp.prox is None:
                    temp.prox = temp_pos
                    break
                temp = temp.prox
    def check_cycle(self):
        temp_1 = self.head
        temp_2 = self.head.prox
        while temp_2 is not None:
            if temp_1 == temp_2:
                print('Clico')
                break
            temp_1 = temp_1.prox
            temp_2 = temp_2.prox.prox
            #The second pointer moves twice the speed of the first one
        if temp_2 is None:
            print('Clico nao encontrado')
#
def main():
    obj_list = LinkedList()
    obj_list.append_last(Node(1))
    obj_list.append_last(Node(2))
    obj_list.append_last(Node(3))
    obj_list.append_last(Node(4))
    obj_list.append_last(Node(5))
    obj_list.create_cycle()
    obj_list.check_cycle()
#
if __name__ == '__main__':
    main()
