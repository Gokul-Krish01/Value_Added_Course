import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
import os

class Student:
    def __init__(self):
        self.name = None
        self.regno = None
        self.mark1 = None
        self.mark2 = None
        self.mark3 = None
        self.average = None

    def details(self, name, regno, mark1, mark2, mark3):
        self.name = name
        self.regno = regno
        self.mark1 = float(mark1)
        self.mark2 = float(mark2)
        self.mark3 = float(mark3)
        self.average = (self.mark1 + self.mark2 + self.mark3) / 3

    def to_list(self):
        return [self.name, self.regno, self.mark1, self.mark2, self.mark3, self.average]

class StudentRankingApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Student Ranking System")
        self.students = []
        self.csv_file = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="CSV File Path:").grid(row=0, column=0, padx=5, pady=5)
        self.filepath_entry = tk.Entry(self.window)
        self.filepath_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.window, text="Set File Path", bg="lightgreen", command=self.set_file_path).grid(row=0, column=2, padx=5, pady=5)

        labels = ["Name:", "Register Num:", "Mark 1:", "Mark 2:", "Mark 3:"]
        self.entries = []
        for i, text in enumerate(labels):
            label = tk.Label(self.window, text=text)
            label.grid(row=i + 1, column=0, padx=5, pady=5)
            entry = tk.Entry(self.window)
            entry.grid(row=i + 1, column=1, padx=5, pady=5)
            self.entries.append(entry)

        self.addbtn = tk.Button(self.window, text="Add Student", bg="skyblue", command=self.add_student)
        self.addbtn.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

        self.rankbtn = tk.Button(self.window, text="Show Rankings", bg="violet", command=self.show_rankings)
        self.rankbtn.grid(row=len(labels) + 2, column=0, columnspan=2, pady=10)

        self.plotbtn = tk.Button(self.window, text="Plot Rankings", bg="orange", command=self.plot_rankings)
        self.plotbtn.grid(row=len(labels) + 3, column=0, columnspan=2, pady=10)

    def set_file_path(self):
        self.csv_file = self.filepath_entry.get()
        if not self.csv_file:
            messagebox.showerror("Error", "Please enter a valid file path")
        else:
            self.load_students_from_csv()

    def add_student(self):
        if not self.csv_file:
            messagebox.showerror("Error", "Please set the file path first")
            return

        name, regno, mark1, mark2, mark3 = [entry.get() for entry in self.entries]

        if not (name and regno and mark1 and mark2 and mark3):
            messagebox.showerror("Error", "All fields must be filled")
            return

        student = Student()
        student.details(name, regno, mark1, mark2, mark3)
        self.students.append(student.to_list())
        self.save_student_to_csv(student)

        for entry in self.entries:
            entry.delete(0, tk.END)

    def show_rankings(self):
        if not self.students:
            messagebox.showerror("Error", "No students to rank")
            return

        self.students.sort(key=lambda x: x[5], reverse=True)

        rankings = "\nStudent Rankings:\n"
        for rank, student in enumerate(self.students, start=1):
            rankings += f"Rank {rank}: {student[0]} (Reg No: {student[1]}), Average: {student[5]:.2f}\n"

        messagebox.showinfo("Rankings", rankings)

    def plot_rankings(self):
        if not self.students:
            messagebox.showerror("Error", "No students to plot")
            return

        names = [student[0] for student in self.students]
        averages = [student[5] for student in self.students]

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(names, averages, color='skyblue')
        ax.set_xlabel('Student Name')
        ax.set_ylabel('Average Marks')
        ax.set_title('Student Rankings Based on Average Marks')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=8, column=0, columnspan=2, pady=10)

    def save_student_to_csv(self, student):
        file_exists = os.path.isfile(self.csv_file)
        with open(self.csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Name', 'Register Num', 'Mark 1', 'Mark 2', 'Mark 3', 'Average'])
            writer.writerow(student.to_list())

    def load_students_from_csv(self):
        if os.path.isfile(self.csv_file):
            with open(self.csv_file, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  
                self.students = [row for row in reader]

if __name__ == "__main__":
    window = tk.Tk()
    app = StudentRankingApp(window)
    window.mainloop()
