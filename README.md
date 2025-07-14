# 📄 Smart Research Assistant

An AI-powered research assistant for summarizing documents, answering questions, and evaluating comprehension through interactive quizzes.
Built using Streamlit, HuggingFace Transformers, and FAISS for modern research workflows.
A fully offline, AI-powered assistant that helps you **understand, question, and test your comprehension** of any research document in PDF format.
Perfect for researchers, students, educators, and developers who want a fast and local GenAI tool to explore documents intelligently.

---

# 📸 Demo
![App Demo](https://github.com/Shahid09092005/EZ_GenAI_Task/blob/main/assets/image.png)

## 🛠️ Tech Stack

| Technology                       | Purpose                             |
|----------------------------------|-------------------------------------|
| 🐍 **Python 3.11**               | Core programming language           |
| 🚀 **Streamlit 1.46**            | Web app framework                   |
| 🤗 **HuggingFace FLAN-T5**       | Text-based reasoning model          |
| 🧠 **SentenceTransformers MiniLM** | Semantic similarity embedding      |
| 🔍 **FAISS**                     | Document vector storage/retrieval   |
| 📄 **NLTK**                      | Text tokenization and preprocessing |

## 📽️ Demo Video

[![Watch the Demo](https://drive.google.com/file/d/1z8mcVBipUww47lbwyNNtLyoJqrw6adgi/view?usp=sharing )

➡️ Click the image above to view the demo video on Google Drive.


## Table of Contents

* [Architecture](#Architecture)
* [Installation](#Installation)
* [Features](#Features)
* [How It Works](#how-it-works)
* [License](#license)

## 🏗️ Architecture

- 🧾 **User uploads a PDF**
- 📄 **Summary generated** using `Sumy` + `TextRank`
- 💬 **"Ask Me"** uses `LangChain` + vector store retrieval (`FAISS`)
- 🧠 **"Challenge Me"** generates 3 open-ended questions with sentence context
- ✅ **User answers are evaluated** using sentence similarity (`SentenceTransformers`)
- 🧮 **Score and feedback** are displayed with deduction logic


## 🛠 Installation
### Steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Shahid09092005/EZ_GenAI_Task.git
   ```

2. Navigate to the project directory:

   ```bash
   cd EZ_GenAI_Task
   ```

3. Install Dependencies

   ```bash
   pip install -r requirements.txt
   ```
   
4. Run the App

   ```bash
   streamlit run app.py
   ```

---
## ⚙️ Features
- ✍️ **Automatically summarizes** the document (120–150 words)
- 💬 **Answers questions** from the document ("Ask Me" mode)
- 🧠 **Challenges users** with logic-based open-ended questions ("Challenge Me" mode)
- 🧮 **Evaluates answers** with scoring and deduction logic
> Built using `Streamlit`, `LangChain`, `Sentence Transformers`, `Flan-T5`, `Sumy`, and `FAISS`.

---


---

## 🖥️ Demo Screenshots

| Upload PDF | Auto Summary |
|------------|---------------|
| ![Upload](https://github.com/Shahid09092005/EZ_GenAI_Task/blob/main/assets/image.png) | ![Summary](https://github.com/Shahid09092005/EZ_GenAI_Task/blob/main/assets/summary.png) |

| Ask Me | Challenge Me |
|--------|---------------|
| ![Ask Me](https://github.com/Shahid09092005/EZ_GenAI_Task/blob/main/assets/askMe.png) | ![Challenge](https://github.com/Shahid09092005/EZ_GenAI_Task/blob/main/assets/challangeMe.png) |

---


## 🚧 Future Improvements

- 🧾 **Export score report as PDF**  
- ❓ **Optional MCQ challenge mode**  
- 🌙 **Add dark mode UI**  
- 🎙️ **Speech-to-text input support**

## 👨‍💻 Author
Shahid Mansuri  
[🐙 GitHub](https://github.com/Shahid09092005) | [💼 LinkedIn](https://www.linkedin.com/in/shahid-mansuri-a3b901285)

## 🪪 License
MIT License

