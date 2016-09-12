def bar_chart(data, bar_char='=', width=80):
	"""Return an horizontal bar chart 

	>>> print bar_chart({
	...     'one': '1',
	...     'two': '2',
	...     'three': '3',
	...     'four': '4',
	...     'five': '5',
	... })
	 five =====
	 four ====
	  one =
	three ===
	  two ==
	>>> print bar_chart({
	...     '1/1': 1/1.0,
	...     '1/2': 1/2.0,
	...     '1/3': 1/3.0,
	...     '1/4': 1/4.0,
	...     '1/5': 1/5.0,
	...     '2': 2,
	...     '3': 3,
	...     '4': 4,
	...     '5': 5,
	... })
	1/1 ===============
	1/2 =======
	1/3 =====
	1/4 ===
	1/5 ===
	  2 ==============================
	  3 =============================================
	  4 ============================================================
	  5 ===========================================================================
	>>> print bar_chart({
	...     '1': 2**1,
	...     '2': 2**2,
	...     '3': 2**3,
	...     '4': 2**4,
	...     '5': 2**5,
	...     '6': 2**6,
	...     '7': 2**7,
	... })
	1 =
	2 ==
	3 ====
	4 =========
	5 ===================
	6 ======================================
	7 =============================================================================
    """
	if type(data) is dict:
		output = []
		max_len = len(max(data, key=len))
		float_values = map(float, data.values())
		max_value = max(float_values)
		min_value = min(float_values)
		all_integer = all(f.is_integer() for f in float_values)
		for key in sorted(data):
			output.append('%s %s'%(key.rjust(max_len, ' '), draw_bar(bar_char, float(data[key]), all_integer, min_value, max_value, width-max_len-2)))
	return '\n'.join(output)

def draw_bar(bar_char, value, all_integer, min_value, max_value, max_width):
	if all_integer and max_value <= max_width:
		return bar_char*int(value)
	return bar_char*int(value*max_width/max_value)

if __name__ == "__main__":
	import doctest
	doctest.testmod()