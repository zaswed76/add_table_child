import fileinput
import glob
import os


def get_style(direct):
    lst_files = []
    for filename in glob.glob(os.path.join(direct, '*.css')):
        lst_files.append(filename)
    css_lines = []
    for line in fileinput.input(lst_files):
        css_lines.append(line.strip())
    return "\n".join(css_lines)