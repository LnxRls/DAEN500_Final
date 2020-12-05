# R Programming Exercise 
# student: stavros kalamatianos

###################
#### Settings #####
###################

# do some memory cleanup.
gc(verbose = TRUE, reset = TRUE)
format(memory.size(), units = "MB")

options(scipen=999) # get rid of scientific notation

# reads the Renviron file to make this compatible with Rscript.exe
readRenviron("~/.Renviron")

# cleans out everything
rm(list=ls())

# defines a vector of courses
myCourses <- c('Physical Chemistry 500', 'Organic Chemistry 600', 'Transport Phenomena 550', 'Chemical Thermodynamics 456', 'Chemical Plant Design 610', 'Chemical Reactors I', 'Chemical Reaction Kinetics 570', 'Mass and Energy Balances 620', 'Analytical Chemistry II', 'Materials Science III') 

# gets the length of the vector myCourses
length(myCourses)

# gets the first two courses from myCourses
myCourses[1:2]

# gets the 3rd and 4th courses from myCourses
myCourses[3]
myCourses[4]

# sorts myCourses using a method
sort(myCourses)

# sorts myCourse in the reverse direction
sort(myCourses, decreasing = TRUE)

