import turtle
from PIL import Image
def draw_image(image_path):
    # Load the image
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure image is in RGB mode
    img = img.resize((50, 50))  # Resize to make it manageable for turtle
    # Create turtle screen
    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    screen.bgcolor("white")
    screen.title("Image Drawer of Small pixels")
    # Create turtle
    drawer = turtle.Turtle()
    drawer.speed(100)
    drawer.penup()
    drawer.hideturtle()
    # Draw the image
    pixel_size = 5
    start_x = -250
    start_y = 250
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b = img.getpixel((x, y))
            color = (r / 255, g / 255, b / 255)  # Normalize the color
            drawer.goto(start_x + x * pixel_size, start_y - y * pixel_size)
            drawer.pendown()
            drawer.fillcolor(color)
            drawer.begin_fill()
            for _ in range(4):
                drawer.forward(pixel_size)
                drawer.right(90)
            drawer.end_fill()
            drawer.penup()
    turtle.done()
# Example usage
draw_image("Ironman.jpeg")
