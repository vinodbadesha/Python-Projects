questions = [
    {
        "prompt": "What is the capital of Bharat?",
        "options": ["A: Hyderabad", "B: New Delhi", "C: Mumbai", "D: Bengaluru"],
        "answer": "B"
    },
    {
        "prompt": "What is the national animal of Bharat?",
        "options": ["A: Cow", "B: Elephant", "C: Cheetah", "D: Royal Bengal Tiger"],
        "answer": "D"
    },
    {
        "prompt": "Who is known as The Ironman of Bharat?",
        "options": ["A: Bhagat Singh", "B: Subhash Chandra Bose", "C: Sardar Vallabhai Patel", "D: Veer Savarkar"],
        "answer": "C"
    },
    {
        "prompt": "Who designed the Tricolor of Bharat?",
        "options": ["A: Dr B.R.Ambedkar", "B: Sarojini Naidu", "C: Pingali Venkaiah", "D: Dadabai Naoroji"],
        "answer": "C"
    }
]

def answer_quiz(questions):
    score = 0

    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Select an option: ").upper()
        if answer == question["answer"]:
            print("Correct Answer!\n")
            score += 1
        else:
            print("Wrong Answer! Correct Answer is ",question["answer"],"\n")
    
    print(f"Your total score is: {score}")

answer_quiz(questions)


        







