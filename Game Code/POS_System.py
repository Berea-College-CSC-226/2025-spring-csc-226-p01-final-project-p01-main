# Username: micklers
# Name: Shadaria Mickler
#
#
#######################################################################################
import customtkinter,random, subprocess


class RightFrameButtonFunctionality:
    def __init__(self, delete_button, cancel_button, order_frame, order, item_ref):
        self.delete_button = delete_button
        self.cancel_button = cancel_button
        self.order_frame = order_frame # Frame that holds orders
        self.item_ref = item_ref
        self.order = order # Reference the display labels

    def cancel_order(self):
        """ This method will destroy all widgets in a window and generate a new order and at the same time updating the order number"""

        # Clear all the current order display widgets
        for widget in self.order_frame.winfo_children():
            widget.destroy()

        # Reset any other components like totals, discount, etc.
        self.order.reset_totals()

    def delete_item(self, p_frame):
        """This method will destroy frames holding individual label widgets for a specific item """

        if hasattr(p_frame, 'item_name'): # ChatGPT
            item_name = p_frame.item_name  # Get the item name from the frame

            # Remove the frame from the UI
            p_frame.destroy()

            # Remove the frame from the item_ref list
            if p_frame in self.item_ref:
                self.item_ref.remove(p_frame)

            # Remove the item from the order dictionary
            self.order.remove_item_from_order(item_name)

            # Update the payment labels
            self.order.update_payment_labels()

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

    def reset_totals(self):
        """
        Clear all the ENTIRE order from the order dictionary
        This method is called when an order is canceled
        """
        self.item_dict.clear()

    def remove_item_from_order(self, item_name):
        """
        Removes a SPECIFIC item from the order dictionary based on the item_name
        This method is called when an item is deleted from the order.
        """
        # Get the price of the item being removed
        item_price = self.item_dict[item_name]['price']
        item_qty = self.item_dict[item_name]['qty']
        total_price_to_subtract = item_price * item_qty  # Subtract the total cost of the item (price * quantity)

        # Delete the item from the order dictionary
        del self.item_dict[item_name]

        # Subtract the item price from the total
        _, sales_tax, discount, total = self.calculate_totals()
        new_total = total - total_price_to_subtract

        # Update the total label to reflect the new total after removal
        self.total_label.configure(text=f"${new_total:.2f}")

        # Update the payment labels (to refresh tax and discount if needed)
        self.update_payment_labels()

class LeftFrame(customtkinter.CTkFrame):
    """ This Frame will display a toggle menu with general buttons and some more buttons"""
    def __init__(self, master, mid_frame, gui_ref):
        super().__init__(master, width=230, height=864, fg_color = "#181818")

        self.pack_propagate(False)  # ChatGPT
        self.mid_frame = mid_frame # Store a reference to the MiddleFrame instance so methods can be called from LeftFrame
        self.gui_ref = gui_ref # reference to gui class

        # Track Menu Visibility
        self.menu_visible = True

        # Top Bar Frame (toggle button and label)
        top_bar_frame = customtkinter.CTkFrame(self, fg_color="transparent", width = 70, height = 50)
        top_bar_frame.pack(pady=15, padx=10, anchor="nw", fill="x")

        # Toggle Button
        self.toggle_btn = customtkinter.CTkButton(top_bar_frame, text="☰", width=35, corner_radius = 3, fg_color = "transparent",hover_color = "#4169E1", command=self.toggle_menu)
        self.toggle_btn.pack(side = "left", padx = (0,10))

        # Title Label
        self.label = customtkinter.CTkLabel(top_bar_frame, text = "StuPOS", width = 35, font = ("Roboto", 17))
        self.label.pack(side = "left")

        # Container Widget
        self.menu_container = customtkinter.CTkFrame(self, fg_color="transparent")
        self.menu_container.pack(fill="both", expand=True, padx=0, pady=20)

        # Button Data
        btn_name = ["Appetizers", "Sandwiches", "Sides", "Desserts", "Drinks"]
        self.btn_ref = {}  # Instant var to store references to each button

        for index, text in enumerate(btn_name):
            btn = customtkinter.CTkButton(
                self.menu_container,
                text=text,
                corner_radius = 3,
                height = 50,
                fg_color = "transparent",
                hover_color = "#4169E1",
                command = lambda category=text: self.call_specific_button(category)
            )
            btn.pack(pady=15, fill="x")
            self.btn_ref[index] = btn # Store button ref

        # Spacer to push Exit button to bottom (ChatGPT)
        spacer = customtkinter.CTkLabel(self.menu_container, text="")
        spacer.pack(expand=True)  # Expands and fills space between buttons and exit

        # Exit Button
        self.exit_btn = customtkinter.CTkButton(self.menu_container, text = "Exit", corner_radius = 3, height = 50, fg_color = "transparent",hover_color = "#4169E1", command = self.exit)
        self.exit_btn.pack(pady = 0, fill = "x")

    def toggle_menu(self):
        """ Checks to see if toggle menu is visible or not to determine whether to display toggle elements"""
        if self.menu_visible:
            self.menu_container.pack_forget() # Hide the container widget
        else:
            self.menu_container.pack(fill="both", expand=True, padx=0, pady= 20) # Show the container widget
        self.menu_visible = not self.menu_visible

    def call_specific_button(self, p_category):
        """ When a general button is clicked, initialize specific buttons related to that category. """
        self.mid_frame.display_specific_buttons(p_category) # Call the method in MiddleFrame from the LeftFrame class and pass the categories of that general button

    def exit(self):
        """ Call exit_pos method in gui class from left frame"""
        self.gui_ref.exit_pos()

