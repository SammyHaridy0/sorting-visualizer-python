import tkinter as tk
import random

class BubbleSortVisualizer:
    def __init__(self, root, num_rectangles=20):
        self.root = root
        self.canvas = tk.Canvas(root, width=600, height=400, bg='black')
        self.canvas.pack()
        self.num_rectangles = num_rectangles
        self.rectangles = []
        self.texts = []
        self.heights = [random.randint(25, 375) for _ in range(num_rectangles)]
        self.spacing = 600 // num_rectangles
        self.draw_rectangles()

        self.sort_button = tk.Button(root, text="Start Sorting", command=self.bubble_sort)
        self.sort_button.pack()
        self.root.update()
        

    def draw_rectangles(self):
        for i in range(self.num_rectangles):
            x1 = i * self.spacing
            y1 = 400 - self.heights[i]
            rect = self.canvas.create_rectangle(x1, 400, x1 + self.spacing - 2, y1, fill="blue")
            text = self.canvas.create_text(x1 + self.spacing // 2, 395, text=str(self.heights[i]), fill="white", font=('Helvetica', '11'))
            self.rectangles.append(rect)
            self.texts.append(text)

    def swap_rectangles(self, i, j):
        # Highlight the rectangles to be swapped
        self.canvas.itemconfig(self.rectangles[i], fill="red")
        self.canvas.itemconfig(self.rectangles[j], fill="red")
        self.root.update()
        self.canvas.after(100)

        # Swap the heights data for accurate rectangle drawing
        self.heights[i], self.heights[j] = self.heights[j], self.heights[i]

        # Swap the positions in the list to maintain index consistency
        self.rectangles[i], self.rectangles[j] = self.rectangles[j], self.rectangles[i]
        self.texts[i], self.texts[j] = self.texts[j], self.texts[i]

        # Calculate new positions for rectangles
        x1_i = i * self.spacing
        x1_j = j * self.spacing
        self.canvas.coords(self.rectangles[i], [x1_i, 400, x1_i + self.spacing - 2, 400 - self.heights[i]])
        self.canvas.coords(self.rectangles[j], [x1_j, 400, x1_j + self.spacing - 2, 400 - self.heights[j]])

        # Update text label positions to new swapped locations
        self.canvas.coords(self.texts[i], [x1_i + self.spacing // 2, 395])
        self.canvas.coords(self.texts[j], [x1_j + self.spacing // 2, 395])

        # Reset rectangle colors back to blue
        self.canvas.itemconfig(self.rectangles[i], fill="blue")
        self.canvas.itemconfig(self.rectangles[j], fill="blue")

        self.root.update()




    def bubble_sort(self):
        n = len(self.heights)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.heights[j] > self.heights[j+1]:
                    self.swap_rectangles(j, j+1)
                    self.root.update()
                    self.canvas.after(200)
    

# Usage
root = tk.Tk()
root.title("Sort Visualization")
app = BubbleSortVisualizer(root)
root.mainloop()
