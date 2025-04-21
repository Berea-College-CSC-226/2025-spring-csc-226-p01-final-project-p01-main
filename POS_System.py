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
import customtkinter,random


class LeftFrame(customtkinter.CTkFrame):
    """ This Frame will display orders and have the payment area"""
    def __init__(self,master, **kwargs):
        super().__init__(master, fg_color="light grey", width=594, height=864, **kwargs) # remove color

        # Grid System




class RightFrame(customtkinter.CTkFrame):
    """ This frame will be where the buttons are"""
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="grey", width=942, height=864, **kwargs) # remove color

        # # Random color generator for visual pop (ChatGpt)
        # def random_color():
        #     return f'#{random.randint(100, 255):02x}{random.randint(100, 255):02x}{random.randint(100, 255):02x}'

        # Grid System (5x5)
        for i in range(5):
            self.grid_rowconfigure(i, weight = 1)
            self.grid_columnconfigure(i, weight = 1)

        # Buttons



        # # Create colorful cells (ChatGPT) Not needed just needed to see a 5x5
        # for row in range(5):
        #     for col in range(5):
        #         color = random_color()
        #         cell = customtkinter.CTkFrame(self, fg_color=color, corner_radius=8)
        #         cell.grid(row=row, column=col, sticky="sew", padx=5, pady=5)




class GUI (customtkinter.CTk):
    """ """
    def __init__(self):
        super().__init__()
        self.title("POS System")

        # Title Bar Color

        # Full Screen (1536 x 864)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}")

        # Appearance
        customtkinter.set_appearance_mode("dark") #Dark Theme
        #self.configure(bg_color="#1A1A1A") # BG for Window

        # Create instances of L/R Frame class w/ self now referred to as master
        self.left_frame = LeftFrame(master = self)
        self.left_frame.pack(side="left", fill="y")

        self.right_frame = RightFrame(master = self)
        self.right_frame.pack(side="left", fill="both", expand=True)


if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
