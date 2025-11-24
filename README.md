1. Project Title
   
Intelligent Waste Sorting Assistant (IWSA)
A simple, interactive Python program that helps users identify the correct disposal category for waste items, promoting proper waste management and environmental awareness.

3. Overview of the Project
   
Improper disposal of waste is a major contributor to pollution and environmental hazards. Many people are unaware of how to correctly sort household and industrial waste into categories like recyclable, organic, hazardous, or general waste.
The Intelligent Waste Sorting Assistant is a command-line program that:
Accepts a description of a waste item from the user.
Determines the correct waste category based on keywords.
Provides instructions on how to properly dispose of the item.
Maintains a summary of all items sorted during a session.
This project emphasizes environmental responsibility while teaching basic programming, modular design, and user interaction in Python.

3. Features
   
Detects waste type: Recyclable, Organic, Hazardous, General Waste, or Unknown
Provides friendly disposal instructions for each item
Stores a summary of all items sorted in the session
Interactive command-line interface
Can be extended with GUI, file storage, or advanced classification

4. Technologies / Tools Used
   
Tool/Technology	Purpose
Python 3.x	Main programming language
VS Code / PyCharm	Code editor / IDE
Command Prompt / Terminal	Running the program
Python Standard Libraries	input, print, list, dict, lower, any, while
Programming Concepts	Functions, loops, conditional statements, modular programming
Optional Extensions	Tkinter for GUI, TextBlob/NLP for smarter classification

5. Steps to Install & Run the Project

Step 1: Install Python
Download Python 3.x from python.org
Check “Add Python to PATH” during installation

Step 2: Install a Code Editor (Optional)
Recommended: VS Code, PyCharm, Sublime Text

Step 3: Create Project Folder
Folder name: WasteSortingAssistant
File name: waste_sorting_helper.py
Paste the Python code into this file

Step 4: Open Project in VS Code (Optional)
Open folder → Open Python file

Step 5: Run the Program
From VS Code: Click Run or press F5
From Terminal:
cd path\to\WasteSortingAssistant
python waste_sorting_helper.py

Step 6: Interact with the program
Enter waste items
Follow the instructions
Type exit to quit and see the summary

6. Instructions for Testing
   
Run the program using the steps above.
Test different types of waste items:
Test Item	Expected Category	Expected Output
plastic bottle	Recyclable	Put in recycling bin
banana peel	Organic	Compost / organic bin
battery	Hazardous	Take to hazardous waste center
tissue	General Waste	Dispose in general waste bin
unknown object	Unknown	Suggest manual checking
Check that the summary at the end accurately lists all items sorted.
Try multiple entries and exit to verify program handles sessions correctly.
