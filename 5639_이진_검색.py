import sys
sys.setrecursionlimit(10**6)  # 파이썬의 재귀 깊이 제한을 늘려줍니다.

def post_order(start, end):
    if start > end:
        return
    
    root = pre_order[start]
    idx = start + 1

    # 오른쪽 서브트리의 시작 지점을 찾습니다.
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1
    
    # 왼쪽 서브트리
    post_order(start + 1, idx - 1)
    # 오른쪽 서브트리
    post_order(idx, end)
    # 루트 노드 출력
    print(root)

pre_order = []
while True:
    try:
        num = int(input())
        pre_order.append(num)
    except:
        break

post_order(0, len(pre_order) - 1)
