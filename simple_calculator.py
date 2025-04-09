######################################################################
# Author: Hope Michael, Tafreed Sardar
# Username: michaelh, sadart
#
# Assignment: P01: Final Project
#
# Purpose: Building an interactive calculator and using a turtle object to write the result.
######################################################################
# Acknowledgements:
#
# some of the code is originally from: https://runestone.academy/ns/books/published/2025_Spring_CSC_226/gu-iand-event-driven-programming_a-programming-example.html

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import tkinter as tk
from tkinter import ttk
import turtle

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Interactive Calculator with turtle")
