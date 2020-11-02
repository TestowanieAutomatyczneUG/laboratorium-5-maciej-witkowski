class Hamming:
    def distance(self, a, b):
        if a == "" and b == "":
            return 0
        elif len(a) == 1 and len(b) == 1:
            if a == b:
                return 0
            else:
                return 1
        elif a == b:
            return 0
