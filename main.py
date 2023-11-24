from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
import tkinter
import webbrowser
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")
        
        # Header Section
        img = Image.open('Images/uiet_logo.jpg')
        img = img.resize((200, 150), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_1b1=Label(self.root,image=self.photoimg)
        f_1b1.place(x=0,y=0,width=200,height=150)
        text_label1 =Label(root, text="University Institute of Engineering and Technology", font=("Arial", 32, "bold"),fg="blue")
        text_label2 =Label(root, text="Kurukshetra University", font=("Arial", 25, "bold"),fg="blue")
        text_label1.place(x=250, y=0, width=1050, height=100)
        text_label2.place(x=250, y=75, width=900, height=50)
        
        #Background Image
        img_back=Image.open('Images/cool-background.png')
        img_back=img_back.resize((1530,710),Image.LANCZOS)
        self.photoimg_back=ImageTk.PhotoImage(img_back)
        bg_img=Label(self.root ,image=self.photoimg_back)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        #Title of the Web Page
        title_label=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35,"bold"), bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)

        #=================Time==========
        def time():
            string= strftime('%d-%m-%Y %I:%M:%S %p')
            
            label.config(text= string)
            label.after(1000,time)

        label=Label(title_label, font=('times new roman',14,'bold'),background='white',foreground='blue')
        label.place(x=0,y=2,width=200,height=50)
        time()

        # Sudent button
        studentButton = Image.open('Images/student_detail.png')
        studentButton = studentButton.resize((220, 220), Image.LANCZOS)
        self.photostudentButton = ImageTk.PhotoImage(studentButton)

        b1 = Button(root, image=self.photostudentButton,command=self.student_detail, cursor="hand2")
        b1.place(x=100, y=200, width=200, height=200)
  

        b1_label = Button(bg_img,command=self.student_detail, text="Student Detail", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=100, y=270, width=200, height=40)

        # Face Detector button
        faceDetector = Image.open('Images/face_detection.png')
        faceDetector = faceDetector.resize((220, 220), Image.LANCZOS)
        self.photofaceDetector = ImageTk.PhotoImage(faceDetector)

        b1 = Button(root, image=self.photofaceDetector, cursor="hand2", command=self.face_data)
        b1.place(x=400, y=200, width=200, height=200)
  

        b1_label = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=400, y=270, width=200, height=40)

        # Train Data  button
        trainDataButton = Image.open('Images/train_data.png')
        trainDataButton = trainDataButton.resize((220, 220), Image.LANCZOS)
        self.phototrainDataButton = ImageTk.PhotoImage(trainDataButton)

        b1 = Button(root, image=self.phototrainDataButton, cursor="hand2", command=self.train_classifier)
        b1.place(x=700, y=200, width=200, height=200)
  

        b1_label = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_classifier, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=700, y=270, width=200, height=40)

        # Attendance button
        attendaceButton = Image.open('Images/facial-recognition_Attendace.png')
        attendaceButton = attendaceButton.resize((220, 220), Image.LANCZOS)
        self.photoattendaceButton = ImageTk.PhotoImage(attendaceButton)

        b1 = Button(root, image=self.photoattendaceButton, cursor="hand2",command=self.attendance_data)
        b1.place(x=1000, y=200, width=200, height=200)
  

        b1_label = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data,font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=1000, y=270, width=200, height=40)

        # Photos button
        photoButton = Image.open('Images/photo_button.jpg')
        photoButton = photoButton.resize((220, 220), Image.LANCZOS)
        self.photophotoButton = ImageTk.PhotoImage(photoButton)

        b1 = Button(root, image=self.photophotoButton, cursor="hand2", command=self.open_img)
        b1.place(x=100, y=450, width=200, height=200)
  

        b1_label = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=100, y=520, width=200, height=40)

        # Project Report button
        reportButton = Image.open('Images/report_button.png')
        reportButton = reportButton.resize((220, 220), Image.LANCZOS)
        self.photoreportButton = ImageTk.PhotoImage(reportButton)

        b1 = Button(root, image=self.photoreportButton,command=self.open_pdf, cursor="hand2")
        b1.place(x=400, y=450, width=200, height=200)
  

        b1_label = Button(bg_img, text="Project Report",command=self.open_pdf, cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=400, y=520, width=200, height=40)

        #Result Tool To extract results of student button
        resultButton = Image.open('Images/results_button.jpeg')
        resultButton = resultButton.resize((220, 220), Image.LANCZOS)
        self.photoresultButton = ImageTk.PhotoImage(resultButton)

        b1 = Button(root, image=self.photoresultButton, cursor="hand2")
        b1.place(x=700, y=450, width=200, height=200)
  

        b1_label = Button(bg_img, text="Results At Ones", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=700, y=520, width=200, height=40)
 

        # Exit button
        exitButton = Image.open('Images/exit_button.jpg')
        exitButton = exitButton.resize((220, 220), Image.LANCZOS)
        self.photoexitButton = ImageTk.PhotoImage(exitButton)

        b1 = Button(root, image=self.photoexitButton, cursor="hand2",command=self.exit)
        b1.place(x=1000, y=450, width=200, height=200)
  

        b1_label = Button(bg_img, text="Exit", cursor="hand2",command=self.exit, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=1000, y=520, width=200, height=40)

    #================== Function button=================

    def open_img(self):
        os.startfile("data")



    # Function button
    def student_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this project",parent=self.root)
        if self.exit >0:
           self.root.destroy()
        else: 
            return
        
    # ================ Train the classifier =======================
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for root, dirs, files in os.walk(data_dir):
           for directory in dirs:
            if directory.isdigit():  # Check if directory name is a digit (considered as ID)
                label = int(directory)
                subject_dir = os.path.join(root, directory)

                for image in os.listdir(subject_dir):
                    img_path = os.path.join(subject_dir, image)
                    img = Image.open(img_path).convert('L')  # Convert to grayscale
                    imageNp = np.array(img, 'uint8')  # Convert image to numpy array

                    faces.append(imageNp)
                    ids.append(label)

                    cv2.imshow("Training", imageNp)
                    cv2.waitKey(1)  # WaitKey inside the loop to display each image

        ids=np.array(ids)

    # ================ Train the classifier and then Save =======================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    # open project report function
    def open_pdf(self):
        pdf_path = 'Project_Report.pdf'
        webbrowser.open(pdf_path)

    




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()

