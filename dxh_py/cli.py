import sys
from cookiecutter.main import cookiecutter

def main():
    if len(sys.argv) != 2:
        print("Usage: dxh_py <template_url>")
        sys.exit(1)

    template_url = sys.argv[1]
    try:
        cookiecutter(template_url)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
