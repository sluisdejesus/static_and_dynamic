### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  # missing : after else
  def check_for_ace(self, card):
  # missing double =
    if card.value = 1:
      return True
    else
      return False
   
  # spelling mistake in def
  # missing comma between card1 and card2
  # if statement is not indented
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    #returning card would give error - only card1 and card2
    return card
  else:
    return card2
  

# function not inside class CardGame
def cards_total(self, cards):
  # total is not defined or given a value
  total
  for card in cards:
    total += card.value
    # return should be outside for loop otherwise it will return after first instance
    # missing string interpolation
    # return statement won't work if total is an int and not a string
    return "You have a total of" + total
  
```
