"""Given a string str, find the shortest possible string which can be achieved by adding characters to
the end of initial string to make it a palindrome.
Example
For str = "mam", the output should be "memamem"."""


def build_palindrome(st):
    wer = st
    while wer != wer[::-1]:
        wer = wer[1:]
    i = st.rfind(wer)
    return st + st[:i][::-1]


res = build_palindrome('ababab')

print(res + ' -', res == res[::-1])
