from turtle import Turtle, Screen
from threading import Thread
import timeit

ANGLE  = 2
color1 = 'black'
color  = 'blue'
color2 = 'red'
color3 = 'yellow'

def circles(t, size, small):
    for i in range(10):
        t.circle(size)
        size=size-small

def circle_small(t, size, repeat, small):
  for i in range (repeat):
    circles(t,size,small)
    t.right(360/repeat)

def spiral(turtle, radius, color_name):
    for i in range(360 // ANGLE):
        turtle.color(color_name)
        turtle.circle(radius)
        turtle.left(ANGLE)


class TurtleAnimator(Thread):
    def __init__(self, turtle, rad, col, flag, size):
        Thread.__init__(self)
        self.t = turtle
        self.r = rad
        self.c = col
        self.f = flag
        self.s = size

    def run(self):
        if self.f == 0:
            self.t.speed("fastest")
            spiral(self.t, self.r, self.c)
        else:
            circle_small(self.t, self.s, self.r, self.c)



def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.title('Burning flower')

    s = Turtle(visible=False)
    s.speed('fastest')
    s.color('red')
    thread1 = TurtleAnimator(s, 10, 4, 1, 200)

    t1 = Turtle(visible=False)
    t1.speed(0)
    t1.color('yellow')
    thread2 = TurtleAnimator(t1, 10, 10, 1, 160)
    thread3 = TurtleAnimator(Turtle(visible=False), 10, color3, 0, 0)

    start = timeit.default_timer()

    thread1.start()
    thread2.start()
    thread3.start()

    end = timeit.default_timer()
    print('Time in s', end - start)

    screen.exitonclick()

if __name__ == "__main__":
    main()
