import os
import dis
from subprocess import run, call




def find_imported_files(dir_path):
    # error_log = open('module_log.log','w')
    # dependency = open('requirment.txt','w')
   
    # file2 = open('python_modules.txt', 'r')
    # Lines = file1.readlines()
  
    count = 0
    # Strips the newline character
    try:
        module_txt = []
        path = dir_path
        print("module loading from path:",dir_path)
        cmd = 'pip install '

        for dirname, dirs, files in os.walk(path):
                for filename in files:
                    if filename.endswith(".py"):
                        os.chdir(dirname)
                        file_obj = open("{}".format(filename),'r',encoding="utf8")
                        
                        file_contant = file_obj.read()
                        instructions = dis.get_instructions(file_contant)
                        imports = [__ for __ in instructions if 'IMPORT' in __.opname]
                        for instr in imports:
                            if instr.opname == 'IMPORT_NAME':
                                if '.' in instr.argval:
                                    before,sep,after = instr.argval.partition('.')
                                    if before not in module_txt:
                                        module_txt.append(before)
                                else:
                                    if instr.argval not in module_txt:
                                        module_txt.append(instr.argval)
                                    

                            
                        
        set(module_txt)
        os.chdir(dir_path)
        print(module_txt)
        # dependency.writelines(module_txt)
        for mod_obj in module_txt:
            command_line = cmd + mod_obj
            run(command_line,shell=True)
    except Exception as e:
        
        print(e)
        
    
                

# folder = 'C:\\Users\\kaity\\Desktop\\mod_ability\\py_func_exercise\\git_hub_ui\\system_monitoring'
# find_imported_files(folder)
        
           