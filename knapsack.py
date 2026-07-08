# ナップサック問題（総当たり）

capacity = int(input("ナップサックの容量: "))
n = int(input("品物の数: "))

items = []

# 品物の入力
for i in range(n):
    print(f"¥n品物{i + 1}") #fはフォーマット文字列。これによりinputの際、1番目の品物、2番目の品物と表示される。

    number = int(input("番号: "))
    weight = int(input("重さ: "))
    value = int(input("値段: "))

    items.append((number, weight, value))

# 最適解を保存する変数
best_value = 0
best_weight = 0
best_items = []

# 全ての組み合わせを調べる
for bit in range(1 << n): #bitを使うことで、全ての組み合わせを表現する。1 << nは2のn乗を意味する。

    total_weight = 0
    total_value = 0
    selected = []

    for i in range(n):
        if bit & (1 << i):
            number, weight, value = items[i]
            total_weight += weight
            total_value += value
            selected.append(items[i])

    # 容量以内で価値が最大なら更新
    if total_weight <= capacity and total_value > best_value:
        best_value = total_value
        best_weight = total_weight
        best_items = selected

# 結果表示
print("¥n===== 結果 =====")
print("最大価値:", best_value)
print("合計重量:", best_weight)
print("選ばれた品物:")

if len(best_items) == 0:
    print("なし")
else:
    for number, weight, value in best_items:
        print(f"番号:{number}  重さ:{weight}  値段:{value}")
