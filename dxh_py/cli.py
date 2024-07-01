import sys
from cookiecutter.main import cookiecutter

def main():
    if len(sys.argv) != 2:
        print("Usage: devxhub_python <template_url>")
        sys.exit(1)

    template_url = sys.argv[1]
    cookiecutter(template_url)

if __name__ == "__main__":
    main()
