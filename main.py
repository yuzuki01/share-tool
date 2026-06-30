import tkinter as tk

class FigurePlot:
    def __init__(self, parent, width=200, height=110, x=5, y=5):
        self.canvas = tk.Canvas(parent, width=width, height=height, bg="white")
        self.canvas.place(x=x, y=y)
        self.width = width
        self.height = height
    
    def draw_axes(self):
        # X轴
        self.canvas.create_line(15, 95, 185, 95, fill="black", width=1)
        # Y轴
        self.canvas.create_line(15, 95, 15, 15, fill="black", width=1)
        
        # X轴刻度
        for x in [40, 80, 120, 160]:
            self.canvas.create_line(x, 95, x, 90, fill="black")
            self.canvas.create_text(x, 103, text=str(x-15), font=("Arial", 7))
        
        # Y轴刻度
        for y in [75, 55, 35]:
            self.canvas.create_line(15, y, 20, y, fill="black")
            self.canvas.create_text(8, y, text=str(95-y), font=("Arial", 7))
    
    def plot_line(self, data_points, line_color="blue", point_color="red"):
        # 绘制折线
        for i in range(len(data_points) - 1):
            x1, y1 = data_points[i]
            x2, y2 = data_points[i + 1]
            self.canvas.create_line(x1, y1, x2, y2, fill=line_color, width=2)
        
        # 绘制数据点
        for x, y in data_points:
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill=point_color, outline=point_color)

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("折线图示例")
        self.root.geometry("400x120")
        self.root.resizable(False, False)
        
        # 创建绘图对象
        self.plot = FigurePlot(self.root)
        self.plot.draw_axes()
        self.plot.plot_line([(40, 75), (80, 55), (120, 65), (140, 35), (160, 60)])
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
