from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for item in question_data:
    q, a = item["question"], item["correct_answer"]
    question = Question(q, a)
    question_bank.append(question)
# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"You final score was: {quiz.score}/{quiz.question_number}")
