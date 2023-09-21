import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pip install matplotlib as mlt


# Streamlitアプリケーションのタイトルを設定
st.title("自動絵画アプリ")

# 円の中心座標と半径のユーザー入力を受け取る
center_x = st.number_input("円の中心のX座標", min_value=0, max_value=500, value=250)
center_y = st.number_input("円の中心のY座標", min_value=0, max_value=500, value=250)
radius = st.number_input("円の半径", min_value=10, max_value=200, value=50)

# 円を描画する
fig, ax = plt.subplots()
circle = plt.Circle((center_x, center_y), radius, fill=False, color='blue', linewidth=2)
ax.add_patch(circle)

# グラフの表示
st.pyplot(fig)


