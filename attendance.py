from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
import pandas as pd
import openpyxl
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")

        # variable
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # Header Section
        img1 = Image.open('Images/attendance.webp')
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
        bg_img.place(x=0,y=150,width=1530,height=710)

         #Title of the Page
        title_label=Label(bg_img,text="Attendance Management System", font=("times new roman", 35,"bold"), bg="green",fg="yellow")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Make A frame over the Background Image
        main_frame=Frame(bg_img,border=2,bg="white")
        main_frame.place(x=0,y=45,width=1350,height=520)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="Student Attendance Detail", font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=660,height=560)

        img_left = Image.open('Images/student_inclass.jpg')
        img_left = img_left.resize((650, 180), Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_1b2=Label(left_frame,image=self.photoimg_left)
        f_1b2.place(x=5,y=0,width=650,height=180)

         #Make A  leftframe over the Background Image
        left_inside_frame=Frame(left_frame,border=2, relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=180,width=720,height=370)

        #Label and entry 
        
        #Roll Number
        rollno_label=Label(left_inside_frame,text="Roll No.:",font=("times new roman",12,"bold"))
        rollno_label.grid(row=0,column=0,padx=4,pady=10,)

        rollno_entry=ttk.Entry(left_inside_frame,width=16, textvariable=self.var_atten_roll,font=("times new roman", 13,"bold"))
        rollno_entry.grid(row=0,column=1,pady=10,)

        
        #Name
        nameLabel=Label(left_inside_frame,text="Name ",font=("times new roman",12,"bold"))
        nameLabel.grid(row=0,column=3)

        studentName_entry=ttk.Entry(left_inside_frame,width=16, textvariable=self.var_atten_name,font=("times new roman", 13,"bold"))
        studentName_entry.grid(row=0,column=4,pady=10,)

                
        #Department
        deplabel=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"))
        deplabel.grid(row=1,column=0)

        atten_dep=ttk.Entry(left_inside_frame,width=16, textvariable=self.var_atten_dep,font=("times new roman", 13,"bold"))
        atten_dep.grid(row=1,column=1,pady=10,)

        #Time
        timelabel=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"))
        timelabel.grid(row=1,column=3)

        atten_time=ttk.Entry(left_inside_frame,width=16, textvariable=self.var_atten_time,font=("times new roman", 13,"bold"))
        atten_time.grid(row=1,column=4,pady=10,)

        
        #date
        datelabel=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"))
        datelabel.grid(row=2,column=0)

        atten_date=ttk.Entry(left_inside_frame,width=16, textvariable=self.var_atten_date,font=("times new roman", 13,"bold"))
        atten_date.grid(row=2,column=1,pady=10,)

        #attandance
        attandancelabel=Label(left_inside_frame,text="Attendance Status",bg="white",font=("times new roman",12,"bold"))
        attandancelabel.grid(row=2,column=3)

        self.atten_status=ttk.Combobox(left_inside_frame, width=16, textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"), state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=2,column=4,pady=10,)
        self.atten_status.current(0)


        #Button Frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=200,width=640,height=38)
        
        #Import CSV Button
        save_btn=Button(btn_frame,text="import csv", command=self.importCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #Export CSV button
        update_btn=Button(btn_frame,text="Export csv", command=self.exportCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        #Update button
        Delete_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)

        #Reset button
        Reset_btn=Button(btn_frame,text="Reset",width=15, command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=4)






        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="Attendance Detail", font=("times new roman",12,"bold"),width=17)
        right_frame.place(x=680,y=10,width=620,height=560)
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=600,height=455)

        #====== scroll bar

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttandanceReportTable=ttk.Treeview(table_frame,column=("roll","name","department","time","date","attandance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttandanceReportTable.xview)
        scroll_y.config(command=self.AttandanceReportTable.yview)
        self.AttandanceReportTable.heading("roll", text="Roll")
        self.AttandanceReportTable.heading("name",text="Name")
        self.AttandanceReportTable.heading("department",text="Department")
        self.AttandanceReportTable.heading("time", text="Time")
        self.AttandanceReportTable.heading("date",text="Date")
        self.AttandanceReportTable.heading("attandance",text="Attandance")


        self.AttandanceReportTable["show"]="headings"



        self.AttandanceReportTable.column("roll",width=100)
        self.AttandanceReportTable.column("name",width=100)
        self.AttandanceReportTable.column("department",width=100)
        self.AttandanceReportTable.column("date",width=100)
        self.AttandanceReportTable.column("time",width=100)
        self.AttandanceReportTable.column("attandance",width=100)
        



        self.AttandanceReportTable.pack(fill=BOTH,expand=1)

        self.AttandanceReportTable.bind("<ButtonRelease>",self.get_cursor)
#      fetch data 
    def fetchdata(self,rows):
        self.AttandanceReportTable.delete(*self.AttandanceReportTable.get_children())
        for  i in rows:
            self.AttandanceReportTable.insert("",END,values=i)
  
  #   import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File","*.csv"),("AL1 File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)



 #     export csv
    def exportCsv(self):
        try:
            records = []
            for row_id in self.AttandanceReportTable.get_children():
               records.append(self.AttandanceReportTable.item(row_id)['values'])

            if len(records) < 1:
               messagebox.showerror("No Data", "No Data found to export", parent=self.root)
               return False
            
            fln = filedialog.asksaveasfilename(
               initialdir=os.getcwd(),
               title="Save CSV",
               filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
               parent=self.root,
               defaultextension=".csv",
             )
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                   exp_write = csv.writer(myfile, delimiter=",")
                   exp_write.writerow(["Roll", "Name", "Department", "Time", "Date", "Attendance"])
                   for record in records:
                    exp_write.writerow(record)


            messagebox.showinfo("Data export", f"Your data exported to {fln} Successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

 
    def get_cursor(self,event=""):
        cursor_row=self.AttandanceReportTable.focus()
        content=self.AttandanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_roll.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_attendance.set(rows[5])

    def reset_data(self):
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

    # ===========update button===========
    def update_data(self):
        roll = self.var_atten_roll.get()
        name = self.var_atten_name.get()
        dep = self.var_atten_dep.get()
        time = self.var_atten_time.get()
        date = self.var_atten_date.get()
        attendance = self.var_atten_attendance.get()

        if roll == "":
           messagebox.showerror("Error", "Roll No. is required", parent=self.root)
        else:
           directory = 'attendance'
           formatted_date = date.replace('/', '-')  # Convert date format to match the file naming convention
           filename = f'{directory}/data_{formatted_date}.csv'

           if os.path.exists(filename):
              df = pd.read_csv(filename)
              mask = df.apply(lambda row: int(row.iloc[0]) == int(roll), axis=1)  # Assuming the first column contains roll numbers
              if mask.any():
                  df.loc[mask] = [int(roll), name, dep, time, date, attendance]
                  df.to_csv(filename, index=False)
                  messagebox.showinfo("Success", "Attendance details updated successfully", parent=self.root)
                  self.fetch_data_csv(filename)  # Pass the filename to update the table
              else:
                  messagebox.showerror("Error", f"Roll No. {roll} not found", parent=self.root)
           else:
               messagebox.showerror("Error", f"File for Date {date} not found", parent=self.root)

    def fetch_data_csv(self, filename):
        try:
           if os.path.exists(filename):
               df = pd.read_csv(filename)
               updated = False
               for index, row in df.iterrows():
                   values = list(row)
                   existing_rows = self.AttandanceReportTable.get_children()
                   existing_roll_numbers = [self.AttandanceReportTable.item(row)["values"][0] for row in existing_rows]
                   if values[0] in existing_roll_numbers:
                      item_index = existing_roll_numbers.index(values[0])
                      self.AttandanceReportTable.item(existing_rows[item_index], values=values)
                      updated = True
                   else:
                      self.AttandanceReportTable.insert("", END, values=values)
                      updated = True

               if not updated:
                   self.AttandanceReportTable.delete(*self.AttandanceReportTable.get_children())  # Clear existing data
                   for index, row in df.iterrows():
                      values = list(row)
                      self.AttandanceReportTable.insert("", END, values=values)

           else:
               messagebox.showerror("Error", f"File '{filename}' not found", parent=self.root)
        except Exception as e:
               messagebox.showerror("Error", f"Error occurred: {str(e)}", parent=self.root)



        
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
