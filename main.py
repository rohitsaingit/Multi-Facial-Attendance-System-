from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

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
        img_back=Image.open('Images/Background_FR.jpg')
        img_back=img_back.resize((1530,710),Image.LANCZOS)
        self.photoimg_back=ImageTk.PhotoImage(img_back)
        bg_img=Label(self.root ,image=self.photoimg_back)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        #Title of the Web Page
        title_label=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35,"bold"), bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)

        # Sudent button
        studentButton = Image.open('Images/student_detail.png')
        studentButton = studentButton.resize((220, 220), Image.LANCZOS)
        self.photostudentButton = ImageTk.PhotoImage(studentButton)

        b1 = Button(root, image=self.photostudentButton, cursor="hand2")
        b1.place(x=100, y=200, width=200, height=200)
  

        b1_label = Button(bg_img, text="Student Detail", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=100, y=270, width=200, height=40)

        # Face Detector button
        faceDetector = Image.open('Images/face_detection.png')
        faceDetector = faceDetector.resize((220, 220), Image.LANCZOS)
        self.photofaceDetector = ImageTk.PhotoImage(faceDetector)

        b1 = Button(root, image=self.photofaceDetector, cursor="hand2")
        b1.place(x=400, y=200, width=200, height=200)
  

        b1_label = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=400, y=270, width=200, height=40)

        # Train Data  button
        trainDataButton = Image.open('Images/train_data.png')
        trainDataButton = trainDataButton.resize((220, 220), Image.LANCZOS)
        self.phototrainDataButton = ImageTk.PhotoImage(trainDataButton)

        b1 = Button(root, image=self.phototrainDataButton, cursor="hand2")
        b1.place(x=700, y=200, width=200, height=200)
  

        b1_label = Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=700, y=270, width=200, height=40)

        # Attendance button
        attendaceButton = Image.open('Images/facial-recognition_Attendace.png')
        attendaceButton = attendaceButton.resize((220, 220), Image.LANCZOS)
        self.photoattendaceButton = ImageTk.PhotoImage(attendaceButton)

        b1 = Button(root, image=self.photoattendaceButton, cursor="hand2")
        b1.place(x=1000, y=200, width=200, height=200)
  

        b1_label = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=1000, y=270, width=200, height=40)

        # Photos button
        photoButton = Image.open('Images/photo_button.jpeg')
        photoButton = photoButton.resize((220, 220), Image.LANCZOS)
        self.photophotoButton = ImageTk.PhotoImage(photoButton)

        b1 = Button(root, image=self.photophotoButton, cursor="hand2")
        b1.place(x=100, y=450, width=200, height=200)
  

        b1_label = Button(bg_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=100, y=520, width=200, height=40)

        # Project Report button
        reportButton = Image.open('Images/report_button.png')
        reportButton = reportButton.resize((220, 220), Image.LANCZOS)
        self.photoreportButton = ImageTk.PhotoImage(reportButton)

        b1 = Button(root, image=self.photoreportButton, cursor="hand2")
        b1.place(x=400, y=450, width=200, height=200)
  

        b1_label = Button(bg_img, text="Project Report", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=400, y=520, width=200, height=40)

        # Exit button
        exitButton = Image.open('Images/exit_button.jpg')
        exitButton = exitButton.resize((220, 220), Image.LANCZOS)
        self.photoexitButton = ImageTk.PhotoImage(exitButton)

        b1 = Button(root, image=self.photoexitButton, cursor="hand2")
        b1.place(x=1000, y=450, width=200, height=200)
  

        b1_label = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_label.place(x=1000, y=520, width=200, height=40)





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()