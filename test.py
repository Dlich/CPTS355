from functools import reduce


class mysteryIter(object):
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        k = self.input1.__next__()
        self.current = (k, self.input2.get(k, '-'))

    def __next__(self):
        if self.current is None:
            raise StopIteration
        k = self.input1.__next__()
        self.current = (k, self.input2.get(k, '-'))
        return self.current
    def __iter__(self):
        return self

def main():
   #print(wordCount(["word", "te", "word", "hi"]))
    it1 = mysteryIter(['hello', 'ty', 'er'], ['t', 'r', 'ert'])
    print(list(it1))

main()