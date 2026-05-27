label chapter5:
    scene bg library
    with dissolve
    show mc_sprite at left_sprite
    narrator "A customer arrives. You begin helping them."
    narrator "The flickering book on the shelf shakes violently."
    narrator "A sudden flash hits you."
    narrator "You see a car skidding in rain."
    narrator "Screeching tires."
    narrator "Your own voice screaming."
    hide mc_sprite
    menu:
        "Your story is what matters right now.":
            show mc_sprite at left_sprite
            mc "Your story is what matters right now."
            mc "Let's finish this together."
            narrator "The customer thanks you warmly."
            $ empathy += 1
            show screen notify("+1 Empathy")
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch5")
            jump chapter6
        "Why do I feel like this book is calling my name?":
            scene bg book_desk
            with dissolve
            show book_overlay
            mc "Why do I feel like this book is calling my name?"
            mc "I have to know."
            narrator "You reach out and touch the flickering book."
            narrator "The vision intensifies — the crash, the rain, your own face."
            $ memory_fragments += 2
            show screen notify("+2 Memory Fragments")
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch5")
            jump chapter6
