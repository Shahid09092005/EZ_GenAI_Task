import streamlit as st
# === Page Config and Title ===
st.set_page_config(page_title="📄 Smart Research Assistant", layout="wide")
st.title("📚 Smart Research Assistant")

with st.sidebar:
    st.header("🔗Connect with me")
    st.markdown("""
        <style>
        .no-underline a {
            text-decoration: none !important;
        }
        </style>
        <div class="no-underline">
            👨‍💻 Built by <strong>Shahid Mansuri</strong><br><br>
            <a href="https://github.com/Shahid09092005" target="_blank">🐙 GitHub</a><br>
            <a href="https://www.linkedin.com/in/shahid-mansuri-a3b901285" target="_blank">💼 LinkedIn</a>
        </div>
    """, unsafe_allow_html=True)

# # === Sidebar Navigation ===
# with st.sidebar:
#     st.header("🔗Connect with me")
#     st.markdown("👨‍💻 Built by **Shahid Mansuri**")
#     st.markdown("[🐙 GitHub](https://github.com/Shahid09092005)")
#     st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/shahid-mansuri-a3b901285)")

# === Imports ===
from extract_text import extract_text_from_pdf 
from qa_pipeline import build_qa_index
from summarizer import summarize_text
from ask_me import answer_question
from challenge_me import run_challenge_mode

# === Upload PDF ===
uploaded_file = st.file_uploader("📁 Upload a PDF", type=["pdf"])

# === Detect New File ===
if uploaded_file:
    # Clear previous state if new file is uploaded
    if (
        "last_uploaded_filename" not in st.session_state
        or st.session_state.last_uploaded_filename != uploaded_file.name
    ):
        # Reset entire session state
        st.session_state.clear()
        st.session_state.last_uploaded_filename = uploaded_file.name

    # Proceed if retriever not initialized
    if "retriever" not in st.session_state or st.session_state.retriever is None:
        try:
            with st.spinner("⏳ Extracting and summarizing document..."):
                raw_text = extract_text_from_pdf(uploaded_file)
                st.session_state.raw_text = raw_text

                summary = summarize_text(raw_text[:5000])
                st.session_state.summary = summary

                retriever, vector_store, num_chunks = build_qa_index(raw_text)
                st.session_state.retriever = retriever
                st.session_state.vector_store = vector_store

            # st.success(f"✅ Document embedded with {num_chunks} chunks.")
        except Exception as e:
            st.error(f"Failed to process PDF: {e}")

# === Show Summary ===
if "summary" in st.session_state and st.session_state.summary:
    st.subheader("Summary")
    st.markdown(st.session_state.summary)

# === Ask or Challenge Buttons ===
if "retriever" in st.session_state and st.session_state.retriever:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💬 Ask Me"):
            st.session_state.mode = "ask"
    with col2:
        if st.button("🧠 Challenge Me"):
            st.session_state.mode = "challenge"

# === ASK ME MODE ===
if st.session_state.get("mode") == "ask":
    user_query = st.text_input("Ask a question from the document:")
    if user_query:
        with st.spinner("Generating answer..."):
            answer, docs = answer_question(user_query, st.session_state.retriever)
        st.markdown(f"### Answer:\n{answer}")
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        st.session_state.chat_history.append((user_query, answer))

# === CHALLENGE ME MODE ===
if st.session_state.get("mode") == "challenge":
    run_challenge_mode(st.session_state.raw_text)

# === Chat History ===
if "chat_history" in st.session_state and st.session_state.chat_history:
    st.markdown("---")
    st.subheader("Chat History")
    for q, a in st.session_state.chat_history:
        st.markdown(f"**Q:** {q}")
        st.markdown(f"**Ans:** {a}")
