import time
def generate_primes(n):
  primes = []
  for i in range(2, n + 1):
    if is_prime(i):
      primes.append(i)
  return primes
def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True
def main():
  n = int(input("Enter a number: "))
  start_time = time.time()
  primes = generate_primes(n)
  end_time = time.time()
  print("The prime numbers up to {} are: {}".format(n, primes))
  print("It took {} seconds to generate the prime numbers.".format(end_time - start_time))
if __name__ == "__main__":
  main()