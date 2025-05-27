#import
from quiz_runner import QuizRunner

#read the quiz1.txt
quiz = QuizRunner("quiz.txt1")
#run the quiz
while True:
        quiz.run()
        if not quiz.ask_play_again():
                break
