class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
            
        result = 1
        while n > 0:
            print("result: " + str(result))
            print("n: " + str(n))
            print("x: " + str(x))
            print("=============")

            if n % 2 == 1:
                print("Multiplying when x is " + str(x))
                result *= x
            x *= x
            n //= 2

        
        return result

print(Solution().myPow(x =2,n =20))