# LOVEANDWAR - Love and War, a game engine where all is fair

A Python game engine in development, which will evaluate both combat and loving as zero-sum attributes of a character class object.

## Development

The game engine is currently just the first draft of an incomplete class definition found in /classes/character.py. The class defines character objects with the following attributes:

- **name** (any printable string)

- **aggro** (any integer value, currently initialized at 50)

- **fought** (integer value of number of times fought, currently initialized at 0)

- **loved** (integer value of number of times loved, currently initialized at 0)

- **reaction** (a tuple consisting of whether the character wants to fight (+1) or wants to love (-1) and a reaction value integer determined through an algorithm explained below)

The class currently has the following methods:

- **reaction()** (evaluates the character's reaction to other player object, returning a tuple of a wants-to-love flag (-1) or wants-to-fight flag(+1) and a *reaction* integer value)

- **encounter(other)** (evaluates whether the outcome of the *reaction* of both the character and the other character are a fight or a love, and adjusts the *aggro* , *fought* , and *loved* atttributes for both accordingly)

The algorithm of *reaction()* is currently very crude and in need of further development:

> *reaction* = if (<random integer between 1 and 100> + <*fight* attribute value for that character> - <*loved* attribute value for that character>) is greater than <*aggro* attribute value for that character>, wants to fight (+1); else wants to love (-1). Both the reaction value integer and the single-digit flag are returned in a tuple

The algorithm of *encounter()* is also very crude and incomplete:

> if character's *reaction* flag and other character's *reaction* flag add up to a positive integer, there is a fight, and both have their *fought* and *aggro* attributes incremented by 1
>
> if they add up to a negative integer, there is a love; the *love* attributes are incremented by 1, and the *aggro* attributes are decremented by 1
>
> if they add up to 0, then the *reaction* values will have to be resolved together to see whether there is a fight or a love; that part of the algorithm is not developed yet.

## To-Do

- greatly improve the two existing algorithms

- implement a way to give meaning to whether self.encounter(other) or other.encounter(self) is evaluated

- generally keep working on the engine framework

## Wish List

- help from math-savvy people to develop the algorithms