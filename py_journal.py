import os.path as os
from shutil import copyfile
import datetime


# Finds monthly journal tex file in the journal directory.
def check_file(name):

    if not os.path.isfile(name):
        copyfile('template.tex', name + '.tex')
    
def user_input(filename):
    
    header = ''
    if input("Header, (y)es or (n)o?") == 'y':
        header = input("Header: ")
    entry = input("Entry: ")

    add_entry(header, filename)

# Add a new journal entry to the monthly journal
def add_entry(header, filename):

    begin_env = "\\begin{entry}{\\today}{" + title + "}"
    with open(filename) as f:
        content = f.readlines()

    

# Returns the current month
def get_date():
    time = datetime.date.now()
    return time.strftime("%B%Y")

if __name__ == "__main__":

    filename = get_date + '.tex'
    check_file(filename)
    user_input(filename)
    
