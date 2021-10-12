import cx_Freeze

executables = [cx_Freeze.Executable ( "main.py" )] 

cx_Freeze.setup ( 
   name = "8-puzzle" , 
   options = { "build_exe" : { "packages" : [ "pygame", "pygame_gui" ],
                              "include_files" : [ "logo.png", "FiraCode-Retina.ttf", "theme.json", "matrix.py", "puzzle.py", "colors.py"]}}, 
   executables = executables
)