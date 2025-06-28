
# 🧠 QA Chatbot with Ollama - LangChain & Streamlit

This is a simple QA Chatbot built using **LangChain**, **Streamlit**, and **Ollama** LLMs such as `gemma3:1b`, `llama3.2`, and `moondream`. The app allows users to ask natural language questions and get helpful responses from a locally hosted model.

---

## 🚀 Features

- Uses **LangChain**'s `ChatPromptTemplate` and `StrOutputParser`
- Runs in a **Streamlit** app for easy interaction
- Supports multiple Ollama models
- Adjustable **temperature** and **max_tokens** via sidebar
- Easy-to-understand modular code

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <project-directory>
```

### 2. Create `.env` File
```env
LANGCHAIN_API_KEY=your_langsmith_api_key
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 📦 Dependencies

- streamlit
- langchain
- python-dotenv
- langchain-community

Install using:
```bash
pip install streamlit langchain python-dotenv
```

---

## 🧠 Models Supported
- `gemma3:1b`
- `llama3.2`
- `moondream`

You can choose the model from the sidebar dropdown.

---

## 📸 UI Preview
- Sidebar for model selection and parameters
- Input box for user questions
- Output section with generated response

---

## 📌 Author

Shiba Sankar Sahu  
GenAI Engineer 🚀 | NLP | LangChain | Streamlit

---

## 📜 License

MIT License
