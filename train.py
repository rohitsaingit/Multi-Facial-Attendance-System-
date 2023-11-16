# LBPH - Local Binary Pattern Histogram(1994)

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")

    # ================ Label =======================
        title_label=Label(self.root,text="Train Data Set", font=("times new roman", 35,"bold"), bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)


    # ================ Top Image =======================
        img_top = Image.open('Images/train_data.png')
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_1b2=Label(self.root,image=self.photoimg_top)
        f_1b2.place(x=0,y=55,width=1530,height=325)

    # ================ Button =======================
        b1_label = Button(self.root, text="Train Data",command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="blue", fg="white")
        b1_label.place(x=0, y=380, width=1530, height=60)


    # ================ Bottom Image =======================
        img_bottom = Image.open('Images/student_inclass.jpg')
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_1b2=Label(self.root,image=self.photoimg_bottom)
        f_1b2.place(x=0,y=440,width=1530,height=325)


    # ================ Train the classifier =======================
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')      # Gray Scale Conversion
            imageNp=np.array(img,'uint8')           # uint8 - Use for Database   (Data-type)
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

    # ================ Train the classifier and then Save =======================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")





if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()