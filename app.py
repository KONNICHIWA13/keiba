import streamlit as st
import pandas as pd
from data_parser import parse_netkeiba
from logic_engine import evaluate_horses
from montecarlo_simulator import simulate_race

st.set_page_config(page_title="競馬革命", layout="wide")

st.title("🏇 競馬革命 - AI競馬予想システム")

st.markdown("""
#### 📋 出馬表を「netkeiba」からコピペして、下に貼り付けてください
""")

user_input = st.text_area("🔽 出馬表貼り付け欄", height=400)

if st.button("AI予想を実行"):
    if not user_input.strip():
        st.warning("⚠️ 出馬表が空です。貼り付けてから実行してください。")
    else:
        try:
            df = parse_netkeiba(user_input)
            df_eval = evaluate_horses(df)
            sim_result = simulate_race(df_eval)

            st.subheader("🎯 勝率付きAI予想（馬番順）")
            st.dataframe(sim_result.sort_values("馬番"))

            st.subheader("📊 モンテカルロ展開分析（上位馬）")
            top3 = sim_result.sort_values("勝率", ascending=False).head(3)
            st.write(top3[["馬番", "馬名", "脚質", "勝率", "AI評価"]])

        except Exception as e:
            st.error(f"予想中にエラーが発生しました: {e}")

