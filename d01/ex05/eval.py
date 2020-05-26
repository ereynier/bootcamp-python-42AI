class Evaluator:

    @staticmethod
    def zip_evaluate(coef, words):
        if (not isinstance(words, list) or not isinstance(coef, list)):
            return (-1)
        if (len(words) != len(coef)):
            return (-1)
        out = 0
        lst = zip(words, coef)
        for i in lst:
            out += len(i[0]) * i[1]
        return (out)

    @staticmethod
    def enumerate_evaluate(coef, words):
        if (not isinstance(words, list) or not isinstance(coef, list)):
            return (-1)
        if (len(words) != len(coef)):
            return (-1)
        out = 0
        for idx, val in enumerate(words):
            out += len(val) * coef[idx]
        return (out)

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))