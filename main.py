import tkinter
import tkinter.messagebox
from typing import Tuple
import customtkinter

from memory_managment import Memory
from operations import *
from read_from_file import *

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):

    WIDTH = 1000
    HEIGHT = 600

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

        # ============ operation choises ============

        self.prompt_operation = customtkinter.CTkLabel(master=self.frame_left,
                                                       text="Choose operation:",
                                                       text_font=("Roboto Medium", -16))  # font name and size in px
        self.prompt_operation.grid(row=1, column=0, pady=10, padx=10)

        self.subtraction_button = customtkinter.CTkButton(master=self.frame_left,
                                                          text="Subtraction",
                                                          # <- custom tuple-color
                                                          fg_color=(
                                                              "gray75", "gray30"),
                                                          command=self.subtraction_button_event)
        self.subtraction_button.grid(row=2, column=0, pady=10, padx=20)

        self.addition_button = customtkinter.CTkButton(master=self.frame_left,
                                                       text="Addition",
                                                       # <- custom tuple-color
                                                       fg_color=(
                                                           "gray75", "gray30"),
                                                       command=self.addition_button_event)
        self.addition_button.grid(row=3, column=0, pady=10, padx=20)

        self.multiplication_button = customtkinter.CTkButton(master=self.frame_left,
                                                             text="Multiplication",
                                                             # <- custom tuple-color
                                                             fg_color=(
                                                                 "gray75", "gray30"),
                                                             command=self.multiplication_button_event)
        self.multiplication_button.grid(row=4, column=0, pady=10, padx=20)

        self.power_button = customtkinter.CTkButton(master=self.frame_left,
                                                    text="Power",
                                                    # <- custom tuple-color
                                                    fg_color=(
                                                        "gray75", "gray30"),
                                                    command=self.power_button_event)
        self.power_button.grid(row=5, column=0, pady=10, padx=20)

        self.inversion_button = customtkinter.CTkButton(master=self.frame_left,
                                                        text="Inversion",
                                                        # <- custom tuple-color
                                                        fg_color=(
                                                            "gray75", "gray30"),
                                                        command=self.inversion_button_event)
        self.inversion_button.grid(row=6, column=0, pady=10, padx=20)

        self.determinant_button = customtkinter.CTkButton(master=self.frame_left,
                                                          text="Determinant",
                                                          # <- custom tuple-color
                                                          fg_color=(
                                                              "gray75", "gray30"),
                                                          command=self.determinant_button_event)
        self.determinant_button.grid(row=7, column=0, pady=10, padx=20)

        self.mode_switch = customtkinter.CTkSwitch(master=self.frame_left,
                                                   text="Dark Mode",
                                                   command=self.change_mode)
        self.mode_switch.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(8, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_matrices = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_matrices.grid(row=0, column=0, columnspan=3,
                                 rowspan=4, pady=20, padx=20, sticky="nsew")

        self.path_entry = customtkinter.CTkEntry(master=self.frame_right,
                                                 width=120,
                                                 placeholder_text="Path:")
        self.path_entry.grid(row=4, column=0, columnspan=1,
                             pady=20, padx=20, sticky="we")

        self.char_entry = customtkinter.CTkEntry(master=self.frame_right,
                                                 width=120,
                                                 placeholder_text="Separating char:")
        self.char_entry.grid(row=4, column=1, columnspan=1,
                             pady=20, padx=20, sticky="we")

        self.read_file_button = customtkinter.CTkButton(master=self.frame_right,
                                                        text="Confirm file",
                                                        command=self.read_file_button_event)
        self.read_file_button.grid(row=4, column=2, columnspan=1,
                                   pady=20, padx=20, sticky="we")

        self.dimention_entry = customtkinter.CTkEntry(master=self.frame_right,
                                                      width=120,
                                                      placeholder_text="Matrix dimention:")
        self.dimention_entry.grid(row=7, column=0, columnspan=2,
                                  pady=20, padx=20, sticky="we")

        self.dimention_button = customtkinter.CTkButton(master=self.frame_right,
                                                        text="Confirm dimention",
                                                        command=self.dimention_button_event)
        self.dimention_button.grid(row=7, column=2, columnspan=1,
                                   pady=20, padx=20, sticky="we")

        self.history_button = customtkinter.CTkButton(master=self.frame_right,
                                                      text="Browse history of operations",
                                                      command=self.history_button_event)
        self.history_button.grid(row=8, column=0, columnspan=3,
                                 pady=20, padx=20, sticky="we")

        # ============ frame_matrices ============

        # configure grid layout (1x3)
        self.frame_matrices.rowconfigure(0, weight=1)
        self.frame_matrices.columnconfigure((0, 1, 2), weight=1)

        self.frame_entry_right = customtkinter.CTkFrame(
            master=self.frame_matrices)
        self.frame_entry_right.grid(row=0, column=1, columnspan=1,
                                    rowspan=4, pady=20, padx=20, sticky="nsew")

        self.frame_entry_left = customtkinter.CTkFrame(
            master=self.frame_matrices)
        self.frame_entry_left.grid(row=0, column=0, columnspan=1,
                                   rowspan=4, pady=20, padx=20, sticky="nsew")

        self.frame_result = customtkinter.CTkFrame(master=self.frame_matrices)
        self.frame_result.grid(row=0, column=2, columnspan=1,
                               rowspan=4, pady=20, padx=20, sticky="nsew")

        self.power_entry = customtkinter.CTkEntry(master=self.frame_matrices,
                                                  width=120,
                                                  placeholder_text="Power:")
        self.power_entry.grid(row=4, column=0, columnspan=3,
                              pady=20, padx=20, sticky="we")

        # set default values
        self.mode_switch.select()
        self.matrix1 = []
        self.matrix2 = []
        self.result_display = []
        self.memory = Memory()

    def read_file_button_event(self):
        matrix = read_matrix_from_file(
            self.path_entry.get(), self.char_entry.get)
        for input in self.matrix1:
            for elem in input:
                elem.grid_remove()
        self.matrix1 = []
        for i in range(len(matrix)):
            self.matrix1.append([customtkinter.CTkEntry(
                master=self.frame_entry_left, width=30, placeholder_text=matrix[i][j]) for j in range(len(matrix))])
        for row_index, row in enumerate(self.matrix1):
            for column_index, elem in enumerate(row):
                elem.grid(row=row_index, column=column_index)

    def dimention_button_event(self):
        dimention = int(self.dimention_entry.get())
        if dimention < 7:

            # clear the previous inputs
            for input in self.matrix1:
                for elem in input:
                    elem.grid_remove()
            for input in self.matrix2:
                for elem in input:
                    elem.grid_remove()
            self.matrix1 = []
            self.matrix2 = []

            # display new entries
            for _ in range(dimention):
                self.matrix1.append([customtkinter.CTkEntry(
                    master=self.frame_entry_left, width=30) for _ in range(dimention)])
                self.matrix2.append([customtkinter.CTkEntry(
                    master=self.frame_entry_right, width=30) for _ in range(dimention)])
            for row_index, row in enumerate(self.matrix1):
                for column_index, elem in enumerate(row):
                    elem.grid(row=row_index, column=column_index)
                    self.matrix2[row_index][column_index].grid(
                        row=row_index, column=column_index)

    def get_data(self) -> Tuple[List[float], List[float], int]:
        matrix1 = []
        matrix2 = []
        try:
            power = int(self.power_entry.get())
        except ValueError:
            power = 0

        for row_index, row in enumerate(self.matrix1):
            vector1 = []
            vector2 = []
            for column_index, elem in enumerate(row):
                try:
                    vector1.append(float(elem.get()))
                except ValueError:
                    vector1.append(0.0)
                try:
                    vector2.append(
                        float(self.matrix2[row_index][column_index].get()))
                except ValueError:
                    vector2.append(0.0)
            matrix1.append(vector1)
            matrix2.append(vector2)

        # for row_index, row in enumerate(self.matrix1):
        #    vector1 = [float(elem.get()) if elem else 0 for elem in row]
        #    matrix1.append(vector1)
        #    vector2 = [
        #        float(elem.get()) if elem else 0 for elem in self.matrix2[row_index]]
        #    matrix2.append(vector2)

        return [matrix1, matrix2, power]

    def display_result(self, result: List[List[float]]) -> None:
        for input in self.result_display:
            for elem in input:
                elem.grid_remove()
        self.result_display = []
        for row in result:
            self.result_display.append([customtkinter.CTkLabel(
                master=self.frame_result, text=f"{value}", width=30) for value in row])
        for row_index, row in enumerate(self.result_display):
            for column_index, value in enumerate(row):
                value.grid(row=row_index, column=column_index)

    def display_operation_history_window(self):
        window = customtkinter.CTkToplevel(self)
        window.title("Operation history")
        window.geometry("600x700")

        window.grid_columnconfigure((0), weight=1)
        window.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

        # create label on CTkToplevel window
        for row, entry in enumerate(self.memory.results_list):

            frame_entry = customtkinter.CTkFrame(master=window,
                                                 width=180,
                                                 corner_radius=0)
            frame_entry.grid(row=row, column=0, sticky="nswe")
            frame_entry.rowconfigure((0), weight=1)
            frame_entry.columnconfigure((0, 1, 2, 3), weight=1)

            frame_matrix1 = customtkinter.CTkFrame(master=frame_entry,
                                                   width=180,
                                                   corner_radius=0)
            frame_matrix1.grid(row=0, column=0, sticky="nswe")

            frame_matrix2 = customtkinter.CTkFrame(master=frame_entry,
                                                   width=180,
                                                   corner_radius=0)
            frame_matrix2.grid(row=0, column=1, sticky="nswe")

            frame_operation = customtkinter.CTkFrame(master=frame_entry,
                                                     width=180,
                                                     corner_radius=0)
            frame_operation.grid(row=0, column=2, sticky="nswe")

            frame_result = customtkinter.CTkFrame(master=frame_entry,
                                                  width=180,
                                                  corner_radius=0)
            frame_result.grid(row=0, column=3, sticky="nswe")

            if entry[3] == "+" or entry[3] == "-" or entry[3] == "*":
                matrix1 = []
                matrix2 = []
                result = []

                for row in entry[0]:
                    matrix1.append([customtkinter.CTkLabel(
                        master=frame_matrix1, text=f"{value}", width=30) for value in row])
                    for row_index, row in enumerate(matrix1):
                        for column_index, value in enumerate(row):
                            value.grid(row=row_index, column=column_index)

                for row in entry[1]:
                    matrix2.append([customtkinter.CTkLabel(
                        master=frame_matrix2, text=f"{value}", width=30) for value in row])
                    for row_index, row in enumerate(matrix2):
                        for column_index, value in enumerate(row):
                            value.grid(row=row_index, column=column_index)

                for row in entry[2]:
                    result.append([customtkinter.CTkLabel(
                        master=frame_result, text=f"{value}", width=30) for value in row])
                    for row_index, row in enumerate(result):
                        for column_index, value in enumerate(row):
                            value.grid(row=row_index, column=column_index)

                operation = customtkinter.CTkLabel(
                    master=frame_operation, text=f"{entry[3]}", width=30)
                operation.grid(row=1, column=1)

            elif entry[3] == "determinant":
                matrix1 = []

                for row in entry[0]:
                    matrix1.append([customtkinter.CTkLabel(
                        master=frame_matrix1, text=f"{value}", width=30) for value in row])
                    for row_index, row in enumerate(matrix1):
                        for column_index, value in enumerate(row):
                            value.grid(row=row_index, column=column_index)

                result = customtkinter.CTkLabel(
                    master=frame_result, text=f"{entry[2]}", width=30)
                result.grid(row=1, column=1)

                operation = customtkinter.CTkLabel(
                    master=frame_operation, text=f"{entry[3]}", width=30)
                operation.grid(row=1, column=1)

            elif entry[3] == '^':
                matrix1 = []
                result = []
                for row in entry[0]:
                    matrix1.append([customtkinter.CTkLabel(
                        master=frame_matrix1, text=f"{value}", width=30) for value in row])
                    for row_index, row in enumerate(matrix1):
                        for column_index, value in enumerate(row):
                            value.grid(row=row_index, column=column_index)
                for row in entry[2]:
                    result.append([customtkinter.CTkLabel(
                        master=frame_result, text=f"{value}", width=30) for value in row])
                    for row_index, row in enumerate(result):
                        for column_index, value in enumerate(row):
                            value.grid(row=row_index, column=column_index)

                power = customtkinter.CTkLabel(
                    master=frame_matrix2, text=f"{entry[1]}", width=30)
                power.grid(row=1, column=1)

                operation = customtkinter.CTkLabel(
                    master=frame_operation, text=f"{entry[3]}", width=30)
                operation.grid(row=1, column=1)

            elif entry[3] == '^-1':

                matrix1 = []
                result = []
                for row in entry[0]:
                    matrix1.append([customtkinter.CTkLabel(
                        master=frame_matrix1, text=f"{value}", width=30) for value in row])
                    for row_index, row in enumerate(matrix1):
                        for column_index, value in enumerate(row):
                            value.grid(row=row_index, column=column_index)
                for row in entry[2]:
                    result.append([customtkinter.CTkLabel(
                        master=frame_result, text=f"{value}", width=30) for value in row])
                    for row_index, row in enumerate(result):
                        for column_index, value in enumerate(row):
                            value.grid(row=row_index, column=column_index)

                operation = customtkinter.CTkLabel(
                    master=frame_operation, text=f"{entry[3]}", width=30)
                operation.grid(row=1, column=1)

    def history_button_event(self):
        self.display_operation_history_window()

    def addition_button_event(self):
        self.memory.add_result(self.get_data()[0], self.get_data()[
                               1], add_matrices(self.get_data()[0], self.get_data()[1]), '+')
        self.display_result(add_matrices(
            self.get_data()[0], self.get_data()[1]))

    def subtraction_button_event(self):
        self.memory.add_result(self.get_data()[0], self.get_data()[
                               1], subtract_matrices(self.get_data()[0], self.get_data()[1]), '-')
        self.display_result(subtract_matrices(
            self.get_data()[0], self.get_data()[1]))

    def multiplication_button_event(self):
        self.memory.add_result(self.get_data()[0], self.get_data()[
                               1], multiply_matrices(self.get_data()[0], self.get_data()[1]), '*')
        self.display_result(multiply_matrices(
            self.get_data()[0], self.get_data()[1]))

    def power_button_event(self):
        self.memory.add_result(self.get_data()[0], self.get_data()[
                               2], raise_to_power(self.get_data()[0], self.get_data()[2]), '^')
        self.display_result(raise_to_power(
            self.get_data()[0], self.get_data()[2]))

    def inversion_button_event(self):
        self.memory.add_result(
            self.get_data()[0], [], invert_matrix(self.get_data()[0]), '^-1')
        self.display_result(invert_matrix(self.get_data()[0]))

    def determinant_button_event(self):
        self.memory.add_result(self.get_data()[0], [], compute_determinant(
            self.get_data()[0]), 'determinant')
        result = [[compute_determinant(self.get_data()[0])]]
        self.display_result(result)

    def change_mode(self):
        if self.mode_switch.get() == 1:
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
