# 📄 Smart Research Assistant (Offline PDF Q&A with Summary & Challenge Mode)
---
# EZ-project
It's an AI assitnce system 
Sure! Here's a sample **README.md** file for an **AI-assisted PDF reader** project. This README explains how to use an AI tool to read and extract information from PDFs.

## 📸 Demo
![App Demo](https://github.com/Shahid09092005/EZ_GenAI_Task/blob/main/assets/image.png)
---


# AI-Assisted PDF Reader

An AI-powered tool designed to read, process, and extract text from PDF documents. It uses Natural Language Processing (NLP) to analyze the content of PDFs and provide useful insights or summaries.

## Table of Contents

* [Architecture](#Architecture)
* [Installation](#Installation)
* [Features](#Features)
* [How It Works](#how-it-works)
* [License](#license)

## Architecture
-🧾 User uploads a PDF
-📄 Summary generated using Sumy + TextRank
-💬 "Ask Me" uses LangChain + vector store retrieval
-🧠 "Challenge Me" mode generates 3 open-ended questions
-✅ User answers are evaluated using sentence similarity
-🧮 Score and feedback displayed

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

##🖼️ App Flow — Screenshots(Ss)
- Demo Ss(Default View)
     ![App Demo](https://github.com/Shahid09092005/EZ_GenAI_Task/blob/main/assets/image.png)
- Summary Ss
     ![App Demo](https://github.com/Shahid09092005/EZ_GenAI_Task/blob/main/assets/summary.png)
- Ask Me
     ![App Demo](https://github.com/Shahid09092005/EZ_GenAI_Task/blob/main/assets/askMe.png)
- Challange me Ss
     ![App Demo](https://github.com/Shahid09092005/EZ_GenAI_Task/blob/main/assets/challangeMe.png)

##🚧 Future Improvements
-🧾 Export score report as PDF
-❓ Optional MCQ challenge mode
-🌙 Add dark mode UI
-🎙️ Speech-to-text input support
