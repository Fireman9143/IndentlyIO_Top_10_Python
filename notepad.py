import tkinter as tk
from tkinter import filedialog, Tk, Text, Frame, Button

class SimpleNotepad:
    def __init__(self, root:Tk) -> None:
        """Initialize notepad class"""
        self.root = root
        self.root.title('My notepad')
        self.filename = ""

        #Text widget
        self.text_area:Text = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        #Frame
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        #Save As button
        self.save_button: Button = Button(self.button_frame, text='Save As', command=self.save_as_file)
        self.save_button.pack(side=tk.LEFT)

        #Save button
        self.save_button: Button = Button(self.button_frame, text='Save', command=self.save_file)
        self.save_button.pack(side=tk.LEFT)

        #Load button
        self.load_button: Button = Button(self.button_frame, text='Load', command=self.load_file)
        self.load_button.pack(side=tk.LEFT)

    def save_as_file(self) -> None:
        """Selecting save as button will automatically load dialogue box for file name"""
        self.filename:str = filedialog.asksaveasfilename(confirmoverwrite=False,
                                                     defaultextension='.txt',
                                                     filetypes=[('Text files', '*.txt')])
        
        with open(self.filename, 'w') as file:
            file.write(self.text_area.get(1.0, tk.END))

        print(f'File saved to: {self.filename}')

    def save_file(self) -> None:
        """Selecing save button will check if filename exists from previous save or load.
        If no filename exists, will prompt for one, other wise will just save"""
        if self.filename == "":
            self.save_as_file
        else:
            with open(self.filename, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

        print(f'File saved to: {self.filename}')

    def load_file(self) -> None:
        """Selecting load button will prompt for the file to load, remove anything in the window, and load the file"""
        self.filename:str = filedialog.askopenfilename(defaultextension='.txt',
                                                     filetypes=[('Text files', '*.txt')])
        
        with open(self.filename, 'r') as file:
            content:str = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.INSERT, content)
            
        print(f'File loaded from: {self.filename}')

    def run(self) -> None:
        """Starts TKINTER loop execution"""
        self.root.mainloop()


def main():
    """Creates instance of TK object named root, 
    uses it to make an instance of SimpleNotepad object named app, 
    then executes the run function for TKINTER main loop"""
    root:Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()

if __name__ == "__main__":
    main()