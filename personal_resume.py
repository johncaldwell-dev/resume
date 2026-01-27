from fpdf import FPDF
import os

#page format
format = 'letter'
# title or headers
font_family = 'Times'
title_size = 16
subtitle_size = 12
title_height = 35
info_height = 15
subheader_size = 15
subheader_height = 30
normal_text_size = 12
normal_height = 12
align_subtitles = 'L'

def boldText(text): return('\033[1m {}\033[0m'.format(text))
pdf = FPDF(orientation='P', unit='pt', format=format)
pdf.add_page()


pdf.set_font(font_family, size=title_size)
full_name = f"John M. Caldwell, Jr."
pdf.cell(w=0, h=title_height, txt=full_name, align='L', ln=True)

pdf.set_font(font_family, size=subtitle_size)
address = f'Marietta, OH'
phone = f'(740) 516-7495'
email = fr'john.caldwell4@gmail.com'
github = fr'GitHub: https://github.com/johncaldwell-dev/'
portfolio = fr'Portfolio: https://johncaldwell4.github.io/portfolio/'
pdf.cell(w=0, h=info_height, txt=f'{address} | {phone} | {email}', ln=True)
pdf.cell(w=0, h=info_height, txt=f'{github} | {portfolio}', ln=True)

pdf.multi_cell(w=0, h=15)

pdf.set_font(font_family, style='B', size=subheader_size)
pdf.cell(w=0, h=subheader_height, txt="summary".upper(), align=align_subtitles, ln=True)

pdf.set_font(font_family, size=normal_text_size)
summary = '''Highly experienced computer professional with over 20 years of hands-on experience in programming, system administration, and networking. Proven ability to successfully implement, maintain, and troubleshoot computer systems. Strong commitment to customer service and a commitment to ensure user experience and productivity is always at its best. Skilled in setting up and maintaining computer systems, as well as coding and software engineering principles.'''
pdf.multi_cell(w=0, h=info_height, txt=summary)

pdf.multi_cell(w=0, h=15)

pdf.set_font(font_family, style='B', size=subheader_size)
pdf.cell(w=0, h=subheader_height, txt="technical skills".upper(), align=align_subtitles, ln=True)



languages_label = "Languages:"
languages_values = "Powershell, VB.NET, Python, JavaScript, HTML/CSS, SQL"

pdf.set_font("Arial", "B", 12)
pdf.cell(w=75, h=15, txt=languages_label, ln=False)

pdf.set_font("Arial", "", 12)
pdf.cell(w=30, h=15, txt=languages_values, ln=1)

frameworks_label = "Frameworks/Libraries:" 
frameworks_values = "Bootstrap, React, Pandas, Numpy, os, CustomTkinter, Pillow"

pdf.set_font("Arial", "B", 12)
pdf.cell(w=135, h=15, txt=frameworks_label, ln=False)
pdf.set_font("Arial", "", 12)
pdf.cell(w=30, h=15, txt=frameworks_values, ln=1)

tools_label = "Tools & Technologies:"
tools_values = 'Git, Github, Docker (basics), Azure, ChatGPT, Deepseek, Amazon Alexa,   VS Code, LabTech, ConnectWise, SolarWind, Office 365, SQLite'

pdf.set_font("Arial", "B", 12)
pdf.cell(w=135, h=15, txt=tools_label, ln=False)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(w=0,h=15, txt=tools_values)

pdf.multi_cell(w=0, h=15)

pdf.set_font(font_family, style='B', size=subheader_size)
pdf.cell(w=0, h=subheader_height, txt="projects".upper(), align=align_subtitles, ln=True)

pdf.multi_cell(w=0, h=15)

pdf.set_font(font_family, style='B', size=subheader_size)
pdf.cell(w=0, h=subheader_height, txt="education".upper(), align=align_subtitles, ln=True)

pdf.multi_cell(w=0, h=15)

pdf.set_font(font_family, style='B', size=subheader_size)
pdf.cell(w=0, h=subheader_height, txt="certifications".upper(), align=align_subtitles, ln=True)

pdf.multi_cell(w=0, h=15)

pdf.set_font(font_family, style='B', size=subheader_size)
pdf.cell(w=0, h=subheader_height, txt="volunteer".upper(), align=align_subtitles, ln=True)

pdf.output('resume.pdf')
