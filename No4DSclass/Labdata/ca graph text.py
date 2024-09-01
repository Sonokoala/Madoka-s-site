import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# テキストファイルが格納されているディレクトリのパス
directory_path = r'D:\tsujimura lab\spce lox chit ink\240716'

# ディレクトリ内のすべてのテキストファイルを取得
file_paths = glob.glob(os.path.join(directory_path, '*.txt'))

# グラフの設定
plt.figure(figsize=(12, 8))

# データを格納するリスト
all_data = []

# 各ファイルを読み取り、プロット
for file_path in file_paths:
    # ファイル名を取得してラベルに使用
    label = os.path.splitext(os.path.basename(file_path))[0]

    # テキストファイルの読み込み
    df = pd.read_csv(file_path, delimiter=r',\s+', skiprows=59, names=['Time/sec', 'Current/A'], engine='python')

    # データの型を確認して必要に応じて変換する
    df['Time/sec'] = pd.to_numeric(df['Time/sec'], errors='coerce')
    df['Current/A'] = pd.to_numeric(df['Current/A'], errors='coerce')

    # データをリストに追加
    all_data.append((df['Time/sec'], df['Current/A'], label))

# 全てのデータを1つのグラフにプロット
lines = []
labels = []
for data in all_data:
    line, = plt.plot(data[0], data[1], linestyle='-', label=data[2])
    lines.append(line)
    labels.append(data[2])

# 凡例の順番を変更する
# ここで手動で順番を指定
custom_order = [1, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2]  # 例: 2番目、1番目、3番目の順番で表示

# リストの長さを確認する
print("Number of lines:", len(lines))
print("Number of labels:", len(labels))

# カスタム順序で凡例を表示
valid_indices = [i for i in custom_order if i < len(lines)]  # 有効なインデックスのみを選択
if len(valid_indices) != len(custom_order):
    print("Warning: Some indices in custom_order are out of range.")

# カスタム順序で凡例を表示
plt.legend([lines[i] for i in valid_indices], [labels[i] for i in valid_indices])

# グラフのタイトルとラベル
plt.xlabel('Time / s')
plt.ylabel('Current / A')

# グリッドを無効にする
plt.grid(False)

# グラフの表示
plt.show()
