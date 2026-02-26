class Brute:
    def reverse(self, x: int) -> int:

        x_min = -(2**31)
        x_max = (2**31) - 1

        isNumberNegative = True if x < 0 else False

        posX: str = str(x)[1:] if isNumberNegative else str(x)

        revPosX: str = posX[::-1]

        # check and add negative sign
        if isNumberNegative:
            X: str = "-" + revPosX

            result: int = int(X)

            if result < x_min:
                return 0
            else:
                return result

        else:

            result = int(revPosX)

            if result > x_max:
                return 0
            else:
                return result


s = Brute()


print(s.reverse(-123))
