label start:
    play music bg_music_character_selection fadein 2.0 
    scene black
    show aine_select at select_left
    show lucian_select at select_right
    with dissolve
    "Choose your character:"
    menu:
        "Aine":
            play sound bgsfx_button_click volume 0.8
            $ mc_choice = "Aine"
            $ mc_name = "Aine"
            $ mc_color = "#cc0066"
            hide aine_select
            show mc_sprite at center_sprite
            with dissolve
        "Lucian":
            play sound bgsfx_button_click volume 0.8
            $ mc_choice = "Lucian"
            $ mc_name = "Lucian"
            $ mc_color = "#0066cc"
            hide lucian_select
            show mc_sprite at center_sprite
            with dissolve
    $ mc = Character(mc_name, color=mc_color)
    stop music fadeout 0.0
    mc "My name is [mc_name]."
    jump prologue_alley

label prologue_alley:
    scene black
    with dissolve
    play music bgm_intro fadein 5.0 volume .75 
    pause 3.0
    narrator "Everything is dark."
    narrator "You slowly open your eyes."
    narrator "Your head hurts."
    narrator "You try to remember something... anything."
    stop music fadeout 1.0
    play sound bgsfx_creepy_sound volume 1.0 loop
    narrator "But there's nothing."
    scene bg dark_street
    with dissolve
    show mc_sprite at center_sprite
    mc "Where am I?"
    narrator "You are standing in a quiet alley."
    narrator "It's empty. Too quiet."
    narrator "At the end of the alley, a soft, warm light spills from an open door."
    stop sound fadeout 1.0
    play music bgm_scary fadein 0.5 volume .75
    narrator "A library."
    menu:
        "Walk toward the light.":
            play sound bgsfx_walking_on_water volume 0.8
            narrator "You walk toward the light."
            stop music fadeout 1.0
        "Stay still.":
            narrator "You stay still."
            stop music fadeout 1.0
            narrator "Silence."
            play sound bgsfx_spooky_sound volume 1.0 loop
            narrator "Then the darkness begins to creep toward you."
            stop sound fadeout 6.0
            pause 6.0
            play sound bgsfx_running_sound fadein 1.0 volume 1.0 loop
            narrator "You run."
    scene bg library
    with dissolve
    stop sound fadeout 1.0
    play music bgm_scary fadein 1.0 volume .75
    play sound bgsfx_opening_door volume 1.0
    pause 4.0
    narrator "The door opens."
    mc "Hello?"
    narrator "Warm light spills from within."
    show screen notify("Saving...")
    $ renpy.take_screenshot()
    $ renpy.save("auto_prologue")
    jump enter_library

label ending_secret:
    scene bg library_warm
    with dissolve
    show mc_sprite at center
    mc "Thank you for letting me help everyone... including myself."
    mc "I'll carry this light with me."
    narrator "You close the book and step toward the door."
    narrator "Not as a lost soul — but as someone who found their ending."
    narrator "And helped others find theirs."
    jump credits

label ending_return:
    scene bg library_warm
    with dissolve
    show mc_sprite at center
    mc "I want to go back."
    mc "My story isn't over yet."
    narrator "Light surrounds you."
    narrator "You wake up."
    narrator "The rain has stopped."
    narrator "You are alive."
    jump credits

label ending_stay:
    scene bg library
    with dissolve
    show mc_sprite at center
    mc "Someone needs to keep the light on for the others."
    mc "I'll stay."
    narrator "You close the book."
    narrator "The door opens."
    narrator "A new customer enters."
    narrator "You smile."
    narrator "There are more stories to help find their ending."
    jump credits

label ending_let_go:
    scene black
    with dissolve
    mc "It's time."
    narrator "You close the book."
    narrator "Light surrounds you."
    narrator "You fade into the light."
    jump credits

label credits:
    scene black
    with dissolve
    show screen notify("Saving...")
    $ renpy.take_screenshot()
    $ renpy.save("auto_end")
    narrator "YOU HAVE COMPLETED The Alley of Light."
    narrator "Thank you for playing."
    $ renpy.full_restart()
