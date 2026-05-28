label chapter4:
    scene bg library_dim
    with dissolve
    pause 3.0
    narrator "One night, no customers came."
    show mc_sprite at center_sprite with dissolve
    play music bgm_chapter_4_music fadein 0.5 volume 0.7
    pause 1.5
    narrator "You are alone."
    narrator "You wander through the endless shelves."
    narrator "No doors. No windows."

    narrator "Books shift positions on their own."
    narrator "A whispering voice echoes."
    narrator "\"This place is between life... and what comes after.\""
    menu:
        "There has to be answers here.":
            mc "There has to be answers here."
            mc "I need to know what this place really is."
            scene bg book_desk_dim
            with dissolve
            $ renpy.pause(0.5, hard=True)
            show book_overlay
            with dissolve
            play sound bgsfx_book_turn_sound volume 1.0
            pause 2.5
            narrator "You search until you find an ancient ledger."
            narrator "\"The library exists for lost souls to finish their stories before moving on.\""
            $ truth += 1
            show screen notify("+1 Truth")
            stop music fadeout 5.0
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch4")
            jump chapter5
        "I should stay at the desk.":
            mc "I should stay at the desk."
            mc "More souls might need me."
            stop music fadeout 5.0
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch4")
            jump chapter5
