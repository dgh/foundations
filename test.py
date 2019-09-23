from char import Char
from alphabet import Alphabet
from string import String

char_test1 = Char('a')
char_test2 = Char('b')
char_test3 = Char('c')
char_test4 = Char('d')

alphabet_test = Alphabet([char_test1, char_test2, char_test3, char_test4])
string_test = String([char_test1, char_test2, char_test3], alphabet_test)

print(alphabet_test)
print(string_test)