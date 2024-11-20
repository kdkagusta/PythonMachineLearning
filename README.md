# Python Machine Learning


## Required
- OS Windows 11 64bit
- Python 3.13.0 [link](https://www.python.org/downloads/)
- Text Editor **Visual Code** [link](https://code.visualstudio.com/Download)
- Extention **Visual Code**
    - Python Extention [link](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - Pylance [link](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
    - Jupyter [link](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
    - Python Debugger [link](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Setup python
*Windows 10 / 11*
- Download & install python
- Setup environment
    - New System variable with 
        - Name : PY_HOME 
        - Value : [drive]:/Python
    - Add System Variable Path
        - %PY_HOME%\Python313\Scripts\
        - %PY_HOME%\Python313\
        - %PY_HOME%\Launcher\
    - New User Variable
        - Name : TCL_LIBRARY
        - Value : [drive]:\Python\Python313\tcl\tcl8.6
        - Name : TK_LIBRARY
        - Value : [drive]:\Python\Python313\tcl\tk8.6
- Update pip cmd `python -m pip install --upgrade pip`
- Check python version cmd `python --version`
- Check pip version cmd `pip -v`
- Running `python -m tkinter` from the command line should open a window demonstrating a simple Tk interface