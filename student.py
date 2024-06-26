from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")

        # ====Data Variable========
        self.var_regno=StringVar()
        self.var_std_name=StringVar()
        self.var_rollno=StringVar()
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_semester=StringVar()
        self.var_mobile=StringVar()
        self.var_gender=StringVar()
        self.var_session=StringVar()
        self.var_teacher=StringVar()
        

        # Header Section
        img1 = Image.open('Images/student-management-system.png')
        img1 = img1.resize((400, 150), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_1b1=Label(self.root,image=self.photoimg1)
        f_1b1.place(x=500,y=0,width=400,height=150)

        img2 = Image.open('Images/college_3rdgate.jpg')
        img2 = img2.resize((500, 150), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_1b2=Label(self.root,image=self.photoimg2)
        f_1b2.place(x=0,y=0,width=500,height=150)

        img3 = Image.open('Images/college_image.jpg')
        img3 = img3.resize((500, 150), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_1b2=Label(self.root,image=self.photoimg3)
        f_1b2.place(x=900,y=0,width=500,height=150)


        #Background Image
        img_back=Image.open('Images/Background_FR.jpg')
        img_back=img_back.resize((1530,710),Image.LANCZOS)
        self.photoimg_back=ImageTk.PhotoImage(img_back)
        bg_img=Label(self.root ,image=self.photoimg_back)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        #Title of the Page
        title_label=Label(bg_img,text="Student Management System", font=("times new roman", 35,"bold"), bg="white",fg="blue")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Make A frame over the Background Image
        main_frame=Frame(bg_img,border=2,bg="white")
        main_frame.place(x=20,y=50,width=1320,height=520)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="Student Detail", font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=660,height=560)

        img_left = Image.open('Images/student_inclass.jpg')
        img_left = img_left.resize((650, 130), Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_1b2=Label(left_frame,image=self.photoimg_left)
        f_1b2.place(x=5,y=0,width=650,height=130)

        #Current Course Information
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white", relief=RIDGE,text="Current Course Information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=650,height=500)
        
        #Department
        Dep_label=Label(current_course_frame,text="Departement :",font=("times new roman",12,"bold") ,bg="white")
        Dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"), state="readonly")
        dep_combo["values"]=("Select Department","ECE","CSE","ME","BT","ECO","AI/ML")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course :",font=("times new roman",12,"bold") ,bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"), state="readonly")
        course_combo["values"]=("Select Course","Biomedical","DIP","Matlab","Labs","Other")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Session :",font=("times new roman",12,"bold") ,bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_session,font=("times new roman",12,"bold"), state="readonly")
        year_combo["values"]=("Select Session","2020-24","2021-25","2022-26","2023-27")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester :",font=("times new roman",12,"bold") ,bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"), state="readonly")
        semester_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #Class Student Information
        class_stu_frame=LabelFrame(left_frame,bd=2,bg="white", relief=RIDGE,text="Class Student Information", font=("times new roman",12,"bold"))
        class_stu_frame.place(x=5,y=260,width=650,height=400)

        #Registration Number
        regno_label=Label(class_stu_frame,text="Reg No. :",font=("times new roman",12,"bold") ,bg="white")
        regno_label.grid(row=0,column=0,padx=10,sticky=W)

        regno_entry=ttk.Entry(class_stu_frame,textvariable=self.var_regno,width=20,font=("times new roman",12,"bold"))
        regno_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #Student Name
        studentName_label=Label(class_stu_frame,text="Student Name :",font=("times new roman",12,"bold") ,bg="white")
        studentName_label.grid(row=0,column=2,padx=10,sticky=W)

        studentName_entry=ttk.Entry(class_stu_frame,textvariable=self.var_std_name,width=20,font=("times new roman", 12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #Roll Number
        rollno_label=Label(class_stu_frame,text="Roll No. :",font=("times new roman",12,"bold") ,bg="white")
        rollno_label.grid(row=1,column=0,padx=10,sticky=W)

        rollno_entry=ttk.Entry(class_stu_frame,textvariable=self.var_rollno,width=20,font=("times new roman", 12,"bold"))
        rollno_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_stu_frame,text="Gender :",font=("times new roman",12,"bold") ,bg="white")
        gender_label.grid(row=1,column=2,padx=10,sticky=W)

        gender_combo=ttk.Combobox(class_stu_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"), state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Phone Number
        phoneNumber_label=Label(class_stu_frame,text="Phone No. :",font=("times new roman",12,"bold") ,bg="white")
        phoneNumber_label.grid(row=2,column=0,padx=10,sticky=W)

        phoneNumber_entry=ttk.Entry(class_stu_frame,textvariable=self.var_mobile,width=20,font=("times new roman", 12,"bold"))
        phoneNumber_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Class
        # class_label=Label(class_stu_frame,text="Section:",font=("times new roman",12,"bold") ,bg="white")
        # class_label.grid(row=2,column=0,padx=10,sticky=W)

        # section_combo=ttk.Combobox(class_stu_frame,textvariable=self.var_division,font=("times new roman",12,"bold"), state="readonly")
        # section_combo["values"]=("A","B")
        # section_combo.current(0)
        # section_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Teacher
        teacher_label=Label(class_stu_frame,text="Teacher Name :",font=("times new roman",12,"bold") ,bg="white")
        teacher_label.grid(row=2,column=2,padx=10,sticky=W)

        teacher_entry=ttk.Entry(class_stu_frame,textvariable=self.var_teacher,width=20,font=("times new roman", 12,"bold"))
        teacher_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Button Frame
        btn_frame=Frame(class_stu_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=120,width=640,height=70)
        
        #Save Button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #Update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        #Delete button
        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)

        #Reset button
        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=4)

        #Button Frame 1
        btn1_frame=Frame(class_stu_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=5,y=157,width=640,height=70)

        #take Sample photos for face recognition button

        TakePhotosButton=Button(btn1_frame,text="Take Sample Photos",command=self.generate_dataset,width=31,font=("times new roman",13,"bold"),bg="blue",fg="white")
        TakePhotosButton.grid(row=0,column=0)

        #Update Photo sample button 
        updatePhotoButton=Button(btn1_frame,text="Update Photo Sample",width=31,font=("times new roman",13,"bold"),bg="blue",fg="white")
        updatePhotoButton.grid(row=0,column=1)


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="Student Detail", font=("times new roman",12,"bold"),width=17)
        right_frame.place(x=680,y=10,width=620,height=560)

        img_right = Image.open('Images/student_img.jpg')
        img_right = img_right.resize((590, 130), Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_1b2=Label(right_frame,image=self.photoimg_right)
        f_1b2.place(x=5,y=0,width=600,height=130)

        #Student Search
        student_search_frame=LabelFrame(right_frame,bd=2,bg="white", relief=RIDGE,text="Student Search", font=("times new roman",12,"bold"))
        student_search_frame.place(x=10,y=135,width=595,height=100)

        student_search_label=Label(student_search_frame,text="Search Student By :",font=("times new roman",13,"bold") ,bg="green", fg="white")
        student_search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        self.student_search_combo=ttk.Combobox(student_search_frame,font=("times new roman",12,"bold"), state="readonly")
        self.student_search_combo["values"]=("Select","Student Name","Roll No.")
        self.student_search_combo.current(0)
        self.student_search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        self.search_entry=ttk.Entry(student_search_frame,width=20,font=("times new roman", 13,"bold"))
        self.search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        # Student search Button
        student_search_button_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        student_search_button_frame.place(x=80,y=200,width=280,height=35)

        search_btn=Button(student_search_button_frame,text="Search",command=self.search_student,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=0)

        showAll_btn=Button(student_search_button_frame,text="Show All",command=self.show_all_students,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=1,padx=4)

        # Delete All
        student_deleteAll_button_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        student_deleteAll_button_frame.place(x=363,y=200,width=280,height=35)

        deleteAll_btn=Button(student_deleteAll_button_frame,text="Delete All",command=self.delete_all, width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        deleteAll_btn.grid(row=0,column=2)

        # ================Student Table Frame================
        student_table_frame=LabelFrame(right_frame,bd=2,bg="white", relief=RIDGE)
        student_table_frame.place(x=10,y=240,width=595,height=240)
        
        scroll_x=ttk.Scrollbar(student_table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(student_table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(student_table_frame, columns=("regno","name","rollno","dep","sem","session","mobile","gender","course","teacher"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("regno", text="Registration No")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("rollno", text="Roll No")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("session", text="Session")
        self.student_table.heading("mobile", text="Phone No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("teacher", text="Teacher")

        self.student_table["show"]="headings"
        self.student_table.column("regno",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("session",width=100)
        self.student_table.column("mobile",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("teacher",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ==============Function Declaration=======================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_rollno.get()=="":
            messagebox.showerror("Error", "All field are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Rohit@9401",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_regno.get(),
                    self.var_std_name.get(),
                    self.var_rollno.get(),
                    self.var_dep.get(),
                    self.var_semester.get(),
                    self.var_session.get(),
                    self.var_mobile.get(),
                    self.var_gender.get(),
                    self.var_course.get(),
                    self.var_teacher.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # ==============Fetch From Database=======================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Rohit@9401", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                  self.student_table.insert("", END, values=i)
             conn.commit()  
        conn.close()

    # ==============Get Cursor=======================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_regno.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_rollno.set(data[2]),
        self.var_dep.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_session.set(data[5]),
        self.var_mobile.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_course.set(data[8]),
        self.var_teacher.set(data[9])
        
    # ================Update Function================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_rollno.get()=="":
            messagebox.showerror("Error", "All field are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student detials",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Rohit@9401",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Name=%s,Roll_No=%s,Dep=%s,Sem=%s,Session=%s,Mobile=%s,Gender=%s,Course=%s,Teacher=%s where Reg_No=%s",(
                        self.var_std_name.get(),
                        self.var_rollno.get(),
                        self.var_dep.get(),
                        self.var_semester.get(),
                        self.var_session.get(),
                        self.var_mobile.get(),
                        self.var_gender.get(),
                        self.var_course.get(),
                        self.var_teacher.get(),
                        self.var_regno.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Details Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    # ================Delete Function================
    def delete_data(self):
        if self.var_regno.get()=="":
            messagebox.showerror("Error","Student Registration number must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student ?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Rohit@9401",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where Reg_No=%s"
                    val=(self.var_regno.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # ==============Reset Function=======================
    def reset_data(self):
        self.var_rollno.set("")
        self.var_std_name.set("")
        self.var_dep.set("Select Department")
        self.var_semester.set("Select Semester")
        self.var_regno.set("")
        self.var_session.set("Select Session")
        self.var_mobile.set("")
        self.var_gender.set("Male")
        self.var_course.set("Select Course")
        self.var_teacher.set("")

    # ==============Generate data set or take photo samples =======================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_rollno.get()=="":
            messagebox.showerror("Error", "All field are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Rohit@9401",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    my_cursor.execute("update student set Name=%s,Roll_No=%s,Dep=%s,Sem=%s,Session=%s,Mobile=%s,Gender=%s,Course=%s,Teacher=%s where Reg_No=%s",(
                        self.var_std_name.get(),
                        self.var_rollno.get(),
                        self.var_dep.get(),
                        self.var_semester.get(),
                        self.var_session.get(),
                        self.var_mobile.get(),
                        self.var_gender.get(),
                        self.var_course.get(),
                        self.var_teacher.get(),
                        self.var_regno.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
    
    # ===========Create Directory/folder to store images
                def create_directory(directory):
                      if not os.path.exists(directory):
                         os.makedirs(directory)

    # ==============Load predifined data on face frontals from opencv =======================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling Factor = 1.3, Minimum Neighbour = 5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    cropped_face = face_cropped(my_frame)
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        # Assuming 'id' variable exists with student's roll number or name
                        directory = f"data/{str(id)}"  # Folder name based on student's ID
                        create_directory(directory)
                        file_name_path= f"{directory}/user.{str(id)}.{str(img_id)}.jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating Data Set Completed!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # =============search student function ============
    def search_student(self):
        search_by = self.student_search_combo.get()
        search_term = self.search_entry.get()

        # Clearing the existing table data
        for row in self.student_table.get_children():
            self.student_table.delete(row)

        conn = mysql.connector.connect(host="localhost", username="root", password="Rohit@9401", database="face_recognizer")
        my_cursor = conn.cursor()

        if search_by == "Student Name":
            my_cursor.execute("SELECT * FROM student WHERE name = %s", (search_term,))
        elif search_by == "Roll No.":
            my_cursor.execute("SELECT * FROM student WHERE Roll_No = %s", (search_term,))

        data = my_cursor.fetchall()

        for row in data:
            self.student_table.insert("", END, values=row)

        conn.close()
    
    # =====Show All==========
    def show_all_students(self):
        # Clearing the existing table data
        for row in self.student_table.get_children():
            self.student_table.delete(row)

        self.fetch_data()  # Fetch and display all students again

    # =====delete All==================
    def delete_all(self):
        try:
            delete = messagebox.askyesno("Student Delete Page", "Do you want to delete all the students?", parent=self.root)
            if delete:
                conn = mysql.connector.connect(host="localhost", username="root", password="Rohit@9401", database="face_recognizer")
                my_cursor = conn.cursor()
                sql = "TRUNCATE TABLE student"
                my_cursor.execute(sql)
                conn.commit()
                conn.close()
                self.fetch_data()  # Refresh data after deletion if needed
                messagebox.showinfo("Delete", "Successfully deleted students details", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
   

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
