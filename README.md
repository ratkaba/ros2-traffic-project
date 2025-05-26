# Közúti tábla detektálása Gazebo világban turtlebot3-al
Projektfeladatunk a BME Kognitiv Robotika tárgy keretében a következő volt:
Gazebo szimulációs környezetben TurtleBot3 segítségével közlekedési táblákat kellett felismerni és azok alapján a megfelelő akciót végrehajtani.
## A projekt elkészítésében részt vettek:
- Rátkai Bálint (DSPQKJ)
- Veres András Jenő ()
- Kis-Tamás Levente

## A Projekt elkészítése
Az órai előadásokon elhangzottak és a kiadott anyagok alapján indultunk el. 
### A világ megalkotása
Mivel közlekedési tábla felismerés volt a feladatunk, ezért egy annak megfelelő világ létrehozása volt a cél. Kezdetben más, már létező világokat kerestünk az interneten. Találtunk is, de nem tudtuk megfelelően beimportálni a szükséges modelleket és textúrákat. Ezért, úgy döntöttünk, hogy nulláról kezdjük és elkészítünk egy saját világot.
Az utakat téglalapokként helyeztük el a ground plane-n, majd a Gazebo saját könyvtárából fákat helyeztünk el a színesebb környezet érdekében. Ezekután táblákra volt szükségünk, mint feladatunk központi elemére. Az interneten talált modellek nem voltak megfelelőek számunkra, ezért Blender környezetben modelleztünk saját táblákat. Az elkészített modellek megtalálhatóak a models mappában. Végül a táblákat elhelyeztük a világban.
### Táblakészítés blenderben
..
.
.
.
### A táblák és a hozzátartozó akciók
Az alábbi táblákat használtul fel (zárójelben az elvégezendő akció):

- Stop tábla: megáll a robot 
- Zebra tábla: lassít, megáll, körülnéz és elindul
- Jobbra tábla: jobbra fordul és elindul
- Balra tábla: balra fordul és elindul

A következő lépés a tanítás, de ezek előtt a robotunkon módosítani kellett pár paramétert.
### TurtleBot3 átalakítása
A MOGI csomag alapján használtuk a TurtleBot-ot, de szükséges volt pár paraméterének a megváltoztatására. Elsődlegesen a sebességét állítottuk át, mivel méretéből adódóan nagyon lassan haladt az eredeti sebességet használva. Ezért sikeresen felgyorsítottuk. Ezekmeleltt a roboton található kamerának paramétereit is meg kellett változtatnunk, Feljebb emeltük a kamerát, hogy a kamera kép tényleg egy autóéhoz hasonlítson. Figyeltünk a robot fizikai jellemzőire is, hogy ezek a változások ne "borítsák fel" a robotunkat.
### Tanítás YOLO-val
Hosszas ötletelés során az alábbi ötletre jutottunk:

 - A robotnak csak a kameráját használjuk a detektálásra.
 - Nem használunk LIDAR-t a távolság meghatározására, helyette bounding box mérete alapján végzi el a robot a feladatot
 - Ha elég nagy a felismert tábla bounding box-ja elvégzi az akciót
 - A tanításhoz képeket mentünk ki a saját világunkból
 - Plusz képeket gyűjtünk be az internetről
 - YOLO segítségével végezzük a tanítást

A tanítást úgy láttuk a legjobbnak, hogy nem wsl2-n futtatjuk, hanem Windows alatt és ha kész a tanulás utána ültetjük át a végeredményt.
### Tesztelés
...
.

.
.
# A szimuláció elindítása
Készíts egy workspace mappát és azonbelül egy source mappát. Majd klónozd le a git repo-t.

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
source /opt/ros/jazzy/setup.bash
source ~/workspace/install/setup.bash

export TURTLEBOT3_MODEL=burger

export GZ_SIM_RESOURCE_PATH=~/workspace/src/ros2-traffic-project/models

export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/workspace/src/ros2-traffic-project/models
```

