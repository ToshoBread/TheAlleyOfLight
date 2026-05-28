label chapter5:
    scene bg library_cool
    with dissolve
    play music bgm_chapter_5_music fadein 1.0 volume 0.7 loop
    show mc_sprite at left_sprite
    narrator "A customer arrives. You begin helping them."
    play sound bgsfx_shaking_book_sound volume 1.0 loop
    narrator "The flickering book on the shelf shakes violently."
    stop sound fadeout 0.5
    pause 0.5
    play sound bgsfx_ears_ringing_sound volume 1.0
    pause 2.5
    narrator "A sudden flash hits you."
    stop sound fadeout 1.0
    narrator "You see a car skidding in rain."
    play sound bgsfx_tire_screeching_sound volume 1.0
    pause 0.5
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
            pause 2.0
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch5")
            jump chapter6
        "Why do I feel like this book is calling my name?":
            scene bg book_desk_dim
            with dissolve
            $ renpy.pause(0.5, hard=True)
            show book_overlay
            with dissolve
            mc "Why do I feel like this book is calling my name?"
            mc "I have to know."
            narrator "You reach out and touch the flickering book."
            narrator "The vision intensifies — the crash, the rain, your own face."
            $ memory_fragments += 2
            show screen notify("+2 Memory Fragments")
            pause 2.0
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch5")
            jump chapter6
