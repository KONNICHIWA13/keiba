import pandas as pd
import re

def parse_netkeiba(text):
    # 馬番と馬名の抽出
    lines = text.strip().split("\n")
    horses = []
    for line in lines:
        match = re.match(r"^\d+\s+[\s✓◎◯▲△消]*([\wァ-ンヴ一-龥ー・]+)", line)
        if match:
            horse_name = match.group(1)
            tokens = line.split()
            try:
                uma_number = int(tokens[0])
            except:
                continue
            horses.append({
                "馬番": uma_number,
                "馬名": horse_name
            })

    df = pd.DataFrame(horses)
    df = df.sort_values("馬番").reset_index(drop=True)
    return df
