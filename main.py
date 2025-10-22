import tkinter as tk
from idlelib.outwin import file_line_pats
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button

class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title('George\'s Notepad')

        # Text widget
        self.text_area: Text = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        # Frame
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        # Save button
        self.save_button: Button = Button(self.button_frame, text='Save', command=self.save_file)
        self.save_button.pack(side=tk.LEFT)

        # Load button
        self.load_button: Button = Button(self.button_frame, text='Load', command=self.load_file)
        self.load_button.pack(side=tk.RIGHT)

    def save_file(self) -> None:
        pass

    def load_file(self) -> None:
        pass

    def run(self) -> None:
        self.root.mainloop()

def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()

if __name__ == '__main__':
    main()