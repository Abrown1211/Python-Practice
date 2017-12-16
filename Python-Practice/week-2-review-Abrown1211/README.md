# Week 2 Review

(1) **[ball_filler.py]** You have been contracted by a bowling ball manufacturer to write a program that estimates the amount of ball "filler" they'll need to order for a new line of bowling balls.

Each spherical bowling ball has a diameter that can vary from 8.4 to 8.6 inches. Inside that ball, there is a core: a uniquely shaped metal object that affects the spin of the ball, and some filler: the stuff packed around the core eventually making the spherical shape. Given the intended diameter of the ball, the volume of a ball's core, and the number of bowling balls to produce, your program should calculate the amount of filler the company should order.

For example, the company wants to produce 100 bowling balls with a diameter of 8.5 inches, and inside each ball, it will contain a core that has a volume of 124 inches cubed. Then your program should produce this:

```
How many bowling balls will be manufactured? 100
What is the diameter of each ball in inches? 8.5
What is the core volume in inches cubed? 124
You will need 19755.509806430524 inches cubed of filler
```

You will need the formula for the volume of a sphere, which is V=4/3πr<sup>3</sup>, to compute the total amount of filler required if there was no core.



(2) **[total_service_score.py]** A franchise restaurant is attempting to understand if customers think their service is good day-to-day.

The manager collects the customer comment cards each day and creates a score for that day: if a comment was positive they add one to the score, and if a comment was negative they subtract one from the score. For example, on a day where there were 7 total comment cards, 5 positive comments and 2 negative comments, the score for that day would be 3 (5 - 2 is 3).

You are tasked with writing a program that will tell them the total score over a given number of days. The user will input the number of days and then the score for each of those days for your program total. For example, if the manager wants the total score over the last 4 days that had scores of 2, 4, -2, and 1, that would look something like this:

```
How many days of scores? 4
Enter score for day 1: 2
Enter score for day 2: 4
Enter score for day 3: -2
Enter score for day 4: 1
The total score of the 4 days is 5
```


(3) **[my_house.py]** In a graphics window, you are to draw an outdoor scene containing a house.

Your drawing should include at least the following shapes:
* three rectangles
* two lines
* one circle
* one text label

Your picture should not be boring black and white. It should include at least three colors, tastefully distributed to bring your house to life.

Finally, it should have some interactive feature such that when a user clicks on your picture something changes (e.g. a color or a few things move). The change only has to happen once.



(4) **[gradient_bar.py]**

![gradient_bar](/images/gradient_bar.png)

In the picture above you will see a gradient bar. Gradients in computer graphics typically show a color progression. The example above is a progression of the green intensity from 0 to 255, with red and blue remaining at intensity 0 through the progression, spread across six rectangles. When you see graduated colors on your computer they are often created using this technique: having thinner and thinner rectangles makes a smoother gradient progression. For example the gradient below is a green progression through 64 rectangles:


![gradient_bar_64](/images/gradient_bar_64.png)

Your task is to draw a gradient bar. You can make the color progression as simple (e.g., just green intensities changing) or sophisticated (e.g., linear equations manipulating the red, green, and blue intensities independently) as you desire. Your main requirements are this:

* The window you draw the bar in must be 400 pixels wide and the progression must be horizontal.
* There can be no gaps in the progression: no spaces between the rectangles or with the edges of the window.
* The number of bars you use must be a multiple of 6 (i.e., 6 bars, 12 bars, 18 bars, etc.)
* The bars must have no outline (hint: setWidth method)
* All bars must have a width within one pixel of the same width. For example, if we have 6 bars in a 400-pixel window, then each bar should be 66 or 67 pixels wide. NOTE: Understanding why I made this constraint is part of the problem.

One of the best ways to approach this problem is to first work out drawing the bars first to fill the window, then start with the `color_rgb` function and work out the color progression.
