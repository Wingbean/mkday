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

# delete_job('0238456987')

# view_job()

print('MKDAY')
