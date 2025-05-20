# Közúti tábla detektálása Gazebo világban turtlebot3-al
Projektfeladatunk során közúti táblákat kell felismernie a robotnak és azok alapján akciót végrehajtania.

# Projekt elkészítése
Első lépésként elkészítettünk egy világot utakkal és fákkal Gazebo-ban. Majd Blenderben közúti táblákat modelleztünk és a megfelelő formátumban kimentve elhelyeztük őket a models mappába. A világban elrendeztük a táblákat. Az alábbi táblákat kell detektálnia a robotunknak (zárójelben az elvégezendő akció):

- Stop tábla: megáll a robot 
- Zebra tábla: lassít, megáll, körülnéz és elindul
- Jobbra tábla: jobbra fordul és elindul
- Balra tábla: balra fordul és elindul

# A szimuláció elindítása
Készíts egy workspace mappát és azonbelül egy source mappát. Majd klónozd le a gitrepot

```
mkdir -p ~/workspace/src
cd workspace/src
```

# Indítsd el a szimulációt!
Ez csak a gazeboban indítja el a robotot és ennyi
```
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

## Szerkeszd a .bashrc file-t!
Ahhoz hogy működjön és megtalálja az elérési útvonalat szerkesztened kell a .bashrch filet
```
nano .bashrc
```

