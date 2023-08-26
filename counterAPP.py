import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter App")
        
        self.counter_value = 0

        self.label = tk.Label(root, text="Counter Value:", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.value_label = tk.Label(root, text=str(self.counter_value), font=("Helvetica", 24, "bold"))
        self.value_label.pack()

        self.increment_button = tk.Button(root, text="Increment", command=self.increment)
        self.increment_button.pack(pady=5)

        self.decrement_button = tk.Button(root, text="Decrement", command=self.decrement)
        self.decrement_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(pady=5)

    def update_counter_label(self):
        self.value_label.config(text=str(self.counter_value))

    def increment(self):
        self.counter_value += 1
        self.update_counter_label()

    def decrement(self):
        if self.counter_value > 0:
            self.counter_value -= 1
            self.update_counter_label()

    def reset(self):
        self.counter_value = 0
        self.update_counter_label()

def main():
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
