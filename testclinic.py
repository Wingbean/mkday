import sqlite3
import tkinter as tk
from fpdf import FPDF

# สร้างฐานข้อมูล
conn = sqlite3.connect('patient.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS patients
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              age INTEGER,
              illness TEXT,
              date TEXT)''')
conn.commit()

# สร้างหน้าต่าง GUI
window = tk.Tk()
window.title("ใบรับรองแพทย์")

# ... (สร้างช่องกรอกข้อมูลต่างๆ)

# ฟังก์ชันบันทึกข้อมูล
def save_data():
    # ... (เก็บข้อมูลจากช่องกรอกและบันทึกลงฐานข้อมูล)

# ฟังก์ชันสร้างใบรับรอง
def create_certificate():
    # ... (อ่านข้อมูลจากฐานข้อมูลและสร้างไฟล์ PDF)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # ... (เขียนข้อมูลลงใน PDF)
    pdf.output("certificate.pdf")

# ... (สร้างปุ่มสำหรับบันทึกและพิมพ์)

window.mainloop()