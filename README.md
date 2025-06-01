# Közúti tábla detektálása Gazebo világban turtlebot3-al
Projektfeladatunk a BME Kognitiv Robotika tárgy keretében a következő volt:
Gazebo szimulációs környezetben TurtleBot3 segítségével közlekedési táblákat kellett felismerni és azok alapján a megfelelő akciót végrehajtani.

[👉 Nézd meg a videót a YouTube-on](https://www.youtube.com/watch?v=Yc2gTMmYv5w)


## A projekt elkészítésében részt vettek:
- Rátkai Bálint (DSPQKJ)
- Veres András Jenő ()
- Kis-Tamás Levente (N1LVWX)

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
Első megoldások esetében, a YOLOv8 alacsonyabb modelljeit használtuk. Azt vettük észre, hogy a tábla felismeréskor a BALRA táblát is JOBBRA táblának detektálja. Nem volt elegendő képünk ennek kiküszöbölésére. Nagyon hasonló a két tábla ezért úgy döntöttünk másra cseréljük a BALRA táblát.

![rossz tábla](assets/images/rossz.jpg)


### Tesztelés
A végleges modellünk a YOLO8 medium verziója. Először Windowson kimentett képeken néztük meg az eredményeket. 

![bal](assets/images/bal1.jpg)
![jobb](assets/images/jobb1.jpg)
![zebra](assets/images/zebra1.jpg)
![stop](assets/images/stop1.jpg)

Az eredményeket látva, tovább léphettünk a WSL2 környezetbe átimportálásra.
#### Tesztelés wsl2-ben

### Összegzés és fejlesztési javaslatok
A projektfeladat elkészítése során számos problémába ütköztünk, de többségére mind találtunk megoldást. Hátráltatott minket a lassú környezet (GPU-t nem tudtuk használni) és sok tárhelyre is volt szükségünk.
Elsajátítottuk a github kezelését, wsl2-ben használt utasításokat, gazebo világ építésést, saját ROS2 nodeírásokat. Összességében a projekt feladatunk képes táblák detektálására szimulációban a turtlebot3 segítségével real time.

A projektfeladat tovább fejleszthető egy erősebb tanítási modellel és nagyobb adatbázissal. A mi megoldásunkban csak kameraképet hasznátunk. LIDAR segítségével komplexebb detektálás is végrehajtható az időben. Mint például gyalogosok a zebrán, más autók távolsága.
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

