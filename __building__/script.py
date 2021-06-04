from re import sub as replace

with open("replace.rpy", "r", encoding="UTF-8") as file:

    strings = []

    for string in file:

        label = replace(r"(?:\+ ?(.*) ?\+)?.*", r"\1", string).strip()

        if label:

            label = "\n    #+"+label+"+#"

            strings.append(label)

            continue

        name = replace("([a-z]*).*", r"\1", string).strip()

        string = string.replace(name, "")

        string = string.strip()

        string = string.replace('\\"', '"')

        string = replace("^ ?-? ?", "", string)

        string = string.strip('"')

        # print(string.replace(str(name), ""))

        string = string.replace("\n", "")

        string = string.replace("...", "…")

        string = replace(r'(\?!|!\?|\?+|!+|[.…]) ', r"\1{w} ", string)



        string = replace(r'"(.*)"', r"«{i}\1{/i}»", string)

        string = replace("( [Ее]|Сем)е(н)?", r"\1ё\2", string)

        if string:

            string = f'    {name+" " if name else ""}"'+string+'"'

        strings.append(string)

# raise Exception()

with open("take.rpy", "w", encoding="UTF-8") as file:

    for string in strings:

        file.write(string+"\n")
