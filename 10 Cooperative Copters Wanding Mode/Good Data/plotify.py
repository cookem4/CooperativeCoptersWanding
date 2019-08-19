# -*- coding: utf-8 -*-
from Tkinter import *
import tkFont
import os
import time
import plotly
import plotly.graph_objs as go

class PlotSettingsGUI():
    def __init__(self):
        self.root = Tk()                                # Create main window
        self.root.geometry("1280x400")                   # Set defualt window size
        self.root.title( "Plotify" )                    # Give it a spunky name
        Grid.rowconfigure(self.root, 0, weight=1)       # Assign a single resizeable row to the window
        Grid.columnconfigure(self.root, 0, weight=1)    # Assign a single resizeable column to the window

        self.frame = Frame(self.root)                   # Create a single frame inside main window
        self.frame.grid(row=0, column=0, sticky=N+S+E+W)# Sticky = frame will expand to fill all corners of the window

        ## Configure rows and columns inside frame ##
        Grid.rowconfigure(self.frame, 0,  weight=0, minsize=25)  # Upper padding row
        Grid.rowconfigure(self.frame, 1,  weight=0)              # Directory and search box row
        Grid.rowconfigure(self.frame, 2,  weight=0, minsize=25)  # Padding row
        Grid.rowconfigure(self.frame, 3,  weight=0)              # Pane labels row
        Grid.rowconfigure(self.frame, 4,  weight=1)              # Variable panes first row
        Grid.rowconfigure(self.frame, 5,  weight=0)              # Variable buttons row 1
        Grid.rowconfigure(self.frame, 6,  weight=0)              # Variable buttons row 2              
        Grid.rowconfigure(self.frame, 7,  weight=0)              # Variable buttons row 3
        Grid.rowconfigure(self.frame, 8,  weight=0, pad=15)              # Variable buttons row 4
        Grid.rowconfigure(self.frame, 9,  weight=0, pad=15)              # Variable buttons row 5
        Grid.rowconfigure(self.frame, 10,  weight=0)             # Variable buttons row 6
        Grid.rowconfigure(self.frame, 11, weight=1)              # Variable panes last row
        Grid.rowconfigure(self.frame, 12, weight=0, minsize=25)  # Padding row
        Grid.rowconfigure(self.frame, 13, weight=0)              # Bottom button row
        Grid.rowconfigure(self.frame, 14, weight=0, minsize=25)  # Padding row

        Grid.columnconfigure(self.frame, 0, weight=0, minsize=25)   # Left padding column
        Grid.columnconfigure(self.frame, 1, weight=1, minsize=375)  # Navigation pane column
        Grid.columnconfigure(self.frame, 2, weight=0)               # Navigation pane scrollbar column
        Grid.columnconfigure(self.frame, 3, weight=0, minsize=25)   # Padding column
        Grid.columnconfigure(self.frame, 4, weight=1)               # Variable search pane column
        Grid.columnconfigure(self.frame, 5, weight=0)               # Variable search pane scrollbar column
        Grid.columnconfigure(self.frame, 6, weight=0, pad=30)               # Variable plot button column
        Grid.columnconfigure(self.frame, 7, weight=1)               # Variable plot pane column
        Grid.columnconfigure(self.frame, 8, weight=0)               # Variable plot pane scrollbar column            
        Grid.columnconfigure(self.frame, 9, weight=0, minsize=25)   # Right padding column


        '''
        numColmns = 4
        numRows   = 10
        epx = 5
        epy = 5
        ipx = 5
        ipy = 5
        
        
        '''

        ## Create Widgets ##
        path = os.getcwd()
        self.navigationBar = Label(self.frame, text=path)                         # Navigation bar displays current directory we are working from        

        self.navigationPane = Listbox(self.frame)                                 # Create navigation pane listbox & corresponding scrollbar
        self.navigationBar_scroll = Scrollbar(self.frame, orient=VERTICAL)
        self.navigationPane.config(yscrollcommand=self.navigationBar_scroll.set)
        self.navigationBar_scroll.config(command=self.navigationPane.yview)

        self.varSearchPane = Listbox(self.frame, selectmode=MULTIPLE)                                  # Create variable search pane & corresponding scrollbar
        self.varSearchPane_scroll = Scrollbar(self.frame, orient=VERTICAL)
        self.varSearchLabel = Label(self.frame, text="Search Results")
        self.varSearchPane.config(yscrollcommand=self.varSearchPane_scroll.set)
        self.varSearchPane_scroll.config(command=self.varSearchPane.yview)
        
        self.varPlotPane = Listbox(self.frame, selectmode=EXTENDED)                # Create variable plot pane & corresponding scrollbar
        self.varPlotPane_scroll = Scrollbar(self.frame, orient=VERTICAL)
        self.varPlotLabel = Label(self.frame, text="Variables to Plot")
        self.varPlotPane.config(yscrollcommand=self.varPlotPane_scroll.set)
        self.varPlotPane_scroll.config(command=self.varPlotPane.yview)

        self.variableSearchEntryLabel = Label(self.frame, text="Search:")
        self.variableSearchEntry = Entry(self.frame)
