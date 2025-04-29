# ❗CSC226 Final Project

## Instructions

️Exclamation Marks  ️indicate action items; you should remove these emoji as you complete/update the items which 
  they accompany. (This means that your final README should have no  ️in it!)


️**Author(s)**: Dayton Conwell Karina Ismailova

  **Google Doc Link**: https://docs.google.com/document/d/1M4_pZLKzrGjGwAjhPCBc2SmoOvJ_NzyybsaB7eOy0ZQ/edit?tab=t.0

---

## Milestone 1: Setup, Planning, Design

️**Title**: Space Adventure

  **Purpose**: `TO inform users about planets through an informational game`

  **Source Assignment(s)**: 
We will use HW06: Oh the Places You'll Go! for putting an image of planets as a background. 
We will use T11: The Legend of Tuna: Breath of Catnip to move the rocket across the planets.
`Chapter 4/ HW02: Python Turtle Graphics – using Turtle for graphics, this chapter will help us with drawing the rocket, planets, and movement.

Chapter 15/ Teamwork 12: GUI and Event-Driven Programming – Since our project involves holding a key to move the rocket, this chapter will help with handling user input and key events.

Chapter 5: Python Modules – organizing our code into separate files for readability, using modules will be useful.

Chapter 6/ Any teamwork and HW with functions: Functions – Using functions will make our code more structured and reusable.

Chapter 17 & 18/ T10-now/ HW9 - now: Classes and Objects – to make our rocket and planets objects with attributes (e.g., name, size, distance), object-oriented programming will be helpful.`

