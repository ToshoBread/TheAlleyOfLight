label enter_library:
    scene bg library
    with dissolve
    show mc_sprite at left_sprite with dissolve
    narrator "Rows of books fill the room."
    narrator "It feels endless."
    narrator "Quiet. Peaceful."
    narrator "Then—"
    narrator "One book on the central desk begins to glow."
    show glowing_book_overlay
    with dissolve
    play sound bgsfx_shimmer volume 1.0
    pause 2.0
    narrator "The light is warm. Inviting."
    mc "Why is that glowing?"
    stop sound fadeout 1.0
    pause 2.0
    play sound bgsfx_bell_chime_sound volume 0.7 loop
    narrator "A bell chimes."
    show customer_sprite at right_sprite
    with dissolve
    customer "Excuse me?"
    stop sound fadeout 1.0
    pause 2.0
    narrator "You turn around."
    customer "Where am I?"
    menu:
        "I don't know.":
            mc "I don't know."
        "This is a library.":
            mc "This is a library."
        "Stay silent.":
            narrator "You stay silent."
    customer "I... I don't remember how I got here."
    mc "Me too."
    play sound bgsfx_shimmer volume 1.0 loop
    pause 2.0
    narrator "The glowing book shines brighter."
    customer "That book... it's glowing."
    stop sound fadeout 1.0
    scene bg book_desk_dim
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show book_overlay
    with dissolve
    narrator "You pick up the glowing book."
    play sound bgsfx_book_turn_sound volume 1.0
    pause 4.0
    narrator "It opens on its own."
    narrator "Images flicker — a building, silence, rain."
    customer "That's me."
    mc "It's your story."
    customer "It's not finished."
    customer "I think... something happened."
    customer "I'm scared."
    menu:
        "Close the book.":
            scene bg library
            with dissolve
            show mc_sprite at left_sprite
            show customer_sprite at right_sprite
            with dissolve
            customer "I'm not ready to let go."
            play sound bgsfx_shimmer volume 0.5 loop
            pause 2.0
            narrator "Light surrounds her."
            stop sound fadeout 1.0
            pause 2.0
            play sound bgsfx_book_closed_sound 
            narrator "She closes the book and walks outside."
            play sound bgsfx_walking_on_wood_sound volume 0.8
            hide customer_sprite with dissolve 
            pause 3.0
        "Let go.":
            scene bg library
            with dissolve
            show mc_sprite at left_sprite
            show customer_sprite_thanks at right_sprite
            with dissolve
            customer "I understand now."
            narrator "She smiles softly."
            customer "Thank you."
            play sound bgsfx_shimmer volume 1.0
            narrator "She fades into light."
            stop sound fadeout 1.0
            hide customer_sprite_thanks with dissolve
            pause 2.0
    narrator "The library is quiet again."
    mc "What was that?"
    narrator "You look around."
    narrator "Then you see it."
    narrator "One book on the shelf is glowing."
    play sound bgsfx_shimmer volume 1.0 loop
    show glowing_book_overlay
    with dissolve
    narrator "Flickering. Different."
    mc "That wasn't there before."
    stop sound fadeout 1.0
    $ renpy.notify("Saving...")
    pause 3.0
    $ renpy.pause(0.1, hard=True)
    $ renpy.take_screenshot()
    $ renpy.save("auto_intro")
    jump chapter1
