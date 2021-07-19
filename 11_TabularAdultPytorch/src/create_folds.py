import pandas as pd
from pathlib import Path
from sklearn import model_selection

path = Path("../data/adult/")


if __name__ == "__main__":
    df = pd.read_csv(path/"adult.csv")
    df["kfold"] = -1

    df = df.sample(frac=1).reset_index(drop=True)

    kf = model_selection.StratifiedKFold(n_splits=5, shuffle=False, random_state=21)

    for fold, (train_idx, valid_idx) in enumerate(kf.split(df, y= df.income.values)):
        print(f'Fold :{fold} , Train Length: {len(train_idx)}, Valid Length: {len(valid_idx)}')
        df.loc[valid_idx, 'kfold'] = fold

    df.to_csv(path/"adult_kfold.csv", index=False)
    print("Complete")