️**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own: 
![Don't leave me in your README!](image/Screenshot%202025-04-09%20092702.png)
![Don't leave me in your README!](image/Screenshot%202025-04-09%20092715.png)
![Don't leave me in your README!](image/Screenshot%202025-04-09%20092734.png)
![Don't leave me in your README!](image/Screenshot%202025-04-09%20092752.png)
****
️**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments, then re-branching out from the merged code.  

```
    Branch 1 starting name: conwelld
    Branch 2 starting name: ismailovak
```

### References 

Throughout this project, you will likely use outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update this 
section as you go. DO NOT forget about it!

Online Documentation & Tutorials
Python Official Documentation (https://docs.python.org/3/) – Referenced for syntax, Turtle graphics, and event-driven programming.

GeeksforGeeks (https://www.geeksforgeeks.org/, https://www.geeksforgeeks.org/python-display-text-to-pygame-window/, https://www.geeksforgeeks.org/how-to-use-multiple-screens-on-pygame/, 
https://www.geeksforgeeks.org/how-to-use-multiple-screens-on-pygame/, https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/,) – Used for examples on handling keyboard events and object-oriented programming, making buttons, putting texts on a screen.

Real Python (https://realpython.com/) – Consulted for best practices in writing modular Python code.

Python Official Documentation (https://docs.python.org/3/library/sys.html) – Referenced for the use of the sys module to handle system-specific parameters and functions like program exit handling.

Pygame Documentation (https://www.pygame.org/docs/) – Used for understanding how to work with images, implement movement, and manage sprite drawing in Pygame.

W3Schools on Python Classes (https://www.w3schools.com/python/python_classes.asp) – Clarifying concepts about object-oriented programming and the structure of classes in Python.

AI & Code Assistance
ChatGPT – Used for brainstorming ideas, debugging code, and refining program structure. Suggestions were implemented after personal review and modifications. (https://chatgpt.com/share/68110b3e-8704-8011-82ba-a0fe70acfe15)

Stack Overflow (https://stackoverflow.com/, https://stackoverflow.com/questions/64254687/how-to-allow-the-user-to-type-only-under-certain-conditions-in-pygame) – Used for troubleshooting specific coding issues related to key event handling and Turtle movement.

T11



---

## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    We did create a structure in the last homework, we are currently working on putting the neccessary stuff on the screen
     of the pygame. We are having some confusion, but we will communicate throyugh slack and issuing in git and will get it 
     this week. We are feeling ok abput our progress. We are not worried too much, more surprised by how fast we are 
     implementing the code. Our general feeling is optimistic.
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

️**Completion Percentage**: `65%`

️**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
    We feel pretty confident in out ability to complete this project, because we have moved along rather quickly 
    and are able to implement the things we want. We could perhaps implement a strategy of using the issue queue a 
    but better 
```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions

In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button 
in PyCharm. 

After hitting the “Run” button in PyCharm, the user will see a rocket on the left side of the screen with a row of planets spread across the background. To move the rocket, the user simply holds down the right arrow key. As the rocket moves toward the planets, it will automatically detect when it reaches one. Once a planet is detected, a “Land” button appears on the screen. By clicking the “Land” button, a pop-up window will display the planet’s name along with a short, kid-friendly description. The user can press the Escape key to close the pop-up window and return to the game. Additionally, pressing the R key will restart the game at any time. The experience is visual and interactive, designed specifically for preschool-aged children to help them learn fun facts about the planets in a simple and engaging way.

### Errors and Constraints

Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.

### Peer Evaluation

It is important that all members of your team contribute equitably. The peer evaluation is your chance to either 
a) celebrate the great work you all did together as an effective team, or b) indicate to the instructor if a member of
your team did not contribute their fair share. Grades will be adjusted for any team member who is evaluated poorly. Your
commit history will be used as evidence, so make sure you are using git effectively!

Our team worked collaboratively and made sure that all members contributed fairly throughout the development of the project. From the beginning, we divided the responsibilities based on our individual strengths and made sure to stay in regular communication. Each person was actively involved in both the coding and the design process, and we consistently used Git to track changes, ensuring that our contributions were transparent and well-documented. Looking at our commit history, it’s clear that we all took equal responsibility in building and refining the game.

The peer evaluation is a fair and important way to acknowledge each team member’s effort. In our case, I feel confident in celebrating the great teamwork we demonstrated. Everyone was engaged, willing to help one another, and flexible when changes or challenges came up. There was a strong sense of mutual respect and shared accountability, which made the collaboration smooth and enjoyable. Using Git effectively not only kept our project organized but also held us accountable for doing our fair share.

### Reflection

Each partner should write three to four well-written paragraphs address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- How well did you work with your partner? What made it go well? What made it challenging?

```
    Partner 1: We chose this project to inform people about planets in a fun and interactive way as opposed to just text on a screen, intended to 
    be a fun and educational project, it resembles fairly closely our intial design the only difference being how controls are handled
    essentially how long a button is pushed turned into pushing a button multiple times. I learned a lot from this process
    for example, how classes interact with each other and how initializing several objects in a class can be useful for 
    describing several things at once. The hardest part in my opinion was handling formatting, more specficaly for buttons
    looking through the mind of the user rather than the programmer, not taking the easy way out but trying to make it easier for
    the user to look at, I had to constantly change the resoultion of the screen, so I had to constantly mess with the parameters of
    the button. What I would do differently is focus on changing the screen as little as possible so I did not have to constantly
    change buttons and such. I think me and my partner worked quite well together, getting to explain the concepts we were
    utilizing allowed me to better understand what I was doing. Furthermore, we were able to get what we wanted done no real
    hiccups and that was good for me. The only chalenging part was getting started, however after the fact the ball was rolling
    and good implementation followed.
```

```
    Partner 2: Karina Ismailova
We chose this rocket and planets game because it combined our interest in space with the opportunity to practice essential coding concepts such as event handling, image manipulation, and collision detection. It was also visually engaging and simple enough in scope to complete within our timeline while still offering room for creativity. We liked the idea of creating something interactive and educational, and the visual aspect of a moving rocket made the project more enjoyable to develop and test.
Our final project stayed fairly close to our initial design, though we simplified some elements. We managed to include all the planets and ensure they each had distinct descriptions, which matched our initial vision for an informative space-themed game.
What We Learned and the Hardest Part:
We learned how to structure a game loop, handle keypress events, and use object-oriented programming to manage game elements like the rocket and planets. The hardest part was getting the rocket to stop moving cleanly at each planet without overshooting or missing the detection area. We had to fine-tune the coordinates and hitboxes to make the game feel natural.
Reflections on Teamwork and Future Improvements:
Working with my partner was smooth and productive. We both contributed code, tested features, and communicated regularly about what we were working on. What went well was our clear division of tasks and shared goal for the project. One challenge was aligning our schedules, especially close to the deadline, but we overcame it by coordinating via messages and Git commits. If we were to do this again, I would start testing visuals earlier to allow easier changes. I also learned the importance of using Git more frequently to avoid merge conflicts and keep better track of progress.
```

---