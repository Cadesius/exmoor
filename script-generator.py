# START

# Note: Selenium must be installed onto the system prior to running this code. Enter the following command into a command prompt window: `python -m pip install selenium`

# Import required packages

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import pathlib

# Define contents of the HTML page

htmlpage = """<!DOCTYPE html>
<html lang="en">
<meta name="viewport" content="width=device-width, initial-scale=1">

<head>
    <link rel="stylesheet" href="../css/root-stylesheet.css">
    <link rel="stylesheet" href="../css/home.css">
    <link rel="stylesheet" href="../css/archive.css">
    <link rel="stylesheet" href="../css/footer.css">
    <link rel="stylesheet" href="../css/tables.css">
    <link rel="stylesheet" href="../css/modal.css">
    <link rel="stylesheet" href="../css/theme-switch.css">
    <link rel="stylesheet" href="../css/media-1600.css">
    <link rel="stylesheet" href="../css/media-980.css">
    <link rel="stylesheet" href="../css/media-750.css">
    <link rel="stylesheet" href="../css/media-print.css">
    <link rel="shortcut icon" href="../media/head/logo-icon.png">
    <link rel="shortcut icon" href="../media/head/logo-icon.png">
    <title>{fullname} - The Exmoor Oral History Archive</title>
</head>

<body style="background-color: rgba(1,1,1,0); padding-bottom: 20%;">

<div class="content">

    <div class="interview-content">

        <div>
            <div class="image-border">
                <img class="main-image" src="../media/photographs/{name}.jpg" alt="{fullname}">
            </div>
        </div>

        <div class="interview-text-block">

            <h2 style="text-align: left; margin-top: 0;">{fullnamecaps}</h2>

            <table class="links-table">
                <tr>
                    <td><a class="link" style="margin-left: 0;" href="{cataloguelink}">CATALOGUE</a></td>
                    <td><a class="link" href="{recordinglink}">INTERVIEW</a></td>
                    <td><a class="link" style="margin-right: 0;" href="{transcriptlink}">TRANSCRIPT</a></td>
                </tr>
            </table>

            <p class="stats-text"><b>BORN: </b>{born}</p>
            <p class="stats-text"><b>LIVED: </b>{lived}</p>
            <p class="stats-text"><b>RECORDING MADE: </b>{date}</p>
            <p class="stats-text"><b>RECORDING LENGTH: </b>{length}</p>

            <p class="body-text">{summary_para1}</p>
            <p class="body-text">{summary_para2}</p>
            <p class="body-text">{summary_para3}</p>
            <p class="body-text">{summary_para4}</p>
            <p class="body-text"><i>{summary_postscript}</i></p>
            <p style="font-size: 10pt;" class="body-text">Photograph by Mark J. Rattenbury</p>

            <div class="print-container">
                <table class="links-table" style="margin-top: 8%;">
                    <tr>
                        <td><a class="link" href="Javascript:window.print();" style="font-size: 12pt;">PRINT THIS PAGE</a></td>
                    </tr>
                </table>
            </div>

        </div>

    </div>

</div>

<div id="theme-switch-icon" style="display: none;"></div>

</body>

</html>

<script src="../javascript/theme-switch.js"></script>"""

# Define the line that is to be piped into the modal-script.js Javascript file

jscript = """`modal_creator ("{lastname}", "{firstname}", "{fullname}", "{lived}")`,"""

# Define variables to be substituted into the HTML page and Javascript code

firstname = input ("Enter first name: ")
lastname = input ("Enter last name: ")
fullname = firstname.title () + " " + lastname.title ()
name = fullname.lower ()
name = name.replace (" ", "_")
fullnamecaps = fullname.upper ()
firstname = firstname.upper()
lastname = lastname.upper()

# image = name + ".jpg"
# thumbs = input ("\nEnter thumbnail image title: ")

iframe = name + ".html"

cataloguelink = input ("\nEnter link to catalogue page: ")
recordinglink = cataloguelink + "/1"
transcriptlink = cataloguelink + "/2"

# width = input ("\nEnter image width (as a percentage of total page width): ")

# Launch Selenium webdriver with Firefox as the browser

driver=webdriver.Firefox ()

# Navigate webdriver to the catalogue page

driver.get (cataloguelink)

time.sleep (3)

# Find all record values

fieldData = driver.find_elements (By.CLASS_NAME, "recordFieldValues")

# Define variables based on record values

born = fieldData [2].text
lived = fieldData [3].text
place = lived
date = fieldData [4].text
length = fieldData [5].text
summary = fieldData [6].text

# Determine number of paragraphs in summary

para_counter = summary.count ("\n")

# Define blank paragraph variables

summary_para1 = ""
summary_para2 = ""
summary_para3 = ""
summary_para4 = ""
summary_postscript = ""

# Split summary into individual paragraphs based on linebreaks, which are then formatted into an array

para_list = summary.split ("\n")

# Check for a postscript, which will need to be formatted differently in the HTML page. If a postscript is found, it will be added to the HTML page, and then deleted from the summary array, and the count for paragraphs will be reduced by one.

if "passed away in" in para_list [para_counter]:
    summary_postscript = para_list [para_counter]
    del para_list [para_counter]
    para_counter = para_counter - 1

# Define paragraphs based on the summary array, using if loops to allow flexibility in number of paragraphs

for i in range (para_counter + 1):
    if i == 0:
        summary_para1 = para_list [i]
    if i == 1:
        summary_para2 = para_list [i]
    if i == 2:
        summary_para3 = para_list [i]
    if i == 3:
        summary_para4 = para_list [i]

# Define the HTML page with the correct variables being substituted in to complete the page

htmlpage_formatted = htmlpage.format (name=name, fullname=fullname, fullnamecaps = fullnamecaps, born = born, lived = lived, date = date, length = length, summary_para1 = summary_para1, summary_para2 = summary_para2, summary_para3 = summary_para3, summary_para4 = summary_para4, summary_postscript = summary_postscript, cataloguelink = cataloguelink, recordinglink = recordinglink, transcriptlink = transcriptlink)

# Remove blank paragraph and postscript elements from the HTML page, to avoid formatting issues once generated

htmlpage_formatted = htmlpage_formatted.replace ("""<p class="body-text"><i></i></p>""", "")
htmlpage_formatted = htmlpage_formatted.replace ("""<p class="body-text"></p>""", "")

# Define the Javascript code with the correct variables being substituted in to complete the script

jscript_formatted = jscript.format (fullname = fullname, lived = lived, firstname = firstname, lastname = lastname)

# Close the Selenium webdriver

driver.close ()

print ("")

# Define save directory for the HTML page

save_directory = 'html/' + name + '.html'

# Write the formatted HTML page to a newly created file in the specified save directory (this will overwrite any existing HTML file with the same name)

with open (save_directory, 'w') as file:
    file.write (htmlpage_formatted)

# Append the formatted Javascript code to the modal-script.js file (this will not overwrite existing code for individuals with the same name, these must be removed)

# with open ("modal-script.js", "a") as file:
#     file.write ("\n" + jscript_formatted)

# Pipe the formatted Javascript code into the modal-script.js file as the first item of the list of interviewees (this will not overwrite existing code for individuals with the same name, these must be removed)

with open ("javascript/modal-script.js", "r") as input:
    with open ("javascript/modal-script-temp.js", "w") as output:
        for line in input:
            if """const modal_creators = ["""  in line.strip ("\n"):
                line = line.replace (line, line + "\t" + jscript_formatted + "\n")
            output.write (line)

os.replace('javascript/modal-script-temp.js', 'javascript/modal-script.js')

# END