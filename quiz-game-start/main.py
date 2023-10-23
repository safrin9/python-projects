from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    question_text=question["question"]
    question_ans=question["correct_answer"]
    new_q=Question(question_text,question_ans)
    question_bank.append((new_q))
q=QuizBrain(question_bank)
while q.still_has_q():

    q.next_q()
print("you completed the quiz")
print(f"your final score: {q.score}/{q.question_number}")