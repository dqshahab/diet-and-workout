

#it's a demo can be done like randomized strength recommendation for all days workout using "random" package and by refering generate_strength_training_day1(goal) function

import argparse

parser = argparse.ArgumentParser(description='Set Streamlit app port')
parser.add_argument('--port', type=int, default=8501, help='Port to run the Streamlit app on')
args = parser.parse_args()

 #command to run this streamlit run pop.py --server.port 8077
 #port number can be used in 8thousand change
 #run this in individual cmd 


import streamlit as st
import random

# Define functions to generate random workouts for each section
@st.cache
def generate_warmup(goal):
  if goal == "Weight Loss":
    return "5 minutes of light cardio (e.g., brisk walking, jumping jacks)"
  else:
    return "5 minutes of dynamic stretching"

@st.cache
def generate_warmup_day1(goal):
  # Day 1 warmup focused on mobility and core activation
  warmup_plan = "Day 1 Warmup:\n"
  warmup_plan += "- Inchworm x 10 repetitions\n"  # Mobilizes spine and hamstrings
  warmup_plan += "- Arm circles (forward and backward) x 15 repetitions each direction\n"  # Improves shoulder mobility
  warmup_plan += "- High knees x 30 seconds\n"  # Increases heart rate and leg activation
  

  return warmup_plan

@st.cache
def generate_warmup_day2(goal):
  # Day 1 warmup focused on mobility and core activation
  warmup_plan = "Day 2 Warmup:\n"
  warmup_plan += "- Butt kicks x 30 seconds\n"  # Increases heart rate and core activation
  warmup_plan += "- Plank hold for 30 seconds\n"  # Core activation and stability
  warmup_plan += "- Bird-dog exercise x 10 repetitions per side\n"  # Core activation and stability

  return warmup_plan

@st.cache
def generate_warmup_day3(goal):
  # Day 1 warmup focused on mobility and core activation
  warmup_plan = "Day 3 Warmup:\n"
  warmup_plan += "- Squats without weight x 15 repetitions (activates lower body muscles)\n"
  warmup_plan += "- Lunges (walking forward and backward) x 10 repetitions per leg (improves lower body stability and balance)\n"
  warmup_plan += "- Ankle circles (forward and backward) x 10 repetitions each direction (improves ankle mobility)\n"
  
  return warmup_plan

@st.cache
def generate_warmup_day4(goal):
  # Day 1 warmup focused on mobility and core activation
  warmup_plan = "Day 4 Warmup:\n"
  warmup_plan += "- Wrist circles (forward and backward) x 10 repetitions each direction (improves wrist mobility)\n"
  warmup_plan += "- Chest stretch (hold for 30 seconds each side) (static stretch for chest)\n"
  warmup_plan += "- Hamstring stretch (hold for 30 seconds each leg) (static stretch for hamstrings)\n"
  
  return warmup_plan

@st.cache
def generate_warmup_day5(goal):
  # Day 1 warmup focused on mobility and core activation
  warmup_plan = "Day 5 Warmup:\n"
  warmup_plan += "- Wrist circles (forward and backward) x 10 repetitions each direction (improves wrist mobility)\n"
  warmup_plan += "- Chest stretch (hold for 30 seconds each side) (static stretch for chest)\n"
  warmup_plan += "- Hamstring stretch (hold for 30 seconds each leg) (static stretch for hamstrings)\n"
  
  return warmup_plan

@st.cache
def generate_warmup_day6(goal):
  # Day 1 warmup focused on mobility and core activation
  warmup_plan = "Day 6 Warmup:\n"
  warmup_plan += "- Arm raises (lateral and front) x 15 repetitions each direction (activates shoulders and upper body)\n"
  warmup_plan += "- Shoulder shrugs x 15 repetitions (activates traps and upper back)\n"
  warmup_plan += "- Bird-dog exercise x 10 repetitions per side\n"  # Core activation and stability
  
  return warmup_plan

@st.cache
def generate_warmup_day7(goal):
  # Day 1 warmup focused on mobility and core activation
  warmup_plan = "Day 7 Warmup:\n"
  warmup_plan += "- Squat jumps x 10 repetitions (explosive lower body activation)\n"
  warmup_plan += "- Push-ups (modified or full) x 10 repetitions (explosive upper body activation)\n"
  warmup_plan += "- Jumping jacks or jumping rope x 30 seconds (increases heart rate and overall body activation)\n"
  
  return warmup_plan

@st.cache
def generate_strength_training_day1(goal):
  exercises = [
      # Push exercises (chest, shoulders, triceps)
      "Push-ups", "Dumbbell bench press", "Overhead press",
      # Pull exercises (back, biceps)
      "Pull-ups", "Dumbbell rows", "Bicep curls",
      # Leg exercises (quads, hamstrings, calves)
      "Squats", "Lunges", "Deadlifts", "Calf raises",
      # Core exercises
      "Plank", "Crunches", "Russian twists"
  ]

  # Day 1 focus on weight loss with more exercises
  workout = random.sample(exercises, 6)
  workout_plan = ""
  for exercise in workout:
      sets = random.randint(3, 4)  # Randomize sets between 3 and 4
      reps = random.randint(8, 12)  # Randomize reps between 8 and 12
      workout_plan += f"\n- {exercise} ({sets} sets of {reps} reps)\n" #used \n in front so it worked and "-" too for bullets

  return workout_plan

