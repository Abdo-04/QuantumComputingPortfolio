# BB84 Quantum Key Distribution

Project 4 of 5. The first quantum key distribution protocol, published by
Bennett and Brassard in 1984.

## What it does

Alice and Bob build a shared secret key over a channel an eavesdropper can
listen to, and can detect whether anyone listened.

Unlike post-quantum cryptography, which uses classical maths believed to be
hard for quantum computers, BB84's security comes from physics. Measuring a
qubit in the wrong basis destroys it, so an eavesdropper cannot read the
channel without leaving evidence.

## The protocol

1. Alice picks a random bit and a random basis for each qubit
2. She encodes: Z basis sends |0> or |1>, X basis sends |+> or |->
3. Bob picks his own random bases, with no knowledge of Alice's
4. Bob measures
5. They publicly compare bases, never bits, and discard mismatches
6. The surviving bits are the sifted key
7. They sacrifice a sample of those bits to check the error rate

## Encoding

| Bit | Basis | State | Gates |
|---|---|---|---|
| 0 | Z | \|0> | none |
| 1 | Z | \|1> | X |
| 0 | X | \|+> | H |
| 1 | X | \|-> | X then H |

## Why eavesdropping shows up

Eve must guess a basis too. When she guesses wrong she gets a random result
and collapses the qubit, then forwards a damaged state to Bob. Bob then gets
the wrong bit even where his basis matched Alice's.

Expected error rate in the sifted key with Eve present: around 25 percent.
Without Eve, on a noiseless simulator: 0 percent.

## Results

Without eavesdropper: