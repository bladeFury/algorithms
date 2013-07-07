

class TreeNode:
	def __init__(self):
		self.l_child = None
		self.r_child = None

	def visit(self):
		pass

def preorder_traverse(node):
	if node is not None:
		node.visit()
		preorder_traverse(node.l_child)
		preorder_traverse(node.r_child)

def inorder_traverse(node):
	if node is not None:
		inorder_traverse(node.l_child)
		node.visit()
		inorder_traverse(node.r_child)

def postorder_travelse(node):
	if node is not None:
		postorder_travelse(node.l_child)
		postorder_travelse(node.r_child)
		node.visit()


def preorder_traverse_nr(node):
	stack = []
	if node is None:
		return
	stack.append(node)
	while len(stack) > 0:
		n = stack.pop()
		n.visit()
		if n.r_child is not None:
			stack.append(n.r_child)
		if n.l_child is not None:
			stack.append(n.l_child)

def inorder_traverse_nr(node):
	stack = []
	if node is None:
		return
	stack.append(node)
	pivot = None
	while len(stack) > 0 or pivot is not None:
		if pivot is None:
			n = stack.pop()
			n.visit()
			pivot = n.r_child
		else:
			stack.append(pivot)
			pivot = pivot.l_child

def postorder_traverse_nr(node):
	stack1 = []
	stack2 = []
	if node is None:
		return
	stack1.append(node)
	while len(stack1) > 0:
		n = stack1.pop()
		stack2.append(n)
		if n.l_child is not None:
			stack1.append(n.l_child)
		if n.r_child is not None:
			stack1.append(n.r_child)
	while len(stack2) > 0:
		n = stack2.pop()
		n.visit()