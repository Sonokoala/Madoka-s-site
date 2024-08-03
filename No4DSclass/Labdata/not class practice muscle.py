# エクササイズを辞書として定義する関数
def create_exercise(name, muscle_group, sets, reps):
    return {
        "name": name,
        "muscle_group": muscle_group,
        "sets": sets,
        "reps": reps
    }

# 重り付きエクササイズを辞書として定義する関数
def create_strength_exercise(name, muscle_group, sets, reps, weight):
    return {
        "name": name,
        "muscle_group": muscle_group,
        "sets": sets,
        "reps": reps,
        "weight": weight
    }

# エクササイズを実行する関数
def perform_exercise(exercise):
    if "weight" in exercise:
        print(f"Performing {exercise['sets']} sets of {exercise['reps']} reps of {exercise['name']} with {exercise['weight']}kg targeting {exercise['muscle_group']}.")
    else:
        print(f"Performing {exercise['sets']} sets of {exercise['reps']} reps of {exercise['name']} targeting {exercise['muscle_group']}.")

# メインプログラム
if __name__ == "__main__":
    # エクササイズの定義
    squat = create_exercise("Squat", "Legs", 3, 10)
    push_up = create_exercise("Push Up", "Chest", 3, 15)
    
    # 重り付きエクササイズの定義
    bench_press = create_strength_exercise("Bench Press", "Chest", 3, 8, 60)
    
    # エクササイズを実行
    perform_exercise(squat)        # Output: Performing 3 sets of 10 reps of Squat targeting Legs.
    perform_exercise(push_up)      # Output: Performing 3 sets of 15 reps of Push Up targeting Chest.
    perform_exercise(bench_press)  # Output: Performing 3 sets of 8 reps of Bench Press with 60kg targeting Chest.
