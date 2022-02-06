from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz= quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)

        # canvas
        self.canvas = Canvas(height=250, width=300)
        self.canvas_text = self.canvas.create_text(150, 125,
                                                   text= "", fill=THEME_COLOR,
                                                   width=290,
                                                   font=("Arial",20,"italic"))

        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)

        #buttons
        image_t_button= PhotoImage(file="true.png")
        self.true_button = Button(image= image_t_button,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        image_f_button= PhotoImage(file="false.png")
        self.false_button= Button(image=image_f_button,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        #labels
        self.score_label= Label(text="Score: 0", fg="white")
        self.score_label.config(bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)



        self.get_next_question()


        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text= self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question_text)
        else:
            self.canvas.itemconfig(self.canvas_text,text="You don`t have more questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):

        self.give_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):

        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config( bg="red")
        self.window.after(1000,self.get_next_question)



