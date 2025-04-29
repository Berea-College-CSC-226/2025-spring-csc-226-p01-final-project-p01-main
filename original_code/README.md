This folder is for holding your original assignments that you are using as a reference. 
Put the code in this folder, but DO NOT modify it directly! 

wn = turtle.Screen() #initializes screen

alex = turtle.Turtle() #makes two turtles
dayton = turtle.Turtle()

wn.bgcolor("white")

alex.speed("fastest") #hi
alex.penup()
dayton.hideturtle()

    def create_textbox1(self):
        """
        Creates a textbox into which the user can type

        :return: None
        """

        self.myTextBox1.pack()                      # pack means add to window

    def create_label1(self, labeltext=""):
        """
        Creates a label on the window and sets the label to labeltext

        :param labeltext: The text on the label
        :return: None
        """

        self.myTextLabel1Text.set(labeltext)        # Sets the Tkinter string variable
        self.myTextLabel1 = tk.Label(self.root, textvariable=self.myTextLabel1Text)
        self.myTextLabel1.pack()       

    def distance_from_origin(self):
        """
        Compute my distance from the origin

        :return: float representing distance from (0, 0)
        """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
import turtle # allows us to use the turtles library
wn = turtle.Screen() # creates a graphics window

txt = self.myTextBox1.get()                 # Retrieves the text entered by the user
        self.count += 1                             # increments each time the handler is called (button is pressed)
        if self.count % 10 == 0:
            message = "Wow, {1} clicks! Keep it up, {0}!".format(txt, self.count)
        else:
            message = "Hey {0}, click it again!\nYou have clicked the button {1} times.".format(txt, self.count)
        self.myTextLabel1Text.set(message)

def main():
    """
    Creates GUI and uses button, textbox and label GUI widgets

    :return: None
    """

    myGUI = MyTkinterApp("CSC226 Hello GUI")           # Create a new myTkinter object

    myGUI.create_button1("What is your name?")      # Calls the create button method to create a button
    myGUI.create_textbox1()                         # Calls the create textbox method for capturing user input
    myGUI.create_label1()                           # Create a label to writing text into (empty for now)

    myGUI.root.mainloop()                           # Needed to start the event loop
    def run(self):
        """
        Runs the game forever

        :return: None
        """
        while self.running:
            # Handle game ending first
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Handle user and game events next
            if pygame.sprite.spritecollide(self.tuna, [self.tacocat], False):
                # Collision! Prints the game ending text to the screen.
                font = pygame.font.SysFont("ComicSans", 36)
                txt = font.render('Taco, you caught me!!', True, "darkblue")
                self.screen.blit(txt, (self.size[0]//2, self.size[1]-100))
            else:
                # Keep playing!
                self.tuna.movement(pygame.key.get_pressed())
                self.tacocat.movement()
                self.screen.fill('#9CBEBA')
                self.screen.blit(self.tuna.surf, self.tuna.rect)
                self.screen.blit(self.tacocat.surf, self.tacocat.rect)
            pygame.display.update()
            self.clock.tick(24)

        pygame.quit()

