import turtle

screen = turtle.Screen()
screen.setup(width=900, height=600)
screen.title("🇮🇳 15 August - Independence Day 🇮🇳")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    t.color(color)
    t.fillcolor(color)

    t.begin_fill()

    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

    t.end_fill()

flag_width = 800
flag_height = 480

x = -400
top_y = 240

band_height = flag_height / 3


draw_rectangle(
    x,
    top_y,
    flag_width,
    band_height,
    "#FF9933"
)

draw_rectangle(
    x,
    top_y - band_height,
    flag_width,
    band_height,
    "white"
)


draw_rectangle(
    x,
    top_y - (2 * band_height),
    flag_width,
    band_height,
    "#138808"
)


chakra_x = 0
chakra_y = 0
chakra_radius = 55

t.penup()
t.goto(chakra_x, chakra_y - chakra_radius)

t.setheading(0)
t.color("#000080")
t.pensize(4)

t.pendown()
t.circle(chakra_radius)


for angle in range(0, 360, 15):

    t.penup()

    # Start from center
    t.goto(chakra_x, chakra_y)

    # Set direction
    t.setheading(angle)

    # Move to edge
    t.forward(chakra_radius)

    # Draw spoke back toward center
    t.pendown()
    t.goto(chakra_x, chakra_y)


t.penup()
t.goto(chakra_x, chakra_y)

t.dot(10, "#000080")


t.penup()
t.goto(-420, 250)
t.pendown()

t.color("gray")
t.pensize(8)

t.goto(-420, -300)

t.goto(-460, -300)
t.goto(-380, -300)

t.penup()

t.goto(0, -350)

t.color("#000080")

t.write(
    "HAPPY INDEPENDENCE DAY",
    align="center",
    font=("Arial", 28, "bold")
)

t.goto(0, -390)

t.color("#FF9933")

t.write(
    "15 AUGUST 🇮🇳",
    align="center",
    font=("Arial", 22, "bold")
)

t.goto(0, -425)

t.color("#138808")

t.write(
    "JAI HIND!",
    align="center",
    font=("Arial", 20, "bold")
)

turtle.done()