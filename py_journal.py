import os.path as os
from shutil import copyfile
import datetime


# Finds monthly journal tex file in the journal directory.
def check_file(name):

    if not os.path.isfile(name):
        copyfile('template.tex', name + '.tex')
    
# If no such file is found, create a new one for the current month. 
# Should only do this at the beginning of each month, or the first
# time that a journal entry is added in a new month.
def create_new_file(): 


# Add a new journal entry to the monthly journal
def add_entry(header, f):

    begin_env = "\\begin{entry}{\\today}{" + title + "}"

# Returns the current month
def get_date():
    time = datetime.date.now()
    return time.strftime("%B%Y")

if __name__ == "__main__":

    cur_name = get_date + '.tex'
    check_file(cur_name)

    with open(cur_name) as f:

    
    
