# Week 1 Review: Programming Exercises

## 1 [temp_converter.py]
Modify the temperature converter we developed in 1.10 Together Project: A Temperature Converter to now convert from Fahrenheit to Celsius. A user should now input a temperature in Fahrenheit and the program should output the equivalent temperature in Celsius. Modify the input prompts and the output message as appropriate.

## 2 [bitcoin_converter.py]
Write a program that converts bitcoin to dollars (usd).

One tricky element to currency conversion, whether crypto-currency or otherwise, is that the price is volatile and changing moment to moment. The program should begin by outputting to the user the date and time at which you recorded the conversion rate for bitcoins to usd (e.g., at this moment it is currently $2086 usd to 1 bitcoin), then the user should input the amount of bitcoin they have, and the program should output how much that bitcoin is worth in dollars. For example:

```
As of 8/1/17 at 11:13 am, bitcoin is currently trading at $2086 per bitcoin.
Enter the bitcoin amount: .5
That is worth 1043 us dollars.
```

## 3 [fight_song.py]
Write a program that outputs the following fight song.

There should be a function named sing_fight_song that when called "sings" the song by printing it out. You should create other functions to show structure and to eliminate redundancy in your program (i.e., your sing_fight_song function should not consist solely of print statements printing each line of the song, that would be highly redundant, it should call other functions that print reusable parts of the song).

```
Go, team, go!
Defeat your foe.

Go, team, go!
Default your foe.
Simply the best,
Better than the rest.
Go, team, go!
Defeat your foe.

Go, team, go!
Default your foe.
Simply the best,
Better than the rest.
Go, team, go!
Defeat your foe.

Go, team, go!
Defeat your foe.
```

## 4. [phrase_repeater.py]
Write a program that repeats a phrase, given by a user, the number of times a user requests it be repeated.

For example, a user could input the phrase "Lazy harp seal has no job" and then input it should be repeated 3 times. The program should then output the phrase three times along with which repetition this is, like this (note the bold text below indicates that the user typed that value: your program should not be printing out the exact things you see below, you should be able to have any phrase repeated any number of times):

```
Input your phrase: Lazy harp seal has no job
How many times should it be repeated? 3
1 Lazy harp seal has no job
2 Lazy harp seal has no job
3 Lazy harp seal has no job
```
