# 🚀 Cosmic Explorer Bot 🪐

Welcome to the Cosmic Explorer Bot! This is an interactive web application that acts as your personal guide to the wonders of our solar system. Ask it any question about the eight planets, and it will provide answers based directly on factual information from NASA.

This project is built using a Retrieval-Augmented Generation (RAG) model, ensuring that the answers are accurate and free from AI hallucinations. The bot's knowledge is strictly limited to the NASA fact sheets it was trained on.

**[Link to your live Streamlit App]** &lt;-- *Don't forget to add the link to your live app here!*



---

## ## Features

* **Interactive Q&A Interface:** Ask questions in plain English through a user-friendly web UI.
* **Accurate, Fact-Based Answers:** All responses are generated based on a curated knowledge base of NASA documents.
* **No Hallucinations:** The model is instructed to state when it doesn't know an answer, rather than making one up.
* **Powered by RAG:** Leverages the power of Large Language Models (LLMs) combined with a local vector store for high-quality, context-aware responses.

---

## ## Technical Stack

* **Language:** Python
* **Core Libraries:**
    * `LangChain`: The framework for building the RAG application.
    * `Gemini (Google AI)`: The Large Language Model used for generating answers.
    * `FAISS`: Powers the efficient, local vector store for document retrieval.
    * `SentenceTransformers`: Used to create the text embeddings.
* **UI and Deployment:**
    * `Streamlit`: For building and serving the interactive web application.
    * `Streamlit Community Cloud / Hugging Face Spaces`: For free, continuous deployment.

---

## ## How to Run This Project Locally

To run the Cosmic Explorer Bot on your own machine, follow these steps:

### ### Prerequisites

* Python 3.9+
* A Google AI (Gemini) API Key

### ### Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone [your-github-repository-url]
    cd cosmic-bot-app
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Your API Key:**
    * Create a folder named `.streamlit` in the project directory.
    * Inside `.streamlit`, create a file named `secrets.toml`.
    * Add your API key to the `secrets.toml` file in the following format:
        ```toml
        GOOGLE_API_KEY = "your_actual_api_key_here"
        ```

5.  **Run the App:**
    ```bash
    streamlit run app.py
    ```
    Your browser should automatically open to the app's local address.

---

## ## Acknowledgements

A huge thanks to NASA for providing the comprehensive and fascinating fact sheets that form the knowledge base for this bot.
