import customtkinter
from api_entity import (
    subject_frame,
    course_frame,
    coursetype_frame,
    university_frame
)

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 980
    HEIGHT = 720

    def __init__(self):
        super().__init__()

        self.title("Comsel API Manager")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        # ============ frame_right ============
        self.frame_right = self.home()

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(7, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="API Entities",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_0 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Home",
                                                command=self.home)
        self.button_0.grid(row=2, column=0, pady=10, padx=20)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Courses",
                                                command=self.show_courses)
        self.button_1.grid(row=3, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Course Types",
                                                command=self.show_coursetypes)
        self.button_2.grid(row=4, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Subjects",
                                                command=self.show_subjects)
        self.button_3.grid(row=5, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Universities",
                                                command=self.show_universities)
        self.button_4.grid(row=6, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

    def home(self):
        # print("Button pressed")
        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=5)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)

        self._info = customtkinter.CTkLabel(master=self.frame_right,text="Welcome to Comsel API Manager\nFeel at home.", justify='center', text_font=("Roboto Medium", 24))
        # self._info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=200, sticky="nsew")
        self._info.pack(anchor='center', pady=300)
        return self.frame_right

    def show_courses(self):
        # print("Button pressed")
        self.frame_right = course_frame.CourseManagerFrame(master=self, corner_radius=5)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)

    def show_coursetypes(self):
        # print("Button pressed")
        self.frame_right = coursetype_frame.CourseTypeManagerFrame(master=self,corner_radius=5)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)

    def show_subjects(self):
        # print("Button pressed")
        self.frame_right = subject_frame.SubjectManagerFrame(master=self, corner_radius=5)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=5, pady=15)

    def show_universities(self):
        # print("Button pressed")
        self.frame_right.columnconfigure(1, weight=1)
        self.frame_right.rowconfigure((0,1), weight=1)
        
        self.frame_right = university_frame.UniversityManagerFrame(master=self, corner_radius=5)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()