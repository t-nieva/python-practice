# Blackjack Game
### Game Rules
1. The deck is unlimited in size. 
2. No jokers are used. 
3. Jack, Queen, and King are all valued at 10 points. 
4. An Ace can count as either 11 or 1, whichever is more advantageous for the player. 
5. The deck is represented as the following list:
```commandline
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```

+ All cards in the list have an equal probability of being drawn. 
+ Cards are not removed from the deck after being drawn (they can appear multiple times). 
+ The computer acts as the dealer.

### Features
+ Automatic handling of Aces to avoid going over 21.
+ Simplified rules to focus on the core mechanics of Blackjack. 
+ Continuous card drawing is allowed for both the player and the dealer based on the rules.

### How to Play
1. You start with two cards. 
2. You can choose to draw another card (type "y") or pass (type "n"). . 
3. If your score exceeds 21, you bust and lose the round. 
4. The dealer will draw cards until they reach a score of at least 17. 
5. The winner is determined by whose final score is closer to 21 without going over.