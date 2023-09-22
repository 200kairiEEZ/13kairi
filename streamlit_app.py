import streamlit as st

# Streamlitアプリケーションのタイトルを設定
st.title("ベースギターWebアプリ")

# ベースギターの基本情報を表示
st.header("ベースギターについて")
st.write("ベースギターは低音の楽器で、リズムとメロディをサポートします。")

# ベースギターの画像を表示
st.image("bass_guitar.jpg", caption="ベースギター", use_column_width=True)

# ベースギターの音符を演奏するコンポーネント
st.header("ベースギターの演奏")

# 選択した音符のリスト
notes = ["C", "D", "E", "F", "G", "A", "B"]

# ドロップダウンメニューで音符を選択
selected_note = st.selectbox("音符を選択してください:", notes)

# 選択した音符を演奏するボタン
if st.button("演奏"):
    st.write(f"ベースギターで {selected_note} を演奏しました！")

# ベースギターの演奏の説明
st.write("音符を選択して「演奏」ボタンを押すと、ベースギターで音を鳴らすことができます。")

# 注意: 実際に音を鳴らすためには、音声処理ライブラリを使用する必要がありますが、
# この例では単純化のために音を再生しない形で実装しています。


