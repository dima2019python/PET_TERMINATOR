from tkinter import Tk

from pet_config import Pet
from pet_motion import PetMotionInit

root = Tk()

pet = Pet(root)
PetMotionInit(pet)

# root.after(2500, lambda: pet.change_body("small"))
# root.after(3500, lambda: pet.change_body("normal"))
# root.after(4500, lambda: pet.change_body("big"))
root.mainloop()
