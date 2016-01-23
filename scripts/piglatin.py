#!/usr/bin/python
import sys, re
REGX_CAPS = re.compile(r"[A-Z]")
REGX_WORD = re.compile(r"\b([bcdfghjklmnpqrstvwxyz]*)(\w\']+)")

def mapper(line):
	words = REGX_WORD.findall(line)
	pigl_word = []
	for word in words:
		original_word = ''.join(word)
		head,tail = word
		head = 'w' if not head else head
		pigl_word = tail + head + 'ay'
		if REGX_CAPS.match(pigl_word):
			pigl_word = pigl_word.lower().capitalize()
		else:
			pigl_word = pigl_word.lower()
		pigl_word.append(pigl_word)
	return " ".join(pigl_word)

	if __name__ == '__main__':
		for line in sys.stdin:
			print mapper(line)

			