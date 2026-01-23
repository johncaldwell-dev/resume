import pandas
from fpdf import FPDF

resume_location = r'C:\Users\jcaldwell\Desktop\Personal\personal_info_background.xlsx'
df = pandas.read_excel(resume_location)

pdf = FPDF(orientation='P', unit='pt', format='letter')
pdf.add_page()

