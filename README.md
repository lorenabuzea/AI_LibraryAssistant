# Smart Librarian — AI-Powered Book Recommendation Chatbot

**Smart Librarian** is a conversational AI chatbot that recommends books based on user interests using Retrieval-Augmented Generation (RAG), OpenAI GPT models, and custom tool calling for detailed summaries — all wrapped in a sleek Streamlit interface.

---

## Features

- 🤖 Natural language conversation powered by GPT-3.5 or GPT-4  
- 📚 Book recommendations using semantic search (ChromaDB + OpenAI embeddings)  
- 🛠️ Custom tool calling: `get_summary_by_title(title)`  
- 🎨 Streamlit-based UI with a friendly green gradient design  
- ✅ Fully local and lightweight — no database or backend setup required  

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/smart-librarian.git
cd smart-librarian
```

2. **Install dependencies**

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

Then install all required packages:

```bash
pip install -r requirements.txt
```

---

## Set Up Your OpenAI API Key

The application requires access to the OpenAI API. You must set your API key as an environment variable.

### On **Windows**:

```cmd
setx OPENAI_API_KEY "your-api-key-here"
```

Then restart your terminal or log out/log in for it to take effect.

### On **macOS/Linux**:

Add this line to your `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Then run:

```bash
source ~/.zshrc    # or the file you modified
```

---

## ▶ Running the App

Once your environment is ready and API key is set, launch the chatbot with:

```bash
py -m streamlit run ui/streamlit_ui.py
```

Or if you're on macOS/Linux and `py` is not available:

```bash
streamlit run ui/streamlit_ui.py
```

Your browser will open at: [http://localhost:8501](http://localhost:8501)

---

## How It Works

1. The user enters a natural language query like:
   > "I want a book about rebellion and dystopia"

2. The system performs semantic search over a curated list of book summaries using ChromaDB and OpenAI embeddings.

3. GPT recommends the most relevant book and automatically calls the tool:
   ```python
   get_summary_by_title("1984")
   ```

4. The full summary is displayed in a natural, conversational format.

---

## Book Data Format

The file `book_summaries.json` contains book entries like:

```json
{
  "title": "1984",
  "author": "George Orwell",
  "summary": "A dystopian novel about surveillance and totalitarian control..."
}
```

Ensure the dataset includes at least 10 book entries.

---

## Acknowledgements

Built with:

- [OpenAI API](https://platform.openai.com/)
- [ChromaDB](https://www.trychroma.com/)
- [Streamlit](https://streamlit.io/)

---

## 🛡 License

This project is open-source. Feel free to modify and extend it for educational or non-commercial use.
