# 🍌🍫 Banana Choco - Flash Card Game

> An interactive, web-based flashcard game designed to make studying and memorization fun and engaging. 

This repository contains the source code for our CS212 course project at Chiang Mai University. Banana Choco allows users to create, manage, and play through custom flashcard decks to test their knowledge.

## 👥 Team Members

* **[Auttakorn Camsoi]** (@AuttakornC) - [Full-stack]
* **[Rachata Thananchai]** (@Meaww2) - [Full-stack]
* **[Mesanee Laihuang]** (@nnyPRO) - [Full-stack]
* **[Warisa Narata]** (@ggodcatt) - [UX/UI design]

## 🛠 Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS (or Bootstrap/Tailwind), JavaScript
* **Database:** SQLAlchemy

## ✨ Key Features

* 🃏 **Custom Flashcards:** Create, edit, and delete your own study cards.
* 🎮 **Interactive Gameplay:** Flip cards to reveal answers and track your learning progress.
* 📂 **Deck Management:** Organize flashcards into different categories or subjects.

## 🚀 Getting Started

Follow these instructions to set up the Python environment and run the Flask application on your local machine.

### Prerequisites

Make sure you have Python installed on your system:
* [Python 3.x](https://www.python.org/downloads/)
* `pip` (Python package installer)

### Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/AuttakornC/p23cs212g12.git](https://github.com/AuttakornC/p23cs212g12.git)
cd p23cs212g12
```  

**2. Create a virtual environment (Recommended):**
```bash
# For Mac/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```  

**4. Run the Flask application:**
```bash
python app.py
```  
The game should now be running locally at `http://127.0.0.1:5000`.  

## 📂 Project Structure
- `app.py`: The main Flask application entry point and route definitions.
- `templates/`: Contains all the HTML files for the web interface.
- `static/`: Houses CSS stylesheets, JavaScript files, and images (like banana and choco assets!).
- `requirements.txt`: List of Python dependencies needed to run the app.
