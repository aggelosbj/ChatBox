from decimal import Decimal, getcontext
import queue
import math
import time

class Node:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.children = []
        self.operation = ""
        self.depth = 0

    def add_children(self, val_bd):
        getcontext().prec = 12
        
        if isinstance(val_bd, Decimal):
            new_root_child = Node(val_bd.sqrt())
            new_root_child.parent = self
            new_root_child.operation = "square root"
            new_root_child.depth = self.depth + 1

            val_bi = int(val_bd)
            int_val = int(val_bd)

            if int_val < 300000:
                subtracted_val = val_bd - Decimal(val_bi)
                epsilon = Decimal('0.00000001')

                if subtracted_val < epsilon:
                    fact_bi = self.factorial(int_val)
                    fact_bd = Decimal(fact_bi)
                    new_factorial_child = Node(fact_bd)
                    self.children.append(new_factorial_child)
                    new_factorial_child.parent = self
                    new_factorial_child.operation = "factorial"
                    new_factorial_child.depth = self.depth + 1

            new_floor_child = Node(int(val_bi))
            new_floor_child.parent = self
            new_floor_child.operation = "floor"
            new_floor_child.depth = self.depth + 1

            self.children.append(new_root_child)
            self.children.append(new_floor_child)

    def factorial(self, num):
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial

    def clear_children(self):
        self.children = []

def breadth_first_search(target_num, root_node):
    start_time = time.time()
    num = Decimal(target_num)
    queue_waiting = queue.Queue()
    queue_waiting.put(root_node)

    while not queue_waiting.empty():
        curr_node = queue_waiting.get()
        curr_node.add_children(curr_node.value)

        if curr_node.value == num:
            print("Search complete!")
            elapsed_time = time.time() - start_time
            print(f"Search time: {elapsed_time} seconds")
            print(f"Depth: {curr_node.depth}")
            return curr_node
        else:
            for child in curr_node.children:
                queue_waiting.put(child)

    return None

def iterative_deepening_search(target_num, root_node, max_depth):
    found_node = None
    for depth in range(max_depth + 1):
        root_node.clear_children()
        found_node = depth_limited_search(root_node, target_num, depth)
        if found_node is not None:
            return found_node
    return None

def depth_limited_search(node, target_num, max_depth):
    start_time = time.time()
    num = Decimal(target_num)
    stack = [node]

    while stack:
        curr_node = stack.pop()
        curr_node.add_children(curr_node.value)

        if curr_node.value == num:
            print("Search complete!")
            elapsed_time = time.time() - start_time
            print(f"Search time: {elapsed_time} seconds")
            print(f"Depth: {curr_node.depth}")
            return curr_node

        if curr_node.depth < max_depth:
            stack.extend(curr_node.children)

    return None

def main():
    chosen_algorithm = 0
    target_num = 0
    operations_list = []
    root_node = Node(4)
    root_node.depth = 0

    print("Choose an algorithm for the search:")
    print("Search Algorithm 1: Breadth First Search")
    print("Search Algorithm 2: Iterative Deepening Search")
    chosen_algorithm = int(input())

    while True:
        if chosen_algorithm != 1 and chosen_algorithm != 2:
            print("Only 2 algorithms are available. Choose 1 or 2")
            chosen_algorithm = int(input())
        else:
            break

    print("Enter the target number:")
    target_num = int(input())

    if chosen_algorithm == 1:
        found_node = breadth_first_search(target_num, root_node)

        if found_node is not None:
            while found_node.parent is not None:
                operations_list.append(found_node.operation)
                found_node = found_node.parent
            operations_list.reverse()
            for operation in operations_list:
                print(operation)
        else:
            print("Result not found")

    elif chosen_algorithm == 2:
        print("Enter the maximum search depth:")
        max_depth = int(input())
        found_node = iterative_deepening_search(target_num, root_node, max_depth)

        if found_node is not None:
            while found_node.parent is not None:
                operations_list.append(found_node.operation)
                found_node = found_node.parent
            operations_list.reverse()
            for operation in operations_list:
                print(operation)
        else:
            print("Result not found")

if __name__ == "__main__":
    main()
