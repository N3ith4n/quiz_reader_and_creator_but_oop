#imports
import random
from animations import Animation

#class
class QuizRunner:
        #__init__
        def __init__(self, filename):
                self.filename = filename
                self.anim = Animation()
#def load questions
        def load_questions(self):
                with open(self.filename, "r") as file_reader:
                        content = file_reader.read().replace('\r\n', '\n').strip()
                        blocks = [b.strip() for b in content.split('\n\n') if b.strip()]
                
                questions = []
                for block in blocks:
                        lines = [line.strip() for line in block.split('\n') if line.strip()]
                        if len(lines) != 6:
                                print(f"Skipping malformed block (expected 6 lines, got {len(lines)}):\n{block}")
                                continue

                        try:
                                question_text = lines[0].replace("Question: ", "").strip()
                                choices = {}
                                for line in lines[1:5]:
                                        if len(line) >= 3 and line[1] == ')':
                                                choices[line[0].lower()] = line[3:].strip()
                                
                                correct = lines[5].replace("Correct answer: ", "").strip().lower()
                                if correct in choices:
                                        questions.append({ 
                                                "question": question_text,
                                                "choices": choices,
                                                "correct": correct
                                        })
                                else:
                                        print(f"Skipping block (invalid correct answer '{correct}'):\n{block}")
                        except Exception as e:
                                print(f"Error parsing block:\n{block}\nError: {e}")
                
                return questions

#def run
        def run(self):
                self.anim.animated_center("Loading Quiz...")
                questions = self.load_questions()

                if not questions:
                        self.anim.spec_print("\033[31mNo questions found in the quiz file.\033[39m\n")
                        return

                self.anim.spec_print(f"\033[32mLoaded {len(questions)} questions.\033[39m\n")
                random.shuffle(questions)
                score = 0

                for question_data in questions:
                        self.anim.spec_print("\033[36m" + question_data["question"] + "\033[39m", new_line=True)

                        for letter, answer in question_data["choices"].items():
                                self.anim.spec_print(f"\033[33m{letter}. {answer}\033[39m", new_line=True)

                        user_answer = input("\033[34mYour answer: ").lower()

                        if user_answer == question_data["correct"]:
                                self.anim.spec_print("\033[32m✅ Correct!\033[39m\n")
                                score += 1
                        else:
                                correct_choice = question_data["correct"]
                                correct_answer = question_data["choices"][correct_choice]
                                self.anim.spec_print(f"\033[31m❌ Wrong.\033[39m The correct answer was {correct_choice}. {correct_answer}\n")

                self.anim.spec_print(f"\033[32mYour final score: {score}/{len(questions)}\033[39m\n")

#def ask play again
        def ask_play_again(self):
                self.anim.spec_print("\033[96mDo you want to play again? (y/n): ", new_line=False)
                answer = input().strip().lower()
                print("\033[39m", end="")
                return answer == "y"
