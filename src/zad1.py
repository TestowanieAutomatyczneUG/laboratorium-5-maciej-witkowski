class Hamming:
    def distance(self, a, b):
        count = 0
        if a == "" and b == "":
            return count
        elif a == b:
            return count
        elif len(a) == len(b):
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            return count
