The general flow of this was:

- Identify corner pieces from part 1.
- Start with a corner piece (arbitrarily bottom left) and iteratively append to it horizontally.  This creates the bottom row
	- See: part2a_bottomborder.py
- Next build a column upward from the bottom left piece to get the left border
	- See: part2b_anycolumn.py
- Next iteratively fill in each row
	- See: part2c_anyrow.py
- Every new row/column I created I manually copied into a text file.  I know this is bad but thats what I did.
- Finally read in the final image, remove borders, rotate to correct orientation, and grep for sea monsterss.