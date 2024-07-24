import streamlit as st
st.title("PERSONAL DETAILS")
st.text_input('Name: ')
st.radio("Gender: ",('Male','Female'))
st.number_input("Age: ")
st.text_input("Address: ")
st.checkbox("Hobbies: ")
st.selectbox('Hobby:',('Dancing','Singing','Swimming','Reading','Running','Listening to music','Riding'))
b=st.number_input("Weight(kg): ")
a=st.number_input("Height(cms): ")
st.write("BMI of the Person: ")
BMI=b//((a/100)**2)
st.write(BMI)
w=BMI
st.write("BMI RESULT:")
if w<16:
    st.write("Severe Thinness")
elif w>=16 and w<=17:
    st.write("Moderate Thinness")
elif w>17 and w<=18.5:
    st.write("Mild Thinness")
elif w>18.5 and w<=25:
    st.write("Normal")
elif w>25 and w<=30:
    st.write("Overweight")
elif w>30 and w<=35:
    st.write("Obese class 1")
elif w>35 and w<=40:
    st.write("Obese class 2")
else:
    st.write("Obese class 3")