class MiddleFrame(customtkinter.CTkFrame):
    """ This frame is where the buttons will go"""
    def __init__(self,master):
        super().__init__(master, width = 500, fg_color = "#121212")

        self.specific_btn_ref = {}  # Store references to specific buttons
        self.right_frame = None # Placeholder (ChatGPT)

        # Search Bar (Entry Widget)
        self.search_bar = customtkinter.CTkEntry(self, placeholder_text = "Search for products . . .", width = 710, height = 40, corner_radius=3, fg_color = "#282828", state = "disable")
        self.search_bar.pack(anchor = "nw", padx = 15, pady = (15,1), fill = "x")

        # Container Frame for Buttons (below search bar)
        self.specific_btn_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.specific_btn_frame.pack(anchor="nw", padx=15, pady=(35, 0), fill="both")

        # Buttons Data
        self.button_data = {
            "Appetizers": [
                ("The Classic Crunch Bites", 7.99),
                ("Smoky BBQ Bliss Bites", 7.99),
                ("Zesty Lemon Kick Bites", 7.99),
                ("Fiery Buffalo Heat Bites", 7.99),
                ("Mozzarella Sticks", 7.99),
                ("Stuffed Jalapeños", 7.99),
                ("Spinach Artichoke Dip", 7.99),
                ("Crispy Calamari", 7.99)
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
                ("Onion Rings", 2.49),
                ("Garlic Bread", 2.29),
                ("Sweet Potato Fries", 2.79),
                ("Baked Mac & Cheese", 3.49),
                ("Corn on the Cob", 2.49)
            ],
            "Desserts": [
                ("Strawberry Shortcake", 3.99),
                ("Banana Pudding", 3.49),
                ("Vanilla Ice Cream", 2.49),
                ("Chocolate Ice Cream", 2.49),
                ("Cheesecake", 4.49),
                ("Apple Pie", 3.99),
                ("Chocolate Lava Cake", 4.49),
                ("Cinnamon Sugar Churros", 3.99)
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

        # Button Colors(ChatGPT)
        button_colors = [
            "#1E3A8A",  # Dark Blue
            "#4C1D95",  # Dark Purple
            "#D61CFF",  # Neon Pink
            "#16A34A",  # Dark Green
            "#2C3E50",  # Charcoal Blue
            "#8B5CF6",  # Medium Purple
            "#10B981",  # Emerald Green
            "#9B4D96"  # Purple
        ]

        # Iterate through menu items (Key) & prices (Value)
        for item_name, item_price in menu_item:
            # Create a button for each item
            btn = customtkinter.CTkButton(
                self.specific_btn_frame,
                text = item_name,
                corner_radius=3,
                height = 175,
                fg_color = button_colors[counter % len(button_colors)],
                font = ("Roboto", 14),
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
        super().__init__(master, width = 550, height=864, corner_radius = 1,fg_color = "#181818", border_width = 1, border_color = "#282828")

        self.pack_propagate(False)  # ChatGPT
        self.item_dict = {} # Dictionary stores item and qty
        self.item_frame_ref = [] # List store ref to frames

        # Upper frame (Order Number and User Labels)
        self.upper_frame = customtkinter.CTkFrame(self, fg_color="#1E1E1E", corner_radius=8, height=40, width=500)
        self.upper_frame.pack(fill="both", expand=False, padx=10, pady=(20, 0))

        # Tables Label
        self.tables_label = customtkinter.CTkLabel(self.upper_frame, text="Tables", font=("Roboto", 15))
        self.tables_label.pack(side="left", padx=(30, 50))

        # Order Number Label
        self.order_num_label = customtkinter.CTkLabel(self.upper_frame, text="Order #", font=("Roboto", 15))
        self.order_num_label.pack(side="left", padx=(110, 0))

        # Order Number Display
        self.order_num_display = customtkinter.CTkLabel(self.upper_frame, text=f"{0}", font=("Roboto", 15))
        self.order_num_display.pack(side="left", padx=(5, 5))

        # Online Label
        self.online_label = customtkinter.CTkLabel(self.upper_frame, text="Online", font=("Roboto", 15))
        self.online_label.pack(side="right", padx=(70, 40))

        # Divider Line (Upper)
        divider1 = customtkinter.CTkFrame(self, height=2, width=800, fg_color="#404040")
        divider1.pack(fill = "both", pady = (45,1))

        # Save, Cancel, Delete Button Container Frame
        button_row = customtkinter.CTkFrame(self, fg_color = "transparent")
        button_row.pack(fill="x", pady=5, padx=5)

        # Cancel Button (Left)
        self.cancel_btn = customtkinter.CTkButton(button_row, text="Cancel", corner_radius=3, height=40, width=125,fg_color = "#4169E1",
                command = self.cancel)
        self.cancel_btn.pack(side="left", padx=(5, 5))

        # Delete Button (Right)
        self.delete_btn = customtkinter.CTkButton(button_row, text="Delete", corner_radius=3, height=40, width=125, state = "disabled",fg_color = "#4169E1")
        self.delete_btn.pack(side="right", padx=(5, 5))

        # Save Button (Center)
        self.save_btn = customtkinter.CTkButton(button_row, text = "Save", corner_radius=3, height=40, width = 125, state = "disabled",fg_color = "#4169E1")
        self.save_btn.pack(padx = (5,5))

        # Divider Line
        divider2 = customtkinter.CTkFrame(self, height=2, width=800, fg_color="#404040")
        divider2.pack(fill = "both", pady = (5,1))

        # Detail Frame (Hold label widgets "Name" "QTY" "Each" "Total")
        self.detail_frame = customtkinter.CTkFrame(self, fg_color="#181818", corner_radius=3, height=30)
        self.detail_frame.pack(fill="both", padx=10, pady=(2, 0), expand=False)

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
        self.order_frame = customtkinter.CTkScrollableFrame(self, fg_color="#181818", width = 400, height = 440, corner_radius=3, border_width = 1, border_color = "#282828")
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

        # Instance of the "Order" class
        self.order = Order(self.item_dict, self.display_tax_label, self.display_total_label, self.display_discount_label)

        # Discount & Pay Button (in a frame)
        button_row2 = customtkinter.CTkFrame(self, fg_color = "transparent")
        button_row2.pack(fill="x", pady=5, padx=10)

        # Discount Button (Left)
        self.discount_btn = customtkinter.CTkButton(button_row2, text="Discount", corner_radius=3, height=45,border_width = 1, fg_color = "transparent", border_color = "#282828", hover_color = "#4169E1", command = self.apply_discount)
        self.discount_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

        # Pay Button (Right)
        self.pay_btn = customtkinter.CTkButton(button_row2, text="Pay", corner_radius=3, height=45,fg_color = "#1E3A8A", hover_color = "#2F7AB1", command = self.pay)
        self.pay_btn.pack(side="right", expand=True, fill="x", padx=(5, 0))

        # Instance of the "RightFrameButtonFunctionality" class
        self.right_btn_ftn = RightFrameButtonFunctionality(delete_button=self.delete_btn, cancel_button=self.cancel_btn,order_frame=self.order_frame, order=self.order, item_ref = self.item_frame_ref)


    def display_menu_item(self, p_name, p_price, item_name = None):
        """ This method takes input parameter from another method and uses it to create a label widgets in the Order Frame(container widget)"""

        # Item name is none so it will be assigned a name
        if item_name is None:
            item_name = p_name

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

                # Item_frame (hold the name and price labels together)
                item_frame = customtkinter.CTkFrame(self.order_frame, fg_color="transparent")
                item_frame.grid(row=row_count, column=0, columnspan=3, sticky="w", padx=(10, 5), pady=5)

                # Item name is assigned to the frame ??
                item_frame.item_name = item_name
                #print(f"Debug: Assigned item name '{item_name}' to the frame.")

                # Store reference
                self.item_frame_ref.append(item_frame)
                #print(f"Debug: Added frame with item name '{item_name}' to the item_frame_ref list.")

                # Hover Over
                item_frame.bind("<Enter>", lambda e, f=item_frame: f.configure(fg_color="#D72222"))
                # Hover Away
                item_frame.bind("<Leave>", lambda e, f=item_frame: f.configure(fg_color="transparent"))

                # Bind left click event to the frame - Clicking the item will delete it
                item_frame.bind("<Button-1>", lambda e, frame=item_frame: self.delete(frame))

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

    def pay(self):
        """
        Temporarily changes the Pay button to 'Paid' with green color, disables it, generates a random order_num, then resets it.
        """
        original_txt = self.pay_btn.cget('text') # Get original text and stores it
        original_color = self.pay_btn.cget('fg_color') # Get the original color and store it

        # Configure Pay button to simulate a paid order
        self.pay_btn.configure(text="Paid", fg_color="green", state = "disabled")

        # Reset the order frame (data)
        for widget in self.order_frame.winfo_children():
            widget.destroy()

        self.order.reset_totals()  # Reset the order (total, tax, discount, etc.)
        self.order.update_payment_labels()  # Update the (sub-tax & total display labels)

        # Reset the button after 2.5 seconds
        self.pay_btn.after(2500,lambda: self.pay_btn.configure(text=original_txt, fg_color=original_color, state="normal"))

        # Generate a random 3-digit order number (between 100 and 999)
        new_order_num = random.randint(100, 999)
        self.order_num_display.configure(text=str(new_order_num))  # Update the label with the new number

    def delete(self,p_frame):
        """
        Calls the delete method from the rightframebuttonfunctionality class and pass the ref frame clicked.
        """
        self.right_btn_ftn.delete_item(p_frame)
        self.order.update_payment_labels()

    def cancel(self):
        """ This method calls the cancel method from the rightframebuttonfunctionality class"""
        self.right_btn_ftn.cancel_order()
        self.order.update_payment_labels()  # update totals to $0.00


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
        self.left_frame = LeftFrame(self, self.mid_frame, gui_ref = self)

        # Pack frames in order: Left -> Middle -> Right
        self.left_frame.pack(side="left", fill="y") # LEFT FRAME (Toggle Menu)
        self.mid_frame.pack(side="left", fill="both", expand=True)  # Middle FRAME (Button Area)
        self.right_frame.pack(side="left", fill="y") # RIGHT FRAME (Display Area)

    def exit_pos(self):
        """ When the exit button is clicked the pos returns to the main window"""
        self.destroy()  # Close the POS GUI



if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
