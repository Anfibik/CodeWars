"""https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python"""


def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]



print(domain_name("https://www.codewars.co.me/kata/514a024011ea4fb54200004b/discuss"))
print(domain_name("https://translate.google.com/?sl=en&tl=ru&text=should%20equal&op=translate"))
print(domain_name("https://codewars.com/kata/514a024011ea4fb54200004b/discuss"))



