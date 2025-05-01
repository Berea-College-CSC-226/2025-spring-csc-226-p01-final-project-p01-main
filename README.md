# CSC226 Final Project

## Instructions

❗️Exclamation Marks ❗️indicate action items; you should remove these emoji as you complete/update the items which 
  they accompany. (This means that your final README should have no ❗️in it!)

**Author(s)**: Kushal Phuyel and Naz Tulegenova

**Google Doc Link**: https://docs.google.com/document/d/1uXYmq2smmy8lrSaCPWos-9aN8YhU7vEmuUgoHlaSnnY/edit?usp=sharing

---

## Milestone 1: Setup, Planning, Design

**Title**: `TurtlEvasion!`

**Purpose**: `This project is a clicking game where players tap a randomly appearing turtle to earn points within a 
20-second timer.`

**Source Assignment(s)**: `T02: Exploring Turtles, T03: Boustrophedon Turtles, HW06: Oh The Places You'll Go, 
HW02: Loopy Turtles and HW 03: Fully Functional Gitty Psychedelic Robotic Turtles. We are planning to use as many 
things we need in order to complete this project. We have a lot of source assignments listed but we will use 
certain things from each one because each assignment has new things about turtle. `

**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own:
  
![Don't leave me in your README!](image/crc_turtle.png)

**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments, then re-branching out from the merged code.  

```
    Branch 1 starting name: kushals branch - phuyelk
    Branch 2 starting name: naz's branch - tulegenovan
```

### References 

Throughout this project, you will likely use outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update this 
section as you go. DO NOT forget about it!

```
    we used ChatGPT when we got absolutely stuck, and needed some guidance. We used it to help us guide us in the right 
    directions when we got stuck. We also used the PyCharm game dictionary along with the Tkinter, we also had to track back
    to some of the HW and TW to get ideas on how to use randit, and things of that sort. 
```

## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    We are feeling good about our project, we made a lot of progress and I feel that we are ahead of others. 
    Only thing that has us worried is how we will implement the different difficulty levels into the game. But overall,
    we are doing well and cooperating well and also putting in equal amount of efforts and work. 
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `85%`

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
    Very confident, we are almost done, and we have been progressing greatly. Something we can keep doing to ensure
    we get this done is keep working on it together, diving everything into small tasks, and make progress everytime we do. While we’ve encountered some 
    challenges, especially with timer and visibility for the fake.png, we’ve been able to solve them through testing 
    and iteration. This gives us confidence that we can handle any remaining issues.

```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions

After you press the Run button in PyCharm, the game window will appear. 
Click on the turtle as fast as you can every time it randomly shows up on 
the screen. Every click on the turtle gives you 1 point, if you end up clicking
on the fake turtle, which is the green fish, you will then lost a point. The game will 
automatically end after 20 seconds. Once the game ends, your final score 
will be displayed, and asked if you want to play again or not. if user presses no
then the game window will close and stop running, if user presses yes then game and window
will restart in order to start another round. 

### Errors and Constraints

I believe that our code runs well, and just the way we want it to. 

### Peer Evaluation

Both partners contributed equally to the project. We communicated effectively, divided 
tasks fairly, and helped each other debug and test the program. Both of us committed 
regularly to the GitHub repository and worked together in meetings to solve problems. 
We feel both partners should receive full credit for the work.

We began the project by outlining the base together, discussing the main structure, how gameplay should work, and what 
features we wanted to include. We were able to create an outline for our program. The first major piece that got built 
was the timer, which was done by Kushal. After that, we were focusing on resollving issues in our code together. 

Once resolved, Naz focused on designing and improving the UI. She worked on how everything looked on screen, cleaning up the 
layout, choosing fonts, animations, and making the overall interface more user-friendly and fun.

Once the UI was shaping up, Kushal added the difficulty level functionality, along with their screen buttons to choose 
between Normal and Hard modes. He also worked on writing reflections in Milestones. Later, he also added a score 
tracking system that stores scores across players and calculates both the average and highest score. 

Around the same time, Naz worked on adding interactive elements like simple loading bar animation, so the user will be prepared.

Overall, we both contributed fairly across the project. Our roles naturally split based on strengths: Kushal focused 
more on functionality and data, and Naz focused more on visuals and player interaction. We communicated through Slack, 
kept each other updated, and helped each other when needed. It was a smooth and balanced collaboration.

### Reflection

Each partner should write three to four well-written paragraphs address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- How well did you work with your partner? What made it go well? What made it challenging?

```
    Partner 1: Naz Tulegenova
    We picked this project because we wanted something fun to play, but also something that felt doable to code. 
    A simple game like this seemed like a good balance. It gave us room to be creative, and it didn’t require anything 
    too complicated to get started. We also liked the idea of building something that reacts to the player and feels 
    kind of alive.

    The final project actually turned out a bit better than I expected. At first, we had a basic idea in mind, but as 
    we worked on it, we kept coming up with more small features to add like the fake image showing up randomly, the 
    message box at the end, "pop" effect, the pre-game “GO!” screen. So it became more complete than we originally 
    thought, which was nice.

    One thing we learned from this was how important it is to build step by step. We didn’t try to do everything at 
    once. Instead, we added one piece at a time and made sure it worked before moving on. That made everything feel 
    more manageable. Also, communication, really, it matters. We had to keep each other in the loop, through 
    Slack, so we didn’t get off track or miss something.

    The hardest part was getting the core of the game working like making the turtle move, behave right, and show up 
    when it should. That foundation took time. After that, adding other things felt more fun and creative. If we did it 
    again, maybe we’d plan out the structure a little more at the beginning. We worked well as partners, there were no 
    issues between us, but syncing our schedules was hard. We made it work by messaging on Slack when we couldn’t meet.

```

```
    Partner 2: We picked this project because we thought it would be fun and we could apply lots of the 
    turtle and graphics techniques we practiced in earlier assignments. 
    
    I think the final project matches our original idea in most ways. We successfully made a working game with a timer and score
    tracking. I learned a lot about working with images, classes, and event handling in Python. 
    
    The hardest part for me was getting the timer and movement to work together without freezing or glitching. If I could change something,
    I would want to start integrating features like the difficulty earlier so we had more time to debug them. 
    I really liked working with my partner; we both stayed motivated and worked hard, and we managed to divide the work 
    fairly while helping each other at the same time.
```

---