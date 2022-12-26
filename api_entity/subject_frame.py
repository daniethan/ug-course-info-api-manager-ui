import asyncio
import customtkinter as ctk
import tkinter as tk
import config.api_config as api_config


ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class SubjectManagerFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.combobox = tk.StringVar()
        self.name = tk.StringVar()
        self.new_name = tk.StringVar()
        self.code = tk.StringVar()
        self.new_code = tk.StringVar()

        self.frm_add_subject = tk.LabelFrame(self)
        self.frm_add_subject.place(relx=0.033, rely=0.133, relheight=0.344
                , relwidth=0.433)
        self.frm_add_subject.configure(relief='solid')
        self.frm_add_subject.configure(text='''ADD SUBJECT''', labelanchor='n', font=("Roboto Medium", 11))
        self.frm_add_subject.configure(borderwidth="1")
        self.frm_add_subject.configure(background="#d9d9d9")

        self.lbl_name = ctk.CTkLabel(self.frm_add_subject)
        self.lbl_name.place(relx=0.038, rely=0.22, height=18, width=43
                , bordermode='ignore')
        self.lbl_name.configure(background="#d9d9d9")
        self.lbl_name.configure(foreground="#000000")
        self.lbl_name.configure(font="TkDefaultFont")
        self.lbl_name.configure(relief="flat")
        self.lbl_name.configure(anchor='w')
        self.lbl_name.configure(justify='left')
        self.lbl_name.configure(text='''Name:''')
        self.lbl_name.configure(compound='left')

        self.entry_name = ctk.CTkEntry(self.frm_add_subject)
        self.entry_name.place(relx=0.231, rely=0.194, relheight=0.135
                , relwidth=0.715, bordermode='ignore')
        self.entry_name.configure(textvariable=self.name)
        self.entry_name.configure(cursor="ibeam")

        self.lbl_code = ctk.CTkLabel(self.frm_add_subject)
        self.lbl_code.place(relx=0.038, rely=0.478, height=17, width=43
                , bordermode='ignore')
        self.lbl_code.configure(background="#d9d9d9")
        self.lbl_code.configure(foreground="#000000")
        self.lbl_code.configure(font="TkDefaultFont")
        self.lbl_code.configure(relief="flat")
        self.lbl_code.configure(anchor='w')
        self.lbl_code.configure(justify='left')
        self.lbl_code.configure(text='''Code:''')
        self.lbl_code.configure(compound='left')

        self.entry_code = ctk.CTkEntry(self.frm_add_subject)
        self.entry_code.place(relx=0.231, rely=0.452, relheight=0.135
                , relwidth=0.715, bordermode='ignore')
        self.entry_code.configure(textvariable=self.code)
        self.entry_code.configure(cursor="ibeam")

        self.btn_add_subject = ctk.CTkButton(self.frm_add_subject)
        self.btn_add_subject.place(relx=0.08, rely=0.76, height=25, relwidth=0.85
                , bordermode='ignore')
        self.btn_add_subject.configure(command=self.on_btn_add_subject)
        self.btn_add_subject.configure(text='''Add Subject''')

        self.frm_edit_subject = tk.LabelFrame(self)
        self.frm_edit_subject.place(relx=0.033, rely=0.533, relheight=0.411
                , relwidth=0.433)
        self.frm_edit_subject.configure(relief='solid')
        self.frm_edit_subject.configure(text='''EDIT SUBJECT''', labelanchor='n', font=("Roboto Medium", 11))
        self.frm_edit_subject.configure(borderwidth="1")
        self.frm_edit_subject.configure(background="#d9d9d9")

        self.combo_name = ctk.CTkLabel(self.frm_edit_subject)
        self.combo_name.place(relx=0.038, rely=0.188, height=21, width=53
                , bordermode='ignore')
        self.combo_name.configure(background="#d9d9d9")
        self.combo_name.configure(foreground="#000000")
        self.combo_name.configure(font="TkDefaultFont")
        self.combo_name.configure(relief="flat")
        self.combo_name.configure(anchor='w')
        self.combo_name.configure(justify='left')
        self.combo_name.configure(text='''Subject:''')
        self.combo_name.configure(compound='left')

        self.lbl_new_name = ctk.CTkLabel(self.frm_edit_subject)
        self.lbl_new_name.place(relx=0.038, rely=0.350, height=21, width=73
                , bordermode='ignore')
        self.lbl_new_name.configure(background="#d9d9d9")
        self.lbl_new_name.configure(foreground="#000000")
        self.lbl_new_name.configure(font="TkDefaultFont")
        self.lbl_new_name.configure(relief="flat")
        self.lbl_new_name.configure(anchor='w')
        self.lbl_new_name.configure(justify='left')
        self.lbl_new_name.configure(text='''New Name:''')
        self.lbl_new_name.configure(compound='left')

        self.entry_new_name = ctk.CTkEntry(self.frm_edit_subject)
        self.entry_new_name.place(relx=0.346, rely=0.324, relheight=0.114
                , relwidth=0.638, bordermode='ignore')
        self.entry_new_name.configure(textvariable=self.new_name)
        self.entry_new_name.configure(cursor="ibeam")

        self.btn_edit_subject = ctk.CTkButton(self.frm_edit_subject, fg_color='green', hover_color='lightgreen')
        self.btn_edit_subject.place(relx=0.08, rely=0.75, height=25, relwidth=0.85
                , bordermode='ignore')
        self.btn_edit_subject.configure(command=self.on_btn_edit_subject)
        self.btn_edit_subject.configure(takefocus="")
        self.btn_edit_subject.configure(text='''Save Changes''')
        self.btn_edit_subject.configure(compound='left')

        self.combo_subject = tk.ttk.Combobox(self.frm_edit_subject, textvariable=self.combobox)
        self.combo_subject.place(relx=0.346, rely=0.162, relheight=0.114
                , relwidth=0.638, bordermode='ignore')

        self.lbl_new_code = ctk.CTkLabel(self.frm_edit_subject)
        self.lbl_new_code.place(relx=0.038, rely=0.512, height=19, width=65
                , bordermode='ignore')
        self.lbl_new_code.configure(background="#d9d9d9")
        self.lbl_new_code.configure(foreground="#000000")
        self.lbl_new_code.configure(font="TkDefaultFont")
        self.lbl_new_code.configure(relief="flat")
        self.lbl_new_code.configure(anchor='w')
        self.lbl_new_code.configure(justify='left')
        self.lbl_new_code.configure(text='''New Code:''')
        self.lbl_new_code.configure(compound='left')

        self.entry_new_code = ctk.CTkEntry(self.frm_edit_subject)
        self.entry_new_code.place(relx=0.346, rely=0.486, relheight=0.114
                , relwidth=0.638, bordermode='ignore')
        self.entry_new_code.configure(textvariable=self.new_code)
        self.entry_new_code.configure(cursor="ibeam")

        self.frm_subjects = tk.LabelFrame(self)
        self.frm_subjects.place(relx=0.5, rely=0.1315, relheight=0.81
                , relwidth=0.467)
        self.frm_subjects.configure(relief='solid')
        self.frm_subjects.configure(text='''ALL SUBJECTS''', labelanchor='n', font=("Roboto Medium", 11))
        self.frm_subjects.configure(borderwidth="1")
        self.frm_subjects.configure(background="#d9d9d9")

        self.list_subjects = tk.Listbox(self.frm_subjects)
        self.list_subjects.place(relx=0.02, rely=0.04, relheight=0.95
                , relwidth=0.965, bordermode='ignore')
        self.list_subjects.configure(background="white")
        self.list_subjects.configure(cursor="xterm")
        self.list_subjects.configure(disabledforeground="#a3a3a3")
        self.list_subjects.configure(font="TkFixedFont")
        self.list_subjects.configure(foreground="black")
        self.list_subjects.configure(highlightbackground="#d9d9d9")
        self.list_subjects.configure(highlightcolor="#d9d9d9")
        self.list_subjects.configure(selectbackground="#c4c4c4")
        self.list_subjects.configure(selectforeground="black")


        self.lbl_subjects_head = ctk.CTkLabel(self)
        self.lbl_subjects_head.place(relx=0.217, rely=0.022, height=39
                , width=335)
        self.lbl_subjects_head.configure(background="#d9d9d9")
        self.lbl_subjects_head.configure(foreground="#000000")
        self.lbl_subjects_head.configure(font="TkDefaultFont")
        self.lbl_subjects_head.configure(relief="flat")
        self.lbl_subjects_head.configure(anchor='center')
        self.lbl_subjects_head.configure(justify='center')
        self.lbl_subjects_head.configure(text='''SUBJECTS MANAGER''', text_font=("Roboto Medium", 20))
        self.lbl_subjects_head.configure(compound='center')

        #configure combobox values
        self.combo_subject.configure(values=asyncio.run(self.get_subjects()))

    def on_btn_add_subject(self):
        print("Adding subject in progress")
        context = {
                "name": self.name.get(),
                "code": self.code.get()
        }

        post = asyncio.run(api_config.APIResources.post_api_resource(
                                                        uri='subjects/add_subject',
                                                        context=context
                                                        ))
        print(f"Post Operation Status: {post}")

    def on_btn_edit_subject(self):
        # print("Editing subject in progress")
        context = {
                "subject": self.combobox.get(),
                "name": self.new_name.get(),
                "code": self.new_code.get()
        }

        # post = api_config.APIResources.post_api_resource(uri='subjects/add_subject')
        # print(f"Context: {context}")

    async def get_subjects(self):
        response = await api_config.APIResources.get_api_resource(resource='subjects')
        if response.ok:
            subjects = sorted([subject.get('name') for subject in response.json()])
        else:
            subjects = sorted(['subject-'+str(i) for i in range(40)])

        self.list_subjects.insert(0, f"")
        for i, subject in enumerate(subjects, start=1):
            self.list_subjects.insert(i, f"  {subject}")
        self.list_subjects.configure(state='disabled',disabledforeground='black')
        return subjects
