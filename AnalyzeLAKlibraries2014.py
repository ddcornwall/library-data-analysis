# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 20:19:55 2017

@author: Daniel
"""

#This program provides some basic analysis on FY 2014 Alaska Public
#library Statistics
#Placeholder for Wish List


#Import the libraries needed for this program
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Get Data from FY 2014 Full Report, originally downloaded from ____ 
#but now stored in the same working directory as this program because
#row and column cleanup were needed.

aklibraries = pd.read_excel("2014_full_report.xlsx", index_col=0)

#Statistical Calculations
#Placeholder for calculations of mean, median, max and min.
#Problem to be solved for max and min - printing out the names of the
#libraries with the max and min values.
#Would also prefer being able to chose a field from a pick list and
#have the calculations done on the fly instead of hard coding fields. 

#Hours open per week
open_hours = np.median(aklibraries["FY2014_Hours_Central_Library_Open_Each_Week"])
print("The median number of open hours per week in FY2014 was", open_hours)


#Chart plots - Plots of data, perhaps in histogram Form
plt.hist(aklibraries["FY2014_Hours_Central_Library_Open_Each_Week"], bins=5)
plt.show()




#Scatterplot charts - Plat different fields against population
#Population will need a log on xscale due to Anchorage
#Are there other meaningful things to plot against (square footage, revenue,
#expenses, etc)


plt.scatter(aklibraries["FY2014_Population_"], aklibraries["FY2014_Hours_Central_Library_Open_Each_Week"])
plt.xscale('log')
plt.show()

