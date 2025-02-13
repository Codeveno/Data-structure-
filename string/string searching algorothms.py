from collections import deque

#string searching algorithms
#String searching algorithms are algorithms that search for a substring in a string.
#There are several string searching algorithms, including the brute force algorithm, the Boyer-Moore algorithm, and the Knuth-Morris-Pratt algorithm.
#The brute force algorithm is the simplest string searching algorithm.
#The brute force algorithm compares the substring with the string character by character.
#The brute force algorithm has a time complexity of O(n*m), where n is the length of the string and m is the length of the
#substring.
#The Boyer-Moore algorithm is a more efficient string searching
#algorithm than the brute force algorithm.
#The Boyer-Moore algorithm uses a heuristic to skip characters in the string that do not match the substring.
#The Boyer-Moore algorithm has a time complexity of O(n+m), where n is the length of the string and m is the length of the substring.
#The Knuth-Morris-Pratt algorithm is another efficient string searching algorithm.
#The Knuth-Morris-Pratt algorithm uses a prefix function to skip characters in the string that do not match the substring.
#The Knuth-Morris-Pratt algorithm has a time complexity of O(n+m), where n is the length of the string and m is the length of the substring.
#The Rabin-Karp algorithm is another string searching algorithm that uses hashing to search for a substring in a string.
#The Rabin-Karp algorithm has a time complexity of O(n+m), where n is the length of the string and m is the length of the substring.
#The Aho-Corasick algorithm is another string searching algorithm that uses a trie data structure to search for multiple substrings in a string.
#The Aho-Corasick algorithm has a time complexity of O(n+m), where n is the length of the string and m is the length of the substring.
#The Z algorithm is another string searching algorithm that uses a Z array to search for a substring in a string.
#The Z algorithm has a time complexity of O(n+m), where n is the length of the string and m is the length of the substring.
#The string searching algorithms are used in text editors, search engines, and other applications that require searching for a substring in a string.
#The string searching algorithms are used in text editors, search engines, and other applications that require searching for a substring in a string.

# Example of string searching algorithms

# Brute Force Algorithm
def brute_force(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1

# Boyer-Moore Algorithm
def boyer_moore(text, pattern):
    def bad_character_table(pattern):
        table = {}
        for i in range(len(pattern)):
            table[pattern[i]] = i
        return table

    n = len(text)
    m = len(pattern)
    bad_char = bad_character_table(pattern)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1

# Knuth-Morris-Pratt Algorithm
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Rabin-Karp Algorithm
def rabin_karp(text, pattern, q=101):
    d = 256
    n = len(text)
    m = len(pattern)
    p = 0
    t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

# Aho-Corasick Algorithm
#determines if a pattern is present in a text

class AhoCorasick:
    def __init__(self, patterns):
        self.trie = {}
        self.build_trie(patterns)
        self.build_failure_links()

    def build_trie(self, patterns):
        for pattern in patterns:
            node = self.trie
            for char in pattern:
                node = node.setdefault(char, {})
            node['$'] = pattern

    def build_failure_links(self):
        queue = deque()
        for char in self.trie:
            if char != '$':
                self.trie[char]['fail'] = self.trie
                queue.append(self.trie[char])
        while queue:
            current_node = queue.popleft()
            for char, next_node in current_node.items():
                if char == 'fail' or char == '$':
                    continue
                fail_node = current_node['fail']
                while fail_node is not None and char not in fail_node:
                    fail_node = fail_node.get('fail')
                next_node['fail'] = fail_node[char] if fail_node else self.trie
                queue.append(next_node)

    def search(self, text):
        node = self.trie
        results = []
        for i, char in enumerate(text):
            while node is not None and char not in node:
                node = node.get('fail')
            if node is None:
                node = self.trie
                continue
            node = node[char]
            if '$' in node:
                results.append((i - len(node['$']) + 1, node['$']))
        return results

# Z Algorithm
#determines if a pattern is present in a text

def z_algorithm(text, pattern):
    concat = pattern + "$" + text
    Z = [0] * len(concat)
    l, r, k = 0, 0, 0
    for i in range(1, len(concat)):
        if i > r:
            l, r = i, i
            while r < len(concat) and concat[r] == concat[r - l]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            k = i - l
            if Z[k] < r - i + 1:
                Z[i] = Z[k]
            else:
                l = i
                while r < len(concat) and concat[r] == concat[r - l]:
                    r += 1
                Z[i] = r - l
                r -= 1
    for i in range(len(Z)):
        if Z[i] == len(pattern):
            return i - len(pattern) - 1
    return -1

# Example usage
text = "ababcabcabababd"
pattern = "ababd"

print("Brute Force:", brute_force(text, pattern))
print("Boyer-Moore:", boyer_moore(text, pattern))
print("KMP:", kmp_search(text, pattern))
print("Rabin-Karp:", rabin_karp(text, pattern))
print("Aho-Corasick:", AhoCorasick([pattern]).search(text))
print("Z Algorithm:", z_algorithm(text, pattern))
