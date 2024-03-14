# Importing necessary libraries
from dietkit import load_ingredient, load_menu, load_diet
import streamlit as st
from PIL import Image
import plotly.graph_objects as go
import pandas as pd

# Calculate Basal Metabolic Rate (BMR) based on age, height, and weight
def calculate_bmr(age, height, weight, gender):
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return bmr

# Function to load sample ingredients, menus, and diets
@st.cache
def load_sample_data(days):
    sample_ingredients = load_ingredient(sample_language='eng')
    sample_menus = load_menu(ingredients=sample_ingredients, sample_language='eng')
    # You may adjust the diet plan generation based on the calculated BMR
    sample_diets = load_diet(menus=sample_menus, num_loads=days, sample_language='eng', sample_name='ML')
    return sample_diets

# Function to convert DataFrame to CSV format
@st.cache
def convert_df(df):
    data = pd.DataFrame(df)
    return data.to_csv().encode('utf-8')

# Function to convert dictionary to DataFrame and then CSV format
@st.cache
def convert_df_2(df):
    data = pd.DataFrame.from_dict(df, orient='index')
    return data.to_csv().encode('utf-8')

# Streamlit app
st.title('AI Diet Creator')
st.write('''This model is for all who have a problem with their eating habits and want to change their life.
            With our model, you don't need to be an expert or go to doctors. You just input your data and let us 
            create your diet depending on your body type.''')

# Load image
image = Image.open('img.png')
st.image(image)

# Header for diet plan creation
st.header('Create your own diet plan')

# Slider to select number of diet days
days = st.slider('Select diet days', 1, 30, 10)

# Slider to select age
age = st.slider('Select age', 18, 100)

# Number input for height
height = st.number_input('Height (cm)')


# Number input for weight
weight = st.number_input('Weight (kg)')

gender = st.selectbox('Gender:', ['Male', 'Female'])
# Calculate daily calorie intake based on age, height, and weight
bmr = calculate_bmr(age, height, weight, gender)

# Display the calculated BMR
#st.write(f'Calculated BMR: {bmr}')

# Load sample data
sample_diets = load_sample_data(days)

# Submit button
submit = st.button('Submit')

# If submit button is clicked
if submit:
    st.write(f'calorie intake required: {bmr}/day')
    st.write("Your meals for the next", days, 'days')
    st.success('Saved', icon="✅")

    # Convert diet plan DataFrame to CSV format
    meals_csv = convert_df(sample_diets.plan)
    ing_csv = convert_df_2(sample_diets.ingredient)
    nutrition_csv = convert_df_2(sample_diets.nutrition)

    # Download buttons for diet plan, ingredients, and nutrition
    st.download_button(
        label="Download your diet meals",
        data=meals_csv,
        file_name='meals_csv.csv',
    )
    st.download_button(
        label="Download your diet ingredients of the meals",
        data=ing_csv,
        file_name='ingredients_csv.csv',
    )
    st.download_button(
        label="Download nutrition of your diet meals",
        data=nutrition_csv,
        file_name='nutrition_csv.csv'
    )

# Subheader to view diet plan
st.subheader('View your diet')

# Slider to select the day to view
select_day = st.slider('Select the day', 1, days)

# Button to view menu
st.write(f'View Menu of day {select_day}')
Menu = st.button('Menu')
if Menu:
    data = sample_diets.plan[select_day - 1]
    st.write(data)

# Button to view ingredients
st.write(f'Ingredients of Menu of day {select_day}')
ing = st.button('Ingredients')
if ing:
    data_ing = sample_diets.ingredient[select_day - 1]
    st.write(data_ing)

# Button to view nutrition values
st.write(f'Nutrition Values for Menu of day {select_day}')
nut = st.button('Nutrition Values')
if nut:
    data_nut = sample_diets.nutrition[select_day - 1]
    # The plot
    fig = go.Figure(
        go.Pie(
            labels=list(data_nut.keys()),
            values=list(data_nut.values()),
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.subheader("Pie chart")
    st.plotly_chart(fig)
    st.subheader('Nutrition Values')
    st.write(data_nut)
