# Username:
#
# Name:
#
#
########################################################################################
# Acknowledgements
# ChatGPT - Interaction between frames - https://chatgpt.com/c/6806f27a-25e4-800a-b15f-08fb55fa6eb9
# ChatGPT - Maintaining Frame Sizes - https://chatgpt.com/c/6806f327-1668-800a-8461-e50208d39257
# ChatGPT - Toggle Menu Walkthrough Steps - https://chatgpt.com/c/6806f391-ead8-800a-bac4-1192ead61ae6
# ChatGPT - Lambda in Command -
# ChatGPT - Spacer -
#######################################################################################
import customtkinter,random


class LeftFrame(customtkinter.CTkFrame):
    """ This Frame will display a toggle menu with general buttons and some more buttons"""
    def __init__(self, master, mid_frame):
        super().__init__(master, width=200, height=864)

        self.pack_propagate(False)  # ChatGPT
        self.mid_frame = mid_frame # Store a reference to the MiddleFrame instance so methods can be called from LeftFrame

        # Track Menu Visibility
        self.menu_visible = True

        # Toggle Button
        self.toggle_btn = customtkinter.CTkButton(self, text="☰", width=35, corner_radius = 1, command=self.toggle_menu)
        self.toggle_btn.pack(pady=15, padx=10, anchor="nw")

        # Container Widget
        self.menu_container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.menu_container.pack(fill="both", expand=True, padx=0, pady=10)

        # Button Data
        btn_name = ["Combos", "Sandwiches", "Sides", "Desserts", "Drinks"]
        self.btn_ref = {}  # Instant var to store references to each button

        for index, text in enumerate(btn_name):
            btn = customtkinter.CTkButton(
                self.menu_container,
                text=text,
                corner_radius = 1,
                height = 50,
                command = lambda category=text: self.call_specific_button(category)
            )
            btn.pack(pady=20, fill="x")
            self.btn_ref[index] = btn # Store button ref

        # Spacer to push Exit button to bottom (ChatGPT)
        spacer = customtkinter.CTkLabel(self.menu_container, text="")
        spacer.pack(expand=True)  # Expands and fills space between buttons and exit

        # Exit Button
        self.exit_btn = customtkinter.CTkButton(self.menu_container, text = "Exit", corner_radius = 1, height = 50)
        self.exit_btn.pack(pady = 20, fill = "x")

    def toggle_menu(self):
        """ Checks to see if toggle menu is visible or not to determine whether to display toggle elements"""
        if self.menu_visible:
            self.menu_container.pack_forget() # Hide the container widget
        else:
            self.menu_container.pack(fill="both", expand=True, padx=10, pady=(0, 10)) # Show the container widget
        self.menu_visible = not self.menu_visible

    def call_specific_button(self, p_category):
        """ When a general button is clicked, initialize specific buttons related to that category. """
        self.mid_frame.display_specific_buttons(p_category) # Call the method in MiddleFrame from the LeftFrame class and pass the categories of that general button



class MiddleFrame(customtkinter.CTkFrame):
    """ This frame is where the buttons will go"""
    def __init__(self,master):
        super().__init__(master, width = 900)

        # Grid Layout (4x4)
        for row in range(4):
            self.grid_rowconfigure(row, weight=1)
        for col in range(4):
            self.grid_columnconfigure(col, weight=1)

        # Buttons Data
        self.button_date = {
            "Combos": [
                ("Combo 1 - Classic Chicken Sandwich", 7.99),
                ("Combo 2 - Honey BBQ Sandwich", 7.99),
                ("Combo 3 - Lemon Pepper Sandwich", 7.99),
                ("Combo 4 - Buffalo Chicken Sandwich", 7.99)
            ],
            "Sandwiches": [
                ("Classic Chicken Sandwich", 5.49),
                ("Honey BBQ Sandwich", 5.49),
                ("Lemon Pepper Sandwich", 5.49),
                ("Buffalo Chicken Sandwich", 5.49)
            ],
            "Sides": [
                ("Fries", 2.49),
                ("Side Salad", 3.29),
                ("Coleslaw", 1.79),
                ("Onion Rings", 2.49)
            ],
            "Desserts": [
                ("Strawberry Shortcake", 3.99),
                ("Banana Pudding", 3.49),
                ("Vanilla Ice Cream", 2.49),
                ("Chocolate Ice Cream", 2.49)
            ],
            "Drinks": [
                ("Coke", 2.29),
                ("Diet Coke", 2.29),
                ("Sweet Tea", 2.29),
                ("Unsweet Tea", 2.29),
                ("Hi-C", 2.29),
                ("Sprite", 2.29),
                ("Dr Pepper", 2.29),
                ("Water", 0)
            ]
        }

        def display_specific_buttons(self, p_category):
            """ When a category is selected, update the display with the specific buttons for that category """

            # Clear any existing specific buttons
            for widget in self.winfo_children():
                widget.destroy()

            # Get the list of specific items based on the general button selected

            # Create specific buttons for each item in the category



