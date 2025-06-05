# 🧠 Quizler — A Python Quiz App with GUI
Quizler is a fun and interactive quiz application built with Python's tkinter. 
It fetches trivia questions from the **Open Trivia Database** and quizzes the user with 
a clean and simple graphical interface.

### 🚀 Features
1. Retrieves boolean (True/False) questions from an online API
2. 🔧 Customization Opportunity
  + Currently, the app fetches 10 True/False questions from the Computer Science category (ID 18) by default.

    You can easily customize:

    ✅ Number of Questions (amount)

    ✅ Question Category (category)

    Edit the parameters dictionary in data.py:
    ```python
    parameters = {
        "amount": 10,         # Change number of questions (e.g., 5, 15, 20)
        "category": 18,       # Change category ID (e.g., 9 = General Knowledge)
        "type": "boolean"
    }
    ```
    
    To explore available category IDs, visit:
    👉 https://opentdb.com/api_category.php

3. Displays questions using a Tkinter GUI 
4. Highlights correct and wrong answers with color feedback 
5. Tracks and displays the user's score 
6. Ends with a summary screen after all questions are answered

