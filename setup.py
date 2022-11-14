from cx_Freeze import setup, Executable
import os 

os.environ['TCL_LIBRARY'] = r'C:\Users\Thiago\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Thiago\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

setup( name = "Space Battle" , version = "1.0" , description = "An awesome space game!" , executables = [Executable("Game.py", base="Win32GUI")]) 