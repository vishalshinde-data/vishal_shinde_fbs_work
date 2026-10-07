import turtle

t = turtle.Turtle()
t.speed(5)

while True:
    t.circle(100)
    t.right(10)

turtle.done()


y = x
x = z
print(f'After swapping: x={x}, y={y}')



x=10
y=20

print(f'Before swapping: x={x}, y={y}')

z = y
y = x
x = z
print(f'After swapping: x={x}, y={y}')

