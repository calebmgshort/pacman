Welcome to pacman!

Quickstart:
- clone this repo
- python main.py

What is it?
- It includes 2 parts:
    - Single player mode: This mode is not as complete as the original. It only has one level, which is the hardest
      level on the original version of pacman. Why did I not create multiple levels and 3 lives and add the fruit? Because pacman has already been created, and you can find better versions of the game out there. I only wanted to prove to myself that I could make basic pacman.
    - Multi-player mode: 
      Player one is the top pacman, and player 2 the bottom. One of the players will randomly be selected as the hunter, and the other will be the hunted. When the hunted is eaten, the hunter wins. So how does the hunted win? If the hunted eats the strawberry, the roles will switch, and the hunted will be come the hunter (and vice versa). If either player eats the cherry, their pacman will duplicate, and they will thus have multiple pacmen. If either player eats the orange, they will spawn a ghost which will work as an ai in their favor. Thus, with multiple pacman and multiple ghosts on each side, a hunter pacman or ghost will always eat a hunted one. When one player's final pacman is eaten, the game ends. The reason that all three fruit respawn when one of them is eaten is that I didn't like the idea of a player using a cheat strategy by hanging around a fruit and playing a waiting game. This makes the game go a lot faster. 


Why did I make it?: 
Since my freshman year of college, when I took Introduction to Computer Science, my professor Russell Lewis use to make pacman in java in front of the class before class started each day, and I thought it was the coolest thing and tried to make it back then, but didn't persevere. Since I recently wanted to learn python, I thought back to this project and decided that pacman would be a good way to learn. Plus, I always thought multi-player pacman would be a lot of fun. 
