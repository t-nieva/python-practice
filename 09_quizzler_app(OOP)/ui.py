from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
RIGHT_ANSWER_BG_COLOR = "#FFDCDC"
WRONG_ANSWER_BG_COLOR = "#B8CFCE"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="test",
            fill=THEME_COLOR,
            font=("Area", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        img_true = PhotoImage(file="images/true.png")
        self.btn_true = Button(image=img_true, border=0, bg=THEME_COLOR, highlightthickness=0,
                               activebackground=THEME_COLOR, command=self.true_pressed)
        self.btn_true.grid(row=2, column=0)

        img_false = PhotoImage(file="images/false.png")
        self.btn_false = Button(image=img_false, border=0, bg=THEME_COLOR, highlightthickness=0,
                                activebackground=THEME_COLOR, command=self.false_pressed)
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz\n"
                                                            f"Your final score was: {self.quiz.score}/"
                                                            f"{self.quiz.question_number}")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right:bool):
        if is_right:
            self.canvas.config(bg=RIGHT_ANSWER_BG_COLOR)
        else:
            self.canvas.config(bg=WRONG_ANSWER_BG_COLOR)
        self.window.after(1000, self.get_next_question)

