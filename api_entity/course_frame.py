import customtkinter as ctk
import tkinter as tk
import config.api_config as api_config


class CourseManagerFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #RESOURCES
        self.subject_resrc = get_resource(resource='subjects')
        self.course_resrc = get_resource(resource='courses')
        self.type_resrc = get_resource(resource='course-types')
        self.univ_resrc = get_resource(resource='universities')

        self.course_subjects = dict()
        self.course_subjects_edit = dict()

        self.course_name = tk.StringVar()
        self.course_code = tk.StringVar()
        self.coursetype = tk.StringVar()
        self.university = tk.StringVar()
        self.subject_type = tk.StringVar(value=0)
        self.new_name = tk.StringVar(value=None)
        self.new_code = tk.StringVar(value=None)
        self.new_type = tk.StringVar(value=None)
        self.edit_course = tk.StringVar()
        self.subject_type_edit = tk.StringVar(value=0)
        self.subject_edit = tk.StringVar()
        self.cut_off_F = tk.StringVar()
        self.cut_off_M = tk.StringVar()
        self.cut_off_edit_F = tk.StringVar()
        self.cut_off_edit_M = tk.StringVar()

        self.frm_add_course = tk.LabelFrame(self)
        self.frm_add_course.place(relx=0.013, rely=0.017, relheight=0.973
                , relwidth=0.49)
        self.frm_add_course.configure(relief='solid')
        self.frm_add_course.configure(borderwidth="1")
        self.frm_add_course.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.frm_add_course.configure(foreground="#000000")
        self.frm_add_course.configure(labelanchor="n")
        self.frm_add_course.configure(relief="solid")
        self.frm_add_course.configure(text='''ADD COURSE''')
        self.frm_add_course.configure(background="#d7d7d7")
        self.frm_add_course.configure(highlightbackground="#d9d9d9")
        self.frm_add_course.configure(highlightcolor="black")

        self.lbl_name = tk.Label(self.frm_add_course)
        self.lbl_name.place(relx=0.016, rely=0.052, height=22, width=48
                , bordermode='ignore')
        self.lbl_name.configure(activebackground="#f9f9f9")
        self.lbl_name.configure(anchor='w')
        self.lbl_name.configure(background="#d9d9d9")
        self.lbl_name.configure(compound='left')
        self.lbl_name.configure(disabledforeground="#a3a3a3")
        self.lbl_name.configure(foreground="#000000")
        self.lbl_name.configure(highlightbackground="#d9d9d9")
        self.lbl_name.configure(highlightcolor="black")
        self.lbl_name.configure(text='''Name:''')

        self.lbl_code = tk.Label(self.frm_add_course)
        self.lbl_code.place(relx=0.016, rely=0.105, height=22, width=48
                , bordermode='ignore')
        self.lbl_code.configure(activebackground="#f9f9f9")
        self.lbl_code.configure(anchor='w')
        self.lbl_code.configure(background="#d9d9d9")
        self.lbl_code.configure(compound='left')
        self.lbl_code.configure(disabledforeground="#a3a3a3")
        self.lbl_code.configure(foreground="#000000")
        self.lbl_code.configure(highlightbackground="#d9d9d9")
        self.lbl_code.configure(highlightcolor="black")
        self.lbl_code.configure(text='''Code:''')

        self.lbl_type = tk.Label(self.frm_add_course)
        self.lbl_type.place(relx=0.016, rely=0.157, height=22, width=48
                , bordermode='ignore')
        self.lbl_type.configure(activebackground="#f9f9f9")
        self.lbl_type.configure(anchor='w')
        self.lbl_type.configure(background="#d9d9d9")
        self.lbl_type.configure(compound='left')
        self.lbl_type.configure(disabledforeground="#a3a3a3")
        self.lbl_type.configure(foreground="#000000")
        self.lbl_type.configure(highlightbackground="#d9d9d9")
        self.lbl_type.configure(highlightcolor="black")
        self.lbl_type.configure(text='''Type:''')

        self.lbl_university = tk.Label(self.frm_add_course)
        self.lbl_university.place(relx=0.016, rely=0.209, height=22, width=58
                , bordermode='ignore')
        self.lbl_university.configure(activebackground="#f9f9f9")
        self.lbl_university.configure(anchor='w')
        self.lbl_university.configure(background="#d9d9d9")
        self.lbl_university.configure(compound='left')
        self.lbl_university.configure(disabledforeground="#a3a3a3")
        self.lbl_university.configure(foreground="#000000")
        self.lbl_university.configure(highlightbackground="#d9d9d9")
        self.lbl_university.configure(highlightcolor="black")
        self.lbl_university.configure(text='''University:''')

        self.entry_name = tk.Entry(self.frm_add_course)
        self.entry_name.place(relx=0.182, rely=0.052, height=22, relwidth=0.505
                , bordermode='ignore')
        self.entry_name.configure(background="white")
        self.entry_name.configure(disabledforeground="#a3a3a3")
        self.entry_name.configure(font="TkFixedFont")
        self.entry_name.configure(foreground="#000000")
        self.entry_name.configure(highlightbackground="#d9d9d9")
        self.entry_name.configure(highlightcolor="black")
        self.entry_name.configure(insertbackground="black")
        self.entry_name.configure(selectbackground="#c4c4c4")
        self.entry_name.configure(selectforeground="black")
        self.entry_name.configure(textvariable=self.course_name)

        self.entry_code = tk.Entry(self.frm_add_course)
        self.entry_code.place(relx=0.182, rely=0.105, height=22, relwidth=0.505
                , bordermode='ignore')
        self.entry_code.configure(background="white")
        self.entry_code.configure(disabledforeground="#a3a3a3")
        self.entry_code.configure(font="TkFixedFont")
        self.entry_code.configure(foreground="#000000")
        self.entry_code.configure(highlightbackground="#d9d9d9")
        self.entry_code.configure(highlightcolor="black")
        self.entry_code.configure(insertbackground="black")
        self.entry_code.configure(selectbackground="#c4c4c4")
        self.entry_code.configure(selectforeground="black")
        self.entry_code.configure(textvariable=self.course_code)

        self.entry_type = tk.ttk.Combobox(self.frm_add_course)
        self.entry_type.place(relx=0.182, rely=0.157, height=22, relwidth=0.505
                , bordermode='ignore')
        self.entry_type.configure(textvariable=self.coursetype)
        self.entry_type.configure(values=sorted([x[-1] for x in self.type_resrc]))

        self.entry_university = tk.ttk.Combobox(self.frm_add_course)
        self.entry_university.place(relx=0.182, rely=0.209, height=22
                , relwidth=0.505, bordermode='ignore')
        self.entry_university.configure(textvariable=self.university)
        self.entry_university.configure(values=sorted([x[-1] for x in self.univ_resrc]))

        #new-frame here for cut-offs
        self.frm_add_cut_off = tk.LabelFrame(self.frm_add_course)
        self.frm_add_cut_off.place(relx=0.016, rely=0.252, relheight=0.11
                , relwidth=0.968, bordermode='ignore')
        self.frm_add_cut_off.configure(relief='solid')
        self.frm_add_cut_off.configure(borderwidth="1")
        self.frm_add_cut_off.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.frm_add_cut_off.configure(foreground="#000000")
        self.frm_add_cut_off.configure(labelanchor="n")
        self.frm_add_cut_off.configure(relief="solid")
        self.frm_add_cut_off.configure(text='''Cut-off Weights''')
        self.frm_add_cut_off.configure(background="#d9d9d9")
        self.frm_add_cut_off.configure(highlightbackground="#d9d9d9")
        self.frm_add_cut_off.configure(highlightcolor="black")

        self.lbl_wgt_fem = tk.Label(self.frm_add_cut_off)
        self.lbl_wgt_fem.place(relx=0.02, rely=0.38, height=22, width=48
                , bordermode='ignore')
        self.lbl_wgt_fem.configure(activebackground="#f9f9f9")
        self.lbl_wgt_fem.configure(anchor='w')
        self.lbl_wgt_fem.configure(background="#d9d9d9")
        self.lbl_wgt_fem.configure(compound='left')
        self.lbl_wgt_fem.configure(disabledforeground="#a3a3a3")
        self.lbl_wgt_fem.configure(foreground="#000000")
        self.lbl_wgt_fem.configure(highlightbackground="#d9d9d9")
        self.lbl_wgt_fem.configure(highlightcolor="black")
        self.lbl_wgt_fem.configure(text='''Female:''')

        self.entry_wgt_fem = tk.Entry(self.frm_add_cut_off, textvariable=self.cut_off_F)
        self.entry_wgt_fem.place(relx=0.18, rely=0.365, height=25, relwidth=0.235
                , bordermode='ignore')

        self.lbl_wgt_male = tk.Label(self.frm_add_cut_off)
        self.lbl_wgt_male.place(relx=0.60, rely=0.38, height=22, width=48
                , bordermode='ignore')
        self.lbl_wgt_male.configure(activebackground="#f9f9f9")
        self.lbl_wgt_male.configure(anchor='w')
        self.lbl_wgt_male.configure(background="#d9d9d9")
        self.lbl_wgt_male.configure(compound='left')
        self.lbl_wgt_male.configure(disabledforeground="#a3a3a3")
        self.lbl_wgt_male.configure(foreground="#000000")
        self.lbl_wgt_male.configure(highlightbackground="#d9d9d9")
        self.lbl_wgt_male.configure(highlightcolor="black")
        self.lbl_wgt_male.configure(text='''Male:''')

        self.entry_wgt_male = tk.Entry(self.frm_add_cut_off, textvariable=self.cut_off_M)
        self.entry_wgt_male.place(relx=0.72, rely=0.365, height=25, relwidth=0.235
                , bordermode='ignore')

        self.frm_add_subjects = tk.LabelFrame(self.frm_add_course)
        self.frm_add_subjects.place(relx=0.018, rely=0.372, relheight=0.553
                , relwidth=0.964, bordermode='ignore')
        self.frm_add_subjects.configure(relief='solid')
        self.frm_add_subjects.configure(borderwidth="1")
        self.frm_add_subjects.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.frm_add_subjects.configure(foreground="#000000")
        self.frm_add_subjects.configure(labelanchor="n")
        self.frm_add_subjects.configure(relief="solid")
        self.frm_add_subjects.configure(text='''Course Subjects''')
        self.frm_add_subjects.configure(background="#d9d9d9")
        self.frm_add_subjects.configure(highlightbackground="#d9d9d9")
        self.frm_add_subjects.configure(highlightcolor="black")

        self.frm_subj_type = ctk.CTkFrame(self.frm_add_subjects,fg_color="#d9d9d9")
        self.frm_subj_type.place(relx=0.01, rely=0.07, relheight=0.08, relwidth=0.98, bordermode='ignore')

        self.radio_ess = tk.Radiobutton(self.frm_subj_type, value='Essential')
        self.radio_ess.place(relx=0.048, rely=0.08, relheight=0.8, relwidth=0.255, bordermode='ignore')
        self.radio_ess.configure(activebackground="beige")
        self.radio_ess.configure(activeforeground="black")
        self.radio_ess.configure(anchor='w')
        self.radio_ess.configure(background="#d9d9d9")
        self.radio_ess.configure(compound='left')
        self.radio_ess.configure(disabledforeground="#a3a3a3")
        self.radio_ess.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.radio_ess.configure(foreground="#000000")
        self.radio_ess.configure(highlightbackground="#d9d9d9")
        self.radio_ess.configure(highlightcolor="black")
        self.radio_ess.configure(justify='left')
        self.radio_ess.configure(selectcolor="#d9d9d9")
        self.radio_ess.configure(text='''Essential''')
        self.radio_ess.configure(variable=self.subject_type, command=self.on_radio_click)

        self.radio_rel = tk.Radiobutton(self.frm_subj_type, value='Relevant')
        self.radio_rel.place(relx=0.358, rely=0.08, relheight=0.8, relwidth=0.255, bordermode='ignore')
        self.radio_rel.configure(activebackground="beige")
        self.radio_rel.configure(activeforeground="black")
        self.radio_rel.configure(anchor='w')
        self.radio_rel.configure(background="#d9d9d9")
        self.radio_rel.configure(compound='left')
        self.radio_rel.configure(disabledforeground="#a3a3a3")
        self.radio_rel.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.radio_rel.configure(foreground="#000000")
        self.radio_rel.configure(highlightbackground="#d9d9d9")
        self.radio_rel.configure(highlightcolor="black")
        self.radio_rel.configure(justify='left')
        self.radio_rel.configure(selectcolor="#d9d9d9")
        self.radio_rel.configure(text='''Relevant''')
        self.radio_rel.configure(variable=self.subject_type, command=self.on_radio_click)

        self.radio_des = tk.Radiobutton(self.frm_subj_type, value='Desirable')
        self.radio_des.place(relx=0.677, rely=0.08, relheight=0.8, relwidth=0.255, bordermode='ignore')
        self.radio_des.configure(activebackground="beige")
        self.radio_des.configure(activeforeground="black")
        self.radio_des.configure(anchor='w')
        self.radio_des.configure(background="#d9d9d9")
        self.radio_des.configure(compound='left')
        self.radio_des.configure(disabledforeground="#a3a3a3")
        self.radio_des.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.radio_des.configure(foreground="#000000")
        self.radio_des.configure(highlightbackground="#d9d9d9")
        self.radio_des.configure(highlightcolor="black")
        self.radio_des.configure(justify='left')
        self.radio_des.configure(selectcolor="#d9d9d9")
        self.radio_des.configure(text='''Desirable''')
        self.radio_des.configure(variable=self.subject_type, command=self.on_radio_click)
        #=====================================================================================================================

        self.list_subject = tk.Listbox(self.frm_add_subjects)
        self.list_subject.place(relx=0.008, rely=0.24, relheight=0.616
                , relwidth=0.984, bordermode='ignore')
        self.list_subject.configure(activestyle="none", selectmode="multiple")

        self.lbl_select_from_list = tk.Label(self.frm_add_subjects)
        self.lbl_select_from_list.place(relx=0.081, rely=0.171, height=22
                , width=304, bordermode='ignore')
        self.lbl_select_from_list.configure(anchor='w')
        self.lbl_select_from_list.configure(background="#d9d9d9")
        self.lbl_select_from_list.configure(compound='left')
        self.lbl_select_from_list.configure(disabledforeground="#a3a3a3")
        self.lbl_select_from_list.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.lbl_select_from_list.configure(foreground="#000000")
        self.lbl_select_from_list.configure(padx="55")
        self.lbl_select_from_list.configure(text='''Select Subjects From List Below''')

        self.btn_add_subject = ctk.CTkButton(self.frm_add_subjects)
        self.btn_add_subject.place(relx=0.09, rely=0.878, height=34
                , relwidth=0.8, bordermode='ignore')
        self.btn_add_subject.configure(command=self.on_btn_add)
        self.btn_add_subject.configure(text='''Add Selected Subjects''')

        self.btn_add_course = ctk.CTkButton(self.frm_add_course)
        self.btn_add_course.place(relx=0.09, rely=0.941, height=27
                , relwidth=0.8, bordermode='ignore')
        self.btn_add_course.configure(text='''Save Course''', command=self.on_btn_save_course)

        self.frm_edit_course = tk.LabelFrame(self)
        self.frm_edit_course.place(relx=0.523, rely=0.017, relheight=0.973
                , relwidth=0.474)
        self.frm_edit_course.configure(relief='solid')
        self.frm_edit_course.configure(borderwidth="1")
        self.frm_edit_course.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.frm_edit_course.configure(foreground="#000000")
        self.frm_edit_course.configure(labelanchor="n")
        self.frm_edit_course.configure(relief="solid")
        self.frm_edit_course.configure(text='''EDIT COURSE''')
        self.frm_edit_course.configure(background="#d7d7d7")
        self.frm_edit_course.configure(highlightbackground="#d9d9d9")
        self.frm_edit_course.configure(highlightcolor="black")

        self.lbl_search_course = tk.Label(self.frm_edit_course)
        self.lbl_search_course.place(relx=0.016, rely=0.052, height=22, width=48
                , bordermode='ignore')
        self.lbl_search_course.configure(activebackground="#f9f9f9")
        self.lbl_search_course.configure(anchor='w')
        self.lbl_search_course.configure(background="#d9d9d9")
        self.lbl_search_course.configure(compound='left')
        self.lbl_search_course.configure(disabledforeground="#a3a3a3")
        self.lbl_search_course.configure(foreground="#000000")
        self.lbl_search_course.configure(highlightbackground="#d9d9d9")
        self.lbl_search_course.configure(highlightcolor="black")
        self.lbl_search_course.configure(text='''Course:''')

        self.lbl_new_name = tk.Label(self.frm_edit_course)
        self.lbl_new_name.place(relx=0.016, rely=0.105, height=22, width=69
                , bordermode='ignore')
        self.lbl_new_name.configure(activebackground="#f9f9f9")
        self.lbl_new_name.configure(anchor='w')
        self.lbl_new_name.configure(background="#d9d9d9")
        self.lbl_new_name.configure(compound='left')
        self.lbl_new_name.configure(disabledforeground="#a3a3a3")
        self.lbl_new_name.configure(foreground="#000000")
        self.lbl_new_name.configure(highlightbackground="#d9d9d9")
        self.lbl_new_name.configure(highlightcolor="black")
        self.lbl_new_name.configure(text='''New Name:''')

        self.lbl_new_code = tk.Label(self.frm_edit_course)
        self.lbl_new_code.place(relx=0.016, rely=0.157, height=22, width=68
                , bordermode='ignore')
        self.lbl_new_code.configure(activebackground="#f9f9f9")
        self.lbl_new_code.configure(anchor='w')
        self.lbl_new_code.configure(background="#d9d9d9")
        self.lbl_new_code.configure(compound='left')
        self.lbl_new_code.configure(disabledforeground="#a3a3a3")
        self.lbl_new_code.configure(foreground="#000000")
        self.lbl_new_code.configure(highlightbackground="#d9d9d9")
        self.lbl_new_code.configure(highlightcolor="black")
        self.lbl_new_code.configure(text='''New Code:''')

        self.lbl_new_type = tk.Label(self.frm_edit_course)
        self.lbl_new_type.place(relx=0.016, rely=0.209, height=22, width=58
                , bordermode='ignore')
        self.lbl_new_type.configure(activebackground="#f9f9f9")
        self.lbl_new_type.configure(anchor='w')
        self.lbl_new_type.configure(background="#d9d9d9")
        self.lbl_new_type.configure(compound='left')
        self.lbl_new_type.configure(disabledforeground="#a3a3a3")
        self.lbl_new_type.configure(foreground="#000000")
        self.lbl_new_type.configure(highlightbackground="#d9d9d9")
        self.lbl_new_type.configure(highlightcolor="black")
        self.lbl_new_type.configure(text='''New Type:''')

        self.entry_new_name = tk.Entry(self.frm_edit_course)
        self.entry_new_name.place(relx=0.242, rely=0.105, height=22
                , relwidth=0.74, bordermode='ignore')
        self.entry_new_name.configure(background="white")
        self.entry_new_name.configure(disabledforeground="#a3a3a3")
        self.entry_new_name.configure(font="TkFixedFont")
        self.entry_new_name.configure(foreground="#000000")
        self.entry_new_name.configure(highlightbackground="#d9d9d9")
        self.entry_new_name.configure(highlightcolor="black")
        self.entry_new_name.configure(insertbackground="black")
        self.entry_new_name.configure(selectbackground="#c4c4c4")
        self.entry_new_name.configure(selectforeground="black")
        self.entry_new_name.configure(textvariable=self.new_name)

        self.entry_new_code = tk.Entry(self.frm_edit_course)
        self.entry_new_code.place(relx=0.242, rely=0.157, height=22
                , relwidth=0.522, bordermode='ignore')
        self.entry_new_code.configure(background="white")
        self.entry_new_code.configure(disabledforeground="#a3a3a3")
        self.entry_new_code.configure(font="TkFixedFont")
        self.entry_new_code.configure(foreground="#000000")
        self.entry_new_code.configure(highlightbackground="#d9d9d9")
        self.entry_new_code.configure(highlightcolor="black")
        self.entry_new_code.configure(insertbackground="black")
        self.entry_new_code.configure(selectbackground="#c4c4c4")
        self.entry_new_code.configure(selectforeground="black")
        self.entry_new_code.configure(textvariable=self.new_code)

        self.entry_new_type = tk.ttk.Combobox(self.frm_edit_course)
        self.entry_new_type.place(relx=0.242, rely=0.209, height=22
                , relwidth=0.522, bordermode='ignore')
        self.entry_new_type.configure(textvariable=self.new_type)
        self.entry_new_type.configure(values=sorted([x[-1] for x in self.type_resrc]))

        self.btn_edit_course = ctk.CTkButton(self.frm_edit_course, fg_color='green', hover_color='lightgreen')
        self.btn_edit_course.place(relx=0.09, rely=0.941, height=27
                , relwidth=0.8, bordermode='ignore')
        self.btn_edit_course.configure(text='''Save Changes''', command=self.on_btn_save_changes)

        self.combo_course_search = tk.ttk.Combobox(self.frm_edit_course)
        self.combo_course_search.place(relx=0.242, rely=0.052, relheight=0.038
                , relwidth=0.74, bordermode='ignore')
        self.combo_course_search.configure(textvariable=self.edit_course)
        self.combo_course_search.configure(values=sorted([x[-1] for x in self.course_resrc]))
       
        #new-frame-here
        self.frm_edit_cut_off = tk.LabelFrame(self.frm_edit_course)
        self.frm_edit_cut_off.place(relx=0.016, rely=0.252, relheight=0.11
                , relwidth=0.968, bordermode='ignore')
        self.frm_edit_cut_off.configure(relief='solid')
        self.frm_edit_cut_off.configure(borderwidth="1")
        self.frm_edit_cut_off.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.frm_edit_cut_off.configure(foreground="#000000")
        self.frm_edit_cut_off.configure(labelanchor="n")
        self.frm_edit_cut_off.configure(relief="solid")
        self.frm_edit_cut_off.configure(text='''Edit Cut-off Weights''')
        self.frm_edit_cut_off.configure(background="#d9d9d9")
        self.frm_edit_cut_off.configure(highlightbackground="#d9d9d9")
        self.frm_edit_cut_off.configure(highlightcolor="black")

        self.lbl_wgt_edit_fem = tk.Label(self.frm_edit_cut_off)
        self.lbl_wgt_edit_fem.place(relx=0.02, rely=0.38, height=22, width=48
                , bordermode='ignore')
        self.lbl_wgt_edit_fem.configure(activebackground="#f9f9f9")
        self.lbl_wgt_edit_fem.configure(anchor='w')
        self.lbl_wgt_edit_fem.configure(background="#d9d9d9")
        self.lbl_wgt_edit_fem.configure(compound='left')
        self.lbl_wgt_edit_fem.configure(disabledforeground="#a3a3a3")
        self.lbl_wgt_edit_fem.configure(foreground="#000000")
        self.lbl_wgt_edit_fem.configure(highlightbackground="#d9d9d9")
        self.lbl_wgt_edit_fem.configure(highlightcolor="black")
        self.lbl_wgt_edit_fem.configure(text='''Female:''')

        self.entry_wgt_edit_fem = tk.Entry(self.frm_edit_cut_off, textvariable=self.cut_off_edit_F)
        self.entry_wgt_edit_fem.place(relx=0.18, rely=0.365, height=25, relwidth=0.235
                , bordermode='ignore')

        self.lbl_wgt_edit_male = tk.Label(self.frm_edit_cut_off)
        self.lbl_wgt_edit_male.place(relx=0.60, rely=0.38, height=22, width=48
                , bordermode='ignore')
        self.lbl_wgt_edit_male.configure(activebackground="#f9f9f9")
        self.lbl_wgt_edit_male.configure(anchor='w')
        self.lbl_wgt_edit_male.configure(background="#d9d9d9")
        self.lbl_wgt_edit_male.configure(compound='left')
        self.lbl_wgt_edit_male.configure(disabledforeground="#a3a3a3")
        self.lbl_wgt_edit_male.configure(foreground="#000000")
        self.lbl_wgt_edit_male.configure(highlightbackground="#d9d9d9")
        self.lbl_wgt_edit_male.configure(highlightcolor="black")
        self.lbl_wgt_edit_male.configure(text='''Male:''')

        self.entry_wgt_edit_male = tk.Entry(self.frm_edit_cut_off, textvariable=self.cut_off_edit_M)
        self.entry_wgt_edit_male.place(relx=0.72, rely=0.365, height=25, relwidth=0.235
                , bordermode='ignore')

        self.frm_edit_subjects = tk.LabelFrame(self.frm_edit_course)
        self.frm_edit_subjects.place(relx=0.016, rely=0.372, relheight=0.553
                , relwidth=0.968, bordermode='ignore')
        self.frm_edit_subjects.configure(relief='solid')
        self.frm_edit_subjects.configure(borderwidth="1")
        self.frm_edit_subjects.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.frm_edit_subjects.configure(foreground="#000000")
        self.frm_edit_subjects.configure(labelanchor="n")
        self.frm_edit_subjects.configure(relief="solid")
        self.frm_edit_subjects.configure(text='''Edit Course Subjects''')
        self.frm_edit_subjects.configure(background="#d9d9d9")
        self.frm_edit_subjects.configure(highlightbackground="#d9d9d9")
        self.frm_edit_subjects.configure(highlightcolor="black")

        self.frm_subj_type_edit = ctk.CTkFrame(self.frm_edit_subjects, fg_color="#d9d9d9")
        self.frm_subj_type_edit.place(relx=0.01, rely=0.07, relheight=0.08, relwidth=0.98, bordermode='ignore')

        self.radio_ess_edit = tk.Radiobutton(self.frm_subj_type_edit, value='Essential')
        self.radio_ess_edit.place(relx=0.048, rely=0.08, relheight=0.8, relwidth=0.255, bordermode='ignore')
        self.radio_ess_edit.configure(activebackground="beige")
        self.radio_ess_edit.configure(activeforeground="black")
        self.radio_ess_edit.configure(anchor='w')
        self.radio_ess_edit.configure(background="#d9d9d9")
        self.radio_ess_edit.configure(compound='left')
        self.radio_ess_edit.configure(disabledforeground="#a3a3a3")
        self.radio_ess_edit.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.radio_ess_edit.configure(foreground="#000000")
        self.radio_ess_edit.configure(highlightbackground="#d9d9d9")
        self.radio_ess_edit.configure(highlightcolor="black")
        self.radio_ess_edit.configure(justify='left')
        self.radio_ess_edit.configure(selectcolor="#d9d9d9")
        self.radio_ess_edit.configure(text='''Essential''')
        self.radio_ess_edit.configure(variable=self.subject_type_edit, command=self.on_radio_click_edit)

        self.radio_rel_edit = tk.Radiobutton(self.frm_subj_type_edit, value='Relevant')
        self.radio_rel_edit.place(relx=0.358, rely=0.08, relheight=0.8, relwidth=0.255, bordermode='ignore')
        self.radio_rel_edit.configure(activebackground="beige")
        self.radio_rel_edit.configure(activeforeground="black")
        self.radio_rel_edit.configure(anchor='w')
        self.radio_rel_edit.configure(background="#d9d9d9")
        self.radio_rel_edit.configure(compound='left')
        self.radio_rel_edit.configure(disabledforeground="#a3a3a3")
        self.radio_rel_edit.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.radio_rel_edit.configure(foreground="#000000")
        self.radio_rel_edit.configure(highlightbackground="#d9d9d9")
        self.radio_rel_edit.configure(highlightcolor="black")
        self.radio_rel_edit.configure(justify='left')
        self.radio_rel_edit.configure(selectcolor="#d9d9d9")
        self.radio_rel_edit.configure(text='''Relevant''')
        self.radio_rel_edit.configure(variable=self.subject_type_edit, command=self.on_radio_click_edit)

        self.radio_des_edit = tk.Radiobutton(self.frm_subj_type_edit, value='Desirable')
        self.radio_des_edit.place(relx=0.677, rely=0.08, relheight=0.8, relwidth=0.255, bordermode='ignore')
        self.radio_des_edit.configure(activebackground="beige")
        self.radio_des_edit.configure(activeforeground="black")
        self.radio_des_edit.configure(anchor='w')
        self.radio_des_edit.configure(background="#d9d9d9")
        self.radio_des_edit.configure(compound='left')
        self.radio_des_edit.configure(disabledforeground="#a3a3a3")
        self.radio_des_edit.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.radio_des_edit.configure(foreground="#000000")
        self.radio_des_edit.configure(highlightbackground="#d9d9d9")
        self.radio_des_edit.configure(highlightcolor="black")
        self.radio_des_edit.configure(justify='left')
        self.radio_des_edit.configure(selectcolor="#d9d9d9")
        self.radio_des_edit.configure(text='''Desirable''')
        self.radio_des_edit.configure(variable=self.subject_type_edit, command=self.on_radio_click_edit)
        #=====================================================================================================================

        self.list_subject_edit = tk.Listbox(self.frm_edit_subjects)
        self.list_subject_edit.place(relx=0.008, rely=0.239, relheight=0.617
                , relwidth=0.983, bordermode='ignore')
        self.list_subject_edit.configure(listvariable=self.subject_edit)
        self.list_subject_edit.configure(activestyle="none", selectmode="multiple")

        self.lbl_select_from_list_edit = tk.Label(self.frm_edit_subjects)
        self.lbl_select_from_list_edit.place(relx=0.081, rely=0.17, height=22
                , width=296, bordermode='ignore')
        self.lbl_select_from_list_edit.configure(activebackground="#f9f9f9")
        self.lbl_select_from_list_edit.configure(anchor='w')
        self.lbl_select_from_list_edit.configure(background="#d9d9d9")
        self.lbl_select_from_list_edit.configure(compound='left')
        self.lbl_select_from_list_edit.configure(disabledforeground="#a3a3a3")
        self.lbl_select_from_list_edit.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.lbl_select_from_list_edit.configure(foreground="#000000")
        self.lbl_select_from_list_edit.configure(highlightbackground="#d9d9d9")
        self.lbl_select_from_list_edit.configure(highlightcolor="black")
        self.lbl_select_from_list_edit.configure(padx="55")
        self.lbl_select_from_list_edit.configure(text='''Select Subjects From List Below''')

        self.btn_add_subject_edit = ctk.CTkButton(self.frm_edit_subjects, fg_color='green', hover_color='lightgreen')
        self.btn_add_subject_edit.place(relx=0.09, rely=0.878, height=34
                , relwidth=0.8, bordermode='ignore')
        self.btn_add_subject_edit.configure(command=lambda to_edit=True :self.on_btn_add(to_edit))
        self.btn_add_subject_edit.configure(text='''Add Selected Subjects''')


    def on_btn_add(self, to_edit: bool=False):
        subjects = list()
        
        if not to_edit:
            self.subject_type_edit.set(value=0)
            for index in self.list_subject.curselection():
                subjects.append(self.list_subject.get(index).strip())

            self.list_subject.delete(0, tk.END)
            self.list_subject.insert(4, f"              {self.subject_type.get().upper()} SUBJECTS ADDED")
            context: dict = self.course_subjects
        else:
            self.subject_type.set(value=0)
            for index in self.list_subject_edit.curselection():
                subjects.append(self.list_subject_edit.get(index).strip())

            self.list_subject_edit.delete(0, tk.END)
            self.list_subject_edit.insert(4, f"              {self.subject_type_edit.get().upper()} SUBJECTS ADDED")
            context: dict = self.course_subjects_edit
        
        if "ess" in self.subject_type.get().lower() or "ess" in self.subject_type_edit.get().lower():
            if not to_edit:
                context.update(
                    {'Essential': subjects}
                )
            else:
                context.update(
                    {'Essential': subjects}
                )                
            
        elif "rel" in self.subject_type.get().lower() or "rel" in self.subject_type_edit.get().lower():
            if not to_edit:
                context.update(
                    {'Relevant': subjects}
                )
            else:
                context.update(
                    {'Relevant': subjects}
                )
            
        elif "des" in self.subject_type.get().lower() or "des" in self.subject_type_edit.get().lower():
            if not to_edit:
                context.update(
                    {'Desirable': subjects}
                )
            else:
                context.update(
                    {'Desirable': subjects}
                )
               
    def on_btn_save_course(self):
        course_data = {
                        'name': self.course_name.get(),
                        'code': self.course_code.get(),
                        'univ_code': get_resource_code(resrc=self.university.get(), collection=self.univ_resrc),
                        'cut_off_male': float(self.cut_off_M.get()) if self.cut_off_M.get() != '' else float('0.0'),
                        'cut_off_female': float(self.cut_off_F.get()) if self.cut_off_F.get() != '' else float('0.0'),
                        'course_type': get_resource_code(resrc=self.coursetype.get(), collection=self.type_resrc),
                    }
               
        self.list_subject.delete(0, tk.END)

        #add the course to API database      
        post = api_config.APIResources.post_api_resource(
                                                        uri='courses/create-course',
                                                        context=course_data
                                                        )
        print(f"Post Operation Status: {post}")

        if len(self.course_subjects.values())>0:
            for subj_type in self.course_subjects.keys():
                for subject in self.course_subjects.get(subj_type):
                    post = api_config.APIResources.post_api_resource(
                                                                        uri=f'subjects/add-course-subject/?subj_type={subj_type}',
                                                                        context={
                                                                            "subject_name": subject,
                                                                            "course_code": course_data["code"]
                                                                        })
                    print(f"{subject} adding as {subj_type} returned status: {post}")
        else: print("No Subjects Changed")
        self.list_subject.insert(4, f"                    COURSE ADDED")
        

    def on_btn_save_changes(self):
        course_data_edit = {
                            'course': get_resource_code(resrc=self.edit_course.get(), collection=self.course_resrc),
                            'new-name': self.new_name.get() if self.new_name.get() != '' else None,
                            'new-code': self.new_code.get() if self.new_code.get() != '' else None,
                            'cut_off_male': float(self.cut_off_edit_M.get()) if self.cut_off_edit_M.get() != '' else None,
                            'cut_off_female': float(self.cut_off_edit_F.get()) if self.cut_off_edit_F.get() != '' else None,
                            'new-type': get_resource_code(
                                                            resrc=self.new_type.get(), 
                                                            collection=self.type_resrc
                                                            ) if self.new_type.get() != '' else None,
                        }
        
        put = api_config.APIResources.update_api_resource(
                                                            uri='courses/edit-course',
                                                            context={
                                                                        'course': course_data_edit["course"],
                                                                        'name': course_data_edit["new-name"],
                                                                        'code': course_data_edit["new-code"],
                                                                        'cut_off_male': course_data_edit["cut_off_male"],
                                                                        'cut_off_female': course_data_edit["cut_off_female"],
                                                                        'course_type': course_data_edit["new-type"],
                                                                    }
                                                            )

        self.list_subject_edit.delete(0, tk.END)
        
        if len(self.course_subjects_edit.values())>0:
            for subj_type in self.course_subjects_edit.keys():
                for subject in self.course_subjects_edit.get(subj_type):
                    post = api_config.APIResources.post_api_resource(
                                                                        uri=f'subjects/add-course-subject/?subj_type={subj_type}',
                                                                        context={
                                                                            "subject_name": subject,
                                                                            "course_code": course_data_edit["course"]
                                                                        })
                    print(f"{subject} adding as {subj_type} returned status: {post}")
        else: print("No Subjects Changed")

        self.list_subject_edit.insert(4, f"                    COURSE EDITED")
        

    def on_radio_click_edit(self):       
        #clear the whole listbox
        self.list_subject.delete(0,tk.END)
        self.list_subject_edit.delete(0,tk.END)

        for i,sub in enumerate(self.subject_resrc):
            self.list_subject_edit.insert(i, f"    {sub}")
    
    def on_radio_click(self):       
        #clear the whole listbox
        self.list_subject_edit.delete(0,tk.END)
        self.list_subject.delete(0,tk.END)

        for i,sub in enumerate(self.subject_resrc):
            self.list_subject.insert(i, f"    {sub}")

def get_resource(resource: str='subjects'):
    response = api_config.APIResources.get_api_resource(resource=resource)
    if response.ok:
        if resource in ('course-types', 'universities', 'courses'):
            resource_return = [(resrc.get('code'), resrc.get('name')) for resrc in response.json()]
        
        else:
            resource_return = sorted([resrc.get('name') for resrc in response.json()])
    else:
        resource_return = sorted([f'{resource}'+str(i) for i in range(20)])
    
    return resource_return

def get_resource_code(resrc: str, collection: list):
    for code,name in collection:
        if name==resrc:
            return code

