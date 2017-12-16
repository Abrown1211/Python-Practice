# Week 3 Review

(1) **[mad-libber.py]** A mad lib is a game where you take a sentence and fill in some of the words to make a (typically) silly story. For example, you might make up a sentence `"She ate the [noun] and [past_tense_verb]."` Then someone else picks a noun and a past tense verb at random, like `"alarm clock"` and `"smiled"`, and they are put into the sentence to make `"She ate the alarm clock and smiled."` Usually the mad libs are a much longer story, but this is the general idea.

You are to create your own mad lib. Here is an example:
```
Madlib Maker
name: Paul
place: airport
verb: wait

Old Mc-Paul had a airport, E-I-E-I-O
And on that airport he liked to wait, E-I-E-I-O
With a wait wait here, and a wait wait there, everywhere a wait wait
```
I picked part of a song, and you could too, but your mad lib should:

* have at least three lines or sentences
* have at least three replacements (mine are name, place, and verb) and two of them must be present in more than one sentence (e.g., in the example note how `airport` is lines 1 and 2, and `wait` is in lines 2 and 3)
* not use the concatenation operator: `+`. Why? Because although it is straightforward to do so, your solution would very likely be tedious and would not work for more than just your sentences. String methods exist to make work with Strings more efficient than that. You can solve this simply with sequences and some String methods.

HINT: If you find yourself devising an elaborate algorithm involving programming content we have not yet covered (e.g., conditionals), you are overthinking it.



(2) **[caesar-encrypter.py, caesar-decrypter.py]** Extend the encrypter to read messages to be encrypted from an input file and write each of them out to the output file. Rather than having the user input a message in the shell, now the user should input a file name, and the encrypter should read that file and encrypt each message in the file, writing the encrypted messages to the output file.

You should not need to modify the decrypter. It should already handle having multiple encrypted messages in the file.



(3) **[sales-totaler.py]** Write a program that takes some sales numbers from a file written as dollars (e.g., `$1120.47`), sums them across rows, and outputs the rows again with the sum at the end. For example for an input file named `17-oct-sales.txt` with these contents:
```
$1120.47 $944.42
$72.29 $588.23
$371.21 $2183.84
```
your program would output to another file the contents:
```
$ 1120.47  $  944.42  $ 2064.89
$   72.29  $  588.23  $  660.52
$  371.21  $ 2183.84  $ 2555.05
```
Notice how in the output file all the numbers are nicely formatted with right alignment. Here is an example interaction:
```
Enter sales file name: 17-oct-sales.txt
Enter name for total sales file: 17-oct-total.txt

Done writing totals to: 17-oct-total.txt
```
You will find the `17-oct-sales.txt` file already included in the repository.



(4) **[dynamic_typography.py]** You will write a program that generates a drawing from a message input by the user. The message should be drawn in some way that is based on the ordinal values of the characters. For example, the input message for the drawing below, `"That was a Freebie."` is drawn such that the position of the letters is based on their integer value.

![dynamic_typography](/images/dyanmic-typography.png)

What's also special about the image is the use of color and the creation of a shadow behind the letters in the message.

Your program should:

* Use the ordinal values of the characters to draw them in some unique way (i.e., we discussed how numbers are used in graphics, be creative in how you use the number of a character to make it unique)
* Have some color, not just black and white
* Change the typography in some way (e.g., size, font)
* Include comments explaining how your program is using the ordinal value to make a unique image from the message
