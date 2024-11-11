import streamlit as st
import pandas as pd
import time
st.title("Hello World")
st.write("Aprendendo steamlit")
st.text_input("Digite seu nome:", key="Nome")
nome=st.session_state.Nome
bar = st.progress(0)
bar.progress(1)
if nome:
    time.sleep(0.2)
    bar.progress(10)
    st.write(f"Olá {nome}, agora vc está aprendendo steamlit")
    dados=pd.DataFrame({'PrimeiraColuna': [1, 2, 3, 4], 'SegundaColuna': [10, 21, 35, 41]})
    time.sleep(0.2)
    bar.progress(20)
    st.write("Mostrando tabela como text")
    st.write(dados)
    st.write("Mostrando tabela como Datatframe")
    time.sleep(0.2)
    bar.progress(40)
    st.dataframe(dados)
    time.sleep(0.2)
    bar.progress(60)
    st.write("Mostrando tabela como Gráfico")
    st.line_chart(dados['SegundaColuna'])
    time.sleep(0.2)
    bar.progress(60)
    st.write("Mostrando um slider")
    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'squared is', x * x)
    time.sleep(0.1)
    bar.progress(80)
    time.sleep(0.1)
    bar.progress(90)
    time.sleep(0.1)
    bar.progress(100)
    add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
