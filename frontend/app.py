import streamlit as st
import streamlit.components.v1 as components
from code_editor import code_editor
import requests

st.set_page_config(layout="wide")
generator_url = "http://127.0.0.1:5000/generate"
generator_emb_url = "http://127.0.0.1:5000/generate_emb"
headers = {"Content-Type" : "application/json"}


# Make a get request with the parameters.
def generate_material(data):
    response = requests.get(generator_url, headers=headers, json=data)

    print(response.json)
    return response.json()['ai_response'], response.json()['cost']




margin1, input_col, margin2 = st.columns([0.3, 0.2, 0.3])
with input_col:
    st.title('Marketing Generator')
    indications = st.text_input('Indications', '')
    product_name = st.text_input('Product Name', '')
    drug_name = st.text_input('Drug Name', '')
    dosing_period = st.text_input('Dosing Period', '')
    pharma_producer = st.text_input('Pharmaceutical Company')
    
    data = {"indications":[indications], "product_name":product_name, "drug_name":drug_name, "dosing_period":dosing_period, "pharma_producer":pharma_producer}
    if 'cumulative_cost' in st.session_state:
        st.write('Cost of generating content in this session: $'+ str(round(st.session_state.cumulative_cost, 4)))

    generate_button = st.button(label='Generate')
st.text("")
st.text("")
st.text("")

margin3, output_col, margin4 = st.columns([0.2, 0.4, 0.2])
with output_col:
    if generate_button:
        # Generate HTML
        marketing_copy, cost = generate_material(data)
        # Store html_code in session state
        st.session_state.marketing_copy = marketing_copy
        st.session_state.last_call_cost = cost
        if 'cumulative_cost' in st.session_state:
            st.session_state.cumulative_cost += cost
        else:
            st.session_state.cumulative_cost = cost
    # If marketing_copy is in session state, display it in text area
    if 'marketing_copy' in st.session_state:
        st.session_state.marketing_copy = st.text_area('Editable Copy', value=st.session_state.marketing_copy, height=600)
        st.write(('Cost of generating this content: $' + str(round(st.session_state.last_call_cost, 4))))
