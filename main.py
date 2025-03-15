class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def leftView(root):
    queue = [root]
    printed = -1
    level = -1

    while len(queue):
        length = len(queue)
        level += 1
        while length:
            current = queue.pop(0)

            if current.left: 
                queue.append(current.left)

            if current.right:
                queue.append(current.right)
            
            if printed < level: 
                print(current.val)
                printed = level

            length -= 1

if __name__ == "__main__":
    root  = Node("root")
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

    root.left = a
    root.right = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    e.right = g
    g.left = h

    leftView(root)
