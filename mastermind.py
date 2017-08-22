from mastermind_exceptions import MastermindError


def feedback(maker_code, breaker_code):
	""" Evaluates breaker_code agains maker_code

	Checks each peg of the breaker_code and they are compared to
	the pegs in the maker_code.
	If the peg is in the same position and same color, a black peg
	is added to the feedback list. 
	If the breaker peg is in the wrong position, but right color,
	a white peg is added to the return list.

	Args:
		maker_code: list of strings (pegs) from the codemaker
		breaker_code: list of strings (pegs) from the codebreaker

	Returns:
		A list of strings ('B' or 'W'), representing black (B) or 
		white (W) pegs. 
		Black pegs are always before white ones. For example:

		['B', 'B', 'W']

	Raises:
		MastermindError: Error raised when the args are invalid.
	"""
	
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
			feedback_pegs.append('B')
		else:
			maker_without_blacks.append(original)
			breaker_without_blacks.append(guess)

    # check pegs with the right color and wrong position
	for peg in breaker_without_blacks:
		if peg in maker_without_blacks:
			feedback_pegs.append('W')
			maker_without_blacks.remove(peg)

	return feedback_pegs
