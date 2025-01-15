import csv
import os
from pyxlsb import open_workbook
from tqdm import tqdm

def convert_xlsb_to_csv(input_path, output_path):
    # Open the workbook
    with open_workbook(input_path) as workbook:
        # Get the first sheet name
        sheet_name = workbook.sheets[0]
        sheet = workbook.get_sheet(sheet_name)
        
        # Open the CSV file for writing
        with open(output_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Get the total number of rows for the progress bar
            total_rows = sum(1 for _ in sheet.rows())
            
            # Write each row of the sheet to the CSV file with a progress bar
            for row in tqdm(sheet.rows(), total=total_rows, desc=f"Converting {os.path.basename(input_path)}"):
                writer.writerow([item.v for item in row])
    
    print(f"Conversion complete for {input_path}!")


def main():
    # Folder containing the .xlsb files
    folder_path = r"<path1>"
    output_folder = r"<path2>"
    
    
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".xlsb"):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.csv")
            
            # Convert the .xlsb file to CSV
            convert_xlsb_to_csv(input_path, output_path)

if __name__ == "__main__":
    main()
