import pandas as pd
import numpy as np

def simulate_race(df_eval, n_simulations=1000):
    horses = df_eval.copy()
    horses["勝利数"] = 0

    # 能力スコアに基づき勝率をシミュレーション
    for _ in range(n_simulations):
        noise = np.random.normal(0, 3, len(horses))
        scores = horses["AI評価"].values + noise
        winner_idx = np.argmax(scores)
        horses.at[winner_idx, "勝利数"] += 1

    horses["勝率"] = (horses["勝利数"] / n_simulations * 100).round(1)
    return horses.sort_values("勝率", ascending=False).reset_index(drop=True)
