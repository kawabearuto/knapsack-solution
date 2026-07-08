# ナップサック問題（動的計画法）

capacity = int(input("ナップサックの容量: "))
n = int(input("品物の数: "))

items = []

for i in range(n):
    print(f"\n品物{i + 1}")
    number = int(input("番号: "))
    weight = int(input("重さ: "))
    value = int(input("値段: "))
    items.append((number, weight, value))

# DPテーブル
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

# DP計算
for i in range(1, n + 1):
    number, weight, value = items[i - 1]

    for w in range(capacity + 1):
        if weight <= w:
            dp[i][w] = max(
                dp[i - 1][w],                  # 入れない
                dp[i - 1][w - weight] + value  # 入れる
            )
        else:
            dp[i][w] = dp[i - 1][w]

# 選ばれた品物を復元
selected = []
w = capacity

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        number, weight, value = items[i - 1]
        selected.append(items[i - 1])
        w -= weight

selected.reverse()

# 結果表示
print("\n===== 結果 =====")
print("最大価値:", dp[n][capacity])

total_weight = 0

print("選ばれた品物:")
for number, weight, value in selected:
    print(f"番号:{number}  重さ:{weight}  値段:{value}")
    total_weight += weight

print("合計重量:", total_weight)