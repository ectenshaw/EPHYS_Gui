import tkinter

import scipy.io as sp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import Frame
import mplcursors
from matplotlib.backend_bases import MouseButton
import customtkinter
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import itertools
import numpy as np
from scipy.signal import find_peaks
import pandas as pd

'''
import scipy.io as sp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import Frame
import mplcursors
from matplotlib.backend_bases import MouseButton
import customtkinter
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import itertools
import numpy as np
from scipy.signal import find_peaks
filelist = ["C:\\Users\\tenshawe\\Desktop\\PycharmProjects\\EPHYSAnalysis\\AmplitudeMeasurementData.mat"]
dataCount = 0
clickCount = 0
peaks = []
feet = []
global canvas
global ix
global iy
def loadData(filelist1, dataCount1):
    mat_contents1 = sp.loadmat(filelist1[dataCount1])
    return mat_contents1
mat_contents = loadData(filelist, dataCount)
x = mat_contents['Time']
y = mat_contents['Vm']
ylist = y.tolist()
ymax = (max(ylist[0:20000]))
ymin = (min(ylist[0:20000]))
x2 = x.ravel()
y2 = y.ravel()
ymax2 = (max(ylist))
ymin2 = (min(ylist))
fig, ax = plt.subplots(figsize=(20, 8))
# create the axis for the x scrollbar
x_axis = plt.axes([0.125, 0.1, 0.775, 0.03])
x_frame = Slider(x_axis, 'X', 0, 5, valinit=0)
def updateX(val):
    ax.axis(xmin=val, xmax=val + 1)
    fig.canvas.draw_idle()
x_frame.on_changed(updateX)
# create the axis for the x scrollbar
y_axis = plt.axes([0.125, 0.05, 0.775, 0.03])
y_frame = Slider(y_axis, 'Y', ymin2[0], ymax2[0], valinit=ymin[0])
# print(y_frame.val)
# Create a function to change x
def updateY(val):
    dif = ymax[0] - ymin[0]
    ax.axis(ymin=val, ymax=val + dif + 0.5)
    fig.canvas.draw_idle()
y_frame.on_changed(updateY)
ax.axis(xmin=0, xmax=1)
ax.axis(ymin=ymin[0] - 0.5, ymax=ymax[0] + 0.5)
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightblue', linestyle='dashed')
originalX = ax.get_xlim()
originalY = ax.get_ylim()
line = ax.plot(x, y, color='black')
'''
# create the app and make a figure to place the plot in
root = customtkinter.CTk()

root.title("Analysis")
root.geometry('2000x700')
root.resizable(width=True, height=True)
filelist = ["AmplitudeMeasurementData.mat"]

dataCount = 0
clickCount = 0
peaks = []
feet = []
global canvas, myFeet, myPeaks
global ix
global iy
global peakLst, footLst


#   mat_contents = loadData(filelist, dataCount)


def loadData(filelist1, dataCount1):
    mat_contents1 = sp.loadmat(filelist1[dataCount1])
    return mat_contents1


