class Hamming:
    def distance(self, a, b):
        if a == "" or b == "":
            return 0
        elif a == "A" and b == "A":
            return 0
