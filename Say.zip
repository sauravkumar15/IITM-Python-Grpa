import pandas as pd
import matplotlib.pyplot as plt
from jinja2 import Template
import sys
import numpy as np

def main():
    args = sys.argv
    args.pop(0)
    df = pd.read_csv('./data.csv')

    if len(args) == 0:
        display_error()
        sys.exit()
    if args[0] == '-s':
        if len(args) == 1:
            display_error()
            sys.exit()
        write(process_s_data(df, args[1]))
    elif args[0] == '-c':
        if len(args) == 1:
            display_error()
            sys.exit()
        write(process_c_data(df, args[1]))
    else:
        display_error()
        sys.exit()
        
def process_s_data(df, sid):
    courses = df.loc[df['Student id'] == int(sid)]

    if len(courses) == 0:
        display_error()
        sys.exit()

    total = courses[' Marks'].sum()

    # Student template as a string
    student_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Student Data</title>
        <style>
            table {
                border: 1px solid;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid;
            }
        </style>
    </head>
    <body>
        <h1>Student Details</h1>
        <table>
            <tr>
                <th>Student id</th>
                <th>Course id</th>
                <th>Marks</th>
            </tr>
            {% for row in courses %}
            <tr>
                <td>{{ row['Student id'] }}</td>
                <td>{{ row[' Course id'] }}</td>
                <td>{{ row[' Marks'] }}</td>
            </tr>
            {% endfor %}
            <tr>
                <td colspan="2">Total Marks</td>
                <td>{{ total }}</td>
            </tr>
        </table>
    </body>
    </html>
    """
    template = Template(student_template)
    content = template.render(courses=courses.to_dict(orient='records'), total=total)
    
    return content

def process_c_data(df, cid):
    marks = df.loc[df[' Course id'] == int(cid)]

    if len(marks) == 0:
        display_error()
        sys.exit()

    avg = marks[' Marks'].mean()
    max_marks = marks[' Marks'].max()

    export_plot(marks)

    course_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Course Data</title>
        <style>
            table {
                border: 1px solid;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid;
            }
        </style>
    </head>
    <body>
        <h1>Course Details</h1>
        <table>
            <tr>
                <th>Average Marks</th>
                <th>Maximum Marks</th>
            </tr>
            <tr>
                <td>{{ avg }}</td>
                <td>{{ max_marks }}</td>
            </tr>
        </table>
        <img src="./bar-chart.png" height="250">
    </body>
    </html>
    """


    template = Template(course_template)
    content = template.render(avg=avg, max_marks=max_marks)

    return content

def display_error():
    error_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Something Went Wrong</title>
    </head>
    <body>
        <h1>Wrong Inputs</h1>
        <p>Something went wrong</p>
    </body>
    </html>
    """
    template = Template(error_template)
    content = template.render()
    write(content)

def write(content):
    with open("output.html", "w") as f:
        f.write(content)
    print("Written to file")

def export_plot(data):
    freq = data[' Marks'].value_counts().sort_index()
    x = np.array(freq.index)
    
    lower_limit = (x.min() // 10) * 10
    
    plt.figure(figsize=(10, 6))
    plt.bar(x, freq.values, width=1, align='center')
    
    plt.xlim(lower_limit, 100)
    plt.xticks(range(lower_limit, 101, 10))
    
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.savefig('bar-chart.png', dpi=300, bbox_inches='tight')
    plt.close()

html_out = main()
