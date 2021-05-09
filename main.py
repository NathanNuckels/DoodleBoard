import projwindow
import board

w1 = projwindow.Proj()  # GODOT inspired project ui
w1.show()

while w1.looping:
    w1.loop()
w1.delete()
if not w1.openfile:
    exit()
path=w1.proj
proj={}
with open(path+"/project.dlp",'r') as f:
    for line in f:
        line=line.strip().split("|")
        proj[line[0]]=line[1]
drawboard=board.Drawboard(proj,path)
drawboard.run()
while drawboard.open:
    drawboard.loop()