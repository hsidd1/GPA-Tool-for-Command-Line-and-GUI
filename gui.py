#Author: Hamza Siddiqui
#Date: 2023-01-08
'''
GUI Display for grades from text file
Run to view GPA in a pop-up window and view grade progression over time

'''
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from sys import argv
from gpa_calculator import courses, calculate_gpa, get_courses



# Edit file name if needed or specify from command line
filename = argv[1] if len(argv) > 1 else "courses.txt" #<--- CHANGE HERE

# Output courses, grades and overall GPA
get_courses()
output = "Course               Grade\n--------------------------------------------------\n"
for course in courses:
  course_name = course[0]
  course_grade = course[1]
  output += f"{course_name:<20} {course_grade}\n"

gpa = calculate_gpa(courses)
output += f"GPA: {gpa:.2f}\n"
if gpa >= 3.5:
  output += 'Congratulations! You are on the Dean\'s Honour List!\n'

# Create pop-up window
root = tk.Tk()
#root.geometry('500x550')
root.title("GPA Calculator")
root['bg'] = '#CDCDC0'



# Function to plot GPA
def plot_gpa():
  fig, ax = plt.subplots()
  canvas = FigureCanvasTkAgg(fig, root)

  # Compute the GPA for each point in time
  gpas = []
  for i in range(len(courses)):
      gpas.append(calculate_gpa(courses[:i+1]))

  # Plot GPA over time
  ax.plot(gpas)
  ax.set_xlabel('Time')
  ax.set_ylabel('GPA')
  canvas.draw()
  canvas.get_tk_widget().pack()


# Table-like Output Display to display output
label = tk.Label(root, text=output, font=("Helvetica", 14), justify=tk.LEFT)
label.pack()

# Button to plot GPA
plot_button = tk.Button(root, text='Plot GPA', height=3, width=7, command=plot_gpa)
plot_button.pack(pady=10)

# Function to close window
def close_window():
    plt.close()
    root.destroy()

# Button to exit pop-up
exit_button = tk.Button(root, text="Exit", height=3, width=5, command=close_window)
exit_button.pack(pady=10)

root.mainloop()
root.protocol("WM_DELETE_WINDOW", close_window)