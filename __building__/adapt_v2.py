from re import sub as replace, match

with open("6_glava.txt", "r", encoding="UTF-8") as file:

    strings = []

    places = 0

    mail = []

    page = ""

    lastcom = None
    label = ""

    for string in file:

        if string == "\n":
            continue

        # label = replace(r"(?:\+ ?(.*) ?\+)?.*", r"\1", string).strip()
        #
        # if label:
        #
        #     label = "\n    #+"+label+"+#"
        #
        #     strings.append(label)
        #
        #     continue

        if match(r"^\+.*\+", string):

            command, label = replace(r"\+. (.*) (.)\+", r"\2|\1", string).split("|")

            command = "me" if command == "m" else command

            if not lastcom:
                places = 0

                strings.append("    window hide dissolve\n")
                strings.append("    $ places = BooleanList(||places||)")
                strings.append("    jump .search\n\n")

                strings.append("label .search:\n")
                strings.append("    window hide dissolve\n")

                strings.append('    menu(screen="tfyl_choice"):\n')

            if lastcom == "?":

                strings.append("\n")

            elif lastcom == "me":

                strings.append(f"""            window hide dissolve # Сдвинуть куда надо

            play sound teleport fadein 2
            scene bg {label}
            hide screen tfyl_old_filter
            with fade2

            play ambience ambience_camp_center_night fadein 3

            pause 2

            play music evnening_25 fadein 4

            window show dissolve
""")

            strings.append('        "'+command+'" ((.5, .5)) if not places['+str(places)+"]: # + "+label.strip()+" +\n")

            strings.append('            $ places.set_true('+str(places)+")")
            strings.append('            window show dissolve\n')

            if command == "me":

                strings.append(f"""            window hide dissolve
            stop music fadeout 3
            play sound teleport
            $ renpy.pause (1)
            scene bg black
            show screen tfyl_old_filter
            with flash
            play music music_list["everyday_theme"]

            $ tfyl.day_time()
            play ambience ambience_camp_center_day fadein 4
            pause 1
            window show dissolve
""")


            places += 1

            lastcom = command


        elif match(r"! .* !", string):

            label = replace(r"^! (.*) !", r"\1", string)
            strings.append('label '+label.strip()+":\n")
            strings.append('    window show dissolve')

        elif "!mail" in string or mail:

            if "!mail" in string:
                mail.append("???")
                strings.append(("    "*2 if lastcom else "") + "    stop music fadeout 2")
                strings.append(("    "*2 if lastcom else "") + "    window hide dissolve")
                strings.append(("    "*2 if lastcom else "") + "    play music latter_25 fadein 1")

            elif "!page" in string:

                if page:
                    mail.append(page)

                    strings.append(("    "*2 if lastcom else "") + "    play sound list_open")
                    strings.append(("    "*2 if lastcom else "") + '    show screen tfyl_mail_in_hand("'+page+'")')
                    strings.append(("    "*2 if lastcom else "") + "    pause")

                page = ""

            elif "!closemail" in string:

                if page:
                    mail.append(page)
                    strings.append(("    "*2 if lastcom else "") + "    play sound list_open")
                    strings.append(("    "*2 if lastcom else "") + "    show screen tfyl_mail_in_hand(\""+page+"\")")
                    strings.append(("    "*2 if lastcom else "") + "    pause")

                strings.append(("    "*2 if lastcom else "") + "    show screen tfyl_mail_in_hand(\""+page+"\", remove=True)")

                strings.append(("    "*2 if lastcom else "") + "    $ tfyl.add_mail(\""+ mail[0]+'",')
                for page in mail[1:]:
                    strings.append(("    "*2 if lastcom else "") + '        "'+page+'",')
                strings.append(("    "*2 if lastcom else "") + ")")
                
                strings.append(("    "*2 if lastcom else "") + "    stop music fadeout 5")
                strings.append(("    "*2 if lastcom else "") + "    $ renpy.pause (2)")
                strings.append(("    "*2 if lastcom else "") + "    window show dissolve")

                page = ""

                mail.clear()

            else:


                string = string.strip()

                string = string.replace('\\"', '"')

                string = replace("^ ?-? ?", "", string)

                string = string.strip('"')

                string = string.replace("\n", "")

                string = string.replace("...", "…")

                string = replace(r'"(.*)"', r"«{i}\1{/i}»", string)

                string = replace("( [Ее]|Сем)е(н)?", r"\1ё\2", string)

                if string:

                    string = replace(r'([^.,!\?])$', r'\1.', string)

                    page += r"\n" if page else ""
                    page += string


        else:

            name = replace(r"(\?\?\?|[a-z]*).*", r"\1", string).strip()

            string = string.replace(name, "")

            name = '"???"' if name == "???" else name

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

                string = ("    "*2 if lastcom else "") + f'    {name+" " if name else ""}"'+string+'"' # "                "

                string = replace(r'([^.,!\?])"$', r'\1."', string)

            strings.append(string)

# raise Exception()

with open("take.rpy", "w", encoding="UTF-8") as file:

    for string in strings:

        file.write(string.replace("||places||", str(places))+"\n\n")
