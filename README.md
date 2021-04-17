# DnD Dungeon Master Tools
## Basic instructions
1. Install Python 3 
2. Install dependencies with `pip3 install -m requirements.txt`
3. Run the program with `python3 main.py`
4. Enter the number of an option to use it
### Dice Roller
- Enter `d20` to roll a 20-sided die
- `3d6 + 4 a` rolls a six-sided die three times, then adds four to the total. It has advantage (takes highest of two rolls for each of the three rolls)
- Press enter to quit to menu
### Fast Initiative
- Enter the number of players
- Prints the d20 roll value for each of the players (perhaps use clockwise around the table)
### Custom Initiative
- Edit `characters.csv` to include your players' names, character names, hit points, armor class, and initiative modifier (dex mod).
- When you run Custom Initiative it will print the characters' rolls and output `Turn 1: <character>` for each character in order
### Monster Roller
- Edit `monsters.csv` to include monster name, armor class, modifier to hit, hit points, number of sides on attack damage dice, and damage modifier (if applicable)
- When it prompts to enter a monster, optionally enter the number of monsters of a certain type, a space, then the name of the monster exactly as written on the spreadsheet, i.e. `3 Wolf` or `Goblin`
- The program will output rolls to hit and damage. Compare these to the target AC to find if it hits.
