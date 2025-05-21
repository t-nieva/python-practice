# Mail Merge Project ✉️

This is a simple Python project that automates the process of generating personalized letters 
using a template and a list of invited names.

## 🧠 How It Works

- Reads a list of names from `invited_names.txt`.
- Reads a letter template from `starting_letter.txt`, which includes a placeholder `[name]`.
- Replaces the `[name]` placeholder with each real name from the list.
- Saves each personalized letter in the `Output/Ready_to_send/` folder as a `.docx` file.

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Place your list of names in `Input/Names/invited_names.txt` (one name per line).
3. Create your letter template in `Input/Letters/starting_letter.txt` with the `[name]` placeholder.
4. Run the script:

```bash
python main.py
