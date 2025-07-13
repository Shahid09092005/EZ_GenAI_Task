# challenge_me.py

import streamlit as st
import random
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

# Load models once
qa_model = pipeline("text2text-generation", model="google/flan-t5-small", max_length=256)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def generate_questions(text, num_questions=3):
    # Use diverse sampled sentences to guide question generation
    sentences = [s.strip() for s in sent_tokenize(text) if len(s.strip()) > 20]
    context = " ".join(random.sample(sentences, min(10, len(sentences))))
    prompt = f"Generate {num_questions} unique open-ended questions from this:\n\n{context}"
    output = qa_model(prompt)[0]["generated_text"]

    questions = [q.strip("-• \n") for q in output.split("\n") if q.strip()]
    # Ensure only unique and non-empty questions
    return list(dict.fromkeys(questions))[:num_questions]

def evaluate_answer(user_answer, correct_answer):
    if not user_answer.strip():
        return 0.0
    emb1 = embedder.encode(user_answer, convert_to_tensor=True)
    emb2 = embedder.encode(correct_answer, convert_to_tensor=True)
    return float(util.pytorch_cos_sim(emb1, emb2).item())

def run_challenge_mode(text):
    if "challenge_state" not in st.session_state:
        st.session_state.challenge_state = {
            "questions": generate_questions(text),
            "answers": [],
            "index": 0,
            "score": 0.0
        }

    state = st.session_state.challenge_state
    total = len(state["questions"])

    if state["index"] < total:
        q = state["questions"][state["index"]]
        st.markdown(f"### Question")
        st.markdown(f"**{q}**")

        user_input = st.text_area("Your Answer:", key=f"answer_{state['index']}")
        if st.button("Submit Answer", key=f"submit_{state['index']}") and user_input:
            # Regenerate answer from model
            prompt = f"Based on the document:\n\n{text[:3000]}\n\nQuestion: {q}\nAnswer:"
            correct_answer = qa_model(prompt)[0]["generated_text"].strip()

            similarity = evaluate_answer(user_input, correct_answer)
            deduction_note = ""

            if similarity >= 0.75:
                result = "Correct"
                st.session_state.challenge_state["score"] += 1
            elif similarity >= 0.4:
                result = "Partial"
                st.session_state.challenge_state["score"] += 0.5
                deduction_note = f" (−0.5) — Expected: {correct_answer}"
            else:
                result = "Incorrect"
                deduction_note = f" (−1) — Correct: {correct_answer}"

            state["answers"].append((q, user_input, result + deduction_note))
            state["index"] += 1
            st.experimental_rerun()

    else:
        st.subheader("Evaluation Summary")
        for i, (q, a, res) in enumerate(state["answers"]):
            # st.markdown(f"**Q{i+1}:** {q}")
            st.markdown(f"**Your Answer:** {a}")
            st.markdown(f"**Result:** {res}")
            st.markdown("---")

        st.markdown(f"### Final Score: {state['score']} / {total}")
        if st.button("🔄 Restart Challenge"):
            del st.session_state.challenge_state
            st.experimental_rerun()
