# ❗CSC226 Final Project

## Instructions

❗️Exclamation Marks ❗️indicate action items; you should remove these emoji as you complete/update the items which 
  they accompany. (This means that your final README should have no ❗️in it!)

️**Author(s)**: Shadaria Mickler

**Google Doc Link**: https://docs.google.com/document/d/18Ollp-Q9-JxPCMsv5_5mtRZN1qjXiAV-MKdliw0oUJ8/edit?usp=sharing
**Repo Link: https://github.com/Berea-College-CSC-226/p01-final-project-fatimaf_shadaria/tree/main

---

## Milestone 1: Setup, Planning, Design

**Title**: StuPOS - Student POS

**Purpose**: Restaurant order taking system

**Source Assignment(s)**: HW_04: A Bugs life

❗️**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own:
  
![Don't leave me in your README!](image/crc.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one. ")

**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments, then re-branching out from the merged code.  

```
    Branch 1 starting name: design_POS (shadaria)
    Branch 2 starting name: functionality_POS (shadaria)
    Branch 3 starting name: ____________________
```

### References 

Throughout this project, you will likely use outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update this 
section as you go. DO NOT forget about it!
````
    Referencece 1: ChatGPT
    # ChatGPT - Interaction between frames - https://chatgpt.com/c/6806f27a-25e4-800a-b15f-08fb55fa6eb9
    # ChatGPT - Maintaining Frame Sizes - https://chatgpt.com/c/6806f327-1668-800a-8461-e50208d39257
    # ChatGPT - Toggle Menu Walkthrough Steps - https://chatgpt.com/c/6806f391-ead8-800a-bac4-1192ead61ae6
    # ChatGPT - Lambda in Command - Prompt - I want to do a function call but i do not want to create a separate function to do so
    # ChatGPT - Spacer - Prompt - How can I push buttons to the bottom of my gui
    # ChatGPT - Nested Dictionary - https://chatgpt.com/c/680efcbe-2ee4-800a-8589-a61576eecf6a
    # Design - https://unipos.com.au/point-of-sale/kounta-dark-mode/
    # Dark mode colors - https://blog.karenying.com/posts/50-shades-of-dark-mode-gray
````
---


## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    Coding wise I am behind but I got a good outline to follow with detailed steps which has helped me so far to move the project along.
    I am somewhat bummed out I waited to do this project because know I am rushing, but its alright. I think the only thing that is worrying me is the test
    I planned on testing the functionality. So when x button is clicked does it do y, but I am unsure of how to create test suites do that, but I have a decent guess of how I can test it.
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `45%`

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
    I am confident in my abilities to complete my portion of the project. Currently, I am coding the design and the next step is the functionality.
    I was going to do a database but I'll do that own my own time. I am 1/2 of completed (Part 1: Design & Part 2: Functionality)
```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions

The POS interface is divided into three main sections:
Left Frame – Category Toggle Menu
Middle Frame – Item Display Area
Right Frame – Order Summary Panel

1.Browsing Menu Categories
Start by using the toggle menu in the left frame.
Press any of the category buttons (e.g., Drink, Sides, Desserts).
Once a category is selected, a new set of buttons representing specific menu items within that category will appear in the middle frame.

2.Adding Items to the Order
In the middle frame, press a button representing a menu item.
Each button will display the item name and its price.
When pressed, the item will be added to the order list shown in the right frame.

3.Viewing and Managing the Current Order
The right frame keeps a running list of all items added to the order.
Each item appears as a separate entry.

To Delete an Item:
Hover your cursor over the item in the right frame.
Once the item flashes red, click it to remove it from the order

A. Cancel Button
Press to clear the entire order and reset the current transaction.

B. Discount Toggle Button
Press once to activate a discount (e.g., percentage off the order).
Press again to turn the discount off.

C. Pay Button
Finalize the transaction by pressing the Pay button.
The system will:
Clear the current order.
Generate a random order number for tracking purposes and turn green to represent a "paid transaction"




### Errors and Constraints

Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.

### Peer Evaluation

It is important that all members of your team contribute equitably. The peer evaluation is your chance to either 
a) celebrate the great work you all did together as an effective team, or b) indicate to the instructor if a member of
your team did not contribute their fair share. Grades will be adjusted for any team member who is evaluated poorly. Your
commit history will be used as evidence, so make sure you are using git effectively!

### Reflection

Each partner should write three to four well-written paragraphs address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- How well did you work with your partner? What made it go well? What made it challenging?

```
    Partner 1: **Replace this text with your reflection
```

```
    Partner 2 (Shadaria): 
    Every job I’ve had so far has been in fast food, and through those experiences, I’ve seen how much more efficient 
    it is to use software rather than pen and paper when handling orders. 
    Initially, my POS system design was more suitable for a large-scale restaurant setup, but I soon realized that 
    for this project—a mock small restaurant—a simpler, more compact layout would be more appropriate. 
    This shift taught me a lot about the importance of tailoring design to fit the scope and context of a project.
    
    Throughout the development process, I gained a deeper understanding of GUI design, particularly how frames interact 
    with each other and how to work with parent and child widgets in Python. I also explored concepts in object-oriented 
    programming and databases, even though I didn’t end up integrating a database into the final project. 
    The most difficult part was ensuring smooth interaction between components and keeping track of the control flow as the code grew longer and more complex. 
    If I were to do the project again, I would prioritize locking down the layout and being confident with my abilities, 
    and I’d also use more debug printing to track reference passing and storage more effectively.
    
    This project had two main components, and I believe both partners contributed effectively to its success. 
    Once we gained clarity on the project requirements, everything moved more smoothly, and we were able to collaborate 
    efficiently. The biggest challenge early on was communication—specifically, aligning our individual ideas with what 
    was actually feasible within our skills and the project’s scope. But as we progressed, that initial uncertainty 
    turned into a shared understanding and ultimately a strong final product.
    
```

---