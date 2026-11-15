import sys
from pathlib import Path

from streamlit.web import cli as stcli

BASE = Path(__file__).resolve().parent

if __name__ == "__main__":
    sys.argv = [
        "streamlit", "run", str(BASE / "main.py"),
        "--browser.gatherUsageStats=false",
        "--theme.base=light",
        "--theme.primaryColor=#025A95",
        "--theme.backgroundColor=#FFFFFF",
        "--theme.secondaryBackgroundColor=#EAF2F8",
        "--theme.textColor=#1B2A3A",
        "--theme.sidebar.backgroundColor=#025A95",
        "--theme.sidebar.secondaryBackgroundColor=#025A95",
        "--theme.sidebar.textColor=#FFFFFF",
    ]
    sys.exit(stcli.main())
