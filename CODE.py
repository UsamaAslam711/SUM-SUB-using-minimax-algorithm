tree = {
    'A': [0, ['B', 'C']],
    'B': [0, ['D', 'E']],
    'C': [0, ['F', 'G']],
    'D': [0, ['H', 'I']],
    'E': [0, ['J', 'K']],
    'F': [0, ['L', 'M']],
    'G': [0, ['N', 'O']],
    'H': [9, 0],
    'I': [2, 0],
    'J': [8, 0],
    'K': [6, 0],
    'L': [8, 0],
    'M': [8, 0],
    'N': [5, 0],
    'O': [3, 0]
}

def min_max(node, method):
    global tree
    #if no child exists
    if(tree[node][1] == 0):
        return tree[node][0]
      
    #If user says he wants to start with subtration i.e The root node contain the difference of its children and the children contain the sum of their children
    if method == 'sub':
        left = min_max(tree[node][1][0], 'sum')
        right = min_max(tree[node][1][1], 'sum')
        #Making sure that the difference will be smallest from largest (Large - small)
        if(left > right):
            left=left-right
            return left
        else: 
            right=right-left
            return right
          
    
    #If user says he wants to start with addition i.e The root node contain the sum of its children and the children contain the difference of their children 
    if method == 'sum':
        left = min_max(tree[node][1][0], 'sub')
        right = min_max(tree[node][1][1], 'sub')
        if(left > right):
            left=left+right
            return left
        else: 
            left=left+right
            return right

#Driver code
print(min_max('A', 'sub'))

