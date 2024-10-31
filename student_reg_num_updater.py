import pandas as pd

def generate_registration_number(index):
    """Generates a registration number with the format HIS/24/NNN."""
    return f"HIS/24/{index:03d}"

def update_registration_numbers(file_path, sheet_name="Sheet1", output_path="Updated_STUDENT_LIST.xlsx"):
    # Load the Excel file
    data = pd.read_excel(file_path, sheet_name=sheet_name)

    # Find rows with missing registration numbers and fill them sequentially
    current_index = 1  # Start from the first number (001)
    for i in range(len(data)):
        if pd.isna(data.at[i, "REGISTRATION NUMBER"]):  # Check if the registration number is missing
            data.at[i, "REGISTRATION NUMBER"] = generate_registration_number(current_index)
            current_index += 1  # Increment for the next student

    # Save the updated data to a new Excel file
    data.to_excel(output_path, index=False)
    print(f"Updated file saved as '{output_path}'.")

# Example usage
file_path = "STUDENT LIST.xlsx"  # Replace with your input file
update_registration_numbers(file_path)