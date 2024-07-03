"""Allow dxh_py to be executable through `python -m dxh_py`."""

from dxh_py.cli import main

if __name__ == "__main__":
    main(prog_name="dxh_py")
