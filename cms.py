import tkinter as tk
from tkinter import messagebox,font,ttk
import sqlite3
from csv import DictReader,DictWriter
import os

root=tk.Tk()
root.title("Complaint Management System")
root.geometry('600x300')
root.configure(background='#AEB6BF')

# style
styles=ttk.Style()
styles.theme_use('classic')

# input label
labels=['Full Name: ','Gender: ','Complaint: ']
for i in range(len(labels)):
   label_name='label'+str(i)
   label_name=tk.Label(root,text=labels[i],background='#AEB6BF')
   label_name.grid(row=i,column=0,padx=10,pady=10)

# varable
fname=tk.StringVar()
gender=tk.StringVar()
# compl=tk.StringVar()

# entry box
fname_entry=ttk.Entry(root,width=40, font=('Arial', 14),textvariable=fname)
fname_entry.grid(row=0,column=1,columnspan=2,padx=10, pady=10)
gender_entry=ttk.Radiobutton(root,text='Female',value='Female',variable=gender).grid(row=1,column=1)
# ttk.Radiobutton(root,text='Student',value='Student',variable=usertype)
gender_entry=ttk.Radiobutton(root,text='Male',value='male',variable=gender).grid(row=1,column=2)
compl_entry=tk.Text(root,width=40,height=5,font=('Arial',14))
compl_entry.grid(row=2,column=1,columnspan=2,padx=10)

# save data
def save_data():
   with open("data.csv",'a',newline='') as fp:
      writer=DictWriter(fp,fieldnames=('Full Name','Gender','Complaint'))
      if fname.get()=='' or gender.get()=='' or compl_entry.get(1.0,'end')=='':
         messagebox.showwarning('Warning','Please enter required input')
      else:
         if os.stat('data.csv').st_size==0:
            writer.writeheader()
         writer.writerow({'Full Name':fname.get(),'Gender':gender.get(),'Complaint':compl_entry.get(1.0,'end')})
         messagebox.showinfo('Success','Your complaint has been submitted')         
   fname_entry.delete(0,tk.END)
   # gender_entry.delete(1.0,tk.END)
   compl_entry.delete(1.0,'end')

# show all
def show_data():
   list_com=tk.Tk()
   list_com.title('View Complaints')
   tree=ttk.Treeview(list_com,columns=('Full Name','Gender','Complaint'),selectmode='extended')
   # 
   tree.heading("Full Name",text="Full Name")
   tree.heading("Gender",text="Gender")
   tree.heading("Complaint",text="Complaint")
   tree.column("#0",minwidth=0,width=0)
   tree.column("#1",minwidth=0,width=70)
   tree.column("#2",minwidth=0,width=90)
   tree.pack()

   with open("data.csv",'r') as fp:
      reader=DictReader(fp,delimiter=',')
      for row in reader:
         fnames=row['Full Name']
         genders=row['Gender']
         compl=row['Complaint']
         # print(row)
         tree.insert("",'end',values=(fnames,genders,compl))
   list_com.mainloop()

# button
list_btn=ttk.Button(root,text='List Complaints',command=show_data).grid(row=4,column=1,padx=10,pady=10)
submit_btn=ttk.Button(root,text='Submit Now',command=save_data).grid(row=4,column=2,padx=10,pady=10)

root.mainloop()