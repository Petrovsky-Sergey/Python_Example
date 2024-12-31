# эта программа наносит звезды созвездия Орион
# названия звезд и линии созвездия
import turtle

# задать размер окна
turtle.setup(500,600)

# установить черепаху
turtle.penup()
turtle.hideturtle()

# создать именование константы для звездных координат
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDLE_BELTSTAR_X = 0
MIDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# нанести звезды
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) # левое плечо
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) # правое плечо
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) # левая звезда в поясе
turtle.dot()
turtle.goto(MIDLE_BELTSTAR_X, MIDLE_BELTSTAR_Y) # средняя звезда в поясе
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) # правая звезда в поясе
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) # левое колено
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) # правое колено
turtle.dot()

# вывести названия звезд
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) # левое плечо
turtle.write('Бетельгейзе')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) # правое плечо
turtle.write('Хатиса')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) # левая звезда в поясе
turtle.write('Альнитак')
turtle.goto(MIDLE_BELTSTAR_X, MIDLE_BELTSTAR_Y) # средняя звезда в поясе
turtle.write('Альнилам')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) # правая звезда в поясе
turtle.write('Минтака')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) # левое колено
turtle.write('Саиф')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) # правое колено
turtle.write('Ригель')

# нанести линию из левого плеча в левую звезду пояса
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

# нанести линию из правого плеча в правую звезду пояса
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# нанести линию из левой звезды пояса в среднюю звезду пояса
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDLE_BELTSTAR_X, MIDLE_BELTSTAR_Y)
turtle.penup()

# нанести линию из средней звезды пояса в правую звезду пояса
turtle.goto(MIDLE_BELTSTAR_X, MIDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# нанести линию из левого плеча в левое колено
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

# нанести линию из правой звезды пояса в правое колено
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.penup()

# оставить окно открытым
turtle.done()
