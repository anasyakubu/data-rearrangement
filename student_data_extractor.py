import fitz  # PyMuPDF
import pandas as pd

def extract_student_data_from_pdf(pdf_path):
    """
    Reads a PDF file and extracts student names, class, and class ID.
    Assumes each line in the PDF contains 'Name, Class, ClassID' format.
    """
    student_data = []

    # Open the PDF file
    with fitz.open(pdf_path) as pdf:
        for page_num in range(pdf.page_count):
            page = pdf[page_num]
            text = page.get_text()  # Extract text from each page
            lines = text.splitlines()  # Split the text into lines

            for line in lines:
                parts = line.split(",")  # Assuming CSV format in the PDF

                if len(parts) == 3:
                    name, class_name, class_id = parts
                    student_data.append({
                        'Name': name.strip(),
                        'Class': class_name.strip(),
                        'ClassID': class_id.strip()
                    })

    return student_data

def generate_registration_number(index):
    """
    Generates a registration number in the format 'DEM/4/XXX' where XXX is a 3-digit number.
    """
    return f"DEM/4/{index:03}"

def create_excel_from_data(student_data, output_path):
    """
    Creates an Excel sheet with columns Name, Registration Number, Class, and ClassID.
    """
    for i, student in enumerate(student_data):
        student['Registration Number'] = generate_registration_number(i + 1)

    # Convert data to DataFrame and reorder columns
    df = pd.DataFrame(student_data)
    df = df[['Name', 'Registration Number', 'Class', 'ClassID']]

    # Save to Excel
    df.to_excel(output_path, index=False)
    print(f"Excel file saved to {output_path}")

# File paths
pdf_path = 'students.pdf'  # Path to the PDF containing student data
output_excel_path = 'students_data.xlsx'  # Output Excel file path

# Extract student data from the PDF
students = extract_student_data_from_pdf(pdf_path)

# Create an Excel file with the extracted data
create_excel_from_data(students, output_excel_path)
