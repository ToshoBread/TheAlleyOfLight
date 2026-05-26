label chapter4:
    scene bg library_int
    with dissolve
    show mc_sprite at center_sprite
    narrator "One night, no customers come."
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
            narrator "You search until you find an ancient ledger."
            narrator "\"The library exists for lost souls to finish their stories before moving on.\""
            $ truth += 1
            show screen notify("+1 Truth")
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch4")
            jump chapter5
        "I should stay at the desk.":
            mc "I should stay at the desk."
            mc "More souls might need me."
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch4")
            jump chapter5
