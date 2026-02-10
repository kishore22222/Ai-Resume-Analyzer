"""
Streamlit Cloud entry point for Smart Resume AI
This file is required by Streamlit Cloud as the default entry point
"""

from app import ResumeApp

if __name__ == "__main__":
    app = ResumeApp()
    app.main()
