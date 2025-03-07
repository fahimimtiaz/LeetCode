from typing import List

class Solution:
    @staticmethod
    def sieve(limit: int) -> List[bool]:
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime

        for num in range(2, int(limit ** 0.5) + 1):
            if primes[num]:
                for multiple in range(num * num, limit + 1, num):
                    primes[multiple] = False
        return primes

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.sieve(right)
        prime_list = [i for i in range(left, right + 1) if primes[i]]

        if len(prime_list) < 2:
            return [-1, -1]

        # Find the pair with the smallest difference
        min_diff = float('inf')
        left_prime, right_prime = -1, -1

        for i in range(1, len(prime_list)):
            diff = prime_list[i] - prime_list[i - 1]
            if diff < min_diff:
                min_diff = diff
                left_prime, right_prime = prime_list[i - 1], prime_list[i]

        return [left_prime, right_prime]

# Example usage:
ans = Solution().closestPrimes(left = 255322, right = 929209)
print(ans)
