import streamlit as st
import random
st.title("素数")
if st.button("素数おみくじを引く"):
    results = ["２","３","５","７","１１","１３","１７","１９","２３","２９",]
    result = random.choice(results)
    st.write(f"結果:{result}")

