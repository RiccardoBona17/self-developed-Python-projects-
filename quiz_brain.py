# CREATE QuizBrain() class to manage the question presentation


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_pool = question_list
        self.score = 0

    # This method checks whether our quiz has still questions left to ask (up to 12 questions)
    def still_has_questions(self):
        return self.question_number < len(self.question_pool)

    def next_question(self):
        # retrieve current question
        current_question = self.question_pool[self.question_number]
        # increase the question number (question number should be + 1 when printed)
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) - ")
        # Calling the method to extract the answer of the user from this method and compare it to the correct one
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # if the answer is correct
        if user_answer.capitalize() == correct_answer:
            # increase the score by 1
            self.score += 1
            print("You are right!")
        else:
            print("You are wrong!")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


