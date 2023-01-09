# GPA-Tool-for-Command-Line-and-GUI

A program to track grades and view and edit them directly in terminal instead of logging into portal and checking each term's grade and requesting a transcript.
<br>Additionally, A GUI pop-up can be displayed from gui.py to view grades in a more visual format along with an option to plot grade progression over time. Note that grades will need to entered in chronological order to view this accurately.
### Usage
Add courses to a txt file with format _COURSE_NAME LETTER_GRADE CREDITS_ with 1 course per line. See courses.txt for an example.
### For usage in terminal:
* Courses can be added directly from the txt file or from terminal using **-a COURSE_NAME LETTER_GRADE CREDITS**<br>
* Courses can be removed directly from the txt file or from terminal using **-r COURSE_NAME**<br>
* Course list can be cleared from terminal using **-c**
