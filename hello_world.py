import numpy as np

#Function takes in an array of data and outputs a sorted verson of the array
#It also runs the array through a gaussian function that produces data for a yaxis
#When the outputs are plotted it will produce a gaussian distribution

#Input : xarray (Array of int or float)
#Ouput : sorted_xarray (Array of int or float), yarray (Array of float)

def gauss(xarray):
    sorted_xarray = np.sort(xarray)

    mean = np.mean(sorted_xarray)
    std = np.std(sorted_xarray)
    yarray = np.ones_like(sorted_xarray)

    for x in range(0,len(sorted_xarray)):
         yarray[x] = (1 / (std * np.sqrt(2*np.pi))) * np.exp(-((sorted_xarray[x]-mean)**2)/(2*std**2))
    return sorted_xarray, yarray

print("Hello World")
