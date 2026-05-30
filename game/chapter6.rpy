label chapter6:
    scene bg book_desk_dim
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show book_overlay
    with dissolve
    play sound bgsfx_book_turn_sound volume 1.0
    pause 2.5
    narrator "You finally open the flickering book."
    narrator "Memories flood in — the accident, regret, unfinished goodbyes."
    play sound bgsfx_strong_rain_sound fadein 1.0 volume 1.0 loop
    pause 1.0
    narrator "The rain. The headlights. The moment everything went dark."
    narrator "You see yourself."
    narrator "You never made it out."
    menu:
        "I remember now. The rain, the crash...":
            mc "I remember now."
            mc "The rain, the crash..."
            mc "I never got to say goodbye to them."
            narrator "The memories settle. Calmness washes over you."
            $ self_awareness += 2
            $ renpy.notify("+2 Self-Awareness")
            stop sound fadeout 5.0
            $ renpy.notify("Saving...")
            $ renpy.pause(0.1, hard=True)
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch6")
            jump chapter7
        "No... this can't be real! I'm not one of the lost!":
            mc "No... this can't be real!"
            mc "I'm the one who helps people — I'm not one of the lost!"
            narrator "Pain intensifies. Denial echoes through the library."
            $ suspicion += 1
            $ renpy.notify("+1 Suspicion")
            stop sound fadeout 5.0
            $ renpy.notify("Saving...")
            $ renpy.pause(0.1, hard=True)
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch6")
            jump chapter7
