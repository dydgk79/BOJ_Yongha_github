def solution(sales, links):
    n = len(sales)
    
    sales = [0] + sales
    
    tree = [[] for _ in range(n + 1)]
    for parent, child in links:
        tree[parent].append(child)
    
    dp = [[0, 0] for _ in range(n + 1)]
    
    def dfs(node):
        dp[node][1] = sales[node]

        not_attend_cost = 0

        has_attend_child = False

        min_extra = float('inf')
        
        for child in tree[node]:
            dfs(child)

            dp[node][1] += min(dp[child][0], dp[child][1])

            if dp[child][0] <= dp[child][1]:
                not_attend_cost += dp[child][0]

                min_extra = min(
                    min_extra,
                    dp[child][1] - dp[child][0]
                )
            else:
                not_attend_cost += dp[child][1]
                has_attend_child = True

        if tree[node] and not has_attend_child:
            not_attend_cost += min_extra
        
        dp[node][0] = not_attend_cost
    
    dfs(1)
    
    return min(dp[1][0], dp[1][1])