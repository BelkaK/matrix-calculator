import tkinter
import tkinter.messagebox
import customtkinter

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("NPG Matrix Calculator")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        # call .on_closing() when app gets closed
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Choose operation:",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Substraction",
                                                # <- custom tuple-color
                                                fg_color=("gray75", "gray30"),
                                                command=self.button_event)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Addition",
                                                # <- custom tuple-color
                                                fg_color=("gray75", "gray30"),
                                                command=self.button_event)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Division",
                                                # <- custom tuple-color
                                                fg_color=("gray75", "gray30"),
                                                command=self.button_event)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Power",
                                                # <- custom tuple-color
                                                fg_color=("gray75", "gray30"),
                                                command=self.button_event)
        self.button_4.grid(row=5, column=0, pady=10, padx=20)

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Inversion",
                                                # <- custom tuple-color
                                                fg_color=("gray75", "gray30"),
                                                command=self.button_event)
        self.button_5.grid(row=6, column=0, pady=10, padx=20)

        self.button_6 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Determinant",
                                                # <- custom tuple-color
                                                fg_color=("gray75", "gray30"),
                                                command=self.button_event)
        self.button_6.grid(row=7, column=0, pady=10, padx=20)

        #self.switch_1 = customtkinter.CTkSwitch(master=self.frame_left)
        #self.switch_1.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=3,
                             rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure((0, 1), weight=1)

        self.frame_entry_right = customtkinter.CTkFrame(master=self.frame_info)
        self.frame_entry_right.grid(row=0, column=0, columnspan=1,
                                    rowspan=4, pady=20, padx=20, sticky="nsew")

        self.frame_entry_left = customtkinter.CTkFrame(master=self.frame_info)
        self.frame_entry_left.grid(row=0, column=1, columnspan=1,
                                   rowspan=4, pady=20, padx=20, sticky="nsew")

        self.power_entry = customtkinter.CTkEntry(master=self.frame_info,
                                                  width=120,
                                                  placeholder_text="Power:")
        self.power_entry.grid(row=4, column=0, columnspan=2,
                              pady=20, padx=20, sticky="we")

        # ============ frame_right ============

        self.dimention_entry = customtkinter.CTkEntry(master=self.frame_right,
                                                      width=120,
                                                      placeholder_text="Matrix dimention:")
        self.dimention_entry.grid(row=7, column=0, columnspan=2,
                                  pady=20, padx=20, sticky="we")

        self.button_dimention = customtkinter.CTkButton(master=self.frame_right,
                                                        text="Confirm dimention",
                                                        command=self.dimention_event)
        self.button_dimention.grid(row=7, column=2, columnspan=1,
                                   pady=20, padx=20, sticky="we")

        self.button_history = customtkinter.CTkButton(master=self.frame_right,
                                                      text="Browse history of operations",
                                                      command=self.dimention_event)
        self.button_history.grid(row=8, column=0, columnspan=3,
                                 pady=20, padx=20, sticky="we")

        # set default values
        self.switch_2.select()
        self.matrix1 = []
        self.matrix2 = []

    def button_event(self):
        print("Button pressed")

    def dimention_event(self):
        for input in self.matrix1:
            for elem in input:
                elem.grid_remove()
        for input in self.matrix2:
            for elem in input:
                elem.grid_remove()
        self.matrix1 = []
        self.matrix2 = []
        n = int(self.dimention_entry.get())
        for _ in range(n):
            self.matrix1.append([customtkinter.CTkEntry(
                master=self.frame_entry_left, width=30) for _ in range(n)])
            self.matrix2.append([customtkinter.CTkEntry(
                master=self.frame_entry_right, width=30) for _ in range(n)])
        for i in range(n):
            for j in range(n):
                self.matrix1[i][j].grid(row=i, column=j)
                self.matrix2[i][j].grid(row=i, column=j)

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
