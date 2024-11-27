# Personal-DIary

This Personal Diary application allows users to write, save, and open daily diary entries using a simple graphical interface created with Python's tkinter library. The app provides a text area for writing multi-line diary entries, along with options to save and open diary entries from text files. Users can also clear the text area to start a new entry.

## Features
- Text Area: A multi-line text box for writing and editing diary entries.
- Save Entry: Save the current diary entry to a text file with a custom filename and location.
- Open Entry: Open a previously saved diary entry from a text file.
- Clear Entry: Clear the text area to start a new entry.
- Menu Bar: A simple menu bar with options to save, open, and exit the application.
- Error Handling: Displays error messages if something goes wrong when saving or opening files.
- Responsive UI: Automatically adjusts to the size of the window.
## Installation
- Ensure you have Python 3.x installed on your system.
- The application uses tkinter, which is included by default in most Python installations. You do not need to install additional packages.
## Running the Application
- Save the Python code into a file named diary_app.py.

- Open a terminal or command prompt.

- Navigate to the directory where diary_app.py is located.

- Run the application with:

```
python diary_app.py
```
This will launch the Personal Diary application.

## Usage Instructions
Once the application is running, you will see the following:

### Text Area:
- The large area at the top of the window is where you can type your diary entry. You can enter multiple lines of text.
### Menu Bar:
- File:
     - Save: Save your diary entry to a text file. When you click "Save", a file dialog will open where you can choose the location and file name.
      - Open: Open a saved diary entry from a text file. You will be prompted to choose a file to open.
     - Exit: Close the application.
### Clear Button:
- A button at the bottom of the window allows you to clear the current text area to start writing a new diary entry.
### Error Handling:
- If you attempt to save an empty entry, a warning message will appear reminding you to write something before saving.
If there's an issue opening or saving a file, an error message will appear with details.
## Example Usage
- Write a Diary Entry: Click in the text area and begin typing your diary entry.
- Save Your Entry: When you're done, click "File" -> "Save". You'll be prompted to select a location and name your file. The diary entry will be saved as a .txt file.
- Open a Previous Entry: To view or edit a previously saved entry, click "File" -> "Open", and choose the file you want to open. The content of the file will be loaded into the text area.
- Clear the Text Area: If you want to start a new entry, click the "Clear" button at the bottom, which will clear the current text.
## Code Explanation
### DiaryApp Class
- __init__(self, root): This method initializes the application's GUI, creating the text area, menu bar, and the "Clear" button.
- save_entry(self): This method handles saving the text from the text area to a text file. It prompts the user to select a location and file name using a file dialog.
- open_entry(self): This method allows the user to open an existing text file, displaying the content in the text area.
- clear_entry(self): This method clears all the text from the text area, allowing the user to start a new diary entry.
### tkinter Widgets Used
- Text: A multi-line text widget used for writing and editing diary entries.
- Menu: A menu bar for the "File" menu, which includes options to save, open, and exit.
- Button: A button at the bottom of the window to clear the text area.
filedialog: A file dialog for opening and saving files.
