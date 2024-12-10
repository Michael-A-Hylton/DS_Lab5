from Card import Card

card1 = Card("Seven", "Hearts")
card1= card1.value
card2 = Card("Queen", "Spades")
card2= card2.value
card3 = Card("Queen", "Diamonds")
card3= card3.value
print(card1 < card2)
print(card2 < card3)
print(card3 < card3)
