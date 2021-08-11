# Regular Expressions in Python
A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world.

The module re provides full support for Perl-like regular expressions in Python. The re module raises the exception re.error if an error occurs while compiling or using a regular expression.

We would cover two important functions, which would be used to handle regular expressions. Nevertheless, a small thing first: There are various characters, which would have special meaning when they are used in regular expression. To avoid any confusion while dealing with regular expressions, we would use Raw Strings as r'expression'.

Basic patterns that match single chars
Expression | Matches
----|----
`a, X, 9, <`|ordinary characters just match themselves exactly.
`. (a period)`|matches any single character except newline '\n'
`\w`|matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_].
`\W`|matches any non-word character.	
`\b`|boundary between word and non-word
`\s`|matches a single whitespace character -- space, newline, return, tab
`\S`|matches any non-whitespace character.
`\t, \n, \r`|tab, newline, return
`\d`|decimal digit [0-9]
`^`|matches start of the string
`$`|match the end of the string
`\`|inhibit the "specialness" of a character.

## Compilation flags
Compilation flags let you modify some aspects of how regular expressions work. Flags are available in the re module under two names, a long name such as IGNORECASE and a short, one-letter form such as I.

Flag | Meaning
----|----
`ASCII, A`|Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
`DOTALL, S`|Make, match any character, including newlines
`IGNORECASE, I`|Do case-insensitive matches
`LOCALE, L`|Do a locale-aware match
`MULTILINE, M`|Multi-line matching, affecting ^ and $
`VERBOSE, X (for ‘extended’)`|Enable verbose REs, which can be organized more cleanly and understandably

## The match Function
This function attempts to match RE pattern to string with optional flags.

Here is the syntax for this function −
```
re.match(pattern, string, flags = 0)
```
Here is the description of the parameters −

Parameter | Description
----|----
`pattern`|This is the regular expression to be matched.
`string`|This is the string, which would be searched to match the pattern at the beginning of string.
`flags`|You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.

The re.match function returns a match object on success, None on failure. We usegroup(num) or groups() function of match object to get matched expression.

Match Object Method | Description
----|----
`group(num = 0)`|This method returns entire match (or specific subgroup num)
`groups()`|This method returns all matching subgroups in a tuple (empty if there weren't any)

**Example**
``` python
#!/usr/bin/python3
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
```
When the above code is executed, it produces the following result −
```
matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter
```
The search Function
This function searches for first occurrence of RE pattern within string with optional flags.

Here is the syntax for this function −
```
re.search(pattern, string, flags = 0)
```
Here is the description of the parameters −

Parameter | Description
----|---
`pattern`|This is the regular expression to be matched.
`string`|This is the string, which would be searched to match the pattern anywhere in the string.
`flags`|You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.

The re.search function returns a match object on success, none on failure. We use `group(num)` or `groups()` function of match object to get the matched expression.

Match Object Method | Description
----|----	
`group(num = 0)`|This method returns entire match (or specific subgroup num)
`groups()`|This method returns all matching subgroups in a tuple (empty if there weren't any)

**Example**
```python

#!/usr/bin/python3
import re

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")
```
When the above code is executed, it produces the following result −
```
matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter
```
## Matching Versus Searching
Python offers two different primitive operations based on regular expressions: match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string (this is what Perl does by default).

Example
```python
#!/usr/bin/python3
import re

