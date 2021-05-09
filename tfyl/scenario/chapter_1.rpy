# -*- coding: utf-8 -*-
label tfyl_chapter_1:

    stop music fadeout 3

    call .loads

    show black

    jump tfyl_gates

label .loads: # Все необходимое для первой главы

    $ tfyl = ModeStore()
    show screen tfyl_diary

    return

label tfyl_gates:

    show screen tfyl_backdrop(1, "Искра", "images/bg/ext_clubs_day.jpg", im.Composite((900,1080), (0,0), "images/sprites/normal/el/el_1_body.png",(0,0), "images/sprites/normal/el/el_1_pioneer.png",(0,0), "images/sprites/normal/el/el_1_normal.png"), im.Composite((900,1080), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png") ) with fade
    scene bg tfyl_road
    $ save_name = '25 лет спустя.\nГлава 1. Искра'
    $ renpy.pause (6)
    hide screen tfyl_backdrop

    play music dark_music_25 fadein 3
    $ renpy.pause (1)
    window show dissolve



    "Никогда бы не подумал что вернусь сюда.{w} Особенно с такой целью.{w} В голове ещё не могли уложиться те письма, а буря старых воспоминаний сильно нагружала голову."
    "Пространство расплывалось.{w} Оно было не интересно.{w} Только ближе к лагерю я стал замечать."
    "Потресканный асфальт давно не видал резины автомобилей, что ж говорить о ноге человека."
    "А бесконечные поля, они не изменились."
    "Безграничные, свободные.{w} Цивилизация не тронула их."
    "Единственное что было, так это ЛЭП, передачи которой шли в лагерь.{w} Те, проржавевшие и охваченные природой, лишь подтверждали мои мысли."
    "Мысли о том, что стало с лагерем за это время."
    window hide dissolve
    $ renpy.pause (1)
    scene bg tfyl_gates
    with fade
    window show dissolve
    "Пеший маршрут подходил к концу.{w} Издали показались парковка и ворота лагеря."
    "Сколько я не бывал, но именно этот вид встречал пионеров, счастливых из-за конца длительного маршрута."
    "Последовательно счастье перерастало в нечто большее.{w} Юнцы начинали беситься, а кто по старше - активно обсуждать планы.{w} В те мгновения салон преображался."
    "Как помню: В первую смену я прижался к вожатой и без конца задавал вопросы.{w} Только что именно?{w} Вряд ли скажу.{w} Хоть убей."
    "Момент истины наступил, когда я вплотную подошёл к этим скрипучим воротам.{w} Их плачевное состояние ударило прямо в глаза."
    "Стены исписаны, бордюров не хватает, а асфальт: местами вырванный, местами провалившийся.{w} Казалось, прошло куда больше времени, чем есть на самом деле."

    window hide dissolve


    $ places = BooleanList(4)

    jump .search


    pause

    jump tfyl_clubs # Игрок не может сюда попасть, но если попадет - его аккуратно перенесут на следующий экран

label .search:

    menu (screen="tfyl_choice"):

        "?" ((.09, .74)) if not places[0]:
            $ places.set_true(0)

            window show dissolve
            "Каждая смена оставляла свой след на этой кирпичной кладке.{w} Говорили - это к счастью."
            "То происходило перед отъездом.{w} Писали год,{w=.5} смену.{w} Отъявленные же оставляли свой росчерк и рисунки."
            "Правда, те особо не расходились.{w} Один кирпичик на одну смену, не более."
            "И таких кирпичиков - тьма.{w} С десяток метров, если не ошибаюсь.{w} Сколько пионеров вырастил Совёнок…"
            "Внезапно, я загорелся желанием найти свою смену.{w}Только нашел совсем другое."
            "1983.{w} Июль.{w} Лена."
            window hide dissolve

        "?" ((.5, .24)) if not places[1]:
            $ places.set_true(1)

            window show dissolve
            "По одному случаю лагерь изменил название на \"Совок\".{w} Две буквы пропали в ночи и сколько не искали - не нашли."
            "Чья-то шутка, сельчан или самих пионеров, разошлась по лагерю и каждый хотел поглазеть.{w} Смех-смехом, а недоразумение серьезное."
            "Поиски ничего не дали.{w} Недоразумение подправили через неделю, когда подвезли новые буквы прямиком с завода."
            window hide dissolve

        "?" ((.95, .75)) if not places[2]:
            $ places.set_true(2)

            window show dissolve
            "Заросшая тропа вела на север.{w} Там, в конце пути, стоял заброшенный лагерь."
            "Вожатая рассказывала, что до времен Совёнка тот процветал, да и был не простым."
            "Снаружи - милые домики и личики, внутри - лабиринт темных, сырых коридоров."
            "Сами гости не знали о них, лишь из-за пары трагедий объект рассекретили."
            "Забросили.{w} Соответственно лагерь потерял смысл в маскировке и был оставлен.{w} "
            "Спустя время территорию оцепили:{w} установили колючку, ветимы, и посадили пару караульных с псами.{w} И те меры были недолгими."
            "Ветхие конструкции начали заваливаться, а коридоры проседать под толщей земли.{w} Некогда огромная сеть, превратилась в парочку проходов и комнат.{w} Остальное завалило."
            "Такая история породила массу слухов{w}, мол, духи буянят, что лагерь приютил в себе неупокоенные души, и всякое."
            "Но как бы оно не было - лагерь все равно наводил ужас.{w} Даже сейчас."
            window hide dissolve

        "me" ((.11, .32)) if places[:-1] and not places[3]:
            $ places.set_true(3)

            window show dissolve
            "Именно здесь пионеры прощались с лагерем и между собой, ведь была вероятность, что посадят в разные автобусы."
            "Здесь ребят строили, пересчитывали, и напоследок одаривали напутственным словом.{w} Среди тех была Ольга Дмитриевна.{w} Вожатая нашего отряда."
            "Каждый раз и со слезами.{w} Она к нам привыкла, даже несмотря на все её слова…"

            window hide dissolve
            stop music fadeout 3
            play sound teleport
            $ renpy.pause (1)
            scene ext_camp_entrance_day
            show screen tfyl_old_filter
            with flash
            play music music_list["lets_be_friends"] fadein 3
            window show dissolve

            "…Автобусы стояли ровными рядами, смирно ожидая пионеров.{w} Скоро они пробудятся, потому что последнее построение подошло к концу."
            "Мы стояли на отшибе, где было не так громко, да и личного пространства куда больше.{w} И вот, оставалось пять минут до разлуки."

            show dv laugh pioneer at fleft
            with dissolve

            dv "Ребят, как всегда все потрясающе.{w} Увидимся следующем летом?"

            show mi cry pioneer at left
            with dissolve

            mi "Обязательно!!!{w} Как я без вас?!"
            "Слезы обычное дело, особенно при таком моменте.{w} Мику не выдержала и её глазки выпустили целый град, успокоить который решилась сама Алиса."

            show sl normal pioneer at cleft
            with dissolve

            sl "Мику.{w} Мы уже сколько смен и все в одном отряде.{w} Вот увидишь, мы опять будем вместе!"

            show us laugh pioneer at right
            with dissolve

            us "Пожалуй, присоединюсь.{w} А, Семён?{w} А тебе есть что сказать?{w} Засранец."
            "Ульяна стояла ко мне ближе всех и, найдя удачный момент, подтолкнула своим плечом.{w} Намекнула, что не время бездействовать."
            "Пока Славяна и Лена бросились успокаивать Мику, я собрался с силами и присоединился к ним."

            show dv normal pioneer at fleft
            with dissolve

            dv "Все-все.{w} Я тебя навещу, как только смогу.{w} Обещаю."

            show mi sad pioneer at left
            with dissolve

            mi "Правда?{w} "
            dv "Да.{w} "
            "Мику более или менее пришла в норму.{w} Мы выпустили её из объятий, но она все равно пыталась быть ближе.{w} Пыталась насладиться этим мгновением."
            "После этого внимание переключилось на Лену.{w} Она максимально старалась показать, что безмятежна,{w} однако красные глазки показали всю истину."

            window hide dissolve
            hide dv
            hide mi
            hide sl
            hide us
            with dissolve
            $ renpy.pause (0.5)
            show un sad pioneer at center
            with dissolve
            window show dissolve

            "Пока четверка отвлеклась разговорами, я быстренько переметнулся к Лене.{w} Она дернулась, попыталась закрыть лицо руками, но я не позволил."
            me "Лена.{w} Не забывай слова Алисы.{w} Мы ещё встретимся, здесь же."
            un "Я-я слышала…{w} А если что-то произойдет?{w} Вдруг я или т-ты{cps=3}?...{/cps}"

            show un cry pioneer at center
            with dissolve

            "Зажмурив глаза, Лена пыталась сдержать слезы.{w} Но они, одна за другой, начали скатываться по щекам.{w} В конце Лена не выдержала и снова открылась."
            "В этих каплях я видел свое отражение.{w} Настолько они чистые, где сдерживались истинные чувства."
            "Я не хотел отпускать.{w} Правда, иначе никак.{w} Подождать бы чуток, когда окрепну и смогу приехать."
            "Придет тот момент, когда преграда в сотни километров рухнет!"
            me "Ничего не случится.{w} Я о тебе все знаю.{w} Если что, я тебя найду или напишу."
            show un sad pioneer at center
            with dissolve
            un "С-смотри мне.{w} Приедь сюда в 83, ты меня понял?!"
            me "Понял, Лен."
            "Лена достала платочек и начала приводить себя в порядок.{w} Иногда я замечал улыбку, которая мимолётно проскакивала."
            show sh normal_smile pioneer at right
            with dissolve
            "Через секунду всех нас окрикнул Шурик.{w} За ним еле-еле плелся Эл, который тянул два чемодана."
            sh "Нас забыли.{w} Посмотрите как Эл устал, он ведь хотел повидаться."
            sl "Так а чего ты не помог ему?"
            show un normal pioneer at center
            with dissolve
            show sh serious pioneer at right
            with dissolve
            sh "А вот нечего спорить и проигрывать.{w} Сам себя наказал."
            "Уставший сбросил чемоданы.{w} На них же присел и начал освежать себя газетой."
            "Славяна присела рядом она явно была обеспокоена его состоянием."
            show mi smile pioneer at left
            with dissolve
            mi "А чего внутри?"
            sh "Куча бумаг.{w} Твоя тонкая душевная организация не поймет…{w} По правде я сам в них ещё не разобрался."
            show mi sad pioneer at left
            with dissolve
            mi "Оу-у.{w} Поняла."
            "Кто-то крикнул, что отправка через пару минут.{w} Наш небольшой отряд сразу взбодрился и снова замкнулся в круг."
            window hide dissolve
            show dv laugh pioneer at fleft
            with dissolve
            dv "Так, пока не забыла.{w} Я очень рада, что это лето я провела рядом с вами.{w} Встречаемся тут, как в общем-то всегда."
            show sl smile pioneer at cleft
            with dissolve
            sl "Спасибо, Алис.{w} С вами было очень круто."
            show un smile pioneer at center
            with dissolve
            un "Я вас всех люблю!{w} Давайте вернёмся целыми и здоровыми."
            window hide dissolve
            hide sh
            with dissolve
            $ renpy.pause (0.2)
            show mt normal pioneer panama at fright
            with dissolve
            mt "{b}Стойте{/b}!!!"
            "Ольга Дмитриевна внезапно появилась из-за ворот и подбежала к нам.{w} Её руки держали фотоаппарат и небольшой, чёрный пакетик."
            mt "Встаньте в одну линию.{w} Ещё есть время!"
            show us laugh pioneer at right
            with dissolve
            show mi smile pioneer at left
            with dissolve
            "Никто не возражал.{w} Девушки построились в одну шеренгу, когда мы, присевшие, находились впереди.{w} Фотоаппарат щелкнул, момент был запечатлен."
            mt "А теперь все сюда.{w} Возьмите магнитики, они для вас.{w} На них прошлогодние вы.{w} Такие красивые…"
            "Транспорт взревел, приглашая пионеров к себе на борт.{w} Под такой шумок мы разобрали магнитики и успели поблагодарить вожатую."
            "После чего наш круг начал уменьшаться."
            window hide dissolve
            hide sl
            hide dv
            with dissolve
            show mi sad pioneer at left
            with dissolve
            window show dissolve
            "Сначала вожатая отвела Славяну и Алису…"
            "…{w}Потом двух братьев…"
            window hide dissolve
            hide us
            with dissolve
            show mi cry pioneer at left
            with dissolve
            window show dissolve
            "…{w}И напоследок собралась забрать Лену с Ульяной…"
            me "Лена…"
            un "Наступила та секунда…{w} Ольга, подождите.{w} Дайте пару секунд."
            "Она не возражала, все равно автобусы не уедут, пока не укомплектуются по полной.{w} Поэтому у нас остались последние секунды."
            show un cry pioneer close at center
            with dissolve
            un "З-закрой глазки, Семён.{w} Пожалуйста.{w} И не открывай их, пока вас не поведут."
            show blink
            "Буквально мгновение и я почувствовал её губы.{w} Обычный поцелуй вызвал во мне бурю энергии.{w} Я загорелся желанием бросить все и уехать с ней."
            mt "Теперь вы Семен и Мику.{w} Вам ехать вместе и ваш автобус последний."
            "Лена?!{w} Как быстро все произошло…{w} Её автобус я видел, он покидал границы лагеря, скрываясь за бесконечными полями."
            "Я стал разбитым, будто откололи два куска и сожгли."
            me "Увидимся в 83…"
            "Мику подошла ближе, обняла.{w} Её личико было заплаканное, видно, кто переживал больше всех…"
            "1983 год должен был стать для нас последним в этом лагере."
            "Лену я больше не видел.{w} Письма от неёя не получал, а отправленные лично мной постоянно возвращались."
            "Как и с другими…{w} Я не мог выйти ни на кого.{w} Так я потерял связь со всеми, так я потерял Лену…"

            window hide dissolve
            stop music fadeout 3
            play sound teleport
            $ renpy.pause (1)
            hide screen tfyl_old_filter
            scene bg tfyl_gates with fade

            play music dark_music_25 fadein 3

        "ar" ((.45, .8)) if places:

            jump tfyl_clubs



    jump .search


label tfyl_clubs:

    scene black with fade2
    $ renpy.pause (3)
    scene bg tfyl_clubs with fade2
    window show dissolve

    "Через секунду я оказался по ту сторону ворот.{w} Пионерлагерь предстал передо мной во всей своей брошенной красоте."
    "Пустым…{w} Вспоминая лучшие времена, я понимал, насколько тут не хватает людей."
    "А плачевное состояние такое непривычное…{w} Смотришь на фотографию и реальность, понимаешь - это разные места.{w} Атмосфера совсем иная."
    "Сердце изливалось кровью, будто бы разорили родной дом.{w} Настроение пропало.{w} Неужели такое возможно?"
    "Ветер усилился, поднял листья и разнообразный мусор.{w} Уволок к домику, такому разрисованному и незнакомому."
    "После пионеров тут обитала шпана.{w} Их обитель был помечен неким Васей, который оставил крупный текст на ближайшей стене:{w} {i}Это наше!{/i}"
    "Именно это ожидало лагерь?{w} Как же Артек, Орленок, да тот же Океан?{w} Почему они живут, а этот нет?"
    "Причину закрытия Совёнка я не мог знать, только предполагал.{w} Надежда была на незнакомца, что он ответит на все мои вопросы."
    "Но встретил меня очередной конверт.{w} Теперь весь грязный, местами влажный."

    window hide dissolve
    $ renpy.pause (0.5)
    show screen tfyl_mail_in_hand
    $ renpy.pause (0.5)
    window show dissolve

    "..."

    window hide dissolve
    $ renpy.pause (0.5)
    show screen tfyl_mail_in_hand(remove=True)
    $ renpy.pause (1)
    play sound latter_open
    $ renpy.pause (6)

    show screen tfyl_mail_in_hand("Семён. Память о Совёнке угасла. Бывшие гости лагеря стали забывать, а некоторые вовсе мертвы...\n... Я прошу.\nЗаписывай абсолютно всё: воспоминания, эмоции, мысли. Все.\nНачни с того, как добрался... В этом тебе поможет мой подарок. Он тут, на столе.\nДа, трудно поверить, но так надо.\nНе оборачивайся спиной, уверяю, ответы скоро будут. Только поторопись.", sender="Твой друг")

    pause

    show screen tfyl_mail_in_hand("Семён. Память о Совёнке угасла. Бывшие гости лагеря стали забывать, а некоторые вовсе мертвы...\n... Я прошу.\nЗаписывай абсолютно всё: воспоминания, эмоции, мысли. Все.\nНачни с того, как добрался... В этом тебе поможет мой подарок. Он тут, на столе.\nДа, трудно поверить, но так надо.\nНе оборачивайся спиной, уверяю, ответы скоро будут. Только поторопись.", remove=True, sender="Твой друг")

    $ renpy.pause (1)

    window show dissolve


    "Записка в теперешний момент была информативней, ярче отражала суть помощи…{w} Невольно я подумал о плохом."
    "Надежды на личную встречу рухнули.{w} Неизвестный, как уверял, покажется, но в конце.{w} В конце чего?{w} Много вопросов…"
    "Хотя бог с ними."
    "Сама просьба бредовая: роль летописца в никому не нужном лагере.{w} Имеет смысл, да."
    "Спокойствие пришло не сразу.{w} Я старался убедить себя в смысле этих действий.{w} И вроде успех, решился играть по правилам."
    "Главное дойти до конца, а там уж, либо я, либо незнакомец на все ответит…"
    "Стараясь не утруждать себя лишними размышлениями, ноги сами привели к \"инструменту\".{w} На столике, в метрах пятидесяти, лежал дневник и с десяток ручек."
    "Ничего особенного: мягкая обложка, закладка и 365 страниц.{w} Исключая корочку, там перечислялись места для посещения."
    "Первое и самое ближайшее - клубы.{w} Центр всех кружков, множества мероприятий.{w} Особенностью были плоды труда, которые так или иначе привлекали внимание общественности."
    "А после починки видеомагнитофона и лампового телевизора все сошли с ума, ведь распорядок дня пополнился на один пункт."
    "Бесконечный просмотр терминатора каждый вечер!{w} Других кассет к сожалению не появлялось."
    "Этот бесявый момент сопроводил меня к зданию не похожему на старые \"клубы\"."
    "Надо свыкнуться, что современный Совёнок кардинально отличается от старого.{w} Здесь больше с уклоном в постапокалипсис, который образовался из мрачной сказки."
    "Окна выбиты, дверцы нету.{w} Покрытие, что сверху, почти все отсутствует."

    "Аварийное состояние сразу намекало, что лучше не заходить.{w} Целее будешь."

    window hide dissolve

    $ places = BooleanList(5)

    jump .search

label .search:

    menu (screen="tfyl_choice"):

        "?" ((.1, .1)) if not places[0]:
            $ places.set_true(0)

            window show dissolve

            "Особенное достояние находилось на крыше этого чудного здания.{w} Создатели неизвестны, но подозревают двух друзей."
            "Платформа собрала в себе множество конфликтов и была на грани сноса."
            "Во-первых небезопасно, во-вторых выговоры проверок."
            "Вожатые собирались снести, пока не вступился Шурик."
            "Он-то установил поручни, укрепил опоры, в целом конструкция стала безопасной."
            "И вроде помогло.{w} Пионеры уже оставили следы, некоторые - надписи.{w} Все прекрасно…"
            "Все равно снесли.{w} Чердак закрыли на замок, а от бывшего наблюдательного поста остался единственный люк."

            window hide dissolve

        "?" ((.05, .7)) if not places[1]:
            $ places.set_true(1)

            window show dissolve

            "Живой уголок располагался прямо за зданием и собирал в себе дюжинную коллекцию."
            "Особое пристрастие вызывал у деток по-младше, любивших животинку."
            "Судя по рассказам ранее тут был голубятник.{w} Именно в нем проследили ту самую любовь и Ольга Дмитриевна принялась за работу."
            "Под её руководством два техника и другие рабочие отстроили вольеры."
            "Главную часть, разумеется, выполняла старшая.{w} Из города она привезла домашних зверушек."
            "Остальное: заботу, питание, внимание организовали пионеры.{w} Лишняя обязанность, да, но какое разнообразие в этом монотонном лагере."
            "А что теперь?{w} Рваная сетка, сломанные временем домики, сбежавшие животные.{w} Даже любимый кролик Ульяны сбежал."

            window hide dissolve

        "?" ((.45, .5)) if not places[2]:
            $ places.set_true(2)

            window show dissolve

            "Обойдя здание по кругу я сделал вывод, что все возможное вынесено, а невозможное побито и оторвано.{w} Это же касалось и  помещений."
            "Через проем, где отсутствовала дверь, я наблюдал довольно длинный коридор.{w} Все, что в нем осталось - плакаты и таблички с названием кружков."
            "Самая крайняя являлась \"Радиотехнической\".{w} Обитель Эла и Шурика, гениев и изобретателей."
            "Те не только по платам.{w} Всякая другая работа, требующая трезвой головы и золотых рук, доставалась им."
            "Вот и во мне увидели такие качества.{w} Приглашали к себе, рассказывали о плюсах, будто тут рай."
            "Правда, одна деталь перечеркнула все."
            "Они не вылезают из помещения!{w} Моменты на питание и туалет не считаю.{w} Как так?{w} Лето и за четырьмя стенами!"
            "Во имя пляжа и девушек я, конечно же, отказался.{w} Но общаться не перестал, как никак поддержка со стороны изобретателей дорогого стоит."

            window hide dissolve

        "?" ((.64, .77)) if not places[3]:
            $ places.set_true(3)

            window show dissolve

            "Помнится тут были списки о наборе и прочие объявления."
            "Здесь пионеры могли найти идеи, как разнообразить свой досуг."
            "Будь-то кружок или мероприятия на вечер.{w} Неважно.{w} Каждый день стэнд обновлял ассортимент новостей."
            "И тут не без участия пионеров.{w} Любой желающий мог прикрепить свой листок с приглашением."
            "Слав…{w} Да, Славяна была ответственна за эту доску.{w} Всякий раз она отсеивала бумагу не по теме, где-то корректировала, поправляла."
            "Ответственно подходила к делу.{w} Вот почему стэнд информирования до сих пор стоит."
            "Ещё одна деталь вызвала во мне удивление - выцветшая фотография, держащаяся на одной кнопке."
            "Потрёпанная дождями, ветрами, чем угодно, но сохранившая оттенок того времени."
            "На ней сцена и пионеры…{w} Мику, да-да, она самая!{w} И девушка с зелёной косой и цветочком…"
            "Столь памятную вещицу я не стал брать.{w} Она принадлежит истории этого лагеря, а не мне."

            window hide dissolve

        "?" ((.96, .65)) if not places[4]:
            $ places.set_true(4)

            window show dissolve

            "Святыня тех, кто когда-либо состоял в кружках.{w} Всегда была закрыта на замок, а сейчас, увы, даже двери нет."
            "Там хранили материалы на стеллажах, и готовые подделки в деревянных ящиках.{w} Причем последние передавались из смены в смену."
            "Если сделал, то будь добр оставить.{w} Все равно нет ничего лучше опыта и приобретенных товарищей.{w} Так говорили вожатые."
            "Вот и скопилось барахлишко.{w} Чего там только не водилось…"
            "Жаль, что вся коллекция собранная годами досталась мародерам."

            window hide dissolve
# понимаю... могу скопировать всю эту хуйню и доделать... но мне тоже спать надо... сначала залей на гит ... ну и ладно ... один день подождут ).. давай спросим нашего сценариста (насяльника) дада
        "!" ((.96, .37)) if places: # Я уже кажется не могу, голова не варит # видать седня обновление не получится сделать... Ну чисто технически, можно обновить прошлые главы, а эта тип " в разработке"

            stop music fadeout 1
            $ renpy.pause (1)
            play music latter_25 fadein 1
            window show dissolve

            "Довольно большой лист был прикреплен к берёзе, некогда посаженной двумя товарищами."
            "Поверх бумаги мигал диод, который, видимо, привлекал мое внимание."
            "Значит незнакомец надеялся, что я прочту это."

            window hide dissolve

            show screen  tfyl_mail_in_hand("""    Друзья, как капля воды.
Двое: Эл и Шурик. Вместе они приехали в этот лагерь, будучи школьниками начальных классов. Оба были чужды друг другу, но один отряд объединил их, увлек одной целью.
Их таланты проявились в том самом кабинете.
Старшие пионеры обучали их, пока было чему.
После пошли книги, журналы и собственный опыт.
Электроник был мастером по металлу, когда его друг наоборот, любил дерево. Но обоих объединяла электроника и детская мечта. Совершить прорыв...""")

            pause

            show screen  tfyl_mail_in_hand("""...Путь был нелегким. В лагере они мастерили, а дома составляли схемы. И даже занятые, они находили для нас минутку.
И вот, когда двое переросли в настоящих комсомольцев, случилось нечто. Открытие было у них под носом.
Оставалась капля.
Ошибки свойственны всем, даже гениям. Вспышка электричества поглотила обоих, утаив их в лучшем мире.
Я буду скучать по двум братьям, именно так их можно назвать.
""")

            pause

            show screen  tfyl_mail_in_hand("""...Путь был нелегким. В лагере они мастерили, а дома составляли схемы. И даже занятые, они находили для нас минутку.
И вот, когда двое переросли в настоящих комсомольцев, случилось нечто. Открытие было у них под носом.
Оставалась капля.
Ошибки свойственны всем, даже гениям. Вспышка электричества поглотила обоих, утаив их в лучшем мире.
Я буду скучать по двум братьям, именно так их можно назвать.
""", remove=True)


#             show screen tfyl_mail(tfyl.add_mail("Друзья, как капля воды", """    Друзья, как капля воды.
# Двое: Эл и Шурик. Вместе они приехали в этот лагерь, будучи школьниками начальных классов. Оба были чужды друг другу, но один отряд объединил их, увлек одной целью.
# Их таланты проявились в том самом кабинете.
# Старшие пионеры обучали их, пока было чему.
# После пошли книги, журналы и собственный опыт.
# Электроник был мастером по металлу, когда его друг наоборот, любил дерево. Но обоих объединяла электроника и детская мечта. Совершить прорыв...""",
#
# """...Путь был нелегким. В лагере они мастерили, а дома составляли схемы. И даже занятые, они находили для нас минутку.
# И вот, когда двое переросли в настоящих комсомольцев, случилось нечто. Открытие было у них под носом.
# Оставалась капля.
# Ошибки свойственны всем, даже гениям. Вспышка электричества поглотила обоих, утаив их в лучшем мире.
# Я буду скучать по двум братьям, именно так их можно назвать.""",
#
# """...Путь был нелегким. В лагере они мастерили, а дома составляли схемы. И даже занятые, они находили для нас минутку.
# И вот, когда двое переросли в настоящих комсомольцев, случилось нечто. Открытие было у них под носом.
# Оставалась капля.
# Ошибки свойственны всем, даже гениям. Вспышка электричества поглотила обоих, утаив их в лучшем мире.
# Я буду скучать по двум братьям, именно так их можно назвать.""")) # Что бы сразу добавлять и показывать

            $ tfyl.add_mail("Друзья, как капля воды", """    Друзья, как капля воды.
Двое: Эл и Шурик. Вместе они приехали в этот лагерь, будучи школьниками начальных классов. Оба были чужды друг другу, но один отряд объединил их, увлек одной целью.
Их таланты проявились в том самом кабинете.
Старшие пионеры обучали их, пока было чему.
После пошли книги, журналы и собственный опыт.
Электроник был мастером по металлу, когда его друг наоборот, любил дерево. Но обоих объединяла электроника и детская мечта. Совершить прорыв...""",

"""...Путь был нелегким. В лагере они мастерили, а дома составляли схемы. И даже занятые, они находили для нас минутку.
И вот, когда двое переросли в настоящих комсомольцев, случилось нечто. Открытие было у них под носом.
Оставалась капля.
Ошибки свойственны всем, даже гениям. Вспышка электричества поглотила обоих, утаив их в лучшем мире.
Я буду скучать по двум братьям, именно так их можно назвать.""",

"""...Путь был нелегким. В лагере они мастерили, а дома составляли схемы. И даже занятые, они находили для нас минутку.
И вот, когда двое переросли в настоящих комсомольцев, случилось нечто. Открытие было у них под носом.
Оставалась капля.
Ошибки свойственны всем, даже гениям. Вспышка электричества поглотила обоих, утаив их в лучшем мире.
Я буду скучать по двум братьям, именно так их можно назвать.""")

            pause 2


            window show dissolve

            "Я прекрасно помнил этих \"клубоседов\", оба жили отстранённо и только везунчикам удавалось узнать их секреты."
            "С 82 больше их не видел.{w} Как в последний день пожали друг другу руки, так разошлись."
            "Еще эти чемоданы.{w} Я точно помню, что они были огромные, даже задавался в прошлом этим вопросом."
            "Но теперь…{w} Их больше нет…"
            "Сколько времени прошло, а потеря таких хороших людей как-то отражается на настроении."
            "В голову пришла мрачная, но вполне реальная мысль.{w} А вдруг это не единственная бумага о смерти товарищей?"
            "Не хотелось бы читать их, ведь есть иллюзия, что у всех все хорошо.{w} Зачем знать лишнее?"
            "Только угодить себе не получится.{w} Хочешь узнать ответы - играй по правилам.{w} А незнакомец плавно, но к чему-то ведёт."
            "Главное держать себя в руках!"

            window hide dissolve

            stop music fadeout 4
            scene black
            with dissolve
            $ renpy.pause (3)
            jump tfyl_stage

    jump .search
