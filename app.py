"""This is the streamlit entry point"""

import sys
import os


import streamlit as st
from src.streamlitUI.main_page import homepage

# # Add the root directory to the sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# # Add the directory `src` containing python code
# sys.path.append(os.path.abspath("../src"))


def main():
    """Main function"""
    homepage()


if __name__ == "__main__":
    main()
