import tkinter as tk
import random

# Create the main application window
root = tk.Tk()
root.title("Bubble Sort Visualization")
root.geometry("600x400")

# Create a canvas widget

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()
canvas.configure(bg='black')

# Generate list of heights and corresponding rectangle IDs
num_rectangles = 20
heights = [random.randint(50, 350) for _ in range(num_rectangles)]
rectangles = []

# Initial placement of rectangles
spacing = 600 // num_rectangles
for i in range(num_rectangles):
    x1 = i * spacing
    rect = canvas.create_rectangle(x1, 400, x1 + spacing - 2, 400 - heights[i], fill="blue")
    rectangles.append(rect)

def swap_rectangles(i, j):
    canvas.itemconfig(rectangles[i], fill="red")
    canvas.itemconfig(rectangles[j], fill="red")
    root.update()
    canvas.after(250)

    # Swap heights in the list
    heights[i], heights[j] = heights[j], heights[i]
    
    # Redraw the swapped rectangles
    canvas.coords(rectangles[i], [i * spacing, 400, i * spacing + spacing - 2, 400 - heights[i]])
    canvas.coords(rectangles[j], [j * spacing, 400, j * spacing + spacing - 2, 400 - heights[j]])

    canvas.itemconfig(rectangles[i], fill="blue")
    canvas.itemconfig(rectangles[j], fill="blue")
def bubble_sort():
    n = len(heights)
    for i in range(n):
        for j in range(0, n-i-1):
            if heights[j] > heights[j+1]:
                swap_rectangles(j, j+1)
                root.update()
                canvas.after(500)  # Adjust the delay to see the animation clearly

# Button to start sorting
root.after(2000, bubble_sort)

root.mainloop()
