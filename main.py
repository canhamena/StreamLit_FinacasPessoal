import streamlit as st
import pandas as pd
st.set_page_config(page_title="Finanças",page_icon=":moneybag:")

st.text("Olá mundo, vamos começar")

st.markdown("""
    # Boas vindas cara!
            
    ### Nosso APP Financeiro! 
            
    Espero que você curta a experiência da nossa solução para organização financeira.

"""


)
file_upload = st.file_uploader(label="Faça upload dos dados aqui", type=["csv"])
if file_upload:
     df = pd.read_csv(file_upload)
     df["Data"] = pd.to_datetime(df["Data"],format='%d/%m/%Y').dt.date

     exp1 = st.expander("Dados brutos")
     columns_fmt = {"Valor":st.column_config.NumberColumn("Valor", format= "dollar")}
     exp1.dataframe(df, hide_index=True,column_config=columns_fmt)

     exp2 = st.expander("Instituições")
     tab_tabela,tab_history,tb_share = exp2.tabs(["Dados","Histórico","Distribuição"])
     df_intituicao = df.pivot_table(index="Data",columns="Instituição",values="Valor")
     with tab_tabela:
       st.dataframe(df_intituicao)
     with tab_history:
      st.line_chart(df_intituicao)
    
     
     with tb_share:
        date = st.date_input("Data para distribuição", min_value= df_intituicao.index.min(), max_value=df_intituicao.index.max())
        if date not in df_intituicao.index:
            st.warning("Entra com uma data válida ...")
        else:
           st.bar_chart(df_intituicao.loc[date])
