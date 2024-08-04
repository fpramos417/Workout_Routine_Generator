import os
import streamlit as st
import openai
st.title('Workout Routine Generator')

openai.api_key = os.getenv('OPENAI_API_KEY')

# Collect user information
age = st.number_input('Enter your age', min_value=10, max_value=100)
gender = st.selectbox('Select your gender', ['Male', 'Female', 'Other'])
height = st.number_input('Enter your height in cm', min_value=100, max_value=250)
weight = st.number_input('Enter your height in lbs', min_value=100, max_value=250)
goal = st.selectbox('Select your fitness goal', ['Build Muscle', 'Lose Weight'])

options = st.selectbox('Choose from dropdown', ['Lower Body', 'Upper Body', 'Core', 'Full Body'])

# Generate a workout routine using GPT-3
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": '''
         You are a helpful assistant. Your task is to generate a workout routine. An example of an uppper body workout routine might include the following: 
        SECTION A:
        - Incline DB Bench Press (3x30 secs-medium weight keep them the blood flowing)
        - Banded Row (2 х 30 веса-месp rowing and the Blond Rowing)
        - MB Fake Chops to Slam (3x 30 secs-keep it moving)
        SECTION B:
        - Spoto Bench Cluster (4x6 -medium weight-close grip 1 set is x3 rest 5 sec x2 rest 5 sec x1)
        - Single Arm DB Row (3x8-10 eа.-pull pause 2-3sec down)
        - Low Single Arm Hold March (3x 12-15 ea. carry)
        SECTION C:
        - DB Arnold Press (1 x 1-12)
        - Jumping ECC Chins (1 x 1-12-Jump to top control down 3-5 sec)
        - Tall Walking Lateral Plank (1x 1-12 ка.-top pushup pos-walk and feet to left then back right keeping plank)
        SECTION D:
        - Sets of 7-7-7 Curls (x3)
        - Sets of OH Tracep Ext (x3)
        - Sets of Front to Loteral Raise (x3)'''},
        {"role": "user", "content": f"I am a {age} year old {gender} with a height of {height} cm and a weight of {weight}. My fitness goal is to {goal}. I need a {options} workout routine."}
    ]
)

workout = response['choices'][0]['message']['content']

st.write(workout)
