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


  def check_for_ace(self, card):
    if card.value = 1:
        # should be == 
      return True
    else
    # missing colon
      return False
   

  dif highest_card(self, card1 card2):
  #should be def, no comma between arguments
  if card1.value > card2.value:
  #no indentation for lines 31-36
    return card
    #should be card1
  else:
    return card2
  

#function has wrong indentation
def cards_total(self, cards):
  total
  #total variable should be assigned some value
  for card in cards:
    total += card.value
    return "You have a total of" + total
    #won't concatenate string and int, f needed
    #if return indented as done here loop will finish after 1 iteration
  
```
