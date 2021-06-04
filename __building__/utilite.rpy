init:

    python:

        def get_mouse_pos(ob_pos=None):

            m = renpy.get_mouse_pos()

            m = round(m[0]/1920.0, 3), round(m[1]/1080.0, 3)

            if ob_pos:
                ob_pos[1] = m

            return m
        def copy_mouse_pos(ob_pos=None):

            m = get_mouse_pos(ob_pos)

            pygame.scrap.put(pygame.SCRAP_TEXT, str(m).encode("utf-8"))

            # return m

    screen tfyl_utilite():


        default musics = False
        default ob_pos = [None, (.5, .5)]

        default imagebutton_sprites = {"?": "mods/tfyl/gui/interactive/q_idle.png", "!": "mods/tfyl/gui/interactive/em_idle.png", "me": "mods/tfyl/gui/interactive/message_idle.png", "ar": "mods/tfyl/gui/interactive/ar_idle.png", None: Null()}

        key "p" action Function(copy_mouse_pos, ob_pos)
        key "m" action SetScreenVariable("musics", not musics)

        key "," action SetScreenVariable("ob_pos", ["me", ob_pos[1]])
        key "." action SetScreenVariable("ob_pos", ["!", ob_pos[1]])
        key "/" action SetScreenVariable("ob_pos", ["?", ob_pos[1]])
        key "\\" action SetScreenVariable("ob_pos", [None, ob_pos[1]])

        add imagebutton_sprites[ob_pos[0]] align ob_pos[1]

        text "utilite on"

        showif musics:

            frame:
                align (.5, .5)

                viewport:
                    area (0, 0, 800, 600)
                    mousewheel True

                    vbox:
                        for i in music_list:

                            hbox:
                                spacing 20
                                textbutton "Copy" style "log_button" text_style "settings_text" action Function(pygame.scrap.put, pygame.SCRAP_TEXT, 'play music music_list["'+i+'"] fadein 3'.encode("utf-8"))
                                textbutton i style "log_button" text_style "settings_text" action Play("music", music_list[i])