##        self.variableSearchEntry.insert(0, "Variable Search Box")

        self.arrowFont = tkFont.Font(family='Helvetica', size=17, weight='bold')
        self.pushLeftBtn = Button(self.frame, text="◄", command=self.pushLeftBtnCMD, font=self.arrowFont)
        self.pushRightBtn = Button(self.frame, text="►", command=self.pushRightBtnCMD, font=self.arrowFont)

        self.plotBtn = Button(self.frame, text="Plot!", command=self.generatePlot)
        
        ## Place widgets in the frame ##
        self.navigationBar.grid(row=1, column=1)
        
        self.navigationPane.grid      (row=2, column=1, rowspan=10, sticky=N+S+E+W)
        self.navigationBar_scroll.grid(row=2, column=2, rowspan=10, sticky=N+S+E+W)

        self.varSearchLabel.grid      (row=3, column=4, sticky=N+S+E+W)
        self.varSearchPane.grid       (row=4, column=4, rowspan=8, sticky=N+S+E+W)
        self.varSearchPane_scroll.grid(row=4, column=5, rowspan=8, sticky=N+S+E+W)

        self.varPlotLabel.grid        (row=3, column=7, sticky=N+S+E+W)
        self.varPlotPane.grid         (row=4, column=7, rowspan=8, sticky=N+S+E+W)
        self.varPlotPane_scroll.grid  (row=4, column=8, rowspan=8, sticky=N+S+E+W)

        self.variableSearchEntryLabel.grid(row=1, column=4, sticky=W)
        self.variableSearchEntry.grid (row=2, column=4, columnspan=5, sticky=N+S+E+W)

        self.pushLeftBtn.grid         (row=7, column=6)
        self.pushRightBtn.grid        (row=8, column=6)

        self.plotBtn.grid             (row=13, column=6) 

        ## Bind widget events to functions ##
        self.variableSearchEntry.bind("<KeyRelease>", self.updateVarSearchPane)
        self.navigationPane.bind("<<ListboxSelect>>", self.getVarsFromFile)

        self.getFileList()  #Populate navigation pane with all data files in current directory
        
        ## Run GUI instance Mainloop ##
##        self.root.after(1000, self.updateVarSearchPane())
        self.count = 0
        self.variables = [] #Initilialize variable list
        self.root.mainloop()
        
    def getFileList(self):
        for file in os.listdir("."):
            if file.endswith(".dat"):
                self.navigationPane.insert(END, file)

    def getVarsFromFile(self, obj):
        self.filename= self.navigationPane.get(self.navigationPane.curselection())
        with open(self.filename, 'r') as f:
            line = f.readline().strip("\n") 
            if line == '':
                self.displayErrorMSG("Could not extract variables from header")
            else:
                self.variables = line.split("\t")
        self.variables = sorted(self.variables, key=lambda s: s.lower()) #Sort the variables alphabetically (case insensitive)
        self.updateVarSearchPane()
        
    def displayErrorMSG(msg):
        pass
    
    def updateVarSearchPane(self, key=None):
        self.varSearchPane.delete(0, END)
        query = self.variableSearchEntry.get()
        for item in self.variables:
            if item.lower().find(query.lower()) != -1:
                self.varSearchPane.insert(END, item)

    def pushLeftBtnCMD(self):
        selectedVars = self.varPlotPane.curselection() # Index of all variables selected in search pane
        legend = []
        print selectedVars
        for i, var in enumerate(self.varPlotPane.get(0, END)): #Iterate thru all elements in plot pane, only add to list the ones that are not currently selected
            if str(i) not in selectedVars:
                legend.append(var)
        
        self.varPlotPane.delete(0, END)
        for item in legend:
            self.varPlotPane.insert(END, item)
        
    def pushRightBtnCMD(self):
        selectedVars = self.varSearchPane.curselection() # Index of all variables selected in search pane

        legend = []
        t = self.varPlotPane.get(0, END)    # Get all variables in Plot pane
        for var in t:
            legend.append(var)

        for v in selectedVars:
            if self.varSearchPane.get(v) not in legend: #Prevent duplicates from being added
                legend.append(self.varSearchPane.get(v))

        legendSorted = sorted(legend, key=lambda s: s.lower())

        self.varPlotPane.delete(0, END)
        for item in legendSorted:
            self.varPlotPane.insert(END, item)

    def generatePlot(self):
        legend = self.varPlotPane.get(0, END)

        cycles = []
        dataToPlot = []
        cycles = []

        for i in range(0, len(legend)): # Initialize empty lists to store data, each list inside the list is a data set pertaining to a variable in 'legend'
            dataToPlot.append([])
        
        with open(self.filename, 'r') as f:
            varList = f.readline().strip("\n").split()
            
            

            line = f.readline().strip("\n").split()
            
            while len(line) == len(varList):
                cycles.append(int(line[varList.index("cycle")]))
                for i, item in enumerate(legend):
                    dataToPlot[i].append(int(line[varList.index(item)])) # Legend item allows us to find the approprate index for the require data, append to the data list
                line = f.readline().strip("\n").split()

            traces = []
            for i,item in enumerate(legend):
                tempTrace = go.Scatter(
                    x = cycles,
                    y = dataToPlot[i],
                    mode = 'lines',
                    name = item
                )

                traces.append(tempTrace)
            
            plotly.offline.plot(traces, filename=self.filename+".html")
    

        

if __name__ == "__main__":
    gui = PlotSettingsGUI()

    lastTime = time.time()
    '''
    while(1):
        if(time.time()-lastTime>1):
            gui.updateVarSearchPane()
            lastTime = time.time()
            print time.time()
    '''
            
    
