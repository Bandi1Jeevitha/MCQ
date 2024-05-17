#!/usr/bin/env python
# coding: utf-8

# Quiz Game Implementation in Python:
# 1. Define Questions and Answers:

# In[2]:


questions = {
    "What is the capital of France?": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"],
    "Which planet is known as the Red Planet?": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    "What is the powerhouse of the cell?": ["A.Mitochondria", "B. Nucleus", "C. Ribosome", "D. Golgi Apparatus"],
    "Capital of India?":["A.Gujarat","B.New York","C.Simla","D.Delhi"]}

answers = {
    "What is the capital of France?": "B",
    "Which planet is known as the Red Planet?": "B",
    "What is the powerhouse of the cell?": "C",
    "Capital of India?":"D"
}


# 2. Scoring System:
# 

# In[3]:


score = 0

def evaluate_answer(question, answer):
    global score
    if answers.get(question) == answer:
        score += 1


# 3. User Input Handling and Quiz Logic:

# In[4]:


def display_question(question, options):
    print(question)
    for option in options:
        print(option)

def take_quiz():
    for question, options in questions.items():
        display_question(question, options)
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        evaluate_answer(question, user_answer)
        if answers.get(question) == user_answer:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", answers.get(question))

def main():
    take_quiz()
    print("Quiz completed! Your final score is:", score)

if __name__ == "__main__":
    main()


# In[ ]:




