from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list of Question objects from the provided question_data
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create a QuizBrain instance with the question bank
quiz = QuizBrain(question_bank)

# Iterate through the questions until there are no more questions
while quiz.still_has_questions():
    quiz.next_question()

# Display a completion message along with the final score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
