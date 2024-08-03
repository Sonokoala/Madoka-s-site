import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Excelファイルのパス
file_path = r'D:\tsujimura lab\spce lox chit ink\240627\ca different lactate.xlsx'

# ファイルの存在確認
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file at path {file_path} was not found.")

# Excelファイルを読み込み
df = pd.read_excel(file_path, usecols="A:T", skiprows=1)

# データフレームの最初の5行をファイルに保存（確認用）
with open("output.txt", "w", encoding='utf-8') as f:
    f.write("Original DataFrame:\n")
    f.write(df.head().to_string())

# データフレームの整形：x列を繰り返してy列をスタック
x = df.iloc[:, 0]
y = df.iloc[:, 1::2]

df_melted = y.copy()
df_melted['Time'] = x
df_melted = df_melted.melt(id_vars='Time', var_name='Concentration', value_name='Current')

# Concentration列を文字列に変換して凡例を正しく表示
df_melted['Concentration'] = df_melted['Concentration'].astype(str)

# Seabornを使ってプロット
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_melted, x='Time', y='Current', hue='Concentration', palette='tab10')

# 軸ラベル、タイトルの設定
plt.xlabel('Time / s')
plt.ylabel('Current / μA')

# 凡例の表示
labels = ['0.5mM lactate', '1mM lactate', '2mM lactate', '3mM lactate', '4mM lactate',
          '5mM lactate', '6mM lactate', '7mM lactate', '8mM lactate', '10mM lactate']
handles, _ = plt.gca().get_legend_handles_labels()
plt.legend(handles=handles, labels=labels)

# グリッドの表示
plt.grid(False)

# グラフの表示
plt.show()
