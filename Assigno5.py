import requests
import json
import re

url = "https://michaelgathara.com/api/python-challenge"

response = requests.get(url)
challenges = response.json()

for challenge in challenges:
    problem_id = challenge['id']
    problem = challenge['problem']
    print(f"Problem {problem_id}: {problem}")
    parts = re.findall(r'\d+|\S', problem)
    operand1 = int(parts[0])
    operator = parts[1]
    operand2 = int(parts[2])
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
 print(f"Solution: {result}\n")
print('Athreya Madugula')
print('blazerid:madugula')