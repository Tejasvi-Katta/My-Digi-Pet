import tkinter as tk
import itertools
import os

class DigiPet:
    def __init__(self, root, frames):
        self.root = root
        self.frames = frames
        self.current_frame = 0
        self.direction = 1 #1=right and -1=left
        #self.current_pet = None
        self.pet_name = "DigiPet"
        #self.happiness = 5
        #self.hunger = 5
        #self.energy = 5
        #self.age = 0

        self.label = tk.Label(root, bd=0, bg='white')
        self.label.pack()

        root.overrideredirect(True)
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-transparentcolor", 'white')

        self.update_animation()
        self.move_pet()
    
    def update_animation(self):
        self.label.config(image=self.frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.label.after(500, self.update_animation)

    def move_pet(self):
        x=self.root.winfo_x() + self.direction*5
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        y=screen_height - 50
        if x<0 or x>screen_width-70:
            self.direction*=-1
        self.root.geometry(f"+{x}+{y}")
        self.root.after(200, self.move_pet)
    
def load_frames(path):
    files = sorted([f for f in os.listdir(path) if f.endswith('.png')])
    return [tk.PhotoImage(file=os.path.join(path, f)) for f in files]

if __name__ == "__main__":
    root = tk.Tk()
    frame_folder = "pet frames"
    os.makedirs(frame_folder, exist_ok=True)

    if not os.listdir(frame_folder):
        from PIL import Image, ImageDraw
        for i in range(4):
            img = Image.new('RGBA', (64,64), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            draw.ellipse((0, 0, 64, 64), fill=(0, 255, 0, 255))
            img.save(os.path.join(frame_folder, f"frame_{i}.png"))
    
    frames = load_frames(frame_folder)

    root.geometry("+100+5000")
    pet=DigiPet(root, frames)
    root.mainloop()