class RightFrame(customtkinter.CTkFrame):
    """ This frame will be where orders show"""
    def __init__(self, master, **kwargs):
        super().__init__(master, width = 800, height=864, corner_radius = 1) # Remove color

        # All Checks Button
        self.all_check_btn = customtkinter.CTkButton(self, text="All checks", corner_radius=1, width= 125, height = 30)
        self.all_check_btn.pack(anchor="ne", padx= 15, pady = 15)

        # Divider Line (Upper)
        divider1 = customtkinter.CTkFrame(self, height=2, width=800, fg_color="grey30")
        divider1.pack(fill = "both", pady = 10)

        # Save, Cancel, Delete Button Container Frame
        button_row = customtkinter.CTkFrame(self, fg_color = "transparent")
        button_row.pack(fill="x", pady=5, padx=10)

        # Cancel Button (Left)
        self.cancel_btn = customtkinter.CTkButton(button_row, text="Cancel", corner_radius=1, height=40, width=125)
        self.cancel_btn.pack(side="left", padx=(5, 5))

        # Delete Button (Right)
        self.delete_btn = customtkinter.CTkButton(button_row, text="Delete", corner_radius=1, height=40, width=125)
        self.delete_btn.pack(side="right", padx=(5, 5))

        # Save Button (Center)
        self.save_btn = customtkinter.CTkButton(button_row, text = "Save", corner_radius=1, height=40, width = 125)
        self.save_btn.pack(padx = (5,5))

        # Divide Line
        divider2 = customtkinter.CTkFrame(self, height=2, width=800, fg_color="grey30")
        divider2.pack(fill = "both", pady = 20)

        self.order_number = 0 # Order number Accumulator

        # Order Number Label (Updated when Pay is clicked)
        self.order_label = customtkinter.CTkLabel(self, text = f"Ch. #{self.order_number}", font=("Arial", 20) )
        self.order_label.pack(padx = 10, pady = 1)

        # Total & Sub-tax (Label)





        # Spacer to push bottom buttons to the bottom of the frame
        spacer = customtkinter.CTkLabel(self, text="")
        spacer.pack(expand=True)

        # Discount & Pay Button (in a frame)
        button_row2 = customtkinter.CTkFrame(self, fg_color = "transparent")
        button_row2.pack(fill="x", pady=15, padx=10)

        # Discount Button (Left)
        self.discount_btn = customtkinter.CTkButton(button_row2, text="Discount", corner_radius=1, height=40)
        self.discount_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

        # Pay Button (Right)
        self.pay_btn = customtkinter.CTkButton(button_row2, text="Pay", corner_radius=1, height=40, command=self.update_order_number)
        self.pay_btn.pack(side="right", expand=True, fill="x", padx=(5, 0))


    def update_order_number(self):
        """
        When the Pay button is clicked the order number is incremented
        :return:
        """
        self.order_number+=1
        self.order_label.configure(text=f"Ch. #{self.order_number}") # Currently the order number is not being saved once the pos system is exited








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
        customtkinter.set_appearance_mode("dark") # Dark Theme


        # MIDDLE FRAME (Create mid_frame first so it to can be passed to the left_frame)
        self.mid_frame = MiddleFrame(self)

        # LEFT FRAME (Toggle Menu)
        self.left_frame = LeftFrame(self, self.mid_frame) # Pass mid_frame object to the left frame (references the mid_frame object inside the LeftFrame instance)
        self.left_frame.pack(side="left", fill="y")

        # Pack the mid_frame(after the left_frame)
        self.mid_frame.pack(side="left", fill="both", expand=True)

        # RIGHT FRAME (Display Area)
        self.right_frame = RightFrame(self)
        self.right_frame.pack(side="left", fill="y")

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
