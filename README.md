# CSC226 Final Project

## Instructions

Exclamation Marks  ️indicate action items; you should remove these emoji as you complete/update the items which 
  they accompany. (This means that your final README should have no  ️in it!)

**Author(s)* Gavin Miller, Alina Petrosyants

**Google Doc Link**: https://docs.google.com/document/d/1Tsf9GHin8wAM7IFgzROiJbQJ-GSK09jl3QHG7QsOEGc/edit?tab=t.0

---

## Milestone 1: Setup, Planning, Design

**Title**: Pepperoni Vs Sausage: The Ultimate Game of Checkers

**Purpose**: This will be a fun and visually appealing two person checkers game

**Source Assignment(s)**: `Barcode assignment dictionary: self.left_side = []
        self.right_side = []

        self.left_dict = {0: '0001101', 1: "0011001", 2: "0010011", 3: '0111101', 4: '0100011',
                          5: '0110001', 6: '0101111', 7: '0111011', 8: '0110111', 9: "0001011"}

        self.right_dict = {0: '1110010', 1: '1100110', 2: '1101100', 3: '1000010', 4: '1011100',
                           5: '1001110', 6: '1010000', 7: '1000100', 8: '1001000', 9: '1110100'}`

        Will refer to T11 and T12 for GUI, we are using pygame but will use GUI basic programming habits
        from tkinter (thoughts? I think pygame will make something like checkers and animation easier than tkinter)

**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own:
  
![Screenshot 2025-04-01 192448.png](image/Screenshot%202025-04-01%20192448.png)
![Screenshot 2025-04-01 192455.png](image/Screenshot%202025-04-01%20192455.png)
![Screenshot 2025-04-01 192506.png](image/Screenshot%202025-04-01%20192506.png)
![Screenshot 2025-04-01 192515.png](image/Screenshot%202025-04-01%20192515.png)
**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments, then re-branching out from the merged code.  

```
    Branch 1 starting name: millerg3
    Branch 2 starting name: petryosyantsa
```

### References 

Throughout this project, you will likely use outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update this 
section as you go. DO NOT forget about it!

[pizza.jpg] Inspiration for pizza checkers, wanted to make it an actual digital game and use cooler checker pieces
(pepperoni and sausage)
---

https://www.pythontutorial.net/tkinter/tkinter-grid/ Using for ideas to set up the board
https://pythonguides.com/python-for-loop-index/ Refresher on how to find current index in list while looping, using for checker pieces
https://www.reddit.com/r/learnpython/comments/3osysb/tkinter_making_buttons_from_a_list_of_items_the/ Using func partial tools
to evalute before runtime
https://www.reddit.com/r/learnpython/comments/41qxp1/why_use_functoolspartial_instead_of_a_lambda/ Information
on partial and lambda, explaining why these tools are used and the application of both
https://emunix.emich.edu/~mevett/AI/Checkers/checkersNotation.html Reference for checkers board + potential matrix
https://stackoverflow.com/questions/68191068/how-to-disappear-a-button-after-clicking-on-it-in-tkinter How to get rid of buttons
https://stackoverflow.com/questions/11541262/basic-query-regarding-bindtags-in-tkinter bindtags in tkinter
## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    We have made a frame and a design plan for our future program. It going pretty well, we are feeling on track. For now, we are worried 
    about grid set up and movement on the board. What suprised us is that our programm seems like a very simple game of checkers, but when we 
    were making a frame - there is actually a lot of steps, and things to be done. We know it will be challenging in some aspects, but 
    we are looking forward to figure it out!  
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `80%`

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
    *We feel pretty confident about the completing the project, we just have some bugs to fix, and 
    make it function better. I think we can keep using the planning strategy that we have to keep track
    of the project and stuff we have left to do. 
```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions

In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button 
in PyCharm. 

The first thing you both select a team and choose your side to play, and if you grey - you can choose your piece by clicking 
on it and move it on the board diagonally once, and then you alternate turns, if you get to hop over a piece - you can go 
diagonally two spaces, and then by clicking on their piece and then clicking backspace - you take their piece, and if one team 
has taken all the pieces of another team - they won the game. If you reach  the other side of the board you can also move backwards.

### Errors and Constraints

Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.

Done!

### Peer Evaluation

It is important that all members of your team contribute equitably. The peer evaluation is your chance to either 
a) celebrate the great work you all did together as an effective team, or b) indicate to the instructor if a member of
your team did not contribute their fair share. Grades will be adjusted for any team member who is evaluated poorly. Your
commit history will be used as evidence, so make sure you are using git effectively!

We are good, we worked well.

### Reflection

Each partner should write three to four well-written paragraphs address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- How well did you work with your partner? What made it go well? What made it challenging?

```
    Partner 1: **We have selected this project because my partner has this idea, and I liked it, then we decided to add something 
    creative to it and planned to do pizza and sausage checkers game. I think our project is reflecting 80% of our initil design, because
    we decided we are not foing to implement graphic design, so we just have primitive checkers game, but it can be played 
    properly, and we are proud of it. I actually learned a lot from working with Gavin, especially how to think about algorithm 
    and how to look for solutions without looking for all the answers or already written program, also I got better at classes. I think my partner worked 
    well, and I believe he made most of the contribution to the coding part, it was challenging for me to keep up, but I learned a lot, and that 
    I should be communicating better on the progress and things that I am working on. Overall, it was great experience, and I am satisfied with our result! 
```

```
    Gavin: ** We selected this project because we were looking for a fun game to make, and checkers seemed like a fun idea that
    seemed simple, but complex enough to give us enough work to do and have a good learning experience, and we liked the idea of
    a unique twist with the pizza idea. Our final design pretty closely reflects the initial ideas, though we didn't get to everything.
    We didn't implement the full design, and not all of the functions/edge cases are fully finished. I learned how to work better
    with GUI's and event handling, implementation of more complex data structures and algorithms, how to work better and communicate
    with my partner, and the software design process. One of the hardest parts was just getting everything to function with 
    Tkinter, and correct implementation of storing pieces. Updating and getting pieces to move was a huge challenge, and doing
    it with Tkinter and scrambling to get everything to work got messy very quickly. Next time, I would try to improve my skills
    at working with a partner, I'm often too quick to do things myself, and we could benefit by communicating better and teaching eachother
    more. I just talked about this one, like I said I do thing I could be better at it, but we did a good job overall. We tried 
    to meet multiple times a week, and we did a good job with issues and really clarifying the next simple steps. It was challenging
    working on our own then meeting to merge and just seeing different things.. It's hard to manage time and work apart, we can't always
    work together. Overall, even though the project is a bit shallow, it is functional as a checkers game at a simple level, and 
    the things we implemented and learned helped us learn a lot, so I am happy with it.
```

---