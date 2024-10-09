// script.js
const form = document.getElementById('certificateForm');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  // รับค่าจากฟอร์ม
  const name = document.getElementById('name').value;
  // ... รับค่าอื่นๆ

  // สร้างไฟล์ PDF
  const doc = new jsPDF();
  doc.text('ใบรับรองแพทย์', 14, 15);
  doc.text(`ชื่อ-นามสกุล: ${name}`, 14, 25);
  // ... เพิ่มข้อมูลอื่นๆ ลงใน PDF

  // ดาวน์โหลดไฟล์ PDF
  doc.save('certificate.pdf');
});