def feedback(maker_code, breaker_code):
	# black = 0
	# white = 0
	feedback_pegs = []
	maker_without_blacks = []
	breaker_without_blacks = []

	for original, guess in zip(maker_code, breaker_code):
		if original == guess:
			# black += 1
			feedback_pegs.append(1)
		else:
			maker_without_blacks.append(original)
			breaker_without_blacks.append(guess)

	for peg in breaker_without_blacks:
		if peg in maker_without_blacks:
			# white += 1
			feedback_pegs.append(0)
			maker_without_blacks.remove(peg)

	# return (black, white)
	return feedback_pegs

print(feedback(['a', 'b', 'b', 'c'], ['b', 'b', 'a', 'c']))
print(feedback(['a', 'b', 'c', 'd'], ['b', 'd', 'a', 'c']))
print(feedback(['a', 'b', 'c', 'd'], ['b', 'd', 'a', 'c']))
print(feedback(['a', 'b', 'c', 'd'], ['e', 'e', 'e', 'e']))



