import random

# ------------------------------------------------------------
#  SETUP – 52 cards, ranks and suits
# ------------------------------------------------------------
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits = ['H','D','C','S']      # Hearts, Diamonds, Clubs, Spades

deck = [(r, s) for r in ranks for s in suits]
random.shuffle(deck)

# ------------------------------------------------------------
#  GAME START – one card on the chain, five in hand
# ------------------------------------------------------------
chain = [deck.pop()]          # the growing chain
hand  = [deck.pop() for _ in range(5)]

# ------------------------------------------------------------
#  HELPER FUNCTIONS
# ------------------------------------------------------------
def show_card(card):
    """Return a short string like '7H' or 'KS'."""
    return f"{card[0]}{card[1]}"

def can_play(card, first, last):
    """True if card matches suit OR rank of first OR last chain card."""
    return (card[0] == first[0] or card[1] == first[1] or
            card[0] == last[0]  or card[1] == last[1])

def any_move_possible(hand, first, last):
    """Check if any card in hand can be played."""
    return any(can_play(c, first, last) for c in hand)

# ------------------------------------------------------------
#  MAIN GAME LOOP
# ------------------------------------------------------------
print("\n=== CARD CHAINS ===\n")
print("Build a chain by adding cards that match suit OR rank")
print("at either end. Empty your hand and deck to win.\n")

while True:
    # --- Show current status ---
    first_card = chain[0]
    last_card  = chain[-1]
    print(f"CHAIN:  {show_card(first_card)}  ...  {show_card(last_card)}  (length {len(chain)})")
    print("\nYour hand:")
    if hand:
        for i, c in enumerate(hand):
            print(f"  {i+1}: {show_card(c)}")
    else:
        print("  (empty)")

    # --- Win / Loss checks ---
    if not deck and not hand:
        print("\n✨ You played every card! You win! ✨")
        break
    if not deck and hand and not any_move_possible(hand, first_card, last_card):
        print("\n💀 No moves left and deck is empty. You lose. 💀")
        break

    # --- Player command ---
    cmd = input("\n> ").strip().lower()

    if cmd == 'quit':
        print("Thanks for playing!")
        break

    elif cmd == 'draw':
        if deck:
            hand.append(deck.pop())
            print("Drew a card.")
        else:
            print("Deck is empty – no more cards.")

    elif cmd.startswith('play'):
        parts = cmd.split()
        if len(parts) == 2 and parts[1].isdigit():
            idx = int(parts[1]) - 1
            if 0 <= idx < len(hand):
                card = hand.pop(idx)
                # Try to add to start or end
                if card[0] == first_card[0] or card[1] == first_card[1]:
                    chain.insert(0, card)
                    print(f"Played {show_card(card)} to the START.")
                elif card[0] == last_card[0] or card[1] == last_card[1]:
                    chain.append(card)
                    print(f"Played {show_card(card)} to the END.")
                else:
                    print("Can't play that card – it doesn't match either end.")
                    hand.append(card)   # put it back
            else:
                print("Invalid card number.")
        else:
            print("Use 'play 3' (with a number).")
    else:
        print("Commands: play N, draw, quit")