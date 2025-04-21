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
    """ This Frame will display a toggle menu with general buttons and some more buttons"""
    def __init__(self,master):
        super().__init__(master, width=200, height=864) # Remove color
        self.pack_propagate(False)  # ChatGPT

        # Track Menu Visibility
        self.menu_visible = True

        # Toggle Button
        self.toggle_btn = customtkinter.CTkButton(self, text="☰", width=35, corner_radius = 1, command=self.toggle_menu)
        self.toggle_btn.pack(pady=10, padx=10, anchor="nw")

        # Container Widget
        self.menu_container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.menu_container.pack(fill="both", expand=True, padx=0, pady=10)

        # Button (in container widget)
        buttons = ["Combos", "Sandwiches", "Sides", "Desserts", "Drinks"]
        for text in buttons:
            btn = customtkinter.CTkButton(self.menu_container, text=text,corner_radius = 1, height = 50 )
            btn.pack(pady=20, fill="x")

        # Spacer to push Exit button to bottom (ChatGPT)
        spacer = customtkinter.CTkLabel(self.menu_container, text="")
        spacer.pack(expand=True)  # Expands and fills space between buttons and exit

        # Exit Button
        exit_btn = customtkinter.CTkButton(self.menu_container, text = "Exit", corner_radius = 1, height = 50)
        exit_btn.pack(pady = 20, fill = "x")


    def toggle_menu(self):
        if self.menu_visible:
            self.menu_container.pack_forget() # Hide the container widget
        else:
            self.menu_container.pack(fill="both", expand=True, padx=10, pady=(0, 10)) # Show the container widget
        self.menu_visible = not self.menu_visible






class MiddleFrame(customtkinter.CTkFrame):
    """ This frame is where the buttons will go"""
    def __init__(self,master):
        super().__init__(master, width = 900)

        # Grid Layout (4x4)
        for row in range(4):
            self.grid_rowconfigure(row, weight=1)
        for col in range(4):
            self.grid_columnconfigure(col, weight=1)

        # Buttons (Only visible when a general button clicked)


class RightFrame(customtkinter.CTkFrame):
    """ This frame will be where orders show"""
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color = "yellow", width = 500, height=864) # Remove color







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
        customtkinter.set_appearance_mode("dark") #Dark Theme

        # LEFT FRAME (Toggle Menu)
        self.left_frame = LeftFrame(self)
        self.left_frame.pack(side="left", fill="y")

        # MIDDLE FRAME (Button Area)
        self.mid_frame = MiddleFrame(self)
        self.mid_frame.pack(side="left", fill="both", expand=True)

        # RIGHT FRAME (Display Area)
        self.right_frame = RightFrame(self)
        self.right_frame.pack(side="left", fill="y")

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