def createPlots(filelist1, dataCount1=0):
    mat_contents = loadData(filelist1, dataCount1)
    x = mat_contents['Time']
    y = mat_contents['Vm']
    ylist = y.tolist()
    ymax = (max(ylist[0:20000]))
    ymin = (min(ylist[0:20000]))
    x2 = x.ravel()
    y2 = y.ravel()
    ymax2 = (max(ylist))
    ymin2 = (min(ylist))

    fig, ax = plt.subplots(figsize=(15,8))

    # create the axis for the x scrollbar
    x_axis = plt.axes([0.125, 0.04, 0.775, 0.02])
    x_frame = Slider(x_axis, 'X', 0, 30, valinit=0)

    def updateX(val):
        ax.axis(xmin=val, xmax=val + 1)
        fig.canvas.draw_idle()

    x_frame.on_changed(updateX)

    # create the axis for the y scrollbar
    y_axis = plt.axes([0.125, 0.00, 0.775, 0.02])
    y_frame = Slider(y_axis, 'Y', ymin2[0], ymax2[0], valinit=ymin[0])

    # print(y_frame.val)
    # Create a function to change x
    def updateY(val):

        dif = ymax[0] - ymin[0]
        ax.axis(ymin=val, ymax=val + dif + 0.5)
        fig.canvas.draw_idle()

    y_frame.on_changed(updateY)

    # create strings for button submissions
    lowerY = customtkinter.StringVar()
    upperY = customtkinter.StringVar()
    lowerX = customtkinter.StringVar()
    upperX = customtkinter.StringVar()

    # draw the plot
    ax.axis(xmin=0, xmax=1)
    ax.axis(ymin=ymin[0] - 0.5, ymax=ymax[0] + 0.5)
    ax.set_axisbelow(True)
    ax.yaxis.grid(color='lightblue', linestyle='dashed')
    originalX = ax.get_xlim()
    originalY = ax.get_ylim()
    line = ax.plot(x, y, color='black')

    # This function creates a frame for the matplotlib plot and then plots it onto the canvas
    # This returns a Frame with the plot inside of it - which is passed onto the root for the TK app
    def createPlotFrame():
        # create an empty frame and add a canvas to it for the plot
        global canvas
        plot2 = Frame()
        canvas = FigureCanvasTkAgg(fig, master=plot2)

        # add a cursor to the plot to show the data on hover
        # mplcursors.cursor(line)
        plot_widget = canvas.get_tk_widget()

        # add a click event so the coordinates are saved
        # buggy !!
        # def plotClick(event):
        #     if event.button == MouseButton.LEFT:
        #        print('Clicked at x=%f, y=%f' % (event.xdata, event.ydata))

        # link the button press to the plot canvas
        # canvas.mpl_connect('button_press_event', plotClick)

        # add the plot to the window
        plot_widget.pack(expand=True)
        canvas.draw()

        # adds the toolbar that pans/zooms for matplotlib plots
        # toolbar = NavigationToolbar2Tk(canvas, plot2)
        # toolbar.update()
        # canvas.get_tk_widget().pack(side='top')
        return plot2



    peaks, _ = find_peaks(y2, prominence=10)
    peak_coordinates = list(zip(x2[peaks], y2[peaks]))

    feet, _ = find_peaks(y2, prominence=-20)
    feet_coordinates = list(zip(x2[feet], y2[feet]))
    global peakLst, footLst

    global myPeaks
    myPeaks = []
    global myFeet
    myFeet = []

    def snapToPeaks():
        global ix, iy
        global peakLst, footLst

        peaksAr = np.array(peak_coordinates)
        coord = np.array((ix, iy))
        distances = np.linalg.norm(peaksAr - coord, axis=1)
        min_index = np.argmin(distances)
        print(f"the closest peak is {peaksAr[min_index]}, at a distance of {distances[min_index]}")
        peakLst.insert('end', coord)
        return peaksAr[min_index]

    def snapToFeet():
        global ix, iy
        global peakLst, footLst

        feetAr = np.array(feet_coordinates)
        coord = np.array((ix, iy))
        distances = np.linalg.norm(feetAr - coord, axis=1)
        min_index = np.argmin(distances)
        print(f"the closest foot is {feetAr[min_index]}, at a distance of {distances[min_index]}")
        footLst.insert('end', coord)
        return feetAr[min_index]
    def addPeak():
        def onclickP(event):
            global ix, iy
            coordinates = []
            ix, iy = event.xdata, event.ydata
            print(f'x = {ix}, y = {iy}')

            coordinates.append((ix, iy))
            coord = snapToPeaks()
            myPeaks.append(list(coord))
            print(myPeaks)
            if len(coordinates) == 1:
                fig.canvas.mpl_disconnect(cid)
        cid = canvas.mpl_connect('button_press_event', onclickP)

    def addFoot():
        def onclickF(event):
            global ix, iy
            coordinates = []
            ix, iy = event.xdata, event.ydata
            print(f'x = {ix}, y = {iy}')

            coordinates.append((ix, iy))
            coord = snapToFeet()
            myFeet.append(list(coord))
            print(myFeet)
            if len(coordinates) == 1:
                fig.canvas.mpl_disconnect(cid)
        cid = canvas.mpl_connect('button_press_event', onclickF)

    def exportPFData():
        peakfoot_df = pd.DataFrame(list(zip(myPeaks, myFeet)), columns=[1, 2])
        peakfoot_df.to_csv("peakfoot List.csv")
        return print("CSV saved")

    def createListBoxFrame():
        global peakLst, footLst

        global myPeaks
        global myFeet
        listFrame = Frame()
        peakLst = tkinter.Listbox(listFrame, listvariable=myPeaks, exportselection=0, width=25, height=30, font=('calibre', 12))
        peakLabel = customtkinter.CTkLabel(listFrame, text='Peaks', font=('calibre', 16, 'bold'))

        footLst = tkinter.Listbox(listFrame, listvariable=myFeet, exportselection=0, width=25, height=30, font=('calibre', 12))
        footLabel = customtkinter.CTkLabel(listFrame, text='Feet', font=('calibre', 16, 'bold'))

        peakLabel.grid(row=0, column = 0, padx=10, pady=10)
        footLabel.grid(row=0, column=1, padx=10, pady=10)
        peakLst.grid(row=1, column=0, padx=10, pady=10)
        footLst.grid(row=1, column=1, padx=10, pady=10)

        peak_btn = customtkinter.CTkButton(listFrame, text='Add Peak', command=lambda: addPeak())
        foot_btn = customtkinter.CTkButton(listFrame, text='Add Foot', command=lambda: addFoot())
        peak_btn.grid(row=2, column=0, padx=10, pady=10)
        foot_btn.grid(row=2, column=1, padx=10, pady=10)

        amp_button = customtkinter.CTkButton(listFrame, text='Calculate Amplitude')
        amp_button.grid(row=3, column=0, padx=10, pady=10)
        export_button = customtkinter.CTkButton(listFrame, text='Export', command=lambda: exportPFData())
        export_button.grid(row=3, column=1, padx=10, pady=10)

        return listFrame



    # function to move graph one second forward
    def oneSecForward():
        # get the current tick positions
        ticks = ax.get_xlim()
        if ticks == (29, 30):
            print("Can't move forward")
        else:
            # set y tick position based on min/max of data
            ticks2 = (ticks[0] + 1, ticks[1] + 1)
            low = int(ticks2[0] * 20000)
            high = int(ticks2[1] * 20000)
            ymax3 = max(y[low:high])
            ymin3 = min(y[low:high])
            x_min = ticks[0] + 1
            x_max = ticks[1] + 1
            y_min = ymin3 - 0.5
            y_max = ymax3 + 0.5
            minim_y = np.array(list(itertools.zip_longest(y_min, fillvalue=0))).T

            # redraw the axes that are shown
            ax.axis(xmin=x_min, xmax=x_max, ymin=y_min, ymax=y_max)
            # reset the x scroller when this button is clicked
            x_frame.set_val(x_max - 1)
            y_frame.set_val(minim_y)

            fig.canvas.draw_idle()

    # function to move graph one second back
    def oneSecBack():
        # get the current tick positions
        ticks = ax.get_xlim()
        if ticks == (0, 1):
            print("Can't move back")
        else:
            # set y tick position based on min/max of data
            ticks2 = (ticks[0] - 1, ticks[1] - 1)
            low = int(ticks2[0] * 20000)
            high = int(ticks2[1] * 20000)
            ymax2 = max(y[low:high], default=0)
            ymin2 = min(y[low:high], default=0)
            x_min = ticks[0] - 1
            x_max = ticks[1] - 1
            y_min = ymin2 - 0.5
            y_max = ymax2 + 0.5

            minim_y = np.array(list(itertools.zip_longest(y_min, fillvalue=0))).T

            # redraw the axes that are shown
            ax.axis(xmin=x_min, xmax=x_max, ymin=y_min, ymax=y_max)
            # reset the x scroller when this button is clicked
            x_frame.set_val(x_max - 1)
            y_frame.set_val(y_min)
            fig.canvas.draw_idle()

    # function that accepts integers to set the XY constraints to
    # currently autoscales to show the max/min of each time frame
    def userXYSubmit():
        min_x = 0
        min_y = 0
        max_x = 0
        max_y = 0
        lowY = lowerY.get()
        upY = upperY.get()
        lowX = lowerX.get()
        upX = upperX.get()
        xticks = ax.get_xlim()
        yticks = ax.get_ylim()

        if lowY == "":
            min_y = yticks[0]
        else:
            min_y = float(lowY)

        if upY == "":
            max_y = yticks[1]
        else:
            max_y = float(upY)
        if lowX == "":
            min_x = xticks[0]
        else:
            min_x = float(lowX)
        if upX == "":
            max_x = xticks[1]
        else:
            max_x = float(upX)

        ax.axis(xmin=min_x, xmax=max_x, ymin=min_y, ymax=max_y)
        fig.canvas.draw_idle()

        print("The lower Y bound is : " + str(min_y))
        print("The upper Y bound is : " + str(max_y))
        print("The lower X bound is : " + str(min_x))
        print("The upper X bound is : " + str(max_x))

        lowerY.set("")
        upperY.set("")
        lowerX.set("")
        upperX.set("")

    # resets the plot to the original view
    def resetXY():
        ax.axis(xmin=originalX[0], xmax=originalX[1], ymin=originalY[0], ymax=originalY[1])
        x_frame.set_val(0)
        fig.canvas.draw_idle()

    # show the entire plot (all 5 seconds)
    def fullPlot():
        ymax = max(y[0:100000])
        ymin = min(y[0:100000])
        ax.axis(xmin=0, xmax=30, ymin=ymin - 0.5, ymax=ymax + 0.5)
        fig.canvas.draw_idle()



    def nextFile():
        global dataCount
        global clickCount
        if dataCount + 1 < len(filelist):
            plot.destroy()
            dataCount += 1
            clickCount += 1
            createPlots(filelist, dataCount)
        else:
            print("out of range")
            clickCount += 1

        return

    def prevFile():
        global dataCount
        global clickCount
        if dataCount - 1 >= 0:
            plot.destroy()
            dataCount = dataCount - 1
            clickCount += 1
            createPlots(filelist, dataCount)
        else:
            print("out of range")
            clickCount += 1
        return

    # creates a frame for the buttons to be stored
    def createButtonFrame():
        buttons2 = Frame()
        lowerY_Label = customtkinter.CTkLabel(buttons2, text='Lower Y Bound', font=('calibre', 10, 'bold'))
        lowerY_Entry = customtkinter.CTkEntry(buttons2, textvariable=lowerY, font=('calibre', 10, 'normal'))
        upperY_Label = customtkinter.CTkLabel(buttons2, text='Upper Y Bound', font=('calibre', 10, 'bold'))
        upperY_Entry = customtkinter.CTkEntry(buttons2, textvariable=upperY, font=('calibre', 10, 'normal'))

        lowerX_Label = customtkinter.CTkLabel(buttons2, text='Lower X Bound', font=('calibre', 10, 'bold'))
        lowerX_Entry = customtkinter.CTkEntry(buttons2, textvariable=lowerX, font=('calibre', 10, 'normal'))
        upperX_Label = customtkinter.CTkLabel(buttons2, text='Upper X Bound', font=('calibre', 10, 'bold'))
        upperX_Entry = customtkinter.CTkEntry(buttons2, textvariable=upperX, font=('calibre', 10, 'normal'))

        # creating a button using the widget
        # Button that will call the submit function
        sub_btn = customtkinter.CTkButton(buttons2, text='Submit', command=lambda: userXYSubmit())

        # add the buttons to the app
        full_Plot = customtkinter.CTkButton(buttons2, text="Show Full Plot", command=lambda: fullPlot())
        backward = customtkinter.CTkButton(buttons2, text="One Sec Back", command=lambda: oneSecBack())
        forward = customtkinter.CTkButton(buttons2, text="One Sec Forward", command=lambda: oneSecForward())
        reset = customtkinter.CTkButton(buttons2, text="Reset Original XY", command=lambda: resetXY())

        nextData = customtkinter.CTkButton(buttons2, text="Next Plot", command=lambda: nextFile())
        prevData = customtkinter.CTkButton(buttons2, text="Previous Plot", command=lambda: prevFile())



        full_Plot.grid(row=0, column=1, padx=10, pady=10)
        reset.grid(row=0, column=3, padx=10, pady=10)
        backward.grid(row=1, column=1, padx=10, pady=10)
        forward.grid(row=1, column=3, padx=10, pady=10)
        lowerY_Label.grid(row=2, column=0)
        lowerY_Entry.grid(row=2, column=1)
        upperY_Label.grid(row=2, column=2)
        upperY_Entry.grid(row=2, column=3)
        lowerX_Label.grid(row=3, column=0)
        lowerX_Entry.grid(row=3, column=1)
        upperX_Label.grid(row=3, column=2)
        upperX_Entry.grid(row=3, column=3)
        sub_btn.grid(row=6, column=0, padx=10, pady=10, sticky='nesw')
        prevData.grid(row=7, column=1, padx=10, pady=10, sticky='w')
        nextData.grid(row=7, column=3, padx=10, pady=10, sticky='e')


        return buttons2

    global plot
    plot = createPlotFrame()
    buttons = createButtonFrame()
    lists = createListBoxFrame()
    sticky = tkinter.NSEW
   # plot.pack(side=tkinter.LEFT)
   # buttons.pack(side=tkinter.LEFT)
   # lists.pack(side=tkinter.RIGHT)
    plot.grid(row=0, column=1, sticky = 'e')
    buttons.grid(row=0, column=2, sticky='e')
    lists.grid(row=0, column=0, sticky='w')

createPlots(filelist)

if __name__ == "__main__":
    root.mainloop()
