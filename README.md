# 📄 Smart Research Assistant
A fully offline, AI-powered assistant that helps you **understand, question, and test your comprehension** of any research document in PDF format.

This app automatically summarizes uploaded PDFs into a clean paragraph, allows you to ask context-aware questions, and challenges you with logic-based open-ended questions — **all without needing internet access for processing**.

Perfect for researchers, students, educators, and developers who want a fast and local GenAI tool to explore documents intelligently.

---

# 📸 Demo
![App Demo](https://github.com/Shahid09092005/EZ_GenAI_Task/blob/main/assets/image.png)

# AI-Assisted PDF Reader

An AI-powered tool designed to read, process, and extract text from PDF documents. It uses Natural Language Processing (NLP) to analyze the content of PDFs and provide useful insights or summaries.

# EZ-project
It's an AI assitnce system 
Sure! Here's a sample **README.md** file for an **AI-assisted PDF reader** project. This README explains how to use an AI tool to read and extract information from PDFs.

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

