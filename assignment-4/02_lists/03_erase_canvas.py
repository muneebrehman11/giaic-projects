import tkinter as tk

CELL_SIZE = 40
GRID_WIDTH = 10
GRID_HEIGHT = 10
ERASER_SIZE = 60

class CanvasEraserApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=GRID_WIDTH*CELL_SIZE, height=GRID_HEIGHT*CELL_SIZE)
        self.canvas.pack()

        self.cells = {}  # Store rectangle items by their coordinates
        self.create_grid()

        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline="black", fill="white", stipple="gray50")
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def create_grid(self):
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                self.cells[(row, col)] = rect

    def move_eraser(self, event):
        x1 = event.x - ERASER_SIZE // 2
        y1 = event.y - ERASER_SIZE // 2
        x2 = event.x + ERASER_SIZE // 2
        y2 = event.y + ERASER_SIZE // 2

        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Check for overlap with grid cells
        for (row, col), rect in self.cells.items():
            coords = self.canvas.coords(rect)
            if self.rects_overlap((x1, y1, x2, y2), coords):
                self.canvas.itemconfig(rect, fill="white")

    def rects_overlap(self, r1, r2):
        # Check if two rectangles (x1, y1, x2, y2) overlap
        return not (r2[2] <= r1[0] or r2[0] >= r1[2] or r2[3] <= r1[1] or r2[1] >= r1[3])

def main():
    root = tk.Tk()
    root.title("Canvas Eraser")
    app = CanvasEraserApp(root)
    root.mainloop()

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
