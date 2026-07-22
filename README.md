# 📄 Job Description Summarizer

An AI-powered **Job Description Summarizer** built using **Python, LangChain, Google Gemini, and Streamlit**. This application transforms lengthy job descriptions into concise, professional summaries, making it easier for recruiters, job seekers, and HR professionals to quickly understand a role.

---

## 🚀 Features

- Summarizes lengthy Job Descriptions into concise overviews
- AI-powered summarization using **Google Gemini**
- Built with **LangChain Prompt Templates**
- Clean and interactive **Streamlit** user interface
- Highlights:
  - Job Role
  - Responsibilities
  - Required Skills
  - Experience
  - Location
- Fast and easy to use

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- Prompt Engineering
- python-dotenv

---

## 📂 Project Structure

```
job-description-summarizer/
│── app.py                 # Streamlit UI
│── main.py                # Console version
│── requirements.txt
│── .env                   # API Key (not uploaded)
│── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/job-description-summarizer.git
cd job-description-summarizer
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key_here
```

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🖥️ Console Version

Run the terminal version:

```bash
python main.py
```

---

## 📸 Sample Input

```
Job Title: React.js Developer

Company: TechNova Solutions Pvt. Ltd.

Location: Pune, Maharashtra (Hybrid)

Experience: 2–4 Years

Responsibilities:
- Develop React applications
- Build reusable UI components
- Integrate REST APIs
- Work with UI/UX designers

Required Skills:
- React.js
- JavaScript
- HTML/CSS
- Git
- SQL
```

---

## 📄 Sample Output

```
TechNova Solutions is hiring a React.js Developer for a full-time hybrid role in Pune. The position requires 2–4 years of experience in developing responsive React applications, integrating REST APIs, and collaborating with UI/UX designers. Candidates should have strong skills in React.js, JavaScript, HTML, CSS, Git, and SQL. The ideal applicant is passionate about building modern web applications and working in an Agile development environment.
```

---

## 📦 Requirements

- Python 3.10+
- Google Gemini API Key

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🎯 Future Enhancements

- PDF Job Description Upload
- DOCX File Upload
- Batch Summarization
- Download Summary as PDF
- Multiple Summary Styles
- Skill Extraction
- ATS Keyword Extraction
- Job Match Score

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your fork.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by **Harsh Malap**.

If you found this project helpful, consider giving it a ⭐ on GitHub.