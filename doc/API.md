### 类

- Card
- Hero
- Minion
- Spell
- Weapon
- Ability
- Signal
- Slot
- Situation
- Game

## ？

- signal

```python
# msg: use / play / summon
class Signal:
    _msg = 'use'
    _obj = some_card
    _index = 2
    _target = enemy_hero
    
    @classmethod
    def form(cls, msg, obj, index, target):
        signal = new Signal()
        signal._msg = msg
        signal._obj = obj
        signal._index = index
        signal._target = target
        return signal
```

when you need to register a signal, use `register(signal_str)`

when you need to register a slot(or a listener) to a signal, use `

- play a card

```python
Game(situation)
Game.check(situation, card)
card.use:
    emit(Signal.form('use', self, 0, None))
    
```

---

new 

