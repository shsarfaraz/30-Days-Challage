import streamlit as st
from agent import root_agent
from pdf_utils import extract_text_from_pdf

# Set page configuration
st.set_page_config(
    page_title="Study Notes Agent",
    page_icon="📚",
    layout="wide"
)

# --- UI ---
st.title("📚 Study Notes Summarizer & Quiz Agent")
st.markdown(
    "Upload a PDF of your study notes, and an AI agent will generate a concise summary and an interactive quiz for you."
)

st.sidebar.header("Instructions")
st.sidebar.info(
    "1. **Upload PDF**: Click the 'Browse files' button to select a PDF file from your computer.\n" 
    "2. **Processing**: The agent will extract text, generate a summary, and create a quiz.\n" 
    "3. **Review**: Read the summary and take the quiz to test your knowledge."
)

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    pdf_bytes = uploaded_file.getvalue()

    with st.spinner("Step 1/3: Extracting text from PDF..."):
        extracted_text = extract_text_from_pdf(pdf_bytes)

    if not extracted_text or not extracted_text.strip():
        st.error(
            "Could not extract text from the PDF. The file might be empty, corrupted, or contain only images."
        )
    else:
        st.success("Text extracted successfully!")

        with st.expander("View Extracted Text"):
            st.text_area("", extracted_text, height=200)

        # Generate Summary
        with st.spinner("Step 2/3: Generating summary..."):
            summary = root_agent.summarize(text=extracted_text)
        
        # Generate Quiz
        with st.spinner("Step 3/3: Generating quiz..."):
            quiz = root_agent.create_quiz(text=extracted_text)

        st.header("📝 Summary")
        st.info(summary)

        st.header("❓ Interactive Quiz")
        if not quiz or "mcq" not in quiz or "short_answer" not in quiz:
            st.warning("Could not generate a valid quiz from the document.")
        else:
            # Display MCQs
            st.subheader("Multiple Choice Questions")
            for i, mcq in enumerate(quiz.get("mcq", [])):
                st.write(f"**{i+1}. {mcq['question']}**")
                options = mcq.get("options", {})
                
                # Use a form for each question to manage state independently
                with st.form(key=f"mcq_form_{i}"):
                    user_answer = st.radio(
                        "Choose your answer:",
                        list(options.values()),
                        key=f"mcq_radio_{i}",
                        index=None, # No default selection
                    )
                    submitted = st.form_submit_button("Check Answer")
                    if submitted:
                        correct_option_key = mcq.get("answer")
                        correct_answer = options.get(correct_option_key)
                        if user_answer == correct_answer:
                            st.success("Correct! 🎉")
                        elif user_answer is None:
                            st.warning("Please select an answer.")
                        else:
                            st.error(f"Incorrect. The correct answer is: **{correct_answer}**")
            
            # Display Short Answer Questions
            st.subheader("Short Answer Questions")
            for i, saq in enumerate(quiz.get("short_answer", [])):
                st.write(f"**{i+1}. {saq['question']}**")
                with st.expander("Show Answer"):
                    st.success(saq.get("answer", "No answer provided."))

else:
    st.info("Please upload a PDF file to begin.")
