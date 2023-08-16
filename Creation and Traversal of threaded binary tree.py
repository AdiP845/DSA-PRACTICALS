class Node:
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None
    # To point to the inorder successor
    self.thread = None

def inorderArray(array, root):
  if root.left:
    inorderArray(array, root.left)
  array.append(root)
  if root.right:                            
    inorderArray(array, root.right)

def createThreads(array):
  for idx, node in enumerate(array):
    if not node.right:
      if idx+1 < len(array):
        node.thread = array[idx+1]
     

def printTreeThreads(root):
  if root.left:
    printTreeThreads(root.left)
  print("Value = ", root.value, "Next Thread = ",  root.thread.value if(root.thread) else None)
  if root.right:
    printTreeThreads(root.right)

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(8)
root.right.left = Node(12)
root.right.right = Node(18)

array = []
inorderArray(array, root)
createThreads(array)
printTreeThreads(root)