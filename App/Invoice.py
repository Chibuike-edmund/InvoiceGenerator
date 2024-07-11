import os
import tkinter as tk
from tkinter import *
from reportlab.pdfgen import canvas
from tkinter import filedialog
from tkcalendar import Calendar

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import DateEntry

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    # Use the selected filename

def selectDate():
    def set_date():
        date.config(text=cal.get_date())
        date_window.destroy()
        
    date_window = tk.Toplevel(wn)
    cal = DateEntry(date_window, selectmode='day', date_pattern='dd/mm/yyyy')
    cal.pack(pady=20)
    ttk.Button(date_window, text="Set Date", command=set_date).pack()

def generateInvoice():
    # Implement invoice generation logic
    pass

wn = tk.Tk()
wn.title("Python Invoice Generator")
wn.geometry("600x600")
wn.configure(bg='white')

style = ttk.Style()
style.configure('TLabel', background='white', foreground='gray', font=("calibre", 12))
style.configure('TEntry', padding=5)
style.configure('TButton', padding=5)

# Title
ttk.Label(wn, text="Enter your company details", font=("calibre", 20, "bold"), foreground="green", background="white").pack(pady=10)

# Company details frame
frame = ttk.Frame(wn, padding=(20, 10), style='TFrame')
frame.pack(fill='x')

ttk.Label(frame, text="Company Name").grid(row=0, column=0, pady=5, sticky='w')
company_name = ttk.Entry(frame)
company_name.grid(row=0, column=1, pady=5, sticky='ew')

ttk.Label(frame, text="Address").grid(row=1, column=0, pady=5, sticky='w')
address = ttk.Entry(frame)
address.grid(row=1, column=1, pady=5, sticky='ew')

ttk.Label(frame, text="City").grid(row=2, column=0, pady=5, sticky='w')
city = ttk.Entry(frame)
city.grid(row=2, column=1, pady=5, sticky='ew')

ttk.Label(frame, text="GST Number").grid(row=3, column=0, pady=5, sticky='w')
gstNo = ttk.Entry(frame)
gstNo.grid(row=3, column=1, pady=5, sticky='ew')

ttk.Label(frame, text="Date").grid(row=4, column=0, pady=5, sticky='w')
date = ttk.Label(frame, text="", style='TLabel')
date.grid(row=4, column=1, pady=5, sticky='ew')
ttk.Button(frame, text="Select Date", command=selectDate).grid(row=4, column=2, padx=10, pady=5)

ttk.Label(frame, text="Phone No").grid(row=5, column=0, pady=5, sticky='w')
phNo = ttk.Entry(frame)
phNo.grid(row=5, column=1, pady=5, sticky='ew')

ttk.Label(frame, text="Customer Name").grid(row=6, column=0, pady=5, sticky='w')
c_name = ttk.Entry(frame)
c_name.grid(row=6, column=1, pady=5, sticky='ew')

ttk.Label(frame, text="Authorized Signatory").grid(row=7, column=0, pady=5, sticky='w')
auSign = ttk.Entry(frame)
auSign.grid(row=7, column=1, pady=5, sticky='ew')

ttk.Label(frame, text="Company Image").grid(row=8, column=0, pady=5, sticky='w')
ttk.Button(frame, text="Browse Files", command=browseFiles).grid(row=8, column=1, pady=5, sticky='ew')

# Submit Button
ttk.Button(wn, text="Submit Details", command=generateInvoice).pack(pady=20)

# Adjust column weights for proper stretching
for i in range(2):
    frame.grid_columnconfigure(i, weight=1)

wn.mainloop()


from reportlab.pdfgen import canvas

def generateInvoice():
    global file_name, company_name, address, city, gstNo, date, c_name, phNo, auSign

    # Create a new canvas for the PDF
    pdf_canvas = canvas.Canvas("Invoice.pdf", pagesize=(200, 250), bottomup=0)

    # Draw lines for the invoice layout
    pdf_canvas.line(5, 45, 195, 45)
    pdf_canvas.line(15, 120, 185, 120)
    pdf_canvas.line(35, 108, 35, 220)
    pdf_canvas.line(115, 108, 115, 220)
    pdf_canvas.line(135, 108, 135, 220)
    pdf_canvas.line(160, 108, 160, 220)
    pdf_canvas.line(15, 220, 185, 220)

    # Draw company logo
    pdf_canvas.translate(10, 40)
    pdf_canvas.scale(1, -1)
    pdf_canvas.drawImage(file_name, 0, 0, width=50, height=30)
    pdf_canvas.scale(1, -1)
    pdf_canvas.translate(-10, -40)

    # Draw company details
    pdf_canvas.setFont("Times-Bold", 10)
    pdf_canvas.drawCentredString(125, 20, company_name.get())
    pdf_canvas.setFont("Times-Bold", 5)
    pdf_canvas.drawCentredString(125, 30, address.get())
    pdf_canvas.drawCentredString(125, 35, f"{city.get()}, India")
    pdf_canvas.setFont("Times-Bold", 6)
    pdf_canvas.drawCentredString(125, 42, f"GST No: {gstNo.get()}")

    # Draw invoice title
    pdf_canvas.setFont("Times-Bold", 8)
    pdf_canvas.drawCentredString(100, 55, "INVOICE")

    # Draw customer details
    pdf_canvas.setFont("Times-Bold", 5)
    pdf_canvas.drawRightString(70, 70, "Invoice No.:")
    pdf_canvas.drawRightString(100, 70, "XXXXXXX")
    pdf_canvas.drawRightString(70, 80, "Customer Name:")
    pdf_canvas.drawRightString(100, 80, c_name.get())
    pdf_canvas.drawRightString(70, 90, "Date:")
    pdf_canvas.drawRightString(100, 90, date.cget("text"))
    pdf_canvas.drawRightString(70, 100, "Phone No.:")
    pdf_canvas.drawRightString(100, 100, phNo.get())

    # Draw table for order details
    pdf_canvas.roundRect(15, 108, 170, 130, 10, fill=0)
    pdf_canvas.drawCentredString(25, 118, "S.No.")
    pdf_canvas.drawCentredString(75, 118, "Orders")
    pdf_canvas.drawCentredString(125, 118, "Price")
    pdf_canvas.drawCentredString(148, 118, "Qty.")
    pdf_canvas.drawCentredString(173, 118, "Total")

    # Draw signature
    pdf_canvas.drawRightString(180, 228, auSign.get())
    pdf_canvas.drawRightString(180, 235, "Signature")

    # Finalize the PDF
    pdf_canvas.showPage()
    pdf_canvas.save()
