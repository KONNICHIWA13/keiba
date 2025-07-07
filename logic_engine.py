import pandas as pd
import numpy as np
import random

def evaluate_horses(df):
    random.seed(42)
    scores = []

    for _, row in df.iterrows():
        # 各ファクターの擬似スコア（本番では実データと連携）
        ability = np.random.normal(70, 8)        # 能力偏差値
        aptitude = np.random.normal(0, 5)        # 距離・馬場適性
        pedigree = np.random.normal(0, 3)        # 血統適性
        pace = np.random.normal(0, 4)            # 展開・位置取り
        jockey = np.random.normal(0, 2)          # 騎手補正
        others = np.random.normal(0, 2)          # 枠・調教など

        total = ability + aptitude + pedigree + pace + jockey + others
        scores.append({
            "馬番": row["馬番"],
            "馬名": row["馬名"],
            "脚質": random.choice(["逃げ", "先行", "差し", "追込"]),
            "AI評価": round(total, 2)
        })

    df_eval = pd.DataFrame(scores)
    return df_eval
