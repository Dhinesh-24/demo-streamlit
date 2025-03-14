import streamlit as sl
import pandas as pd
from PIL import Image

sl.set_page_config(page_title="Demo")

sl.header("Streamlit")

sl.subheader("Content")

sl.markdown("_Hello_")

sl.text("Nonchangeable")

sl.latex("y=mx+c")

sl.caption("Caption")

sl.code('''if i!=0:
        print("Odd")
''',language='python')

data = pd.read_csv(r"D:\AIML\lab1.csv")

sl.dataframe(data)

#sl.write(data)
#sl.table(data)

json={'a':[1,2,3],'b':[7,8]}
sl.json(json)

sl.metric('Apple','$70','+4%')

col1,col2=sl.columns(2)

with col1:
    sl.metric('Apple','$70','+4%')
with col2:
    sl.metric('Samsung','$70','+4%')

submit=sl.button('submit')
if submit:
    sl.dataframe(data)
    sl.radio("Choose one:",('a','b','c'))
    sl.checkbox('button')

cols=list(data.columns)
sl.write(cols)

name=sl.selectbox('Choose a feature:',cols)
sl.write(cols)
sl.write('the column selected by use is',name)

col3,col4=sl.columns(2)
with col3:
    a=sl.number_input("Enter a number1:")
    #a=sl.slider("enter Number:",0,100,10)
with col4:
    b=sl.number_input("Enter a number2:")
submit=sl.button('Add')

if submit:
    sl.write(a+b)

option=sl.multiselect('Choose Variable',cols)    
sl.write("Your selection",option)

submit=sl.checkbox('show image')
if submit:
    img = Image.open(r"C:\Users\HP\Pictures\Screenshots\Screenshot 2024-12-12 001723.png")
    sl.image