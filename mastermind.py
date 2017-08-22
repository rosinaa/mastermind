from mastermind_exceptions import MastermindError


def feedback(maker_code, breaker_code):
	# check maker_code and breaker_code validity
	if not isinstance(maker_code, list):
		raise MastermindError('Invalid maker code')
	if not isinstance(breaker_code, list):
		raise MastermindError('Invalid breaker code')
	if len(maker_code) != len(breaker_code):
		raise MastermindError("Codes have different lengths")

	feedback_pegs = []
	maker_without_blacks = []
	breaker_without_blacks = []

	# check guess pegs in the right position and color
	for original, guess in zip(maker_code, breaker_code):
		if original == guess:
			feedback_pegs.append(1)
		else:
			maker_without_blacks.append(original)
			breaker_without_blacks.append(guess)

    # check pegs with the right color and wrong position
	for peg in breaker_without_blacks:
		if peg in maker_without_blacks:
			feedback_pegs.append(0)
			maker_without_blacks.remove(peg)

	return feedback_pegs

print(feedback(['a', 'b', 'b', 'c'], ['b', 'b', 'a', 'c']))
print(feedback(['a', 'b', 'c', 'd'], ['b', 'd', 'a', 'c']))
print(feedback(['a'], ['e', 'e', 'e', 'e']))
