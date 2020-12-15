# python3
import sys


def ComputePrefixFunction(pattern):
    p_len = len(pattern)
    s = [0] * p_len
    border = 0
    for i in range(1, p_len):
        while border > 0 and pattern[i] != pattern[border]:
            border = s[border - 1]
        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s

def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  if len(pattern) > len(text):
      return
  
  string = pattern + '$' + text
  s = ComputePrefixFunction(string)
  
  result = []
  # Implement this function yourself
  for i in range(len(pattern) + 1, len(string)):
      if s[i] == len(pattern):
          result.append(i - 2*len(pattern))
  
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

