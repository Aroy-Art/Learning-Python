import math

print('''Which Area/Volume Are You Calculating
[0]  Quit
[1]  Square
[2]  Cube
[3]  Pyramid
[4]  Circle
[5]  Arch Length
[6]  Circle Section
[7]  Cylinder
[8]  Cone
[9]  Sphere
[10] Triangle
[11] Prism''')

calcOpti = int(input('Choose An Option For The List Above: '))

if calcOpti == 1:
    print('\nYou have chosen the option: Square')
    SideA = float(input('How Wide is side A: '))
    SideB = float(input('How Wide is side B: '))
    sAxsB = SideA * SideB
    print(f'The Square Area is: {sAxsB:.3f}')

if calcOpti == 2:
    print('\nYou have chosen the option: Cube')
    SideA = float(input('How Wide is side A: '))
    SideB = float(input('How Wide is side B: '))
    SideC = float(input('How Wide is side C: '))
    sAxsBxsC = SideA * SideB * SideC
    print(f'The Cube Volume is: {sAxsBxsC:.3f}')

if calcOpti == 3:
    print('\nYou have chosen the option: Pyramid')
    SideA = float(input('How Wide is side A: '))
    SideB = float(input('How Wide is side B: '))
    Height = float(input('How High is it: '))
    sAxsBxsH = SideA * SideB * Height / 3
    print(f'The Pyramid Volume is: {sAxsBxsH:.3f}')

if calcOpti == 4:
    print('\nYou have chosen the option: Circle')
    Radius = float(input('How Wide is Radius: '))
    preArea = Radius * Radius
    prePi = 3.14159265359 * preArea
    print('The Circle Area is: ', prePi)

if calcOpti == 5:
    print('\nYou have chosen the option: Arch Length')
    Angle = float(input('What is the angle(°): '))
    Radius = float(input('What is the Radius: '))
    a = Angle
    r = Radius
    Answer = a / 360 * 3.14159265359 * 2 * r
    print('The arch length is: ', Answer)

if calcOpti == 6:
    print('\nYou have chosen the option: Circle Section')
    Angle = float(input('What is the angle(°): '))
    Radius = float(input('What is the Radius: '))
    a = Angle
    r = Radius
    Answer = a / 360 * 3.14159265359 * r * r
    print('The  Circle Section area is: ', Answer)

if calcOpti == 7:
    print('\nYou have chosen the option: Cylinder')
    Radius = float(input('How Wide is Radius: '))
    Height = float(input('How High is it: '))
    preArea = Radius * Radius
    prePi = 3.14159265359 * preArea
    preCyl = prePi * Height
    print('The Cylinder Volume is: ', preCyl)

if calcOpti == 8:
    print('\nYou have chosen the option: Cone')
    Radius = float(input('How Wide is Radius: '))
    Height = float(input('How High is it: '))
    preArea = Radius * Radius
    prePi = 3.14159265359 * preArea
    preCyl = prePi * Height / 3
    print('The Cone Volume is: ', preCyl)

if calcOpti == 9:
    print('\nYou have chosen the option: Sphere')
    Radius = float(input('How Wide is Radius: '))
    r = Radius
    prePi = r * r * r
    pre4 = prePi * 3.14159265359
    preD3 = pre4 * 4
    Answer = preD3 / 3
    print('The Sphere Volume is: ', Answer)

if calcOpti == 10:
    print('\nYou have chosen the option: Triangle')
    print('Base = Any one of the three sides.')
    Base = float(input('How Wide is Base: '))
    print('\nHeight = The distance between the base\nand the corner opposite the Base')
    Height = float(input('How high is the heigth: '))
    Answer = Base * Height / 2
    print('The Triangle Area is: ',Answer )

if calcOpti == 11:
    print('\nYou have chosen the option: Prism')
    print('Base = Any one of the three sides.')
    Base = float(input('How Wide is Base: '))
    Height = float(input('How high is the heigth: '))
    print('\nHeight = The distance between the base\nand the corner opposite the Base')
    Length = float(input('How long is the Prism: '))
    Answer = Base * Height / 2 * Length
    print('The Prism Volume is: ',Answer )

if calcOpti == 0:
    exit()