lookup = [];

function fibonacci(n) {
  if (n == 1 | n == 2) {
      if(lookup[n] == undefined) {
          lookup[n] = 1;
      }
    return 1;
  }
    if(lookup[n] == undefined) {
          lookup[n] = fibonacci(n-2) + fibonacci(n-1);
        return lookup[n];
      }
  return fibonacci(n-2) + fibonacci(n-1);
}
print(fibonacci(12))
