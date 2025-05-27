#import
from quiz_runner import QuizRunner

#read the quiz1.txt
quiz = QuizRunner("quiz1.txt")
#run the quiz
while True:
        quiz.run()
        if not quiz.ask_play_again():
                break
