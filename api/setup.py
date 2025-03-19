import subprocess
import sys
import venv
from pathlib import Path

def setup_environment():
    api_dir = Path(__file__).parent
    venv_dir = api_dir / "venv"
    requirements_file = api_dir / "requirements.txt"

    # Create venv if it doesn't exist
    if not venv_dir.exists():
        print("Creating virtual environment...")
        venv.create(venv_dir, with_pip=True)

    # Determine pip path based on OS
    pip_path = venv_dir / ("Scripts" if sys.platform == "win32" else "bin") / "pip"
    
    # Install requirements
    print("Installing requirements...")
    subprocess.run([str(pip_path), "install", "-r", str(requirements_file)], check=True)
    
    print("Python environment setup complete! ✨")

if __name__ == "__main__":
    setup_environment() 