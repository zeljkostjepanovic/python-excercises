import json
import os

current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

with open('questions.json', 'r') as file:
    content = file.read()
    
    
data = json.loads(content)

score = 0

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        question["result"] = "Correct Answer"
    else:
        question["result"] = "Wrong Answer"

for index, question in enumerate(data):
    message = f"{question['result']}: {index + 1 } - Your answer: {question['user_choice']}, \
Correct answer: {question['correct_answer']}"
    print(message)

       
print(f"\nYour score: {score}/{len(data)}")