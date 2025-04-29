# Username: micklers
# Name: Shadaria Mickler
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
        super().__init__(master, width=230, height=864, fg_color = "#181818")

        self.pack_propagate(False)  # ChatGPT
        self.mid_frame = mid_frame # Store a reference to the MiddleFrame instance so methods can be called from LeftFrame

        # Track Menu Visibility
        self.menu_visible = True

        # Toggle Button
        self.toggle_btn = customtkinter.CTkButton(self, text="☰", width=35, corner_radius = 3, command=self.toggle_menu)
        self.toggle_btn.pack(pady=15, padx=10, anchor="nw")

        # Container Widget
        self.menu_container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.menu_container.pack(fill="both", expand=True, padx=0, pady=20)

        # Button Data
        btn_name = ["Combos", "Sandwiches", "Sides", "Desserts", "Drinks"]
        self.btn_ref = {}  # Instant var to store references to each button

        for index, text in enumerate(btn_name):
            btn = customtkinter.CTkButton(
                self.menu_container,
                text=text,
                corner_radius = 3,
                height = 50,
                command = lambda category=text: self.call_specific_button(category)
            )
            btn.pack(pady=15, fill="x")
            self.btn_ref[index] = btn # Store button ref

        # Spacer to push Exit button to bottom (ChatGPT)
        spacer = customtkinter.CTkLabel(self.menu_container, text="")
        spacer.pack(expand=True)  # Expands and fills space between buttons and exit

        # Exit Button
        self.exit_btn = customtkinter.CTkButton(self.menu_container, text = "Exit", corner_radius = 3, height = 50)
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
        super().__init__(master, width = 500, fg_color = "#121212")
        self.specific_btn_ref = {}  # Store references to specific buttons

        # Search Bar (Entry Widget)
        self.search_bar = customtkinter.CTkEntry(self, placeholder_text = "Search for products . . .", width = 710, height = 35, corner_radius=3, fg_color = "#282828")
        self.search_bar.pack(anchor = "nw", padx = 15, pady = (15,5), fill = "x")

        # Container Frame for Buttons (below search bar)
        self.specific_btn_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.specific_btn_frame.pack(anchor="nw", padx=15, pady=(35, 0), fill="both")

        # Buttons Data
        self.button_data = {
            "Combos": [
                ("The Classic Crunch Combo", 7.99),
                ("Smoky BBQ Bliss Combo", 7.99),
                ("Zesty Lemon Kick Combo", 7.99),
                ("Fiery Buffalo Heat Combo", 7.99)
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
        """ When a category is selected, update the display with specific buttons for that category """

        # Clear any existing specific buttons in the button frame
        for widget in self.specific_btn_frame.winfo_children():
            widget.destroy()

        # Create menu items
        counter = 0
        menu_item = self.button_data.get(p_category,[]) # Grabs key from dictionary

        # Iterate through menu items (Key), ignoring their prices
        for item_name,_ in menu_item:
            # Create a button for each item
            btn = customtkinter.CTkButton(self.specific_btn_frame, text = item_name, corner_radius=3, height = 175)
            # Place the buttons in Grid Layout
            btn.grid(row = counter//4, column = counter % 4, padx = 3, pady = 3, sticky = "nsew")
            counter+=1 # Increment Counter

        # Makes columns expandable in the button frame
        for col in range(4):
            self.specific_btn_frame.grid_columnconfigure(col, weight=1)





class RightFrame(customtkinter.CTkFrame):
    """ This frame will be where orders show"""
    def __init__(self, master, **kwargs):
        super().__init__(master, width = 550, height=864, corner_radius = 1,fg_color = "#121212")
        self.pack_propagate(False)  # ChatGPT

        # All Checks Button
        self.all_check_btn = customtkinter.CTkButton(self, text="All checks", corner_radius=3, width= 125, height = 40)
        self.all_check_btn.pack(anchor="ne", padx= 10, pady = (15,15))

        # Divider Line (Upper)
        divider1 = customtkinter.CTkFrame(self, height=2, width=800, fg_color="#404040")
        divider1.pack(fill = "both", pady = (25,5))

        # Save, Cancel, Delete Button Container Frame
        button_row = customtkinter.CTkFrame(self, fg_color = "transparent")
        button_row.pack(fill="x", pady=5, padx=5)

        # Cancel Button (Left)
        self.cancel_btn = customtkinter.CTkButton(button_row, text="Cancel", corner_radius=3, height=40, width=125)
        self.cancel_btn.pack(side="left", padx=(5, 5))

        # Delete Button (Right)
        self.delete_btn = customtkinter.CTkButton(button_row, text="Delete", corner_radius=3, height=40, width=125)
        self.delete_btn.pack(side="right", padx=(5, 5))

        # Save Button (Center)
        self.save_btn = customtkinter.CTkButton(button_row, text = "Save", corner_radius=3, height=40, width = 125)
        self.save_btn.pack(padx = (5,5))

        # Divider Line
        divider2 = customtkinter.CTkFrame(self, height=2, width=800, fg_color="#404040")
        divider2.pack(fill = "both", pady = (5,5))

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
        self.discount_btn = customtkinter.CTkButton(button_row2, text="Discount", corner_radius=3, height=40)
        self.discount_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

        # Pay Button (Right)
        self.pay_btn = customtkinter.CTkButton(button_row2, text="Pay", corner_radius=3, height=40, command=self.update_order_number)
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
