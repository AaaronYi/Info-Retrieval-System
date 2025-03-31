import streamlit as st
import time
from src import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain

def main():
    st.set_page_config("Information Retrieval")
    st.header("Information Retrieval System")

    with st.sidebar:
        st.title("Menu")
        pdf_docs = st.file_uploader("Upload PDF documents", type="pdf", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                # logic
                time.sleep(2)
                st.success("Done")

if __name__ == "__main__":
    main()  # call the main function