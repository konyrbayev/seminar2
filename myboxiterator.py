class MyBoxIterator():
	def __init__(self):
		self.a = 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.a <= 5:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration

if __name__ == "__main__":
	L = MyBoxIterator()
	for item in L:
		print(item)
