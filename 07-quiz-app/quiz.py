# 07 - Quiz App using JSON + random
import json
import random

FILE_NAME = "questions.json"

def load_questions():
    try:
        with open(FILE_NAME, "r") as f:
            questions = json.load(f)
            random.shuffle(questions) # shuffle so order is different each time
            return questions
    except FileNotFoundError:
        print("questions.json not found!")
        return []
    except json.JSONDecodeError:
        print("questions.json is corrupted!")
        return []

def run_quiz():
    questions = load_questions()
    if not questions:
        return

    score = 0
    print("--- Python Quiz App ---")
    print(f"Total Questions: {len(questions)}\n")

    for i, q in enumerate(questions, 1):
        print(f"Q{i}. {q['question']}")
        for idx, opt in enumerate(q['options'], 1):
            print(f"  {idx}. {opt}")

        # User can type 1/2/3/4 or full text
        user_ans = input("Your answer (1-4 or text): ").strip()

        # Convert number to text if user typed number
        if user_ans.isdigit() and 1 <= int(user_ans) <= len(q['options']):
            user_ans = q['options'][int(user_ans) - 1]

        # Check - case insensitive
        if user_ans.lower() == q['answer'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct is: {q['answer']}\n")

    print("--- Result ---")
    print(f"Your Score: {score}/{len(questions)}")
    percent = (score / len(questions)) * 100
    print(f"Percentage: {percent:.1f}%")

    if percent == 100:
        print("Perfect! You're a pro!")
    elif percent >= 70:
        print("Great job!")
    elif percent >= 50:
        print("Good, keep practicing!")
    else:
        print("Keep learning, you got this!")

run_quiz()