from tkinter import ttk
import tkinter as tk
class Template(object):

    def labelEntry(self, window, textData, var,rowData, status= ""):
        tk.Label(window, text=textData).grid(column=0, row=rowData)
        tb=tk.Entry(window, textvariable=var, width=27, show=status)
        tb.grid(column=1, row=rowData)
    
    def labelEntryPatient(self, window, textData, var,rowData,):
        tk.Label(window, text=textData,  background="#FFA781", foreground="white").grid(column=0, row=rowData, sticky="W")
        tb=tk.Entry(window, textvariable=var, width=25,bd=3, relief=tk.GROOVE)
        tb.grid(column=1, row=rowData)
    
    def button(self, window, textData, comData, col, rowData):
        bt=tk.Button(window, text=textData, command=comData, width=10)
        bt.grid(column=col, row=rowData, pady=5)

    def comboPatient(self, window, textData, var, values,rowdata):
        tk.Label(window, text=textData,  background="#FFA781", foreground="white").grid(column=0,row=rowdata, sticky="W")
        combo=ttk.Combobox(window, textvariable=var, width=24)
        combo['values']=values
        combo.grid(column=1, row=rowdata)
    
    def form(self, window, textData, rowData, dataType):
        tk.Label(window, text=textData, background="#FFA781", foreground="white",).grid(column=0,row=rowData, sticky="W")
        tb=tk.Entry(window, textvariable=dataType)
        tb.grid(column=1,row=rowData)
    
    def label(self, window, textData, col):
        tk.Label(window, text=textData, font="Consolas 7", background="#F2EAED").grid(column=col,row=0, padx=2, ipady=3)
    
    def buttonHp(self, window, textData, com, col):
        bt=tk.Button(window, text=textData, command=com, width=18)
        bt.grid(column=col, row=1)