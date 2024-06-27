import pandas as pd

# CSVファイルのパス
csv_file_path = '/Users/madoka/trantura_ondisk/practice/decision_tree/diabetics/diabetes.csv'

# CSVファイルを読み込む
data = pd.read_csv(csv_file_path)

# データの前処理
# 欠損値の処理
data = data.dropna()  # 欠損値を含む行を削除する

# 特徴量と目的変数の分割
X = data.drop('Outcome', axis=1)  # 特徴量
y = data['Outcome']  # 目的変数

# データの確認
print(X.head())  # 特徴量の先頭5行を表示
print(y.head())  # 目的変数の先頭5行を表示


import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルのパス
csv_file_path = '/Users/madoka/trantura_ondisk/practice/decision_tree/diabetics/diabetes.csv'

# CSVファイルを読み込む
data = pd.read_csv(csv_file_path)

# データの前処理
data = data.dropna()

# グラフの作成
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 10))

# 各特徴量と糖尿病の発症との関係をグラフ化
for i, column in enumerate(data.columns[:-1]):
    ax = axes[i//3, i%3]
    data.boxplot(column, by='Outcome', ax=ax)
    ax.set_title(f'{column} vs Outcome')
    ax.set_xlabel('Outcome')
    ax.set_ylabel(column)

# グラフの表示
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSVファイルのパス
csv_file_path = '/Users/madoka/trantura_ondisk/practice/decision_tree/diabetics/diabetes.csv'

# CSVファイルを読み込む
data = pd.read_csv(csv_file_path)

# データの前処理
data = data.dropna()

# ヒストグラムの作成
data.hist(figsize=(12, 8))
plt.tight_layout()
plt.show()

# 散布図の作成
sns.pairplot(data, hue='Outcome')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

# CSVファイルのパス
csv_file_path = '/Users/madoka/trantura_ondisk/practice/decision_tree/diabetics/diabetes.csv'

# CSVファイルを読み込む
data = pd.read_csv(csv_file_path)

# データの前処理
data = data.dropna()

# ランダムフォレストによる特徴量の重要度の計算
X = data.drop('Outcome', axis=1)
y = data['Outcome']
forest = RandomForestClassifier(n_estimators=100, random_state=0)
forest.fit(X, y)
importances = forest.feature_importances_

import numpy as np
import matplotlib.pyplot as plt

# 必要なライブラリのインポート
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

# データフレームの列名を確認
print(data.columns)

# 特徴量とラベルの分割
X = data.drop('Outcome', axis=1)  # 'Outcome'列を除いた特徴量データ
y = data['Outcome']  # ラベルデータ

# データセットの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 決定木モデルの構築と学習
model = DecisionTreeClassifier(random_state=0)
model.fit(X_train, y_train)

# テストデータの予測
y_pred = model.predict(X_test)

# モデルの評価
accuracy = accuracy_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# 結果の表示
print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{confusion_mat}')
print(f'Classification Report:\n{classification_rep}')

# 特徴量の重要度を取得
importances = model.feature_importances_

# 特徴量の名前を取得
feature_names = X_train.columns

# 特徴量の重要度と名前をペアにしてソート
indices = np.argsort(importances)[::-1]
sorted_importances = importances[indices]
sorted_feature_names = feature_names[indices]

# 特徴量の重要度の可視化
plt.figure(figsize=(10, 6))
plt.bar(sorted_feature_names, sorted_importances)
plt.xticks(rotation=45)
plt.title('Feature Importances')
plt.show()

# 必要なライブラリのインポート
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import matplotlib.font_manager as fm

# データフレームの列名を確認
print(data.columns)

# 特徴量とラベルの分割
X = data.drop('Outcome', axis=1)  # 'Outcome'列を除いた特徴量データ
y = data['Outcome']  # ラベルデータ

# データセットの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 決定木モデルの構築と学習（パラメータを調整）
model = DecisionTreeClassifier(random_state=0, max_depth=3, min_samples_split=10, min_samples_leaf=5)
model.fit(X_train, y_train)

# テストデータの予測
y_pred = model.predict(X_test)

# モデルの評価
accuracy = accuracy_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# 結果の表示
print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{confusion_mat}')
print(f'Classification Report:\n{classification_rep}')

# 特徴量の重要度を取得
importances = model.feature_importances_

# 特徴量の名前を取得
feature_names = X_train.columns

# 特徴量の重要度と名前をペアにしてソート
indices = np.argsort(importances)[::-1]
sorted_importances = importances[indices]
sorted_feature_names = feature_names[indices]

# 特徴量の重要度の可視化
plt.figure(figsize=(10, 6))
plt.bar(sorted_feature_names, sorted_importances)
plt.xticks(rotation=45)
plt.title('Feature Importances')
plt.show()

# 日本語フォントの設定
font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc'  # フォントのパスを指定
font_prop = fm.FontProperties(fname=font_path)

# 決定木の可視化
plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=feature_names, class_names=['0', '1'], filled=True, fontsize=10, max_depth=3)
plt.title('Decision Tree')

# 目的変数と説明変数の説明を表示
plt.figtext(0.9, 0.5, '目的変数:\n1: 糖尿病発症\n0: 発症しない\n\n説明変数:\n妊娠\n血糖値\n血圧\n肌の厚さ\nインシュリンレベル\nBMI\n糖尿病血統関数\n年齢', 
            horizontalalignment='left', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.show()


