# QUIZ
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Initializing question_bank (list of question objects)
question_bank = []

# Loop through the question data list
for question in question_data:
    # extracting the question text and answer
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text=question_text,
                            question_answer=question_answer)
    question_bank.append(new_question)

# Initialize the quiz_brain object (question manager)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

# The quiz is finished
print("--------------------")
print(f"You did a good job! Your final score is: {quiz.score}/{quiz.question_number}")



