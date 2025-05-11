# # First Row Buttons
# all_checks_btn = customtkinter.CTkButton(self, text="All checks", width=150, height=45)
# all_checks_btn.grid(row=0, column=3, padx=10, sticky="ew")
# exit_btn = customtkinter.CTkButton(self, text="Exit", fg_color="#ff4d4d", hover_color="#e60000", width=150,
#                                    height=45)
# exit_btn.grid(row=0, column=4, padx=10, sticky="ew")
#
# # Divider under top buttons (Row 0)
# divider_top = customtkinter.CTkFrame(self, height=2, width=1000, fg_color="#E5BF00")
# divider_top.grid(row=1, column=0, columnspan=5, sticky="n", padx=10, pady=0)
#
# # General Buttons
# general_btn = ["Combo", "Sandwiches", "Sides", "Desserts", "Drinks"]
# for index, name in enumerate(general_btn):
#     btn = customtkinter.CTkButton(self, text=name, height=70, width=300)
#     btn.grid(row=1, column=index, sticky="ew", padx=10)

# def random_color():
#     return f'#{random.randint(100, 255):02x}{random.randint(100, 255):02x}{random.randint(100, 255):02x}'
#
# for row in range(6):
#     for col in range(6):
#         color = random_color()
#         cell = customtkinter.CTkFrame(self, fg_color=color, corner_radius=8)
#         cell.grid(row=row, column=col, sticky="sew", padx=5, pady=5)
# Grid Layout (6x6)
# for row in range(6):
#     self.grid_rowconfigure(row, weight=1)
# for col in range(6):
#     self.grid_columnconfigure(col, weight=1)
#
# # Create Frames (to place buttons in)
# self.frames = []  # Store references to row
# color_pal = ["#023547", "#17718B", "#1CCEE8", "#27EEC4", "#1BE37E", "#28A71A"]
#
# for row in range(6):  # Iterate through the six colors
#     color = color_pal[row]
#     row_frames = []
#     for col in range(6):
#         cell = customtkinter.CTkFrame(self, fg_color=color, corner_radius=6)
#         cell.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
#         row_frames.append(cell)  # Add frame references to empty list
#     self.frames.append(row_frames)
#
# # General Buttons (placed inside frames in column 0, rows 1–5)
# general_btn = ["Combos", "Sandwiches", "Sides", "Desserts", "Drinks"]
# hover_pal = ["#045a6b", "#1e8da6", "#44dcf1", "#4ff1d3", "#39eb98", "#44c32e"]
#
# for i, name in enumerate(general_btn):  # Iterate through rows in column 0
#     btn = customtkinter.CTkButton(
#         self.frames[i + 1][0],  # i+1 to start from row 1, column 0
#         text=name,
#         corner_radius=6,
#         fg_color=color_pal[i + 1],
#         hover_color=hover_pal[i + 1],
#         text_color="white")
#     btn.pack(expand=True, fill="both", padx=2, pady=2)
#
# # Hide Colorful frames (until one of the general buttons are clicked)
#
#
# # Specific buttons (initialize specific buttons, pack them into the colorful frames)
# # Create colorful frames for button layout (4x4 grid)
# self.frames = []  # Store references to rows
# color_pal = ["#1CCEE8", "#27EEC4", "#1BE37E", "#28A71A"]
#
# for row in range(4):  # Iterate through the four rows
#     color = color_pal[row]  # Pick color for this row
#     row_frames = []
#     for col in range(4):  # Iterate through the four columns
#         cell = customtkinter.CTkFrame(self, fg_color=color, corner_radius=3)
#         cell.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
#         row_frames.append(cell)  # Store the frame reference
#     self.frames.append(row_frames)  # Store the row in the frames list
# def filter_buttons(self, event):
#     """ This method captures the word the user types and compares it the name of buttons in the button frame to find a match"""
#
#     search_word = self.search_bar.get().lower()
#     # For every child widget (specific button) in the button frame
#     for button in self.specific_btn_frame.winfo_children():
#         button_text = button.cget('text').lower()  # Get the text of the button and store it
#         if search_word in button_text:
#             button.grid()  # show button
#         else:
#             button.grid_remove()  # hide button