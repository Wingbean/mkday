from tkinter import *
from tkinter import ttk

# import code from basic sql มาใช้
##############DATABASE###################
import sqlite3 # เรียก sql

#create connection to sql

conn = sqlite3.connect('mydatabase.sqlite3') # (name database)
c = conn.cursor() # c เหมือน operator ไปสั่ง ขั้นตอนต่าง ๆ

# ต่อมา เรียก c มาทำงาน
# if not exists หมายถึงว่า ถ้า มันมีอยู่แล้วมันจะไม่สร้างใหม่
c.execute("""CREATE TABLE IF NOT EXISTS job (
          ID INTEGER PRIMARY KEY AUTOINCREMENT,
          fullname TEXT,
          tel TEXT,
          position TEXT)""")
#auto increment คือ ให้มันสร้างตัวเลขเอง เรียงมาเรื่อย ๆ

# create fn insert
def insert_job(fullname,tel,position):
    with conn:
        command = 'INSERT INTO job VALUES(?,?,?,?)' # เหมือน sql value ใช้ ? แทน กี่ field ใน table
        c.execute(command,(None,fullname,tel,position)) # เรียก command บรรทัดบนมาใช้ ในวงเล็บ 4 ตัว คือค่าที่จะใส่ อันแรก คือ ID ให้เป็น None เพราะเราทำ Auto increment ไปแล้ว
        conn.commit # commit ปิดหลัง insert ค่า
        print('saved เรียบร้อย')

# insert_job('memory', '0987569875', 'cfo')

# fn view date in table
def view_job():
    with conn:
        command = 'SELECT * FROM job'
        c.execute(command)
        result = c.fetchall() # fetchall แปลว่า ดึงมาทั้งหมด
    print(result)

# view_job()

# fn update
def update_job(newvalue, field, tel): # ค่าใหม่ , column ไหน , เงื่อนไข tel อะไร
    with conn:
        command = 'UPDATE job SET {} = (?) WHERE tel = (?)'.format(field)
        c.execute(command,(newvalue,tel))
        conn.commit()
        print('update ข้อมูลเรียบร้อย')

# update_job('woranuch', 'fullname', '0987569875')

# fn delete
def delete_job(tel):
    with conn:
        command = 'DELETE FROM job WHERE tel = (?)'
        c.execute(command,([tel]))
        conn.commit()
        print('delete ข้อมูลเรียบร้อย')

##############//DATABASE###################

# import thinker as tk
GUI = Tk() #GUI = tk.Tk()
GUI.geometry('500x500')
GUI.title('โปรแกรมสมัครงาน by หมี') # title at title bar

L = Label(GUI, text = 'กรอกใบสมัครที่นี่', font=('Tahoma', 12)) #ใส่ label กำหนดชนิดอักษร ขนาด
L.pack() # pack code ใส่เข้าไปใน โปรแกรม

L = Label(GUI, text = 'คุณสมบัติ \n\n -ต้องอายุมากกว่า 20 ปี\n-วุฒิ ม.6\n', font=('Tahoma', 10))
L.pack()

#---------------------------------------------
v_fullname = StringVar() #v_fullname มารับค่า
L = Label(GUI, text = 'ชื่อ- สกุล', font=('Tahoma', 14))
L.pack()
E1 = ttk.Entry(GUI,textvariable = v_fullname, font = ('Tahoma', 12)) # textvariable= มารับค่า input
E1.pack()

v_tel = StringVar()
L = Label(GUI, text = 'เบอร์โทร', font=('Tahoma', 14))
E2 = ttk.Entry(GUI, textvariable = v_tel, font = ('Tahoma', 12))
L.pack()
E2.pack()

v_position = StringVar()
L = Label(GUI, text = 'ตำแหน่ง', font=('Tahoma', 14))
E3 = ttk.Entry(GUI, textvariable = v_position, font = ('Tahoma', 12),width = 30) #กำหนดขนาดช่อง 30
L.pack()
E3.pack()

#ใส่ fn
import csv # เรียกใช้ csv
def writetocsv(data): # data ต้องเป็นค่า list
    with open('data.csv','a',newline='',encoding='utf-8',) as file:
        #with open แปลว่า เปิดแล้วปิดให้ด้วย , a คือ เขียนลงไปเรื่อย ๆ newline '' ทำให้ไม่มีช่องว่างระหว่างบรรทัด
        fw = csv.writer(file) #ให้ csv เขียนลงไปใน file file คือดบรรทัดบน
        fw.writerow(data) # เขียนอะไรลงไป เขียน data ลงไป และ data ต้องเป็น list


def save():
    fullname = v_fullname.get() #.get() เป็นความสามารถพิเศษของ StringVar ไปอ่าน Class เพิ่ม , มันทำให้เราดึงค่ามาจาก StringVar ได้
    tel = v_tel.get()
    position = v_position.get()
    #print(fullname,tel,position) #เทสว่า get ค่าได้ไหม ให้print ออกมา
    data = [fullname, tel, position]
    # writetocsv(data) # เขียนเป็น csv file
    
    # เปลี่ยนเป็น insert เข้า sql database
    insert_job(fullname,tel,position)

    v_fullname.set('') # กำหนดให้ช่องกับมาว่างหลัง กดปุ่ม
    v_tel.set('')
    v_position.set('')
    # ขอดู ข้อมูล ใน db
    view_job()


#----------------------------------------------
B1 = ttk.Button(GUI, text='บันทึก', command=save) #สร้างปุ่มกด บอก fn ของ ปุ่ม ด้วย command= fn save ด้านบน
B1.pack(pady=20, ipadx=30,ipady=20) #กำหนดให้ button มีช่องว่างกับตัวอื่น 20 pixel , กำหนดขาดปุ่มด้วย ipad x y

GUI.mainloop()