line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!")
```
When the above code is executed, it produces the following result −
```
No match!!
search --> matchObj.group() :  dogs
```
## Search and Replace
One of the most important re methods that use regular expressions is sub.

**Syntax**
```
re.sub(pattern, repl, string, max=0)
```
This method replaces all occurrences of the RE pattern in string with repl, substituting all occurrences unless max is provided. This method returns modified string.

**Example**
```python
#!/usr/bin/python3
import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)
```
When the above code is executed, it produces the following result −
```
Phone Num :  2004-959-559
Phone Num :  2004959559
```
## Regular Expression Modifiers: Option Flags
Regular expression literals may include an optional modifier to control various aspects of matching. The modifiers are specified as an optional flag. You can provide multiple modifiers using exclusive OR (|), as shown previously and may be represented by one of these −

Modifier | Description
----|----
`re.I`|Performs case-insensitive matching.
`re.L`|Interprets words according to the current locale. This interpretation affects the alphabetic group (\w and \W), as well as word boundary behavior (\b and \B).
`re.M`|Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).
`re.S`|Makes a period (dot) match any character, including a newline.
`re.U`|Interprets letters according to the Unicode character set. This flag affects the behavior of `\w, \W, \b, \B`.
`re.X`|Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set `[]` or when escaped by a backslash) and treats unescaped # as a comment marker.

## Regular Expression Patterns
Except for the control characters, `(+ ? . * ^ $ ( ) [ ] { } | \)`, all characters match themselves. You can escape a control character by preceding it with a backslash.

The following table lists the regular expression syntax that is available in Python −

Here is the list of regular expression syntax in Python.
## Regular Expression Examples
### Literal characters
Example | Description
----|----
`python`|Match "python".

### Character classes
Example | Description
----|----
`[Pp]ython`|Match "Python" or "python"	
`rub[ye]`|Match "ruby" or "rube"
`[aeiou]`|Match any one lowercase vowel
`[0-9]`|Match any digit; same as [0123456789]
`[a-z]`|Match any lowercase ASCII letter
`[A-Z]`|Match any uppercase ASCII letter
`[a-zA-Z0-9]`|Match any of the above	
`[^aeiou]`|Match anything other than a lowercase vowel
`[^0-9]`|Match anything other than a digit

### Special Character Classes
Example | Description
----|----
`.`|Match any character except newline
`\d`|Match a digit: [0-9]
`\D`|Match a nondigit: [^0-9]
`\s`|Match a whitespace character: [ \t\r\n\f]
`\S`|Match nonwhitespace: [^ \t\r\n\f]
`\w`|Match a single word character: [A-Za-z0-9_]
`\W`|Match a nonword character: [^A-Za-z0-9_]

### Repetition Cases
Example | Description
----|----
`ruby?`|Match "rub" or "ruby": the y is optional
`ruby*`|Match "rub" plus 0 or more ys
`ruby+`|Match "rub" plus 1 or more ys
`\d{3}`|Match exactly 3 digits
`\d{3,}`|Match 3 or more digits
`\d{3,5}`|Match 3, 4, or 5 digits

### Nongreedy repetition
This matches the smallest number of repetitions −

Example | Description
----|----
`<.*>`|Greedy repetition: matches "<python>perl>"
`<.*?>`|Nongreedy: matches `"<python>"` in `"<python>perl>"`

### Grouping with Parentheses
Example | Description
----|----
`\D\d+`|No group: + repeats \d
`(\D\d)+`|Grouped: + repeats \D\d pair
`([Pp]ython(,)?)+`|Match "Python", "Python, python, python", etc.

### Backreferences
This matches a previously matched group again −

Example | Description
----|----
`([Pp])ython&\1ails`|Match python&pails or Python&Pails
`(['"])[^\1]*\1`|Single or double-quoted string. \1 matches whatever the 1st group matched. \2 matches whatever the 2nd group matched, etc.

### Alternatives
Example | Description
----|----
`python|perl`|Match "python" or "perl"
`rub(y|le)`|Match "ruby" or "ruble"
`Python(!+|\?)`|"Python" followed by one or more ! or one ?

### Anchors
This needs to specify match position.

Example | Description
----|----	
`^Python`|Match "Python" at the start of a string or internal line
`Python$`|Match "Python" at the end of a string or line
`\APython`|Match "Python" at the start of a string
`Python\Z`|Match "Python" at the end of a string
`\bPython\b`|Match "Python" at a word boundary
`\brub\B`|\B is nonword boundary: match "rub" in "rube" and "ruby" but not alone
`Python(?=!)`|Match "Python", if followed by an exclamation point.
`Python(?!!)`|Match "Python", if not followed by an exclamation point.

### Special Syntax with Parentheses
Example | Description
----|----
`R(?#comment)`|Matches "R". All the rest is a comment
`R(?i)uby`|Case-insensitive while matching "uby"
`R(?i:uby)`|Same as above
`rub(?:y|le))`|Group only without creating \1 backreference
