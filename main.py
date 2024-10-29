import random

quotes = [
    "The only way to do great work is to love what you do.",
    "Strive not to be a success, but rather to be of value.",   
    "The future belongs to those who believe in the beauty of their dreams.", 
    "Formal education will make you a living. Self-education will make you a fortune.\nJim Rohn",
    "Programming is not easy like Sunday morning, it is silent poetry.\nWaseem Latif",
    "These days, the problem isn't how to innovate; it's how to get society to adopt the good ideas that already exist.\nDouglas Engelbart",
    "If you say \"I told you so\", you are the one who has failed. Because you knew, but did not manage to stop the train wreck.\nRobert C. Martin",
    "What one programmer can do in one month, two programmers can do in two months.\nFrederick P. Brooks",
    "Bad programmers worry about the code. Good programmers worry about data structures and their relationships.\nLinus Torvalds",
    "The competent programmer is fully aware of the strictly limited size of his own skull; therefore he approaches the programming task in full humility, and among other things he avoids clever tricks like the plague.\nE. W. Dijkstra",
    "UNIX is simple. It just takes a genius to understand its simplicity.\nDennis M. Ritchie",
    "I know testers who make good devs. I know devs who make good testers. I know Scrum Masters who make good coffee.\nDavid Evans",
    "We crave for new sensations but soon become indifferent to them. Wonders of yesterday are today common occurrences.\nNikola Tesla" 
]

random_quote = random.choice(quotes)

print(random_quote)