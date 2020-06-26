from tkinter import *

from root_settings import RootWindowSettings


class Pet(RootWindowSettings):
    def __init__(self, root):
        super().__init__(root, eat_func=lambda: self.change_body("big"))
        self.root = root
        self.canvas = Canvas(self.root, width=400, height=400, bg='dark blue', highlightthickness=0)
        self.body_color = 'yellow'
        self.canvas.body_color = self.body_color
        self.canvas.eyes_crossed = False
        self.canvas.happy_level = 2
        self.canvas.tongue_out = False
        self.body = None
        self.pupil_left = None
        self.pupil_right = None
        self.eye_left = None
        self.eye_right = None
        self.mouth_normal = None
        self.ear_left = None
        self.ear_right = None
        self.foot_left = None
        self.foot_right = None
        self.create_pet()
        self.canvas.pack()

    def change_body(self, size):
        pet_coords = {
            "normal": (35, 20, 365, 350,),
            "big": (15, 20, 395, 350,),
            "small": (40, 20, 360, 350,),
        }
        self.canvas.coords(self.body, pet_coords[size])

    def create_pet(self, ):
        self.create_body_form()
        self.create_inner_body()

    def create_body_form(self):
        self.body = self.canvas.create_oval(35, 20, 365, 350, outline=self.body_color, fill=self.body_color)

    def create_inner_body(self):
        self.create_mouth()
        self.create_ear_left()
        self.create_ear_right()
        self.create_foot_left()
        self.create_foot_right()
        self.create_eye_left()
        self.create_eye_right()
        self.create_pupil_left()
        self.create_pupil_right()

    def create_mouth(self):
        self.mouth_normal = self.canvas.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)

    def create_ear_left(self):
        self.ear_left = self.canvas.create_polygon(75, 80, 75, 10, 165, 70, outline=self.body_color,
                                                   fill=self.body_color)

    def create_ear_right(self):
        self.ear_right = self.canvas.create_polygon(255, 45, 325, 10, 320, 70, outline=self.body_color,
                                                    fill=self.body_color)

    def create_foot_left(self):
        self.foot_left = self.canvas.create_oval(65, 320, 145, 360, outline=self.body_color, fill=self.body_color)

    def create_foot_right(self):
        self.foot_right = self.canvas.create_oval(250, 320, 330, 360, outline=self.body_color, fill=self.body_color)

    def create_eye_left(self):
        self.eye_left = self.canvas.create_oval(130, 110, 160, 170, outline='black', fill='white')

    def create_eye_right(self):
        self.eye_right = self.canvas.create_oval(230, 110, 260, 170, outline='black', fill='white')

    def create_pupil_left(self):
        self.pupil_left = self.canvas.create_oval(140, 145, 150, 155, outline='black', fill='black')

    def create_pupil_right(self):
        self.pupil_right = self.canvas.create_oval(240, 145, 250, 155, outline='black', fill='black')
