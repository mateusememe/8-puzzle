import streamlit as st
import pandas as pd
import numpy as np

"""
# 8 Puzzle
Um simulador de buscas informadas para o jogo das 8 peças
"""
df = pd.DataFrame({
    'Buscas Informadas': ["Hill Climb", "A*", "Best First"],
    'Eficiência': [10, 20, 30]
})
df


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    chart_data

option = st.sidebar.selectbox(
    'Qual tipo de busca você pretende utilizar?',
    df['Buscas Informadas'])

'Busca Selecionada:', option
