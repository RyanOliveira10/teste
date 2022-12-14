import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bf = pd.read_csv('BlackFriday.csv')
print('Número de linhas: ', bf.shape[0])
print('Número de colunas: ', bf.shape[1])

#inicio do app
st.title('Data Analysis')

marital_true = bf.Age.loc[bf.Marital_Status == 1].value_counts()
marital_false = bf.Age.loc[bf.Marital_Status == 0].value_counts()

x1 = marital_true.index
y1 = marital_true.values

x2 = marital_false.index
y2 = marital_false.values

plt.bar(x1, y1, label='Casados', width=0.4, align='edge')
plt.bar(x2, y2, label='Não casados', width=0.4, align='edge')
plt.legend()
plt.title('Casados e não casados por idade')

st.pyplot(plt)
plt.clf()

porc_gender = bf.Gender.value_counts(normalize=True)
x = porc_gender.values
plt.pie(x, labels=['Homens', 'Mulheres'], autopct='%1.1f%%')
st.pyplot(plt)