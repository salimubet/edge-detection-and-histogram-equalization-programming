import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, root)
chart_type.get_tk_widget().pack()
df = df[['First Column','Second Column']].groupby('First Column').sum()
df.plot(kind='Chart Type such as bar', legend=True, ax=ax)
ax.set_title('The Title for your chart')
