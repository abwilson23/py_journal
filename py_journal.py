import os.path
import subprocess
from shutil import copyfile
import datetime


# Finds monthly journal tex file in the journal directory.
def check_file(name):

    if not os.path.isfile(name):
        copyfile('template.tex', name)
    
def user_input(filename):
    
    header = ''
    if input("Header, (y)es or (n)o?") == 'y':
        header = input("Header: ")
    entry = input("Entry: ")

    add_entry(header, entry, filename)


# Add a new journal entry to the monthly journal
def add_entry(header, entry, filename):

    begin_env = "\\begin{entry}{\\today}{" + header + "}"
    end_env = "\\end{entry}\n\\end{document}"
    with open(filename, 'r+') as f:
        content = f.readlines()
        content[-1] = begin_env
        content.append(entry)
        content.append(end_env)
        f.seek(0)
        
        for line in content:
            f.write("%s" % line)
        f.truncate()
        compile_tex(filename)


# Returns the current month
def get_date():
    time = datetime.datetime.now()
    return time.strftime("%B%Y")


# Compiles the journal
def compile_tex(name):
    subprocess.check_call(['pdflatex', name])


if __name__ == "__main__":

    filename = str(get_date()) + ".tex"
    check_file(filename)
    user_input(filename)
    
