# TODO zrobić nowa dokumentację

# Dokumentacja do komunikacji RPI=>Arduino

## Symbole dzielimy na WARTOŚCI oraz KOMENDY
aktualne WARTOŚCI jakie możemy przesyłac to 1-bajtowe zmienne o wartościach od 0 do 180
aktualne KOMENDY jakie możemy przesyłac to 1-bajtowe zmienne o wartościach od 200 do 255

## Paczka danych
Paczka danych jest prosta i zawiera PARĘ BAJTÓW:
1 bajt to KOMENDA
2 bajt to WARTOŚĆ

## dokładne typy komend
205 - zmiana kamery w PIONIE (V)
206 - zmiana kamery w POZIOMIE (H)
209 - zmiana prędkości koła LEWEGO (L)
210 - zmiana prędkości koła PRAWEGO (R)


## przykłady
(205, 110) - ustawia kamerę lekko do góry
(206, 20) - ustawia kamerę mocno w lewo
(209,90) - zatrzymuje silnik L
(210,120) - lekko porusza silnik R do przodu

## uwagi
Dla SILNIKÓW wartość spoczynkowa to '90'
Jazda do przodu to wartości z przedziału od '0' do '89' a do tyłu '91' do '180'



