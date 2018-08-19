
cpdomains = ["900 google.chat.domain.com", "1050 yahoo.chat.domain.com", "1 intel.stocks.domain.com"]


d = dict()
answer = []
for countpair in cpdomains:

    no_of_visit, address = countpair.split(' ')
    no_of_visit = int(no_of_visit)

    d[address] = no_of_visit

    while True:
        try:
            address = address.split('.', maxsplit=1)[1]
            if address in d:
                d[address] += no_of_visit
            else:
                d[address] = no_of_visit
        except IndexError:
            break

for key, value in d.items():
    answer.append("{value} {key}".format(key=key, value=value))

print(answer)
