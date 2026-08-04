import sys
import subprocess
import platform


def install_package(package):
    subprocess.run([sys.executable, '-m', 'pip', 'install', package], check=True)


def main():
    system = platform.system()
    print(f"🖥️  OS: {system}")

    if system == 'Windows':
        print("📦 Install pygetwindow...")
        install_package('pygetwindow')

    elif system == 'Linux':
        print("📦 Install xdotool...")
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'xdotool'], check=False)
        print("If the installation fails, perform the following steps: sudo apt-get install xdotool")

    elif system == 'Darwin':  # macOS
        print("📦 macOS: no additional dependencies are required")

    print("✅ All dependencies are installed!")


if __name__ == "__main__":
    main()