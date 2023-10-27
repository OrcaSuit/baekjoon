def traverse(node, order):
    if node == '.': #현재 노드가 비었는가?
        return ''
    
    left = traverse(tree[node][0], order) #왼쪽 탐색
    right = traverse(tree[node][1], order) #오른쪽 탐색
    
    if order == 'preorder': # 전위 순회시 ABD..CE.FG....
        return node + left + right 
    elif order == 'inorder':
        return left + node + right
    elif order == 'postorder':
        return left + right + node

# 메인 코드
if __name__ == "__main__":
    tree = {}
    N = int(input())
    
    # 트리 정보 입력 받기
    for _ in range(N):
        node, left, right = input().split()
        tree[node] = (left, right)

    # 전위, 중위, 후위 순회 결과 출력
    print(traverse('A', 'preorder'))
    print(traverse('A', 'inorder'))
    print(traverse('A', 'postorder'))