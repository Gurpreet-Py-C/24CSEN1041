# String initialization
s1 = "Hello"
s2 = 'Python'
s3 = """Welcome to string demo"""

print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
print()

# Accessing strings (indexing)
print("First character of s1:", s1[0])        # H
print("Last character of s1:", s1[-1])        # o
print()

# Basic operations
# Concatenation
s4 = s1 + " " + s2
print("Concatenation (s1 + ' ' + s2):", s4)

# Repetition
s5 = s1 * 3
print("Repetition (s1 * 3):", s5)

# Length
print("Length of s3:", len(s3))

# Membership
print("'Py' in s2?", "Py" in s2)
print("'java' not in s2?", "java" not in s2)
print()

# String slicing
text = "Programming"
print("text =", text)

print("text[0:4]   =", text[0:4])     # Prog
print("text[3:]    =", text[3:])      # gramming
print("text[:5]    =", text[:5])      # Progr
print("text[-4:]   =", text[-4:])     # ming
print("text[::2]   =", text[::2])     # Pormig
print("text[::-1]  =", text[::-1])    # reverse
print()

# String functions and methods
sample = "   hello python world   "
print("Original sample: '", sample, "'", sep="")

# strip: remove leading/trailing spaces
print("strip()       -> '", sample.strip(), "'", sep="")

# upper and lower
print("upper()       ->", sample.upper())
print("lower()       ->", sample.lower())

# replace
print("replace('python', 'Java') ->", sample.replace("python", "Java"))

# split (by whitespace)
words = sample.strip().split()
print("split() ->", words)

# join
joined = "-".join(words)
print("'-'.join(words) ->", joined)

# find
print("find('python') ->", sample.find("python"))

# count
print("count('l') ->", sample.count("l"))

# startswith / endswith
print("startswith('   he') ->", sample.startswith("   he"))
print("endswith('world   ') ->", sample.endswith("world   "))

# isalpha / isdigit (after stripping spaces)
only_letters = "HelloWorld"
only_digits = "12345"
print("'HelloWorld'.isalpha() ->", only_letters.isalpha())
print("'12345'.isdigit() ->", only_digits.isdigit())
