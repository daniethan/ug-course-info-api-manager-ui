import asyncio
import customtkinter as ctk
import tkinter as tk
import config.api_config as api_config

ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class UniversityManagerFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.university =tk.StringVar()
        self.name = tk.StringVar()
        self.new_name = tk.StringVar()
        self.code = tk.StringVar()
        self.new_code = tk.StringVar()
        self.district = tk.StringVar()
        self.new_district = tk.StringVar()

        self.frm_add_university = tk.LabelFrame(self)
        self.frm_add_university.place(relx=0.033, rely=0.131, relheight=0.338
                , relwidth=0.433)
        self.frm_add_university.configure(text='''ADD UNIVERSITY''')
        self.frm_add_university.configure(relief='solid', labelanchor='n', font=("Roboto Medium", 11))
        self.frm_add_university.configure(borderwidth="1")
        self.frm_add_university.configure(background="#d9d9d9")

        self.lbl_name = ctk.CTkLabel(self.frm_add_university)
        self.lbl_name.place(relx=0.038, rely=0.168, height=18, width=43
                , bordermode='ignore')
        self.lbl_name.configure(background="#d9d9d9")
        self.lbl_name.configure(foreground="#000000")
        self.lbl_name.configure(font="TkDefaultFont")
        self.lbl_name.configure(relief="flat")
        self.lbl_name.configure(anchor='w')
        self.lbl_name.configure(justify='left')
        self.lbl_name.configure(text='''Name:''')
        self.lbl_name.configure(compound='left')

        self.entry_name = ctk.CTkEntry(self.frm_add_university)
        self.entry_name.place(relx=0.231, rely=0.168, relheight=0.135
                , relwidth=0.715, bordermode='ignore')
        self.entry_name.configure(textvariable=self.name)

        self.lbl_code = ctk.CTkLabel(self.frm_add_university)
        self.lbl_code.place(relx=0.038, rely=0.387, height=17, width=43
                , bordermode='ignore')
        self.lbl_code.configure(background="#d9d9d9")
        self.lbl_code.configure(foreground="#000000")
        self.lbl_code.configure(font="TkDefaultFont")
        self.lbl_code.configure(relief="flat")
        self.lbl_code.configure(anchor='w')
        self.lbl_code.configure(justify='left')
        self.lbl_code.configure(text='''Code:''')
        self.lbl_code.configure(compound='left')

        self.entry_code = ctk.CTkEntry(self.frm_add_university)
        self.entry_code.place(relx=0.231, rely=0.387, relheight=0.135
                , relwidth=0.715, bordermode='ignore')
        self.entry_code.configure(textvariable=self.code)

        self.btn_add_university = ctk.CTkButton(self.frm_add_university)
        self.btn_add_university.place(relx=0.08, rely=0.83, height=25
                , relwidth=0.85, bordermode='ignore')
        self.btn_add_university.configure(command=self.on_btn_add_university)
        self.btn_add_university.configure(takefocus="")
        self.btn_add_university.configure(text='''Add University''')
        self.btn_add_university.configure(compound='left')

        self.lbl_district = tk.Label(self.frm_add_university)
        self.lbl_district.place(relx=0.038, rely=0.581, height=21, width=49
                , bordermode='ignore')
        self.lbl_district.configure(anchor='w')
        self.lbl_district.configure(background="#d9d9d9")
        self.lbl_district.configure(compound='left')
        self.lbl_district.configure(disabledforeground="#a3a3a3")
        self.lbl_district.configure(foreground="#000000")
        self.lbl_district.configure(text='''District:''')

        self.entry_district = ctk.CTkEntry(self.frm_add_university)
        self.entry_district.place(relx=0.231, rely=0.581, relheight=0.135
                , relwidth=0.715, bordermode='ignore')
        self.entry_district.configure(textvariable=self.district)

        self.frm_edit_university = tk.LabelFrame(self)
        self.frm_edit_university.place(relx=0.033, rely=0.523, relheight=0.403
                , relwidth=0.433)
        self.frm_edit_university.configure(relief='solid', labelanchor='n', font=("Roboto Medium", 11))
        self.frm_edit_university.configure(text='''EDIT UNIVERSITY''')
        self.frm_edit_university.configure(borderwidth="1")
        self.frm_edit_university.configure(background="#d9d9d9")

        self.combo_name = ctk.CTkLabel(self.frm_edit_university)
        self.combo_name.place(relx=0.038, rely=0.162, height=21, width=63
                , bordermode='ignore')
        self.combo_name.configure(background="#d9d9d9")
        self.combo_name.configure(foreground="#000000")
        self.combo_name.configure(font="TkDefaultFont")
        self.combo_name.configure(relief="flat")
        self.combo_name.configure(anchor='w')
        self.combo_name.configure(justify='left')
        self.combo_name.configure(text='''University:''')
        self.combo_name.configure(compound='left')

        self.lbl_new_name = ctk.CTkLabel(self.frm_edit_university)
        self.lbl_new_name.place(relx=0.038, rely=0.324, height=21, width=73
                , bordermode='ignore')
        self.lbl_new_name.configure(background="#d9d9d9")
        self.lbl_new_name.configure(foreground="#000000")
        self.lbl_new_name.configure(font="TkDefaultFont")
        self.lbl_new_name.configure(relief="flat")
        self.lbl_new_name.configure(anchor='w')
        self.lbl_new_name.configure(justify='left')
        self.lbl_new_name.configure(text='''New Name:''')
        self.lbl_new_name.configure(compound='left')

        self.entry_new_name = ctk.CTkEntry(self.frm_edit_university)
        self.entry_new_name.place(relx=0.346, rely=0.324, relheight=0.114
                , relwidth=0.638, bordermode='ignore')
        self.entry_new_name.configure(textvariable=self.new_name)

        self.btn_edit_university = ctk.CTkButton(self.frm_edit_university, fg_color='green', hover_color='lightgreen')
        self.btn_edit_university.place(relx=0.08, rely=0.85, height=25, relwidth=0.85
                , bordermode='ignore')
        self.btn_edit_university.configure(command=self.on_btn_edit_university)
        self.btn_edit_university.configure(takefocus="")
        self.btn_edit_university.configure(text='''Save Changes''')
        self.btn_edit_university.configure(compound='left')

        self.combo_university = tk.ttk.Combobox(self.frm_edit_university)
        self.combo_university.place(relx=0.346, rely=0.162, relheight=0.114
                , relwidth=0.638, bordermode='ignore')
        self.combo_university.configure(textvariable=self.university)

        self.lbl_new_code = ctk.CTkLabel(self.frm_edit_university)
        self.lbl_new_code.place(relx=0.038, rely=0.486, height=19, width=65
                , bordermode='ignore')
        self.lbl_new_code.configure(background="#d9d9d9")
        self.lbl_new_code.configure(foreground="#000000")
        self.lbl_new_code.configure(font="TkDefaultFont")
        self.lbl_new_code.configure(relief="flat")
        self.lbl_new_code.configure(anchor='w')
        self.lbl_new_code.configure(justify='left')
        self.lbl_new_code.configure(text='''New Code:''')
        self.lbl_new_code.configure(compound='left')

        self.entry_new_code = ctk.CTkEntry(self.frm_edit_university)
        self.entry_new_code.place(relx=0.346, rely=0.486, relheight=0.114
                , relwidth=0.638, bordermode='ignore')
        self.entry_new_code.configure(textvariable=self.new_code)

        self.lbl_new_district = tk.Label(self.frm_edit_university)
        self.lbl_new_district.place(relx=0.038, rely=0.649, height=21, width=49
                , bordermode='ignore')
        self.lbl_new_district.configure(anchor='w')
        self.lbl_new_district.configure(background="#d9d9d9")
        self.lbl_new_district.configure(compound='left')
        self.lbl_new_district.configure(disabledforeground="#a3a3a3")
        self.lbl_new_district.configure(foreground="#000000")
        self.lbl_new_district.configure(text='''District:''')

        self.entry_new_district = ctk.CTkEntry(self.frm_edit_university)
        self.entry_new_district.place(relx=0.346, rely=0.649, relheight=0.114
                , relwidth=0.638, bordermode='ignore')
        self.entry_new_district.configure(textvariable=self.new_district)

        self.frm_universities = tk.LabelFrame(self)
        self.frm_universities.place(relx=0.5, rely=0.131, relheight=0.795
                , relwidth=0.467)
        self.frm_universities.configure(relief='solid', labelanchor='n', borderwidth=1)
        self.frm_universities.configure(text='''ALL UNIVERSITIES''', font=("Roboto Medium", 11))
        self.frm_universities.configure(background="#d9d9d9")

        self.list_university = tk.Listbox(self.frm_universities)
        self.list_university.place(relx=0.004, rely=0.035, relheight=0.96
                , relwidth=0.99, bordermode='ignore')
        self.list_university.configure(background="white")
        self.list_university.configure(disabledforeground="#a3a3a3")
        self.list_university.configure(font="TkFixedFont")
        self.list_university.configure(foreground="black")
        self.list_university.configure(highlightbackground="#d9d9d9")
        self.list_university.configure(highlightcolor="#d9d9d9")
        self.list_university.configure(selectbackground="#c4c4c4")
        self.list_university.configure(selectforeground="black")


        self.lbl_universitys_head = ctk.CTkLabel(self)
        self.lbl_universitys_head.place(relx=0.217, rely=0.022, height=39
                , width=335)
        self.lbl_universitys_head.configure(background="#d9d9d9")
        self.lbl_universitys_head.configure(foreground="#000000")
        self.lbl_universitys_head.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.lbl_universitys_head.configure(relief="flat")
        self.lbl_universitys_head.configure(anchor='center')
        self.lbl_universitys_head.configure(justify='center')
        self.lbl_universitys_head.configure(text='''UNIVERSITY MANAGER''')

        self.lbl_universitys_head.configure(compound='center')
        
        #configure combobox values
        self.combo_university.configure(values=asyncio.run(self.get_universities()))

    def on_btn_add_university(self):
        print("Adding university in progress")
        context = {
                "name": self.name.get(),
                "code": self.code.get(),
                "district": self.district.get()
        }

        post = asyncio.run(api_config.APIResources.post_api_resource(
                                                        uri='universities/create-university',
                                                        context=context
                                                        ))
        print(f"Post Operation Status: {post}")

    def on_btn_edit_university(self):
        print("Editing university in progress")
        context = {
                "university": self.university.get(),
                "name": self.new_name.get(),
                "code": self.new_code.get(),
                "district": self.new_district.get()
        }
        print(f"Context: {context}")

    async def get_universities(self):       
        response = await api_config.APIResources.get_api_resource(resource='universities')
        if response.ok:
            universities = sorted([univ.get('name') for univ in response.json()])
        else:
            universities = sorted(['University-'+str(i) for i in range(15)])

        self.list_university.insert(0, f"")
        for i, university in enumerate(universities, start=1):
            self.list_university.insert(i, f" {university}")

        self.list_university.configure(
            state='disabled', 
            disabledforeground='black',
            )
        return universities