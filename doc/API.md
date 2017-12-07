### 类

- Card
- Deck
- BattleField
- Hand
- Hero
- Minion
- Spell
- Weapon
- Ability
- Signal
- Slot
- Player
- Situation
- Game

## ？

## 类的成员和方法

---

---



class Card

```python
class Card:
    # member
    ctype # string
    ori_cost # unsigned
    cost # unsigned
    
    # method
    def use(self)
    def play(self)
```

class Deck

```python
# dependencies
from signal_slot import *
class Deck:
    # member
    cards # [Card]
    fatigue # unsigned (疲劳)
    
    # slot
    class DrawSlot(Slot)
    class LookupSlot(Slot)
    
    # direct signal
    'fatigue'
    'insert'
    'fetch'
    
    # method
    
    # params: 
    # return: unsigned
    # description: number of cards in deck
    depth() 
    
    # params: 
    # return: unsigned
    # description: select a random card, return its index
    random()
    
    # params: 
    #  fil: method (takes <Card> returns <bool>)
    # return: [unsigned]
    # description: select cards which makes fil(card) return true
    select(fil)
    
    # params:
    #   i: unsigned
    # return: Card
    # description: get a card's infomation whose index is i
    lookup(i)
    
    # params:
    #   i: unsigned
    # return: Card
    # description: get a card whose index is i, remove it from deck
    fetch(i)
    
    # params:
    #   lis: [unsigned]
    # return: [Card]
    # description: get cards whose index is in lis, remove them from deck
    fetchall(lis)
    
    # params:
    #   card: Card
    # return: 
    # description: insert a card into deck
    insert(card)
    
    # params:
    #   cards: [Card]
    # return:
    # description: insert a list of cards into deck
    insertall(cards)
```

class Player

```python
class Player:
    # member
    deck # Deck
    battlefield # BattleField
    hand # Hand
    hero # Hero
    # method
```

class Situation

```python
class Situation:
  # member
  you # Player
  enemy # Player
  turn # 'you' / 'enemy'
  # method
```



