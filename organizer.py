import re, shutil
from os import listdir, rename, chdir
from os.path import join, isfile, splitext


dirpath = '/Volumes/DATA/_Ebook'
dirpath_pdf = '/Volumes/DATA/_Ebook/_pdf'
dirpath_mobi = '/Volumes/DATA/_Ebook/_mobi'
dirpath_epub = '/Volumes/DATA/_Ebook/_epub'

#change directory
chdir(dirpath)
allcontent = listdir(dirpath)
onlyfiles = [files for files in allcontent if (isfile(join(dirpath, files)) and not files.startswith('.'))]
#for i in onlyfiles:
#    print(i)

#clean name formatting e.g. [Leona_Haas,_Mark_Hunziker]_Building_Blocks_of_Per(BookZZ.org) --> title - author
authRegex = re.compile('(\[.+\])') #take words starting with capitals, inside bracket
titleRegex = re.compile('[^(\[.\])]+(?=\(.*\))') #take words outside bracket and before parenthesis
clean = re.compile("([^[\]_.'-,]+)") #clean special chars

for j in [j for j in onlyfiles if j.startswith('[')]:
    filename, extension = splitext(j)[0], splitext(j)[1]
    auth = authRegex.findall(filename)
    if auth != []:
        auth = clean.findall(auth[0])
        auth = ' '.join(auth)
    else:
        auth = ''
    title = titleRegex.findall(filename)
    if title != []:
        title = clean.findall(title[0])
        title = ' '.join(title)
    else:
        title = ''
    new_filename = ' - '.join([title,auth])
    print('old filename : ', j)
    rename(j, new_filename + extension)
    print('new filename : ', new_filename + extension)

#move files to folder by filetype
for i in onlyfiles:
    if i.endswith('.pdf'):
        shutil.move(join(dirpath, i), join(dirpath_pdf, i))
    elif i.endswith('.epub'):
        shutil.move(join(dirpath, i), join(dirpath_epub, i))
    elif i.endswith('.mobi'):
        shutil.move(join(dirpath, i), join(dirpath_mobi, i))