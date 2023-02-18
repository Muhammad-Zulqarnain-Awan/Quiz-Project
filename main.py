from questions import question_data
from question_model import Questions
from quiz_brain import QuizBrain

question_list = []

for question in question_data:
    question = Questions(question['text'], question['answer'])
    question_list.append(question)

quiz = QuizBrain(question_list)
while quiz.still_has_question():
    quiz.next_question()
    print()
