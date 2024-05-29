# To search for strings inside a file and folder. The .endswith() is used to run function.
# Here you passes the suffix of the string as an argument into the .endswith() and search

#searching strings

filename = input('Enter file name')
if filename.endswith('.txt'):
    print('that file is a text file')
elif filename.endswith('.py'):
    print('file is a python')
elif filename.endswith('.docx'):
    print('file is a word document')
elif filename.endswith('.pdf'):
    print('file is a PDF file')
elif filename.endswith('.ppt'):
    print('file is a powerpoint file')
elif filename.endswith('.image/Jpeg'):
    print('file is a Jpeg image')
elif filename.endswith('.excel'):
    print('file is a microsodt excel file')
elif filename.endswith('.pub'):
    print('file is a microsoft publisher file')
elif filename.endswith('.md'):
    print('file is a markdown structure file')
elif filename.endswith('.html'):
    print('file is a HTML document')
else:
    print('unknown file type!')