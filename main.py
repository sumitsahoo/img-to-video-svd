from dotenv import load_dotenv
from src.ui.svd_ui import SVDUI

# Launch the Gradio UI

if __name__ == "__main__":
    # Take environment variables from .env.
    load_dotenv()
    svd_ui = SVDUI()
    svd_ui.launch_ui()
