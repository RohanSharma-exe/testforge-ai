# 🧪 TestForge AI

> **AI-Powered Software Testing Platform** built with **Python, Selenium, Pytest, Streamlit, and Google Gemini AI**.

TestForge AI combines modern UI automation with Generative AI to help QA Engineers automate testing, generate professional test cases, create bug reports, and visualize test execution from a single dashboard.

---

## ✨ Features

### 🔹 Automation Testing

- Selenium 4 UI Automation
- Pytest Test Framework
- Page Object Model (POM)
- Explicit Waits
- Parameterized Tests
- HTML Test Reports
- Automatic Failure Screenshots
- Structured Logging
- Cross-browser ready architecture

---

### 🔹 AI Features

- 🤖 AI Test Case Generator
- 🐞 AI Bug Report Generator
- Markdown Export
- Google Gemini Integration

---

### 🔹 Dashboard

- Streamlit Web Interface
- Run Automation Tests
- View Execution Results
- Download HTML Reports
- View Failure Screenshots
- AI Tools Integration

---

### 🔹 CI/CD

- GitHub Actions
- Ruff Code Formatting
- Automated Test Execution

---

# 📂 Project Structure

```
testforge-ai
│
├── ai/
│   ├── generator.py
│   ├── bug_report.py
│   ├── prompts.py
│   └── __init__.py
│
├── app/
│   └── dashboard.py
│
├── automation/
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   └── cart_page.py
│   │
│   └── tests/
│       ├── test_login.py
│       ├── test_inventory.py
│       └── test_cart.py
│
├── config/
│   └── settings.py
│
├── logs/
├── reports/
├── screenshots/
│
├── test_data/
│
├── utils/
│   ├── driver.py
│   ├── logger.py
│   ├── helpers.py
│   └── report.py
│
├── .github/
│   └── workflows/
│
├── README.md
├── pyproject.toml
├── pytest.ini
└── .env
```

---

# 🚀 Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python 3.13 |
| Automation | Selenium 4 |
| Framework | Pytest |
| Dashboard | Streamlit |
| AI | Google Gemini |
| Reports | pytest-html |
| Driver | webdriver-manager |
| Logging | Loguru |
| Environment | python-dotenv |
| CI/CD | GitHub Actions |
| Formatting | Ruff |

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/testforge-ai.git

cd testforge-ai
```

Install dependencies

```bash
uv sync
```

or

```bash
pip install -e .
```

---

# 🔑 Environment Variables

Create a `.env`

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶ Running the Dashboard

```bash
uv run streamlit run app/dashboard.py
```

---

# ▶ Running Tests

Run all tests

```bash
uv run pytest
```

Run Login Tests

```bash
uv run pytest automation/tests/test_login.py
```

Run Inventory Tests

```bash
uv run pytest automation/tests/test_inventory.py
```

Run Cart Tests

```bash
uv run pytest automation/tests/test_cart.py
```

---

# 📊 Dashboard

The Streamlit dashboard provides a unified interface for:

- Running automation suites
- Viewing execution status
- Downloading HTML reports
- Viewing failure screenshots
- Generating AI Test Cases
- Generating AI Bug Reports

---

# 🤖 AI Test Case Generator

Input

```
User should be able to login using username and password.
```

Output

- Functional Test Cases
- Positive Test Cases
- Negative Test Cases
- Boundary Tests
- Edge Cases
- Security Tests

---

# 🐞 AI Bug Report Generator

Input

```
Selenium Stack Trace

NoSuchElementException
```

Output

- Bug Title
- Summary
- Environment
- Steps to Reproduce
- Expected Result
- Actual Result
- Severity
- Priority
- Root Cause Analysis
- Suggested Fix

---

# 📈 Reports

After every execution

```
reports/report.html
```

is automatically generated.

---

# 📸 Failure Screenshots

Failed tests automatically capture screenshots.

```
screenshots/
```

---

# 📝 Logging

Execution logs are stored in

```
logs/testforge.log
```

---

# 🧪 Test Design

The framework follows the **Page Object Model (POM)** design pattern.

Benefits:

- Reusable page objects
- Low maintenance
- Cleaner tests
- Better scalability

---

# 📌 Current Features

- Selenium Automation
- Page Object Model
- Login Automation
- HTML Reports
- Failure Screenshots
- Streamlit Dashboard
- AI Test Case Generator
- AI Bug Report Generator

---

# 🔮 Planned Features

- API Testing
- Performance Testing
- Playwright Support
- Visual Regression Testing
- AI Test Script Generator
- AI Root Cause Analysis
- Email Notifications
- Slack Integration
- Docker Support
- Multi-browser Execution
- Parallel Testing
- Test Analytics Dashboard

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Rohan Sharma**

- Python Developer
- QA Automation Engineer
- AI & Agentic AI Enthusiast

GitHub: https://github.com/RohanSharma-exe

LinkedIn: https://www.linkedin.com/in/rohan-sharma-372ab2252

---

⭐ If you found this project useful, consider giving it a star.