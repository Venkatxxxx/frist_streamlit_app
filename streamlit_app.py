import streamlit
import pandas
streamlit.title('My Parents New healthy Dinner')
streamlit.header('Breakfast menu')

streamlit.text('🥗Omega 3 & Buleberry oatmeal')
streamlit.text('🍗Kale, Spanich & Rocket Smoothie')
streamlit.text('🍣Hard-Boiled Free-Range Egg')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
