import subprocess
import time
from pathlib import Path
import sys
import streamlit as st
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ai.generator import generate_test_cases
from ai.bug_report import generate_bug_report

# ------------------------------------------------------------------
# Paths
# ------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
REPORT_FILE = ROOT / "reports" / "report.html"
SCREENSHOT_DIR = ROOT / "screenshots"

# ------------------------------------------------------------------
# Page Config
# ------------------------------------------------------------------

st.set_page_config(
    page_title="TestForge AI",
    page_icon="🧪",
    layout="wide",
)

# ------------------------------------------------------------------
# Session State
# ------------------------------------------------------------------

if "generated_test_cases" not in st.session_state:
    st.session_state.generated_test_cases = ""

if "generated_bug_report" not in st.session_state:
    st.session_state.generated_bug_report = ""

# ------------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------------

with st.sidebar:

    st.title("🧪 TestForge AI")

    st.markdown("---")

    st.subheader("Framework")

    st.success("Python 3.13")
    st.success("Selenium 4")
    st.success("Pytest")
    st.success("Streamlit")
    st.success("Gemini AI")
    st.success("GitHub Actions")

    st.markdown("---")

    st.subheader("Project")

    st.write("Version : 1.0")

    st.write("Status : Development")

    st.markdown("---")

    st.caption("Built using Python + Selenium + AI")

# ------------------------------------------------------------------
# Header
# ------------------------------------------------------------------

st.title("🧪 TestForge AI")

st.write(
    """
AI-Powered Software Testing Platform

Run Selenium automation tests, view reports,
inspect screenshots and generate AI-assisted QA assets.
"""
)

st.divider()

# ------------------------------------------------------------------
# Layout
# ------------------------------------------------------------------

left, right = st.columns([2, 1])

# ==================================================================
# LEFT COLUMN
# ==================================================================

with left:

    st.subheader("Automation")

    website = st.text_input(
        "Application URL",
        value="https://www.saucedemo.com/",
    )

    test_suite = st.selectbox(
        "Select Test Suite",
        [
            "Login Tests",
            "Inventory Tests",
            "Cart Tests",
        ],
    )

    test_mapping = {
        "Login Tests": "automation/tests/test_login.py",
        "Inventory Tests": "automation/tests/test_inventory.py",
        "Cart Tests": "automation/tests/test_cart.py",
    }

    if st.button(
        "▶ Run Test",
        use_container_width=True,
        type="primary",
    ):

        selected_test = test_mapping[test_suite]

        start_time = time.time()

        with st.spinner("Running Tests..."):

            result = subprocess.run(
                [
                    "uv",
                    "run",
                    "pytest",
                    selected_test,
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )

        execution_time = round(time.time() - start_time, 2)

        st.divider()

        if result.returncode == 0:

            st.success("✅ All Tests Passed")

        else:

            st.error("❌ Some Tests Failed")

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "Execution Time",
                f"{execution_time} sec",
            )

        with c2:
            st.metric(
                "Exit Code",
                result.returncode,
            )

        st.divider()

        with st.expander(
            "Console Output",
            expanded=False,
        ):

            st.code(result.stdout)

            if result.stderr:

                st.code(result.stderr)

# ==================================================================
# RIGHT COLUMN
# ==================================================================

with right:

    st.subheader("Reports")

    if REPORT_FILE.exists():

        with open(REPORT_FILE, "rb") as report:

            st.download_button(
                "📄 Download HTML Report",
                report,
                file_name="report.html",
                mime="text/html",
                use_container_width=True,
            )

    else:

        st.info("No report generated yet.")

    st.divider()

    st.subheader("Latest Failure Screenshot")

    screenshots = sorted(
        SCREENSHOT_DIR.glob("*.png"),
        reverse=True,
    )

    if screenshots:

        latest = screenshots[0]

        image = Image.open(latest)

        st.image(
            image,
            caption=latest.name,
            use_container_width=True,
        )

    else:

        st.info("No screenshots found.")

# ================================================================
# AI SECTION
# ================================================================

# ================================================================
# AI ASSISTANT
# ================================================================

st.divider()

st.header("🤖 AI Assistant")

tab1, tab2 = st.tabs(
    [
        "📝 Test Case Generator",
        "🐞 Bug Report Generator",
    ]
)

# ================================================================
# TEST CASE GENERATOR
# ================================================================

with tab1:

    st.subheader("Generate Software Test Cases")

    requirement = st.text_area(
        "Requirement",
        placeholder=(
            "Example:\n"
            "User should be able to login using username and password."
        ),
        height=180,
    )

    generate_tc = st.button(
        "🚀 Generate Test Cases",
        use_container_width=True,
    )

    if generate_tc:

        if not requirement.strip():

            st.warning("Please enter a software requirement.")

        else:

            try:

                with st.spinner(
                    "Generating test cases using Gemini..."
                ):

                    output = generate_test_cases(requirement)

                st.session_state.generated_test_cases = output

                st.success("Test Cases Generated Successfully")

            except Exception as e:

                st.error(f"Generation Failed\n\n{e}")

    if st.session_state.generated_test_cases:

        st.markdown("---")

        st.markdown(
            st.session_state.generated_test_cases
        )

        st.download_button(
            "⬇ Download Test Cases",
            data=st.session_state.generated_test_cases,
            file_name="test_cases.md",
            mime="text/markdown",
            use_container_width=True,
        )


# ================================================================
# BUG REPORT GENERATOR
# ================================================================

with tab2:

    st.subheader("Generate AI Bug Report")

    application = st.text_input(
        "Application Name",
        value="SauceDemo",
    )

    environment = st.text_input(
        "Environment",
        value="QA",
    )

    browser = st.text_input(
        "Browser",
        value="Chrome",
    )

    error = st.text_area(
        "Paste Error / Stack Trace",
        placeholder="Paste Selenium error or stack trace here...",
        height=220,
    )

    generate_bug = st.button(
        "🐞 Generate Bug Report",
        use_container_width=True,
    )

    if generate_bug:

        if not error.strip():

            st.warning("Please enter an error or stack trace.")

        else:

            try:

                with st.spinner(
                    "Generating Bug Report..."
                ):

                    report = generate_bug_report(
                        application=application,
                        error=f"""
Environment: {environment}

Browser: {browser}

Error:

{error}
""",
                    )

                st.session_state.generated_bug_report = report

                st.success("Bug Report Generated Successfully")

            except Exception as e:

                st.error(f"Generation Failed\n\n{e}")

    if st.session_state.generated_bug_report:

        st.markdown("---")

        st.markdown(
            st.session_state.generated_bug_report
        )

        st.download_button(
            "⬇ Download Bug Report",
            data=st.session_state.generated_bug_report,
            file_name="bug_report.md",
            mime="text/markdown",
            use_container_width=True,
        )

# ------------------------------------------------------------------
# Footer
# ------------------------------------------------------------------

st.divider()

st.caption(
    "TestForge AI • Version 1.0 • Powered by Python, Selenium, Pytest, Streamlit & Gemini AI"
)