# Username: micklers
# Name: Shadaria Mickler
#
#
#######################################################################################
import customtkinter,random

class Order:
    """ This class has methods that calculates the tax, total, and discount"""
    def __init__(self, item_dict, tax_label,total_label, discount_label):
        self.item_dict = item_dict
        self.tax_label = tax_label
        self.total_label = total_label
        self.discount_label = discount_label
        self.tax_rate = 0.06      # Kentucky Sales Tax
        self.discount_rate = 0.10 # Set Discount Rate
        self.discount_active = False # initial state


    def calculate_totals(self):
        """ This method calculates sales tax, discount and total"""

        subtotal = 0
        for value in self.item_dict.values():
            qty_x_price = (value['qty'] * value['price'])
            subtotal += qty_x_price

        sales_tax = subtotal * self.tax_rate

        if self.discount_active:
            discount = subtotal * self.discount_rate # positive discount
        else:
            discount = 0

        total = subtotal + sales_tax - discount
        return subtotal,sales_tax, discount, total

    def update_payment_labels(self):
        """This method updates labels in the payment_frame"""
        _,sales_tax,discount,total = self.calculate_totals()
        # Configure the text with updated values
        self.tax_label.configure(text = f"${sales_tax:.2f}")
        self.total_label.configure(text=f"${total:.2f}")
        self.discount_label.configure(text=f"${discount:.2f}")

    def toggle_discount(self):
        self.discount_active = not self.discount_active
        self.update_payment_labels()


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
        self.exit_btn.pack(pady = 0, fill = "x")

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
        self.right_frame = None # Placeholder (ChatGPT)

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

    def set_right_frame(self, right_frame):
        """ This sets the reference to the right frame after it's created """
        self.right_frame = right_frame

    def display_specific_buttons(self, p_category):
        """ When a category is selected, update the display with specific buttons for that category """

        # Clear any existing specific buttons in the button frame
        for widget in self.specific_btn_frame.winfo_children():
            widget.destroy()

        # Create menu items
        counter = 0
        menu_item = self.button_data.get(p_category,[]) # Grabs key from dictionary

        # Iterate through menu items (Key) & prices (Value)
        for item_name, item_price in menu_item:
            # Create a button for each item
            btn = customtkinter.CTkButton(
                self.specific_btn_frame,
                text = item_name,
                corner_radius=3,
                height = 175,
                command = lambda name = item_name, price = item_price: self.call_right_frame(name,price) # When specific button clicked pass button's data
            )
            # Place the buttons in Grid Layout
            btn.grid(row = counter//4, column = counter % 4, padx = 3, pady = 3, sticky = "nsew")
            counter+=1 # Increment Counter

        # Makes columns expandable in the button frame
        for col in range(4):
            self.specific_btn_frame.grid_columnconfigure(col, weight=1)

    # When a specific button is pressed call a method (from: Middle Frame to: RightFrame) and pass button data
    def call_right_frame(self, p_name, p_price):
        """ This method will call a method from RightFrame """

        # if true invoke the method display_menu_item method in the right frame class and pass menu_item and its price
        if self.right_frame:
            self.right_frame.display_menu_item(p_name,p_price)



class RightFrame(customtkinter.CTkFrame):
    """ This frame will be where orders show"""
    def __init__(self, master):
        super().__init__(master, width = 550, height=864, corner_radius = 1,fg_color = "#121212")

        self.pack_propagate(False)  # ChatGPT
        self.item_dict = {} # Dictionary stores item and qty


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

        # Detail Frame (Hold label widgets "Name" "QTY" "Each" "Total")
        self.detail_frame = customtkinter.CTkFrame(self, fg_color="#181818", corner_radius=3, height=30)
        self.detail_frame.pack(fill="both", padx=10, pady=(5, 0), expand=False)

        # Name (inside the detail_frame)
        label_one = customtkinter.CTkLabel(self.detail_frame, text="Name")
        label_one.grid(row=0, column=0, sticky="w", padx=(25, 15))

        # QTY (inside the detail_frame)
        qty_label = customtkinter.CTkLabel(self.detail_frame, text="Qty")
        qty_label.grid(row=0, column=1, sticky="ew", padx=(20, 20))

        # Total (inside the detail_frame)
        total_label = customtkinter.CTkLabel(self.detail_frame, text="Total")
        total_label.grid(row=0, column=2, sticky="e", padx=(10, 30))

        # Even columns
        for index in range(3):
            self.detail_frame.grid_columnconfigure(index, weight=1)


        # Order Scrollable Frame (where orders will be displayed)
        self.order_frame = customtkinter.CTkScrollableFrame(self, fg_color="#181818", width = 400, height = 440, corner_radius=3,border_width = 1, border_color = "#282828")
        self.order_frame.pack(fill="both", padx=10, expand = True)

        # Total, Sub-tax, Discount (Frame)
        self.payment_frame = customtkinter.CTkFrame(self, fg_color = "#181818", corner_radius = 3, height = 60)
        self.payment_frame.pack(fill = "both", padx = 10, pady = 1, expand = True)

        # Tax (Left - inside of payment_frame)
        tax_label = customtkinter.CTkLabel(self.payment_frame, text = "Tax", fg_color = "transparent", corner_radius = 3, font = ("Roboto", 13))
        tax_label.grid(row = 0, column = 0, sticky = "w", padx = (20,5), pady = 1)

        # Discount (Left - inside the payment_frame)
        discount_label = customtkinter.CTkLabel(self.payment_frame, text = "Discount", fg_color = "transparent", corner_radius = 3, font = ("Roboto", 13))
        discount_label.grid(row = 1, column = 0, sticky = "w", padx = (20,5), pady = 1)

        # Total (left - inside of payment_frame)
        total_label = customtkinter.CTkLabel(self.payment_frame, text = "Total", fg_color = "transparent", corner_radius = 3, font = ("Roboto", 13, "normal"))
        total_label.grid(row = 2, column = 0, sticky = "w", padx = (20,5))

        # Display Tax Label (right - inside the payment frame)
        self.display_tax_label = customtkinter.CTkLabel(self.payment_frame, text = f"$0.00", fg_color = "transparent", corner_radius = 3, font = ("Roboto", 13))
        self.display_tax_label.grid(row = 0, column = 1, sticky = "e", padx = (385,5), pady = 1)

        # Display Discount label (right - inside the payment frame)
        self.display_discount_label = customtkinter.CTkLabel(self.payment_frame, text = f"$0.00", fg_color = "transparent", corner_radius = 3, font = ("Roboto", 13))
        self.display_discount_label.grid(row = 1, column = 1, sticky = "e", padx = (385,5))

        # Display Total label (right - inside the payment frame)
        self.display_total_label = customtkinter.CTkLabel(self.payment_frame, text = f"$0.00", fg_color = "transparent", corner_radius = 3, font =("Roboto", 15))
        self.display_total_label.grid(row = 2, column = 1, sticky = "e", padx = (385,5))

        # Make even column spacing
        for col in range(2):
            self.payment_frame.grid_columnconfigure(col, weight=1)

        # Instance of the order class
        self.order = Order(self.item_dict, self.display_tax_label, self.display_total_label, self.display_discount_label)


        # Discount & Pay Button (in a frame)
        button_row2 = customtkinter.CTkFrame(self, fg_color = "transparent")
        button_row2.pack(fill="x", pady=5, padx=10)

        # Discount Button (Left)
        self.discount_btn = customtkinter.CTkButton(button_row2, text="Discount", corner_radius=3, height=45,border_width = 1, fg_color = "transparent", border_color = "#404040", hover_color = "#3B8ED0", command = self.apply_discount)
        self.discount_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

        # Pay Button (Right)
        self.pay_btn = customtkinter.CTkButton(button_row2, text="Pay", corner_radius=3, height=45)
        self.pay_btn.pack(side="right", expand=True, fill="x", padx=(5, 0))


    def display_menu_item(self,p_name, p_price):
        """ This method takes input parameter from another method and uses it to create a label widgets in the Order Frame(container widget)"""

        # Check to see it the item in dict
        if p_name in self.item_dict:
            # Item in dict, add 1 to qty (Nested dictionary "Item name" : {"qty": x, "price": y})
            self.item_dict[p_name]["qty"] +=1
            self.update_qty_label(p_name, self.item_dict[p_name]['qty'])
        else:
            # Item does not exist, the parameters are not empty, then create a new label and add to dictionary
            if p_name and (p_price is not None):

                # Row count = how many items (name + price) have already been added - ChatGPT
                row_count = len(self.order_frame.winfo_children())  # length of total number of widgets

                # Create a frame to hold the name and price labels together
                item_frame = customtkinter.CTkFrame(self.order_frame, fg_color="transparent")
                item_frame.grid(row=row_count, column=0, columnspan=3, sticky="w", padx=(10, 5), pady=5)

                # Create label for item name (left)
                name_label = customtkinter.CTkLabel(item_frame, text=p_name, fg_color="transparent", anchor="w", width = 160)
                name_label.grid(row=0, column=0, sticky="w", padx=(10, 5), pady=5)

                # Create a QTY Label (center)
                qty_label_accum = customtkinter.CTkLabel(item_frame, text="1", fg_color="transparent",anchor="w")
                qty_label_accum.grid(row=0, column=1, sticky="ew", padx=(75, 10), pady=5)

                # Create label for item price (right)
                price_label = customtkinter.CTkLabel(item_frame, text=f"${p_price:.2f}", fg_color="transparent", anchor="e")
                price_label.grid(row=0, column=2, sticky="w", padx=(105, 5), pady=5)

                # Configure grid columns to be the same size
                for i in range(3):
                    item_frame.grid_columnconfigure(i, weight=1, uniform="column")

                # Add the qty & price to the specific dictionary key
                self.item_dict[p_name] = {"qty": 1, "price": p_price}

            # Update the (subtotal and total display labels)
            self.order.update_payment_labels()

    def update_qty_label(self, p_name, p_updated_qty):
        """ This method will increase the qty amount"""

        # Iterate over all frames in order_frame to find the correct label
        for item_frame in self.order_frame.winfo_children():
            children_in_item_frame = item_frame.winfo_children() # Get and store all child widgets located in the item_frame
            label_name = children_in_item_frame[0]  # First child is the name_label
            #print(f"Label name: {label_name.cget("text")}")  # Debug print

            if label_name.cget("text") == p_name:
                qty_label = children_in_item_frame[1] # (second child widget in each item_frame)
                #print(f"Current qty: {qty_label.cget("text")}")  # Debug print
                qty_label.configure(text=f"{p_updated_qty}")  # Update the quantity label

                # Call update_price_label to update the price based on current qty
                self.update_price_label(p_name, self.item_dict[p_name]["price"], p_updated_qty)

        # Update the (sub-tax & total display labels)
        self.order.update_payment_labels()


    def update_price_label(self,p_name,p_price, p_updated_qty):
        """ This method will update the price amount in the label based on the updated quantity. """

        # Total Price =  Qty x Price
        total_price = p_updated_qty * p_price

        for item_frame in self.order_frame.winfo_children():
            children_in_item_frame = item_frame.winfo_children()   # Find the name of each label within each item_frame
            label_name = children_in_item_frame[0]  # First child is the name_label

            if label_name.cget("text") == p_name:
                price_label = children_in_item_frame[2] # (third child widget in each item_frame)
                price_label.configure(text=f"${total_price:.2f}")  # Update the price label with total price

    def apply_discount(self):
        """ This method calls a method in the order class to apply discount open clicking the discount button"""

        # Call the toggle method in the order class to apply or remove discount
        self.order.toggle_discount()


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

        # RIGHT FRAME (create the right_frame second so it can be pass to the middle frame)
        self.right_frame = RightFrame(self)

        # Pass right_frame into mid_frame
        self.mid_frame.set_right_frame(self.right_frame)

        # LEFT FRAME (Create the left frame last and pass mid_frame to the left frame)
        self.left_frame = LeftFrame(self, self.mid_frame)

        # Pack frames in order: Left -> Middle -> Right
        self.left_frame.pack(side="left", fill="y") # LEFT FRAME (Toggle Menu)
        self.mid_frame.pack(side="left", fill="both", expand=True)  # Middle FRAME (Button Area)
        self.right_frame.pack(side="left", fill="y") # RIGHT FRAME (Display Area)

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
