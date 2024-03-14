import webbrowser

def browser(url):
    webbrowser.open(url, new=0, autoraise=True)

def printf(contents):
    import numpy as np
    print(contents)