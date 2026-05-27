label chapter6:
    scene bg book_desk
    with dissolve
    show book_overlay
    narrator "You finally open the flickering book."
    narrator "Memories flood in — the accident, regret, unfinished goodbyes."
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
            show screen notify("+2 Self-Awareness")
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch6")
            jump chapter7
        "No... this can't be real! I'm not one of the lost!":
            mc "No... this can't be real!"
            mc "I'm the one who helps people — I'm not one of the lost!"
            narrator "Pain intensifies. Denial echoes through the library."
            $ suspicion += 1
            show screen notify("+1 Suspicion")
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch6")
            jump chapter7
