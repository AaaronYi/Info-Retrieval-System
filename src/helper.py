import os
from PyPDF2 import PDFReader
from langchain.text_splitter import RecursiveTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# load google api key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

# extract text from a pdf file
def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader = PDFReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# convert text to chunks
def get_text_chunks(text):
    text_splitter = RecursiveTextSplitter(chunk_size=1000,chunk_overlap=20)
    chunks = text_splitter.split_text(text)
    return chunks

# convert chunks to embeddings
def get_vector_store(text_chunks):
    embeddings = GooglePalmEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embeddings=embeddings)
    return vector_store

# get conversational chain
def get_conversational_chain(vector_store):
    llm = GooglePalm()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(), memory=memory)
    return conversation_chain