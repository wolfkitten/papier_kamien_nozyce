#!/usr/bin/env python
#-*- coding: utf-8 -*-

                                        #zdefiniowanie zbioru
zbior={1:'PAPIER',2:'KAMIEŃ',3:'NOŻYCE'}

                                        #zdefiniowanie wyborów player1
class class_player_one():
    wybor_player1 = []
    powtorzenia_palyer1 = 0
    def __init__(self):
        self.player1=input()

    def player1_wariant_wyboru(self):
        if self.player1=='1':
            z=zbior[1]
            print('Wybrałeś:',z)
            return self.wybor_player1.append(z)
        elif self.player1=='2':
            z=zbior[2]
            print('Wybrałeś:', z)
            return self.wybor_player1.append(z)
        elif self.player1=='3':
            z=zbior[3]
            print('Wybrałeś:', z)
            return self.wybor_player1.append(z)
        else:
            return p1.komunikaty_dla_else()

                                    #komunikaty dla różnych wyników else
    def komunikaty_dla_else(self):
        if self.powtorzenia_palyer1==0:
            print('Nie ma takiej możliwości wybierz 1, 2 lub 3')
        elif self.powtorzenia_palyer1==1:
            print('Czytaj masz wybrać z kalawiatury numerycznej 1 lub 2 lub 3')
        elif self.powtorzenia_palyer1 >1:
            print('Jesteś DEBIL!!! Tak możemy bez końca. Wybierz 1 lub lub 3')
        self.powtorzenia_palyer1 += 1
        class_player_one().player1_wariant_wyboru()

    def liczba_powtorzen(self):
        return self.powtorzenia_palyer1


                                        #zdefiniowanie wyborów player2
class class_player_two():
    wybor_player2 = []
    powtorzenia_palyer2 = 0

    def __init__(self):
        self.player1 = input()

    def player2_wariant_wyboru(self):
        if self.player1 == '1':
            z = zbior[1]
            print('Wybrałeś:', z)
            return self.wybor_player2.append(z)
        elif self.player1 == '2':
            z = zbior[2]
            print('Wybrałeś:', z)
            return self.wybor_player2.append(z)
        elif self.player1 == '3':
            z = zbior[3]
            print('Wybrałeś:', z)
            return self.wybor_player2.append(z)
        else:
            return p2.komunikaty_dla_else()

                                                # komunikaty dla różnych wyników else

    def komunikaty_dla_else(self):
        if self.powtorzenia_palyer2 == 0:
            print('Twoja kolej wybierz 1, 2 lub 3')
        elif self.powtorzenia_palyer2 == 1:
            print('Na numerycznej klawiaturze musisz wybrać 1 lub 2 lub 3')
        elif self.powtorzenia_palyer2 > 1:
            print('Jesteś DEBIL!!! Tak możemy bez końca. Wybierz 1 lub lub 3')
        if p1.liczba_powtorzen() >= 3 and p2.liczba_powtorzen() >= 3:
            print('Mam przyjemność z prawdziwymi głąbami')
        self.powtorzenia_palyer2 += 1
        class_player_two().player2_wariant_wyboru()

    def liczba_powtorzen(self):
        return self.powtorzenia_palyer2

# wybor player 1
print('PLAYER 1')
print('Wybierz 1 lub 2 albo 3')
p1=class_player_one()
p1.player1_wariant_wyboru()


# wybor palyer2
print('PlAYER 2')
print('Wybierz 1 lub 2 albo 3')
p2=class_player_two()
p2.player2_wariant_wyboru()







