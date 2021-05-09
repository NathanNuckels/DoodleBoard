import projwindow

w1 = projwindow.Proj()  # GODOT inspired project ui
w1.show()

while w1.looping:
    w1.loop()
w1.delete()
