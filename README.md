## ISO-DIN Match Finder

A Python application to find matching ISO-DIN numbers.

## Prerequisites

- **Python 3.11**: Make sure you have Python 3.11 installed on your system.

### Additional Python Packages

Install the required packages using the following commands:

```sh
pip install pillow
pip install pandas
pip install customtkinter

```
Running the Program
You can run the program with a simple Python command:
```sh
python main.py
```
Creating an Executable
To create a standalone executable, you can use PyInstaller. Run the following command:
```
pyinstaller --onefile -w --add-data "ISO-DIN_data.csv;." --add-data "icons/settings.png;icons" main.py
```
After running the above command, the executable will be generated in the dist folder. Move the .exe file from the dist folder to the same directory as main.py to ensure it has access to the necessary data files and icons.

## Directory Structure
Ensure your project directory is structured as follows:
```css
project_directory/
│
├── main.py
├── *Possible main.exe*
├── ISO-DIN_data.csv
├── icons/
│   └── settings.png
└── README.md
```

## Usage
Enter ISO or DIN Number: Use the text entry field to input the ISO or DIN number you want to find.

Find Button: Click the "Find" button or press Enter to search for matches.

Find All Button: Click the "Find all" button to display all ISO-DIN pairs in the dataset.

Settings: Click the settings icon (top right) to add or delete entries from the dataset.

Adding/Deleting Entries
To modify the dataset:

  1. Add Entry:

   * Enter the ISO and DIN numbers in the provided fields.
   * Click the "Add" button to add the entry to the dataset.

  Ensure the ISO and DIN entries follow the format:

  ISO: ISO xxxx

  DIN: DIN xxxx

  2. Delete Entry:

   * Enter the ISO and DIN numbers in the provided fields.
   * Click the "Delete" button to remove the entry from the dataset.

### Author: Atte Hiltunen
