# 📚 PaperWhiz AI – Understand Research, Fast.

Welcome to **PaperWhiz AI**, your intelligent academic paper assistant that helps you **summarize, understand, and query** research papers in seconds. Whether you're a student, researcher, or curious learner, PaperWhiz AI saves you hours of reading and helps extract key insights instantly.

> ⚡ Built using **Google Gemini API** to power accurate, simplified, and contextual academic summaries and Q&A.

---

## 🚀 Key Features

- 🧠 **Smart Paper Summarization** – Get simplified summaries with core findings, methods, and objectives.
- ❓ **Ask Anything from the Paper** – Enter your own questions and get precise answers using Gemini AI.
- 🔍 **PDF Parsing Support** – Supports multi-page PDFs for full-paper comprehension.
- 🎓 **Explains Jargon in Plain Language** – Makes academic writing accessible to everyone.
- 📄 **Real-Time Streaming with Streamlit** – Fast, intuitive interface for seamless use.

---

## 🏆 Impact Metrics (Sample)

| Metric | Achievement |
|--------|-------------|
| 📄 Papers Processed | 500+ |
| ⏱️ Time Saved | Avg. 30+ min/paper |
| 🔁 Summarization Accuracy | 90%+ |
| 💬 Query Responses | 2000+ Questions Answered |

---

## 🖼️ Screenshots

| Upload PDF | Ask Questions | Paper Summary |
|------------|----------------|----------------|
| ![](https://github.com/pranavjoshi075/PaperWhiz-AI/blob/main/public/upload.jpg) | ![](https://github.com/pranavjoshi075/PaperWhiz-AI/blob/main/public/questions.jpg) | ![](https://github.com/pranavjoshi075/PaperWhiz-AI/blob/main/public/summary.jpg) |

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, PyMuPDF, dotenv
- **AI Model**: Google Gemini 1.5 Flash API
- **PDF Parsing**: `fitz` (PyMuPDF)

---

## 📦 Installation & Setup

```bash
# Clone the repo
git clone https://github.com/pranavjoshi075/PaperWhiz-AI.git
cd PaperWhiz-AI

# Install dependencies
pip install -r requirements.txt

# Add your Gemini API key in .env file
echo "GOOGLE_API_KEY=your-api-key" > .env

# Run the app
streamlit run app.py

# Open in browser
http://localhost:8501

# Demo Link
https://paperwhiz-ai-app.streamlit.app/
