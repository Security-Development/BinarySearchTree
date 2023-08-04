import random

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

class BST:
    def __init__(self):
        self.root = None

    def set_root(self, val):
        self.root = Node(val)

    def find_node(self, node, val):
        if (node is None):
            return None
        elif node.value == val:
            return node
        elif val < node.value:
            return self.find_node(node.left, val)
        else:
            return self.find_node(node.right, val)

    def serach(self, val):
        return self.find_node(self.root, val)

    def insert_node(self, node, val):
        if val <= node.value:
            if node.left:
                self.insert_node(node.left, val)
            else:
                node.left = Node(val)
        elif val > node.value:
            if node.right:
                self.insert_node(node.right, val)
            else:
                node.right = Node(val)

    def insert(self, val):
        if self.root is None:
            self.set_root(val)
        else:
            self.insert_node(self.root, val)

    def serach_root(self, node, val):
        if (node is None):
            return None
        elif (node.left and node.left.value == val) or (node.right and node.right.value == val):
            return node
        elif val < node.value:
            return self.serach_root(node.left, val)
        else:
            return self.serach_root(node.right, val)

    def min_node(self, node):
        result = node

        while not(result and result.left is None):
            result = result.left

        return result

    def max_node(self, node):
        result = node

        while not(result and result.right is None):
            result = result.right

        return result

    def delete(self, val):
        root = self.root
        if val != self.root.value:
            root = self.serach_root(self.root, val)
            if root is None:
                return False

        child = self.serach(val)

        # 1 case
        if child.left is None and child.right is None:
            if (root.left is not None and root.left.value) == val:
                root.left = None
            elif (root.right is not None and root.right.value) == val:
                root.right = None
        # 2 case
        elif child.left is not None and child.right is None:
            if root.value == self.root.value:
                temp = self.max_node(root.left)
                
                self.serach_root(self.root, temp.value).left = temp.left
                root.value = temp.value
            elif child.value < root.value:
                root.left = child.left
            elif child.value > root.value:
                root.right = child.left
        
        # 3 case
        elif child.left is None and child.right is not None:
            if root.value == self.root.value:
                temp = self.min_node(root.right)
                self.serach_root(self.root, temp.value).right = temp.right
                root.value = temp.value 
            elif child.value < root.value:
                root.left = child.right
            elif child.value > root.value:
                root.right = child.right

        # 4 case
        elif child.left is not None and child.right is not None:
            temp = self.min_node(child.right)
            root_temp = self.serach_root(self.root, temp.value)

            if self.root.value == root.value and (root.right.left is None or root.right.right is None):
                if root_temp.left is not None and root_temp.right is None:
                    root_temp.left = None
                elif root_temp.left is None and root_temp.right is not None:
                    root_temp.left = None

                root_temp.right = temp.right
            else:
                root_temp.left = temp.right
            
            child.value = temp.value


    # reference link : https://www.delftstack.com/howto/python/print-binary-tree-python/
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self, node=None):
        if node is None:
            node = self.root
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % node.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


node_list = random.sample(range(1, 1000,),10)#[768,431,794,279,708,963,121,621,749,118, 852, 864, 849, 788, 792, 786, 755]#[33, 20, 51, 2, 34, 50, 64, 85, 56]
bst = BST()

for node in node_list:
    bst.insert(node)

bst.display()

target = random.choice(node_list)
print("delete target:", node_list[0])
bst.delete(node_list[0])

bst.display()
