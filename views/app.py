import customtkinter as ctk
from controllers.conversions import seconds2hours

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Convert Seconds to H-M-S")
        self.answer = None

        self.mainframe = ctk.CTkFrame(self)
        self.mainframe.pack(padx=20, pady=20)

        self.welcomelabel = ctk.CTkLabel(self.mainframe, text='Convert Seconds to HMS')
        self.welcomelabel.configure(font=('Helvetica', 30, 'bold'))
        self.welcomelabel.grid(row=0, column=0, padx=50, pady=(20, 20), columnspan=2)

        self.inputsecondslabel = ctk.CTkLabel(self.mainframe, text='Input Seconds')
        self.inputsecondslabel.configure(font=('Helvetica', 20, 'bold'))
        self.inputsecondslabel.grid(row=1, column=0, padx=(50, 10), pady=(3, 20), sticky='w')

        self.inputsecondsentry = ctk.CTkEntry(self.mainframe, placeholder_text='Input Integer Number of Seconds')
        self.inputsecondsentry.configure(width=300, corner_radius=50, justify='center')
        self.inputsecondsentry.grid(row=1, column=1, padx=(10, 50), pady=(3, 20), sticky='ew')

        self.convertbutton = ctk.CTkButton(self.mainframe, text='Convert')
        self.convertbutton.configure(font=('Helvetica', 20, 'bold'), command=self.convert, corner_radius=50)
        self.convertbutton.grid(row=2, column=0, columnspan=2, sticky='ew', padx=(50, 50), pady=20)

        self.hoursdisplay = ctk.CTkLabel(self.mainframe, text='Hours: ')
        self.hoursdisplay.configure(font=('Helvetica', 30, 'bold'))
        self.hoursdisplay.grid(row=3, column=0, padx=20, pady=(3, 3), columnspan=2)

        self.minutesdisplay = ctk.CTkLabel(self.mainframe, text='Minutes: ')
        self.minutesdisplay.configure(font=('Helvetica', 30, 'bold'))
        self.minutesdisplay.grid(row=4, column=0, padx=20, pady=(3, 3), columnspan=2)

        self.secondsdisplay = ctk.CTkLabel(self.mainframe, text='Seconds: ')
        self.secondsdisplay.configure(font=('Helvetica', 30, 'bold'))
        self.secondsdisplay.grid(row=5, column=0, padx=20, pady=(3, 20), columnspan=2)

    def convert(self):
        time: str = self.inputsecondsentry.get()
        seconds: int = int(time)
        self.answer: list[int] = seconds2hours(seconds)
        [print(num, end=' ') for num in self.answer]
        print()
        self.hoursdisplay.configure(text=f'Hours: {self.answer[0]}')
        self.minutesdisplay.configure(text=f'Minutes: {self.answer[1]}')
        self.secondsdisplay.configure(text=f'Seconds: {self.answer[2]}')
