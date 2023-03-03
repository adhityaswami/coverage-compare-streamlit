import streamlit as st
import json

st.set_page_config(layout = 'wide')
st.title('Coverage Experiments')

data = json.load(open('coverage_experiments.json'))
mapping_dict = {idx: el for idx, el in enumerate(data.keys())}
indices = list(mapping_dict.keys())
slider_index = st.slider(label = 'Chunk', min_value = min(indices) + 1, max_value = max(indices) + 1) - 1

chunkData = data[mapping_dict[slider_index]]
st.markdown(body = chunkData['text'])
exp_names = [el for el in list(chunkData.keys()) if 'text' not in el]

tabs = st.tabs(exp_names)

for idx, tab in enumerate(tabs):
    with tab:
        st.json(chunkData[exp_names[idx]])

