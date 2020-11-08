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

if calcOpti == 0:   # If calcOpti is 0 then quit.
    exit()

if calcOpti == 1:   # Calculating the area of a square.
    print('\nYou have chosen the option: Square')
    SideA = float(input('How Wide is side A: '))
    SideB = float(input('How Wide is side B: '))
    sAxsB = SideA * SideB
    print(f'The Square Area is: {sAxsB:.6f}')

if calcOpti == 2:   # Calculating the volume of a cube.
    print('\nYou have chosen the option: Cube')
    SideA = float(input('How Wide is side A: '))
    SideB = float(input('How Wide is side B: '))
    SideC = float(input('How Wide is side C: '))
    sAxsBxsC = SideA * SideB * SideC
    print(f'The Cube Volume is: {sAxsBxsC:.6f}')

if calcOpti == 3:   # Calculating the volume of a pyramid.
    print('\nYou have chosen the option: Pyramid')
    SideA = float(input('How Wide is side A: '))
    SideB = float(input('How Wide is side B: '))
    Height = float(input('How High is it: '))
    sAxsBxsH = SideA * SideB * Height / 3
    print(f'The Pyramid Volume is: {sAxsBxsH:.6f}')

if calcOpti == 4:   # Calculating the area of a circle.
    print('\nYou have chosen the option: Circle')
    Radius = float(input('How Wide is Radius: '))
    preArea = Radius * Radius
    prePi = math.pi * preArea
    print(f'The Circle Area is: {prePi:.6f}')

if calcOpti == 5:   # Calculating the arch length of a circle.
    print('\nYou have chosen the option: Arch Length')
    Angle = float(input('What is the angle(°): '))
    Radius = float(input('What is the Radius: '))
    a = Angle
    r = Radius
    Answer = a / 360 * math.pi * 2 * r
    print(f'The arch length is: {Answer:.6f}')

if calcOpti == 6:   # Calculating the area of a circle section.
    print('\nYou have chosen the option: Circle Section')
    Angle = float(input('What is the angle(°): '))
    Radius = float(input('What is the Radius: '))
    a = Angle
    r = Radius
    Answer = a / 360 * math.pi * r * r
    print(f'The  Circle Section area is: {Answer:.6f}')

if calcOpti == 7:   # Calculating the volume of a cylinder.
    print('\nYou have chosen the option: Cylinder')
    Radius = float(input('How Wide is Radius: '))
    Height = float(input('How High is it: '))
    preArea = Radius * Radius
    prePi = math.pi * preArea
    preCyl = prePi * Height
    print(f'The Cylinder Volume is: {preCyl:.6f}')

if calcOpti == 8:   # Calculating the volume of a cone.
    print('\nYou have chosen the option: Cone')
    Radius = float(input('How Wide is Radius: '))
    Height = float(input('How High is it: '))
    preArea = Radius * Radius
    prePi = math.pi * preArea
    preCyl = prePi * Height / 3
    print(f'The Cone Volume is: {preCyl:.6f}')

if calcOpti == 9:   # Calculating the volume of a sphere.
    print('\nYou have chosen the option: Sphere')
    Radius = float(input('How Wide is Radius: '))
    r = Radius
    prePi = r * r * r
    pre4 = prePi * math.pi
    preD3 = pre4 * 4
    Answer = preD3 / 3
    print(f'The Sphere Volume is: {Answer:.6f}')

if calcOpti == 10:  # Calculating the area of a triangle
    print('\nYou have chosen the option: Triangle')
    print('Base = Any one of the three sides.')
    Base = float(input('How Wide is Base: '))
    print('\nHeight = The distance between the base\nand the corner opposite the Base')
    Height = float(input('How high is the heigth: '))
    Answer = Base * Height / 2
    print(f'The Triangle Area is: {Answer:.6f}')

if calcOpti == 11:  # Calculating the volume of a prism.
    print('\nYou have chosen the option: Prism')
    print('Base = Any one of the three sides.')
    Base = float(input('How Wide is Base: '))
    Height = float(input('How high is the heigth: '))
    print('\nHeight = The distance between the base\nand the corner opposite the Base')
    Length = float(input('How long is the Prism: '))
    Answer = Base * Height / 2 * Length
    print(f'The Prism Volume is: {Answer:.6f}')