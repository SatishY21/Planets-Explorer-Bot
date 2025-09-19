import streamlit as st
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="🚀 Planets Explorer Bot",
    page_icon="🪐",
    layout="wide"
)

# --- CACHING AND MODEL LOADING ---
# This is a key Streamlit feature. It caches the result of this function.
# The function will only run once, the first time the app is loaded.
# On subsequent user interactions, it will reuse the loaded models, making the app much faster.
@st.cache_resource
def load_models():
    """
    Loads the embedding model and the FAISS vector store from local files.
    """
    # Load the embedding model that you used in Colab
    model_name = "all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    
    # Load the FAISS index from the local folder
    vector_store = FAISS.load_local("faiss_cosmic_explorer", embeddings, allow_dangerous_deserialization=True)
    
    return vector_store

# --- GOOGLE API KEY SETUP ---
# For Streamlit deployment, we use st.secrets to securely store the API key.
# You will set this up in the Streamlit Community Cloud settings, not in the code.
try:
    google_api_key = st.secrets["GOOGLE_API_KEY"]
except KeyError:
    st.error("Google API Key not found. Please set it in your Streamlit secrets.")
    st.stop()

# --- APP UI AND LOGIC ---
st.title("🚀 Cosmic Explorer Bot")
st.write("Your personal guide to the wonders of our solar system, powered by NASA data.")

# Load the vector store using the cached function
vector_store = load_models()

# Initialize the LLM (Gemini)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest",
                             google_api_key=google_api_key,
                             temperature=0.3)

# Create the RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever()
)

# Get user input
user_question = st.text_input("Ask a question about any of our solar system's 8 planets:")

# When the user enters a question, run the RAG chain
if user_question:
    with st.spinner("Searching the cosmos for an answer..."):
        # Get the answer from the RAG chain
        result = qa_chain.run(user_question)
        st.write(result)