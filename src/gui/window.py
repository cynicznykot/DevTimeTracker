"""
Statistics window for DevTimeTracker.

Provides a simple Tkinter window to display statistics.
"""

import tkinter as tk
from tkinter import ttk

from src.storage.json_storage import JsonStorage

def show_stats_window(storage: JsonStorage):
    """
    Show a window with statistics.

    Args:
        storage: JsonStorage instance.
    """
    # Create window
    root = tk.Tk()
    root.title("DevTimeTracker - Statistics")
    root.geometry("500x400")

    # Title
    title = tk.Label(root, text="📊 Statistics", font=('Arial', 16, 'bold'))
    title.pack(pady=10)

    # Get data
    stats = storage.get_all_stats()
    total = sum(stats.values()) if stats else 0

    # Full Statistics
    hours = total // 3600
    minutes = (total % 3600) // 60
    total_label = tk.Label(
        root,
        text=f"Total time: {hours}h {minutes}m",
        font=('Arial', 12)
    )
    total_label.pack(pady=5)

    # Table by editors
    if stats:
        frame = tk.Frame(root)
        frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        tree = ttk.Treeview(frame, columns=('Editor', 'Time'), show='headings')
        tree.heading('Editor', text='Editor')
        tree.heading('Time', text='Time')

        for editor, seconds in sorted(stats.items(), key=lambda x: x[1], reverse=True):
            h = seconds // 3600
            m = (seconds % 3600) // 60
            tree.insert("", tk.END, values=(editor, f"{h}h, {m}m"))

        tree.pack(fill=tk.BOTH, expand=True)
    else:
        no_data = tk.Label(root, text="No data yet", font=('Arial', 12))
        no_data.pack(pady=20)

    # Close button
    close_btn = tk.Button(root, text='Close', command=root.destroy)
    close_btn.pack(pady=10)

    root.mainloop()

