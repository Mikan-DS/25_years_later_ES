import re

with open("replace.rpy", encoding="UTF-8") as file:
    newfile = []
    for i in file:
        i = re.sub(r"'(.*)'", r'"\1"', i)
        i = i.replace(' "', '"')
        i = i.replace("{w}", "")
        # i = re.sub(r'"{font=.*}(.*){/font}"', r'"\1"', i)
        i = i.replace("...", "…")
        i = re.sub(r'(\?!|!\?|\?+|!+|[.…])([^"])', r"\1{w}\2", i)

        i = re.sub(r"(persistent|renpy|tfyl|\d)\.{w}", r"\1.", i)

        i = re.sub(r"window (hide|show)", r"window \1 dissolve", i)

        i = i.replace('{w} "', '"')

        i = re.sub(r"\$ ?_window_(hide|show)\(dissolve\)", r"window \1 dissolve", i)

        i = i.replace('   "', '    "')
        newfile.append(i)


with open("take.rpy", "w", encoding="UTF-8") as file:
    file.write("".join(newfile))
