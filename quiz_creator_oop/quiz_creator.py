#imports
import time

#imports but the animations.py this time
from animations import Animation

#class
class QuizCreator:
        #__init__
        def __init__(self, filename):
                self.filename = filename
                self.choices = ["a", "b", "c", "d"]
                self.anim = Animation()

        #def create_quiz
        def create_quiz(self):
                self.anim.animated_center("loading...")
                with open(self.filename, "a") as file_writer:
                        while True:
                                self.anim.spec_print('Enter a question (type "stop" to finish): ')
                                question = input()
                                if question.lower() == "stop":
                                        break

                                answers = {}
                                correct = ""

                                for choice in self.choices:
                                        self.anim.spec_print(f"{choice}. ")
                                        ans = input()
                                        self.anim.spec_print("Is this the correct answer? (y/n): ")
                                        is_correct = input().lower()
                                        answers[choice] = ans
                                        if is_correct == "y":
                                                correct = choice

                                #animation
                                index = 0
                                while index < len(question):
                                        print(f"{self.filename} < {question[index:]}")
                                        index += 1
                                        time.sleep(0.1)

                                #write to file
                                file_writer.write(f"Question: {question}\n")
                                for key in self.choices:
                                        file_writer.write(f"{key}) {answers[key]}\n")
                                file_writer.write(f"Correct answer: {correct}\n\n")
