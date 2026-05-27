label enter_library:
    scene bg library
    with dissolve
    show mc_sprite at left_sprite
    narrator "Rows of books fill the room."
    narrator "It feels endless."
    narrator "Quiet. Peaceful."
    narrator "Then—"
    narrator "One book on the central desk begins to glow."
    show glowing_book_overlay
    with dissolve
    mc "Why is that glowing?"
    narrator "A bell chimes."
    show customer_sprite at right_sprite
    with dissolve
    customer "Excuse me?"
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
    narrator "The glowing book shines brighter."
    customer "That book... it's glowing."
    scene bg book_desk_dim
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show book_overlay
    with dissolve
    narrator "You pick up the glowing book."
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
            narrator "Light surrounds her."
            narrator "She closes the book and walks outside."
        "Let go.":
            scene bg library
            with dissolve
            show mc_sprite at left_sprite
            show customer_sprite_thanks at right_sprite
            with dissolve
            customer "I understand now."
            narrator "She smiles softly."
            customer "Thank you."
            narrator "She fades into light."
    narrator "The library is quiet again."
    mc "What was that?"
    narrator "You look around."
    narrator "Then you see it."
    narrator "One book on the shelf is glowing."
    show glowing_book_overlay
    with dissolve
    narrator "Flickering. Different."
    mc "That wasn't there before."
    show screen notify("Saving...")
    $ renpy.take_screenshot()
    $ renpy.save("auto_intro")
    jump chapter1