@st.cache
def generate_strength_training_day2(goal):
  exercises = [
      # Push exercises (chest, shoulders, triceps)
      "Push-ups", "Dumbbell bench press", "Overhead press",
      # Pull exercises (back, biceps)
      "Pull-ups", "Dumbbell rows", "Bicep curls",
      # Leg exercises (quads, hamstrings, calves)
      "Squats", "Lunges", "Deadlifts", "Calf raises",
      # Core exercises
      "Plank", "Crunches", "Russian twists"
  ]

  # Day 2 focus on upper body
  workout = random.sample(exercises[:7], 5)  # Select exercises from upper body and core
  workout_plan = ""
  for exercise in workout:
      sets = random.randint(3, 4)  # Randomize sets between 3 and 4
      reps = random.randint(8, 12)  # Randomize reps between 8 and 12
      workout_plan += f"\n- {exercise} ({sets} sets of {reps} reps)\n"
      
      

  return workout_plan

@st.cache
def generate_strength_training_day3(goal):
  exercises = [
      # Push exercises (chest, shoulders, triceps)
      "Push-ups", "Dumbbell bench press", "Overhead press",
      # Pull exercises (back, biceps)
      "Pull-ups", "Dumbbell rows", "Bicep curls",
      # Leg exercises (quads, hamstrings, calves)
      "Squats", "Lunges", "Deadlifts", "Calf raises",
      # Core exercises
      "Plank", "Crunches", "Russian twists"
  ]

  # Day 3 focus on lower body
  workout = random.sample(exercises[6:], 5)  # Select exercises from lower body and core
  workout_plan = ""
  for exercise in workout:
      sets = random.randint(3, 4)  # Randomize sets between 3 and 4
      reps = random.randint(8, 12)  # Randomize reps between 8 and 12
      workout_plan += f"{exercise} ({sets} sets of {reps} reps)\n"

  return workout_plan

# ... Define similar functions for day4, day5, day6, day7 (same pattern)
@st.cache
def generate_cardio(goal):
  if goal == "Weight Loss":
    return "20 minutes of moderate-intensity cardio (e.g., jogging, cycling, elliptical)"
  elif goal == "Weight Gain":
    return "15 minutes of low-intensity cardio or rest intervals between strength sets"
  elif goal == "General Fitness":
    return "10 minutes of low-intensity cardio or rest intervals between strength sets"
  else:
    return "5 minutes of cardio tailored to maintain heart rate in the fat-burning zone"

# Define a function to generate a workout plan for a single day based on user inputs
@st.cache
def generate_workout(goal, day):
  workout_plan = f"Your customized workout plan:\n"
  
  # Warm-up
  workout_plan += "\nWarm-up:\n"
  if day == 1:
      workout_plan += generate_warmup_day1(goal) + "\n"
  elif day == 2:
      workout_plan += generate_warmup_day2(goal) + "\n"
  elif day == 3:
      workout_plan += generate_warmup_day3(goal) + "\n"
  elif day == 4:
      workout_plan += generate_warmup_day4(goal) + "\n"
  elif day == 5:
      workout_plan += generate_warmup_day5(goal) + "\n"
  elif day == 6:
      workout_plan += generate_warmup_day6(goal) + "\n"
  elif day == 7:
      workout_plan += generate_warmup_day7(goal) + "\n"
  # ... Call the appropriate warmup function based on day
  else:
      workout_plan += generate_warmup(goal) + "\n"  # Fallback to general warmup
  
  # Strength Training
  workout_plan += "\nStrength Training:\n"
  if day == 1:
      workout_plan += generate_strength_training_day1(goal) + "\n"
  elif day == 2:
      workout_plan += generate_strength_training_day2(goal) + "\n"
  elif day == 3:
      workout_plan += generate_strength_training_day3(goal) + "\n"
  # ... Call the appropriate function based on day (day4, day5, day6, day7)
  else:
      workout_plan += "Strength training plan not defined for this day yet.\n"
  
  # Cardio
  workout_plan += "\nCardio:\n"
  workout_plan += generate_cardio(goal) + "\n"
  
  # Cool-down
  workout_plan += "\nCool-down:\n"
  workout_plan += "7 minutes of stretching focusing on major muscle groups\n"
  
  return workout_plan

# Streamlit app UI
st.title('Custom Workout Generator')
st.write('''Welcome to the Custom Workout Generator! 
  Enter your details below to get a personalized workout plan.''')

# User input fields
# age = st.slider('Select your age:', 18, 100)
# fitness_level = st.selectbox('Select your fitness level:', ['Beginner', 'Intermediate', 'Advanced'])
goal = st.selectbox('Select your fitness goal:', ['General Fitness', 'Weight Loss', 'Weight Gain', 'Muscle Building'])
days = st.slider('Select number of workout days:', 1, 7)

# Generate workout plan for multiple days upon button click
if st.button('Generate Workout Plan'):
  for day in range(1, days + 1):
    st.header(f'Day {day} Workout Plan:')
    workout_plan = generate_workout(goal, day)  # Generate random workout for each day
    st.write(workout_plan)
    st.markdown('---')  # Add a horizontal line between each day's workout plan
