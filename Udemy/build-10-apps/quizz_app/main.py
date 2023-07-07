import json

with open('questions.json', 'r') as file:
    content = file.read()
    
    
data = json.loads(content)

print(data)

for question in data:
    print(question["question_text"])