from tkinter import *
from tkinter import ttk

a = Tk()
a.geometry('500x600')
a.title("แบบบันทึกใบลา by หมี")

l = Label(a, text = 'ลงบันทึกข้อมูลการลาด้านล่างนี้', font = ('Tahoma', 14))
l.pack()

l = Label(a, text='ใส่ข้อมูลให้ครบทุกช่อง\n วันที่เป็นปี คศ. \n รูปแบบวันที่ YYYY-MM-DD', font=('Tahoma', 12))
l.pack()

#---------
v_firstname = StringVar()
l = Label(a, text='ชื่อ - Firstame', font=('Tahoma', 11))
l.pack()
E1 = ttk.Entry(a, textvariable= v_firstname, font=('Tahoma', 11), justify='center')
E1.pack()

v_lastname = StringVar()
l = Label(a, text='นามสกุล - Lastname', font=('Tahoma', 11))
l.pack()
E2 = ttk.Entry(a, textvariable=v_lastname, font=('Tahoma', 11), justify='center')
E2.pack()

v_dept = StringVar()
l = Label(a, text='แผนก - Department', font=('Tahoma', 11))
l.pack()
E3 = ttk.Entry(a, textvariable= v_dept, font=('Tahoma', 11), justify='center')
E3.pack()

v_tel = StringVar()
l = Label(a, text='เบอร์โทร - Tel', font=('Tahoma', 11))
l.pack()
E4 = ttk.Entry(a, textvariable= v_tel, font=('Tahoma', 11), width= 15, justify='center')
E4.pack()

v_sdate = StringVar()
l = Label(a, text='วันที่เริ่มต้นการลา - Start Date Leave', font=('Tahoma', 11))
l.pack()
E5 = ttk.Entry(a, textvariable= v_sdate, font=('Tahoma', 11), justify='center')
E5.pack()

v_ldate = StringVar()
l = Label(a, text='วันที่สิ้นสุดการลา - Last Date Leave', font=('Tahoma', 11))
l.pack()
E6 = ttk.Entry(a, textvariable= v_ldate, font=('Tahoma', 11), justify='center')
E6.pack()

v_tdate = StringVar()
l = Label(a, text='รวมลาครั้งนี้ทั้งหมดกี่วัน - Total leave date', font=('Tahoma', 11))
l.pack()
E7 = ttk.Entry(a, textvariable= v_tdate, font=('Tahoma', 11), width=10, justify='center')
E7.pack()
#--------------
#fn
import csv
def writetocsv(data):
    with open('leavelog.csv','a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)        

def save():
    fname = v_firstname.get()
    lname = v_lastname.get()
    dept = v_dept.get()
    tel = v_tel.get()
    sdate = v_sdate.get()
    ldate = v_ldate.get()
    tdate = v_tdate.get()
    data = [fname, lname, dept, tel, sdate, ldate, tdate]
    writetocsv(data)

    v_firstname.set('')
    v_lastname.set('')
    v_dept.set('')
    v_tel.set('')
    v_sdate.set('YYYY-MM-DD')
    v_ldate.set('YYYY-MM-DD')
    v_tdate.set('')
    
#--------------
B1 = ttk.Button(a, text = 'กดเพื่อบันทึก\nClick for Save', command=save)
B1.pack(pady=20, ipadx=30, ipady=20)

#--------------
a.mainloop()