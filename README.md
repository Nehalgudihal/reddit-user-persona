# Reddit User Persona Generator 🧠

This project analyzes a Reddit user's activity to generate a **user persona**, highlighting traits like interests, tone, subreddit preferences, hobbies, and personality, based on their posts and comments.

---
## 🚀 Features

- 🔗 Input: Any Reddit profile URL
- 📄 Scrapes all posts and comments from that user
- 🤖 Builds a rich persona using an LLM prompt
- 📁 Outputs a `.txt` file containing the persona and citations to the original content

---
## 🧪 Sample Input
Input:
https://www.reddit.com/user/kojied/

Output:
The program saves the generated persona in a file like:
output_kojied.txt

⚙️ Installation & Setup
1. Clone the repository:
git clone https://github.com/Nehalgudihal/reddit-user-persona.git
cd reddit-user-persona

2. Set up virtual environment (recommended):
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On macOS/Linux

3. Install dependencies:
pip install -r requirements.txt


🚀 How to Run
python generate_persona.py https://www.reddit.com/user/kojied/

📁 Project Structure
reddit-user-persona/
├── generate_persona.py           # Main script
├── manual_prompt_kojied.txt      # Prompt used for persona generation
├── output_kojied.txt             # Sample persona output
├── requirements.txt              # Required Python libraries
├── .gitignore                    # Ignored files/folders
├── README.md                     # Project documentation
└── .venv/                        # Virtual environment (not tracked)

📝 Notes
This project is for educational and evaluation purposes.
You can extend this to analyze more Reddit profiles or build a UI later.


