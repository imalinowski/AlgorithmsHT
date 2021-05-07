from queue import Queue
class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0


class AVLTree(object):
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def unbalance(self, node):
        return abs(self.height(node.left) - self.height(node.right)) >= 2

    def root_balance(self):
        return str(self.height(self.root.right)-self.height(self.root.left))
    
    def right_rotate(self, node):
        node_right = node
        node = node.left
        node_right.left = node.right
        node.right = node_right

        self.update_height(node_right)
        self.update_height(node)

        return node

    def left_rotate(self, node):
        node_left = node
        node = node.right
        node_left.right = node.left
        node.left = node_left

        self.update_height(node_left)
        self.update_height(node)

        return node

    def left_right_rotate(self, node):
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)

    def right_left_rotate(self, node):
        node.right = self.right_rotate(node.right)
        return self.left_rotate(node)

    def _insert(self, key, node):
        if node is None:
            node = Node(key)

        elif key < node.key:
            node.left = self._insert(key, node.left)
            if self.unbalance(node):
                if key < node.left.key:  # LL
                    node = self.right_rotate(node)
                else:  # LR
                    node = self.left_right_rotate(node)

        elif key > node.key:
            node.right = self._insert(key, node.right)
            if self.unbalance(node):
                if key < node.right.key:  # LR
                    node = self.right_left_rotate(node)
                else:  # RR
                    node = self.left_rotate(node)

        self.update_height(node)

        return node

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = self._insert(key, self.root)

    def _delete(self, key, node):
        if node == None:
            print("Can't find %d" % key)
            return node

        elif key < node.key:
            node.left = self._delete(key, node.left)
            if self.unbalance(node):  # if right - left > 1
                if self.height(node.right.left) > self.height(node.right.right):
                    node = self.right_left_rotate(node)
                else:
                    node = self.left_rotate(node)
            self.update_height(node)

        elif key > node.key:
            node.right = self._delete(key, node.right)
            if self.unbalance(node):  # if left - right > 1
                if self.height(node.left.right) > self.height(node.left.left):
                    node = self.left_right_rotate(node)
                else:
                    node = self.right_rotate(node)
            self.update_height(node)

        elif node.key == key:
            if node.left and node.right:
                if self.height(node.left) >= self.height(node.right):
                    max_node = node.left
                    while max_node.right != None:
                        max_node = max_node.right
                    node.key = max_node.key
                    node.left = self._delete(node.key, node.left)
                else:
                    min_node = node.right
                    while min_node.left != None:
                        min_node = min_node.left
                    node.key = min_node.key
                    node.right = self._delete(node.key, node.right)
                self.update_height(node)
            else:
                if node.left:
                    node = node.left
                elif node.right:
                    node = node.right
                else:
                    node = None

        return node

    def delete(self, key):
        self.root = self._delete(key, self.root)

    def contains(self, key) -> bool:
        bfs_queue = Queue()
        bfs_queue.put(self.root)

        while not bfs_queue.empty():
            removed = bfs_queue.get()
            if removed.key == key:
                return True

            if key < removed.key and removed.left is not None:
                bfs_queue.put(removed.left)
            if key > removed.key and removed.right is not None:
                bfs_queue.put(removed.right)
        return False

def main():

    f_in =  open('input.txt')
    f_out=  open('output.txt', 'w')

    n = int(f_in.readline().strip())

    tree = AVLTree()
    for i in range(n):
        line = f_in.readline().strip()
        if line[0]=='+':
            tree.insert(int(line[1:]))
            f_out.write(str(tree.root_balance()+'\n'))
        if line[0]=='-':
            tree.delete(int(line[1:]))
            if tree.root:
                f_out.write(str(tree.root_balance()) + '\n')
            else:
                f_out.write('0\n')
        elif line[0] == '?':
                f_out.write(str(tree.contains(int(line[1:]))).lower() + '\n')
if __name__ == '__main__':
    main()
