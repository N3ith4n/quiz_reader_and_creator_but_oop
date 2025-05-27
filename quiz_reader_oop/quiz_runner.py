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

#def ask play again
