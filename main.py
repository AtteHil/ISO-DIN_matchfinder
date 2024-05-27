import csv
import customtkinter as ctk
import pandas as pd
from PIL import Image

class CSVHandler:
    def find_match(string): # find matching strings
        matches = []
        with open('ISO-DIN_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if  string in str(row[0])or string in str(row[1]):
                    matches.append(CSVHandler.textToReadable(row))
        
        return matches
    def find_all(): # find everything from file
        matches = []
        with open('ISO-DIN_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                matches.append(CSVHandler.textToReadable(row))
        return matches
    def textToReadable(row): # print used for every row to textfield
        
        return (
        f"""
        {row[0]} | {row[1]}
        --------------------------""")
                






class SimpleApp:
    def __init__(self, master): ## Initialize application and set fields
        self.master = master
        self.master.geometry("500x500")
        self.master.title("ISO-DIN Finder")
        self.settings_icon = ctk.CTkImage(light_image=Image.open("icons/settings.png"),
                                  dark_image=Image.open("icons/settings.png"),
                                  size=(20, 20))
        self.label = ctk.CTkLabel(self.master, text="Enter ISO or DIN number:")


        self.label.grid(row=0,column=2,sticky="w",pady=10,padx=10)

        self.entry = ctk.CTkEntry(self.master, placeholder_text="Type here...")
        self.entry.bind("<Return>", self.on_find)
        self.entry.grid(row=0, column=3,pady=10)

        self.button = ctk.CTkButton(self.master, text="Find", command=self.on_find)
        self.button.grid(row=1,column=2, columnspan=1,pady=10)
        self.button = ctk.CTkButton(self.master, text="Find all", command=self.on_find_all)
        self.button.grid(row=1,column=3, columnspan=1,pady=10)
        self.textbox = ctk.CTkTextbox(self.master,text_color=("black","white"), width=500, corner_radius=3, height=300)
        self.textbox.grid(row=2,column=0, columnspan=6)
        self.textbox.configure(state="disabled")
        self.moreButton = ctk.CTkButton(self.master,text="",image=self.settings_icon, width=25, height=25, command=self.on_settings_click)
        self.moreButton.grid(row=0, column=5)
        
        
    def on_find(self, event=None): # event None so Enter or <Return> key press works 
        entered_text = self.entry.get()
        matches =CSVHandler.find_match(entered_text)
        self.text_box_write(matches)

    def on_find_all(self):
        matches =CSVHandler.find_all()
        self.text_box_write(matches)
    def text_box_write(self,matches):
        if len(matches):
            self.textbox.configure(state="normal")  # Enable the textbox
            self.textbox.delete("1.0", "end")  # Clear previous text
            for match in matches:
                self.textbox.insert("end", f"{match}\n")
            self.textbox.configure(state="disabled") 
        else:
            self.textbox.configure(state="normal")  # Enable the textbox
            self.textbox.delete("1.0", "end")
            self.textbox.insert("end", "No matching ISO or DIN was found. Check your number.\nIf it should exist you can add it from top right corner")
            self.textbox.configure(state="disabled")

    def on_settings_click(self): # open popup where user can delete or add new lines to file
        popup = ctk.CTkToplevel(self.master)
        popup.geometry("350x250")
        popup.title("modify data")
        popup.transient(self.master)
        popup.grab_set()
        popup.focus_set()
        label = ctk.CTkLabel(popup, text=f"Enter details for item and press correct button:")
        label.grid(row=0, column=0,columnspan=2,pady=10)

        result_label = ctk.CTkLabel(popup, text="")
        result_label.grid(row=3, column=0, columnspan=2, pady=10)

        ISO_entry = ctk.CTkEntry(popup, placeholder_text="ISO ****")
        ISO_entry.grid(row=1, column=0,pady=10,padx=2)
        DIN_entry = ctk.CTkEntry(popup, placeholder_text="DIN ****")
        DIN_entry.grid(row=1, column=1,pady=10,padx=2)
        submit_button = ctk.CTkButton(popup, text="Add", command=lambda: self.on_add( ISO_entry.get(), DIN_entry.get(), result_label))
        submit_button.grid(row=2, column=0,pady=10,padx=2)
        delete_button = ctk.CTkButton(popup, text="Delete", command=lambda: self.on_delete( ISO_entry.get(), DIN_entry.get(), result_label))
        delete_button.grid(row=2, column=1,pady=10 ,padx=2)
        
    
    def on_add(self, ISO_string, DIN_string, result_label): 
        if ISO_string and DIN_string and ISO_string.startswith("ISO ") and DIN_string.startswith("DIN "):  # Ensure both entries are not empty
            with open('ISO-DIN_data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([ISO_string, DIN_string])
            result_label.configure(text="Item added successfully")
        else:
            result_label.configure(text="Failed to add item. Ensure both fields are filled correctly.")
    
    def on_delete(self, ISO_string, DIN_string, result_label): # Delete line from file if found
         
        
        df = pd.read_csv('ISO-DIN_data.csv')

        # Check if the entry exists
        entry_exists = ((df['ISO'] == ISO_string) & (df['DIN'] == DIN_string)).any()

        if entry_exists:
            # Filter out the row that matches the given ISO and DIN pair
            df = df[~((df['ISO'] == ISO_string) & (df['DIN'] == DIN_string))]

            # Write the updated DataFrame back to the CSV file
            df.to_csv('ISO-DIN_data.csv', index=False)
            result_label.configure(text="Item deleted successfully")
            
        else:
            result_label.configure(text="Item not found.")
            
        
        

if __name__ == "__main__":
    root = ctk.CTk()
    app = SimpleApp(root)
    root.mainloop()