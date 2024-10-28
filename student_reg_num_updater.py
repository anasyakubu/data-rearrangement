import openai
import pandas as pd

# Set up OpenAI API key
openai.api_key = "your_openai_api_key_here"

# Load the spreadsheet
file_path = "STUDENT LIST update.xlsx"
data = pd.read_excel(file_path, sheet_name="Sheet1")

# Define function to generate registration numbers
def generate_registration_number(index):
    return f"HIS/24/{index:03}"

# Detect missing registration numbers and fill them
start_index = 1  # Start from 1 if needed or adjust based on existing data
data['REGISTRATION NUMBER'] = data['REGISTRATION NUMBER'].fillna(
    pd.Series([generate_registration_number(i) for i in range(start_index, start_index + len(data[data['REGISTRATION NUMBER'].isna()]))])
)

# Optional: Use OpenAI API to assist in data reorganization or formatting feedback
def clean_data_with_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Prepare a prompt for OpenAI API to verify data structure
prompt = (
    "Here is a dataset with student names, registration numbers, gender, and class. "
    "Please ensure all fields are filled accurately. Missing fields should be filled sequentially in "
    "'REGISTRATION NUMBER' starting from HIS/24/001."
)
cleaned_data = clean_data_with_openai(prompt)

# Save the updated data to a new Excel file
updated_file_path = "Updated_STUDENT_LIST.xlsx"
data.to_excel(updated_file_path, index=False)

print(f"Data has been updated and saved to {updated_file_path}")
