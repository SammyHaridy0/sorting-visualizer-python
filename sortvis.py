import tkinter as tk
import random

class BubbleSortVisualizer:
    def __init__(self, root, num_rectangles=20):
        self.root = root
        self.canvas = tk.Canvas(root, width=600, height=400, bg='black')
        self.canvas.pack()
        self.num_rectangles = num_rectangles
        self.rectangles = []
        self.heights = [random.randint(50, 350) for _ in range(num_rectangles)]
        self.spacing = 600 // num_rectangles
        self.draw_rectangles()

    def draw_rectangles(self):
        for i in range(self.num_rectangles):
            x1 = i * self.spacing
            rect = self.canvas.create_rectangle(x1, 400, x1 + self.spacing - 2, 400 - self.heights[i], fill="blue")
            self.rectangles.append(rect)

    def swap_rectangles(self, i, j):
        self.canvas.itemconfig(self.rectangles[i], fill="red")
        self.canvas.itemconfig(self.rectangles[j], fill="red")
        self.root.update()
        self.canvas.after(250)

        self.heights[i], self.heights[j] = self.heights[j], self.heights[i]
        self.canvas.coords(self.rectangles[i], [i * self.spacing, 400, i * self.spacing + self.spacing - 2, 400 - self.heights[i]])
        self.canvas.coords(self.rectangles[j], [j * self.spacing, 400, j * self.spacing + self.spacing - 2, 400 - self.heights[j]])

        self.canvas.itemconfig(self.rectangles[i], fill="blue")
        self.canvas.itemconfig(self.rectangles[j], fill="blue")

    def bubble_sort(self):
        n = len(self.heights)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.heights[j] > self.heights[j+1]:
                    self.swap_rectangles(j, j+1)
                    self.root.update()
                    self.canvas.after(500)

    def start_sorting(self):
        self.root.after(2000, self.bubble_sort)

# Usage
root = tk.Tk()
root.title("Bubble Sort Visualization")
root.geometry("600x400")
app = BubbleSortVisualizer(root)
app.start_sorting()
root.mainloop()
