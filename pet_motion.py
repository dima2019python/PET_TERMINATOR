from tkinter import *


class PetMotionInit:
    def __init__(self, pet):
        self.pet = pet
        self.cheek_left = self.cheek_left()
        self.cheek_right = self.cheek_right()
        self.mouth_happy = self.mouth_happy()
        self.mouth_sad = self.mouth_sad()
        self.tongue_tip = self.tongue_tip()
        self.tongue_main = self.tongue_main()
        self.pet.canvas.bind('<Motion>', self.show_happy)
        self.pet.canvas.bind('<Leave>', self.hide_happy)
        self.pet.canvas.bind('<Double-1>', self.cheeky)
        self.pet.root.after(1000, self.blink)
        self.pet.root.after(5000, self.sad)

    def toggle_eyes(self):
        current_color = self.pet.canvas.itemcget(self.pet.eye_left, 'fill')
        new_color = self.pet.canvas.body_color if current_color == 'white' else 'white'
        current_state = self.pet.canvas.itemcget(self.pet.pupil_left, 'state')
        new_state = NORMAL if current_state == HIDDEN else HIDDEN
        self.pet.canvas.itemconfigure(self.pet.pupil_left, state=new_state)
        self.pet.canvas.itemconfigure(self.pet.pupil_right, state=new_state)
        self.pet.canvas.itemconfigure(self.pet.eye_left, fill=new_color)
        self.pet.canvas.itemconfigure(self.pet.eye_right, fill=new_color)

    def blink(self):
        self.toggle_eyes()
        self.pet.root.after(250, self.toggle_eyes)
        self.pet.root.after(3000, self.blink)

    def show_happy(self, event):
        if (20 <= event.x <= 350) and (20 <= event.y <= 350):
            self.pet.canvas.itemconfigure(self.cheek_left, state=NORMAL)
            self.pet.canvas.itemconfigure(self.cheek_right, state=NORMAL)
            self.pet.canvas.itemconfigure(self.mouth_happy, state=NORMAL)
            self.pet.canvas.itemconfigure(self.pet.mouth_normal, state=HIDDEN)
            self.pet.canvas.itemconfigure(self.mouth_sad, state=HIDDEN)
            self.pet.canvas.happy_level = 1
        return

    def hide_happy(self, event):
        self.pet.canvas.itemconfigure(self.cheek_left, state=HIDDEN)
        self.pet.canvas.itemconfigure(self.cheek_right, state=HIDDEN)
        self.pet.canvas.itemconfigure(self.mouth_happy, state=HIDDEN)
        self.pet.canvas.itemconfigure(self.pet.mouth_normal, state=NORMAL)
        self.pet.canvas.itemconfigure(self.mouth_sad, state=HIDDEN)
        return

    def sad(self):
        if self.pet.canvas.happy_level == 0:
            self.pet.canvas.itemconfigure(self.mouth_happy, state=HIDDEN)
            self.pet.canvas.itemconfigure(self.pet.mouth_normal, state=HIDDEN)
            self.pet.canvas.itemconfigure(self.mouth_sad, state=NORMAL)
        else:
            self.pet.canvas.happy_level -= 1
        self.pet.root.after(5000, self.sad)

    def cheeky(self, event):
        self.toggle_tongue()
        self.toggle_pupils()
        self.hide_happy(event)
        self.pet.root.after(1500, self.toggle_tongue)
        self.pet.root.after(1500, self.toggle_pupils)
        return

    def toggle_tongue(self):
        if not self.pet.canvas.tongue_out:
            self.pet.canvas.itemconfigure(self.tongue_tip, state=NORMAL)
            self.pet.canvas.itemconfigure(self.tongue_main, state=NORMAL)
            self.pet.canvas.tongue_out = True
        else:
            self.pet.canvas.itemconfigure(self.tongue_tip, state=HIDDEN)
            self.pet.canvas.itemconfigure(self.tongue_main, state=HIDDEN)
            self.pet.canvas.tongue_out = False

    def toggle_pupils(self):
        if not self.pet.canvas.eyes_crossed:
            self.pet.canvas.move(self.pet.pupil_left, 10, -5)
            self.pet.canvas.move(self.pet.pupil_right, -10, -5)
            self.pet.canvas.eyes_crossed = True
        else:
            self.pet.canvas.move(self.pet.pupil_left, -10, 5)
            self.pet.canvas.move(self.pet.pupil_right, 10, 5)
            self.pet.canvas.eyes_crossed = False

    def mouth_happy(self):
        return self.pet.canvas.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)

    def mouth_sad(self):
        return self.pet.canvas.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)

    def tongue_main(self):
        return self.pet.canvas.create_rectangle(170, 250, 230, 270, outline='red', fill='red', state=HIDDEN)

    def tongue_tip(self):
        return self.pet.canvas.create_oval(170, 250, 230, 300, outline='red', fill='red', state=HIDDEN)

    def cheek_left(self):
        return self.pet.canvas.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)

    def cheek_right(self):
        return self.pet.canvas.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)
