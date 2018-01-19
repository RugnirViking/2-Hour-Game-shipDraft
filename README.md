# A game made in 2 hours: An exercise in getting started

I started off today like I do many days: wondering why I can't find the motivation to do the many projects in my head.
My usual problem is starting a project but burning out on some minor detail and never getting anywhere near completeing. By the next day, I was already thinking about a new, far more *exciting* project
If only I could just **finish** a project, everything would fall into place as I could have the motivation to improve upon it.

Thats where I had the idea: Make a deadline that forces me to finish a project **NOW**! I needed to make sure that I couldn't wriggle out of it by saying to myself "I can't possibly spare an entire day to program" so I made it into a challenge that I could fit into an evening.

I didnt get nearly as much as I wanted to do done (obviously). I knew I wanted to make a spaceship game so I started off by making a csv file of ship hulls with hp values and costs. Then I set to work getting a basic file reader setup working with it and a class system to store them.

Later on I refactored it to use a more general 'part' class that it inherits from. Even with a system this small, I feel like this was a worthwhile endevour to keep things clear in my head.

It was around this time that the arena draft system from hearthstone popped into my head. It seemed like a great idea for this parts based system and immediately I thought about the rare and common techs in stellaris as well as inspirations.
Quickly I started writing a generalised system to randomly pick a part from a list of rarity categories, as well as systems to output the statistics of hull parts to the console. Around this time I hit the 30 minuite mark and decided to create a github repository for the project. This was done in a matter of minuites.

For the next 30 minuites I worked on polishing the draft section, getting the items to be chosen randomly and not to pick the same item twice in the same draft. I also found ways to get the 'press any key to continue' working in python as well as clearing the screen.

At around an hour into the project I began adding a ship class which held a list of parts and a hull. This took a while to make sure that it held all of the statistics of a ship (many of which were later unimportant such as power, hull repair etc) and added and subtracted them correctly when adding parts.

At this time I found myself distracted, thinking about putting on a podcast or something to drown out my increasing awareness that my apartment was totally silent apart from the clicking of my keys. I shook the distraction clear from my head and put on some music to see if that would satisfy my brain. For now, it did.

I then moved on to adding another category of parts, armour. I started doing this around the 1 hour 20 minuites mark, and it ended up taking me about 20 mins to complete as I also had to add a general system into the code for components on the ship as well as generalise the draft system to allow it to use any kind of part lists.

Finally with the clock showing 1 hour 40 I went into panic mode, tying up loose ends within the armour system and then moving onto the largest remaining task. Really I should have known to give it more time, but I was getting carried away polishing systems thinking of what I wanted the game to be and not what I could realistically achieve. I began to start on the combat.

By this point my brain was beginning to cloud a little more with the intensity of focusing for so long so I got up and put on the kettle to clear me head a little. This was seemingly enough to get me focused and I wrote a quick system to start the combat as well as a series of lines to create an opponent ship to fight against. My early class-based structure paid it's dividends here, allowing me to create and then output the two competitor's ships and their statistics within ten or so minuites.

I then wrote a method to simulate a single turn in the game very quickly, painfully aware of the clock and how it showed that I only had 10 minuites left. I had to be careful not to introduce any bugs at this late stage, despite my rushing I had no time to go back and correct anything. I kept telling myself that if it compiled at all at the end of the day that was better than an error and that allowed me to take my time just enough to finish up.

I quickly sprinkled a check to make sure it would check if you win or lose and show an appropriate message then stopped the clock. The time said 1 hour 58 minuites and I had finished! 

Sure, the game wasn't quite what I was imagining halfway through and sure, the game wasn't exactly a challenge to win but I feel that I have learned something in this time about reconcilling ambition with extremely tight deadlines even with this very simple example.

Known issues (very glaring ones)
You have 1000 coins but the title screen says 100
On the first pick (hulls) it doesn't show the stats of the hulls
When using rarities of more than epic, they are never chosen (none included with the 2 hour files)
The strategy to win is very simple (always pick highest hp armour and so long as you get more than 220 you win)

