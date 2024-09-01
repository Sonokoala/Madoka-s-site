# Exerciseクラスの定義
class Exercise:
    def __init__(self, name, muscle_group, sets, reps):
        self.__name = name
        self.__muscle_group = muscle_group
        self.__sets = sets
        self.__reps = reps

    # ①ゲッターと②セッター
    # クラスの属性に対するアクセスを制限するためのメソッド
    #①の目的：クラスのプライベートな属性の値を取得するメソッド
    #②の目的：クラスのプライベートな属性の値を取得するメソッド
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_muscle_group(self):
        return self.__muscle_group

    def set_muscle_group(self, muscle_group):
        self.__muscle_group = muscle_group

    def get_sets(self):
        return self.__sets

    def set_sets(self, sets):
        self.__sets = sets

    def get_reps(self):
        return self.__reps

    def set_reps(self, reps):
        self.__reps = reps

    # エクササイズの実行メソッド
    def perform(self):
        print(f"Performing {self.__sets} sets of {self.__reps} reps of {self.__name} targeting {self.__muscle_group}.")


# StrengthExerciseクラスの定義（Exerciseクラスを継承）
class StrengthExercise(Exercise):
    def __init__(self, name, muscle_group, sets, reps, weight):
        super().__init__(name, muscle_group, sets, reps)
        self.weight = weight

    # エクササイズの実行メソッドをオーバーライド
    def perform(self):
        print(f"Performing {self.get_sets()} sets of {self.get_reps()} reps of {self.get_name()} with {self.weight}kg targeting {self.get_muscle_group()}.")


# エクササイズの実行を汎用的に扱う関数
def perform_exercise(exercise):
    exercise.perform()


# メインプログラム
if __name__ == "__main__":
    # Exerciseクラスのオブジェクトを作成
    squat = Exercise("Squat", "Legs", 3, 10)
    push_up = Exercise("Push Up", "Chest", 3, 15)

    # StrengthExerciseクラスのオブジェクトを作成
    bench_press = StrengthExercise("Bench Press", "Chest", 3, 8, 60)

    # エクササイズを実行
    perform_exercise(squat)        # Output: Performing 3 sets of 10 reps of Squat targeting Legs.
    perform_exercise(push_up)      # Output: Performing 3 sets of 15 reps of Push Up targeting Chest.
    perform_exercise(bench_press)  # Output: Performing 3 sets of 8 reps of Bench Press with 60kg targeting Chest.
