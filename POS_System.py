# Username:
#
# Name:
#
#
########################################################################################
#
#
#
#
#
#
#######################################################################################
import customtkinter


# class LeftFrame(customtkinter.CTkFrame):
#     """ This Frame will display orders and have the payment area"""
#     def __init__(self,master, **kwargs):
#         super().__init__(master, **kwargs)
#
#         # Temporary (add color to see the frame)
#         #self.configure(fg_color ="pink")
#
#         # Frame size
#
#
#         # Grid System




class RightFrame(customtkinter.CTkFrame):
    """ This frame will be where the buttons are"""
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)

        # Temporary (add color to see the frame)
        self.configure(fg_color="pink")

        # Frame Size


        # Grid System




class GUI (customtkinter.CTk):
    """ """
    def __init__(self):
        super().__init__()

        # Key Attributes
        self.title("POS System")

        # Title Bar Color


        # Full Screen (1536 x 864)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}")

        # Appearance
        customtkinter.set_appearance_mode("dark")
        self.configure(bg_color = "#1A1A1A")

        # Create instances of L/R Frame class w/ self as master
        self.left_frame = LeftFrame(master = self)
        self.right_frame = RightFrame(master = self)



if __name__ == "__main__":
    gui = GUI() # Create an instance of the Widget class
    gui.mainloop()
