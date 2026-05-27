label chapter3:
    scene bg library
    with dissolve
    show mc_sprite at left_sprite
    narrator "A man walks in. He looks at you strangely."
    narrator "Something about him is unsettlingly familiar."
    show mirror_man_sprite at right_sprite
    with dissolve
    mirror_man "You... you feel so familiar. Have we met?"
    mirror_man "Your eyes... I swear I've seen them before."
    menu:
        "Tell me everything you remember about me.":
            mc "You know me?"
            mc "Please tell me everything you remember about me."
            $ suspicion += 1
            show screen notify("+1 Suspicion")
            hide mirror_man_sprite with dissolve
            show mirror_man_sprite_2 at right_sprite with dissolve
            mirror_man "You were in an accident... there was rain, headlights..."
            mirror_man "Wait, was that you?!"
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch3")
            jump chapter4
        "Let's focus on your story first.":
            mc "Let's focus on your story first."
            mc "The book is waiting for your ending."
            $ clarity += 1
            show screen notify("+1 Clarity")
            mirror_man "Alright... but something about you feels unfinished too."
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch3")
            jump chapter4
