class Node:
    def __init__(self, value):
        self.value = value
        self.prox = None
    def show_node(self):
        return f'{self.value}'
class Queue:
    def __init__(self):
        self.head = None
    def show(self):
        a = ''
        if self.head is None:
            print('Empty List')
        else:
            temp = self.head
            while temp is not None:
                a += f'{temp.show_node()}' + ' '
                temp = temp.prox
            print(a)
    
    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.prox is not None:
                temp = temp.prox
            temp.prox = node
    def out(self):
        if self.head is None:
            print('Empty List')
        else:
            self.head = self.head.prox
    def get_first_element(self):
        return self.head.value
def main():
    times = int(input())
    
    quantum, max_up = input().split()
    quantum = int(quantum)
    max_up = int(max_up)

    id_input = input().split()
    process_ids = Queue()
    for x in id_input:
        process_ids.add(int(x))
        
    ups_input = input().split()
    process_ups = Queue()
    for x in ups_input:
        process_ups.add(int(x))
        
    def next_round(up, id):
        process_ups.out()
        process_ids.out()
        process_ups.add(up)
        process_ids.add(id)
    def both_out():
        process_ids.out()
        process_ups.out()
    def both_show():
        process_ids.show()
        process_ups.show()
    def calculate(max_up): 
        while max_up != 0:
            id = process_ids.get_first_element()
            up = process_ups.get_first_element()
            if up < max_up:
                if max_up < quantum:
                    both_out()
                    both_show()
                    max_up = 0
                else:
                    if up > quantum:
                        up -= quantum    
                        next_round(up, id)
                        max_up -= quantum
                    else:
                        both_out()
                        max_up -= up
            else:
                if up > quantum:
                    if max_up > quantum:
                        up -= quantum
                        next_round(up, id)
                        max_up = max_up - quantum
                    else:
                        up -= max_up
                        next_round(up, id)
                        both_show()
                        max_up = 0
                else:
                    up -= max_up
                    next_round(up, id)
                    both_show()
                    max_up = 0
    calculate(max_up) 
if __name__ == '__main__':
    main()

