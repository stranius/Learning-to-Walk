# Learning-to-Walk
See the code for how an AI names Bill living in his simulated world learned to walk.

# Purpose for Project
Midwestern State University
Seminar (CMPS 4991)
NTASC Presentation

This repo shows the code for the project made for a presentation at the National Texas Area Student Conference (NTASC). 

# Overview
In this project, I created a character that would be placed into a simulated, 2D world and would attempt to learn how to walk using a machine learning algorithm known as Neuro-evolution of Augmentin Topologies or NEAT for short.

The end goal of this project is to have the characted progressively improve it's ability to walk over a number of generations. Using NEAT, the character will start out blind to the world, not knowing what to do exactly, but will be given points for moving forward in the x direction (to the right) and will have points deducted for movement in the negative x direction (to the left). Over generations, natural selection should happen, picking only the best versions of the character, and in the end, a species of the characted with the best walking mechanisms will be evaluated. 

These final generations should be fairly good at walking, at least that is the hope. Regardless, I will make an update to this file in the future examining the outcomes of the algorithm as well as what could be done better and if this acts as a proof of concept for more complex problems.
