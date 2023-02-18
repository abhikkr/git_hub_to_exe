import os
from subprocess import PIPE, run
import platform
import re
from module_loader import *
import pathlib
import sys


def git_repo(link):
    os.system('git clone {} git_dir'.format(link))


def check_sys_os():
    sys_os = platform.platform().lower()
    # print(sys_os)
    os_regex = r"(?:windows)|(?:linux)|(?:mac)"
    sys_platform = re.findall(os_regex,sys_os)
    sys_platform = ''.join(sys_platform)
    print("system platform:",sys_platform)
    print('\n')
    return sys_platform
    
def module_load(path):
    filename = 'requirements.txt'
    # dir_path = os.getcwd()
    for dirname, dirs, files in os.walk(path):
        if filename in files:
            command = 'pip install -r requirements.txt'
            if check_sys_os == 'windows':
                        result = run(command)
                        print(result)
            if check_sys_os == 'linux':
                         result = run(command,shell=True)
                         print(result)
            return True
            break
        else:
            return False

def check_modules(dir):
    if module_load(dir):
        print("requirments.txt is present")
    else:
        find_imported_files(dir)





def find_files(main_file_name):
    # dir_path = dir_path.replace("\\","/")
    command_line = 'python3 -m PyInstaller '
    present_dir = os.getcwd()
    # check_modules(present_dir)
    print("Present working directory:>",present_dir)
    # file_name = input("enter the main file name:")
    # cwd = dir_path
    # os.chdir(dir_path)
    main_dir_obj = os.scandir()
    # for obj in main_dir_obj:
        # print(obj)
        # if obj.is_file() and obj.name.endswith('.py'):
        #     run(command_line + obj.name)
        #     print('\n')
        #     print("\n::::::::::::::::::::::exec file name ::::::::::",obj.name)
        #     print('\n')
        # if obj.is_dir():
        #     print(f"directory in current directory:",obj.name)
        #     dir_in_pwd = obj.path
        #     compile_programe(dir_in_pwd,cwd)
    for dirname, dirs, files in os.walk(present_dir):
        if main_file_name in files:
            print("\n :::::main file directory::::\n",dirname)
            check_modules(dirname)
            os.chdir(dirname)
            if main_file_name in files:
                run(command_line + main_file_name,shell=True)


def compile_programe(path,cwd):
    command_line = 'python -m nuitka '
    dir = path
    # print(os.getcwd())
    os.chdir(dir)
    # print(os.getcwd())
    dir_objs = os.scandir()
    for value in dir_objs:
                # print(f"{obj.name} objects:",value.name)
                if value.name.endswith('.py'):
                    print("Python file name in {}::::".format(dir),value.name)
                    comand = command_line + value.name
                    # result = run(comand, stdout=PIPE, stdin=PIPE, universal_newlines=True)
                    sys_os= check_sys_os()
                    if  sys_os == 'windows':
                        result = run(comand)
                        print(result)
                    if sys_os == 'linux':
                         result = run(comand,shell=True)
                         print(result)
    os.chdir(cwd)







# find_files()