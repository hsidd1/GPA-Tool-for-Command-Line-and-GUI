# GPA-Tool-for-Command-Line-and-GUI
A program to track course grades and also view and edit them directly in terminal instead of logging into portal and checking each term's grade and requesting a transcript.
<br>Additionally, A GUI pop-up can be displayed from [gui.py](gui.py) to view grades in a visual format along with an option to plot grade progression over time.
# Usage
Add courses to a txt file with format `COURSE_NAME LETTER_GRADE CREDITS` with 1 course per line as in [courses.txt](courses.txt).
### For usage in terminal:
* Courses can be added directly from the txt file or from terminal using `-a COURSE_NAME LETTER_GRADE CREDITS`<br>
* Courses can be removed directly from the txt file or from terminal using `-r COURSE_NAME`<br>
* Course list can be cleared from terminal using `-c`
# Demo
## Terminal View
![Terminal demo](/demo/cli_demo.png)
## GUI Pop-up
![GUI demo](/demo/gui_demo.png)

