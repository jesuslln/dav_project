#from .utils import print_tree
import os

def print_py_files(dir_path, indent=''):
    with os.scandir(dir_path) as entries:
        for entry in entries:
            if entry.is_dir():
                print(f"{indent}[{entry.name}]")
                print_py_files(entry.path, indent + '  ')
            elif entry.is_file() and entry.name.endswith('.py'):
                print(f"{indent}{entry.name}")


project_path = r"C:\Users\jesus\Desktop\Curso 5\Cuatri I\DAV\dav_project"
print(f"Project Structure for {project_path}")
print_py_files(project_path)