import streamlit as st
import json

st.title('Coverage Experiments')

data = json.load(open('coverage_experiments.json'))
exp_names = list(data.keys())

tabs = st.tabs(exp_names)

for idx, tab in enumerate(tabs):
    with tab:
        st.json(sorted(data[exp_names[idx]]))

