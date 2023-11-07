from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")

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

        #current Course Information
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white", relief=RIDGE,text="Current Course Information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=650,height=500)
        
        #Department
        Dep_label=Label(current_course_frame,text="Departement :",font=("times new roman",12,"bold") ,bg="white")
        Dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"), state="readonly")
        dep_combo["values"]=("Select Department","CSE","ECE","ME","BT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course :",font=("times new roman",12,"bold") ,bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"), state="readonly")
        course_combo["values"]=("Select Course","Biomedical","DIP","Matlab","Labs")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Session :",font=("times new roman",12,"bold") ,bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"), state="readonly")
        year_combo["values"]=("Select Session","2020-24","2021=25","2022-26","2023-27")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester :",font=("times new roman",12,"bold") ,bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"), state="readonly")
        semester_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class Student Information
        class_stu_frame=LabelFrame(left_frame,bd=2,bg="white", relief=RIDGE,text="Class Student Information", font=("times new roman",12,"bold"))
        class_stu_frame.place(x=5,y=260,width=650,height=400)

        #Student Name
        studentName_label=Label(class_stu_frame,text="Student Name :",font=("times new roman",12,"bold") ,bg="white")
        studentName_label.grid(row=0,column=0,padx=10,sticky=W)

        studentName_entry=ttk.Entry(class_stu_frame,width=20,font=("times new roman", 13,"bold"))
        studentName_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        

        #Roll Number
        rollno_label=Label(class_stu_frame,text="Roll No.:",font=("times new roman",12,"bold") ,bg="white")
        rollno_label.grid(row=0,column=2,padx=10,sticky=W)

        rollno_entry=ttk.Entry(class_stu_frame,width=16,font=("times new roman", 13,"bold"))
        rollno_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_stu_frame,text="Gender :",font=("times new roman",12,"bold") ,bg="white")
        gender_label.grid(row=1,column=0,padx=10,sticky=W)

        gender_entry=ttk.Entry(class_stu_frame,width=20,font=("times new roman", 13,"bold"))
        gender_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Phone Number
        phoneNumber_label=Label(class_stu_frame,text="Phone Number:",font=("times new roman",12,"bold") ,bg="white")
        phoneNumber_label.grid(row=1,column=2,padx=10,sticky=W)

        phoneNumber_entry=ttk.Entry(class_stu_frame,width=16,font=("times new roman", 13,"bold"))
        phoneNumber_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Class
        class_label=Label(class_stu_frame,text="Class Division.:",font=("times new roman",12,"bold") ,bg="white")
        class_label.grid(row=2,column=0,padx=10,sticky=W)

        class_entry=ttk.Entry(class_stu_frame,width=20,font=("times new roman", 13,"bold"))
        class_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Teacher
        teacher_label=Label(class_stu_frame,text="Teacher Name :",font=("times new roman",12,"bold") ,bg="white")
        teacher_label.grid(row=2,column=2,padx=10,sticky=W)

        teacher_entry=ttk.Entry(class_stu_frame,width=16,font=("times new roman", 13,"bold"))
        teacher_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #button Frame
        btn_frame=Frame(class_stu_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=120,width=640,height=70)
        
        #Save Button
        save_btn=Button(btn_frame,text="Save",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #update button
        update_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        #Delete button
        Delete_btn=Button(btn_frame,text="Delete",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)

        #Reset button
        Reset_btn=Button(btn_frame,text="Reset",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=4)

        #Button Frame 1
        btn1_frame=Frame(class_stu_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=5,y=157,width=640,height=70)

        #take Sample photos for face recognition button
        TakePhotosButton=Button(btn1_frame,text="Take Sample Photos",width=31,font=("times new roman",13,"bold"),bg="blue",fg="white")
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
        student_search_frame.place(x=10,y=135,width=595,height=80)



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()