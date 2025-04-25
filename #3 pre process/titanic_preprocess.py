import os
import pandas as pd

# ファイルパスを指定
file_path = '/Users/madoka/trantura_ondisk/practice/train.csv'
# ファイルの存在を確認し、読み込む
if os.path.exists(file_path):
    # CSVファイルの読み込み
    titanic_df = pd.read_csv(file_path)
    
    # データフレームの先頭5行を表示
    print(titanic_df.head())

    # データフレームの基本情報を表示
    print("\nデータフレームの基本情報:")
    print(titanic_df.info())

    # 主要な統計情報を表示
    print("\n主要な統計情報:")
    print(titanic_df.describe())

    # Age列の先頭5行を表示
    print("\nAge列の先頭5行:")
    print(titanic_df['Age'].head())

    # 欠損値チェック
    print("\n欠損値の数:")
    print(titanic_df.isnull().sum())

    # 生存者と非生存者の人数をカウント
    print("\n生存者と非生存者の人数:")
    print(titanic_df['Survived'].value_counts())
else:
    print(f"ファイルが見つかりません: {file_path}")
print(titanic_df.info())
print(titanic_df.describe())
print(titanic_df.isnull().sum())
print(titanic_df['Survived'].value_counts())
# Age列の欠損値を中央値で補完
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)

# Embarked列の欠損値を最頻値で補完
titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode().iloc[0], inplace=True)

# Cabin列の欠損値を 'Unknown' で補完
titanic_df['Cabin'].fillna('Unknown', inplace=True)

# 振り返り: 欠損値の数を確認
print(titanic_df.isnull().sum())
# 補完後の統計情報を表示
print(titanic_df.describe())

# データが適切に補完されたことを確認する
print(titanic_df.info())
# 'SibSp' (兄弟姉妹/配偶者の数) と 'Parch' (両親/子供の数) を足して、家族の人数を計算
titanic_df['FamilySize'] = titanic_df['SibSp'] + titanic_df['Parch'] + 1  # +1 は本人を含む

print(titanic_df[['FamilySize', 'SibSp', 'Parch']].head())
import pandas as pd

# 'Sex' カラムをワンホットエンコーディングする
titanic_df = pd.get_dummies(titanic_df, columns=['Sex'], drop_first=True)

# エンコーディング結果の確認
print(titanic_df.head())
# 結果を確認
print(titanic_df.head())

