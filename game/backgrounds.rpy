image bg dark_street = Transform("images/Assets/bg/Dark_street.jpg", fit="cover")
image bg main_menu = Transform("images/Assets/bg/Spooky_walkway.jpg", fit="cover", matrixcolor=BrightnessMatrix(-0.25))
image bg library = Transform("images/Assets/bg/Library.jpg", fit="cover", align=(0, 0.5))
image bg book_desk = Transform("images/Assets/bg/Book_desk.jpg", fit="cover")
image bg book_desk_dim = Transform("bg book_desk", matrixcolor=BrightnessMatrix(-0.15))

image bg library_dim = Transform("bg library", matrixcolor=BrightnessMatrix(-0.10) * SaturationMatrix(0.7))
image bg library_cool = Transform("bg library", matrixcolor=TintMatrix((0.69, 0.77, 0.87, 1.0)) * BrightnessMatrix(-0.05))
image bg library_warm = Transform("bg library", matrixcolor=TintMatrix((1.0, 0.84, 0.0, 1.0)) * BrightnessMatrix(0.05))

image book_overlay = Transform("images/Assets/items/book.png", rotate=-10, zoom=0.45, align=(0.5, 0.5))
image glowing_book_overlay = Transform("images/Assets/items/glowing_book.png", zoom=0.05, align=(0.56, 0.30))
