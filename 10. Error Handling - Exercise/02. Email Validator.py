import re

regex = r"(\b(?P<Name>[a-z]{4,}))(?P<Symbol>@)[a-zA-Z]+(?P<Domain>.com|.bg|.net|.org)"


class MustContainAtSymbolError(Exception):
    pass


class NameTooShort(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidEmail(Exception):
    pass


email = input()

while email != "End":

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, *_ = email.split('@')

    if len(name) < 4:
        raise NameTooShort("Name must be more than 4 characters")

    if len(_) > 1:
        raise InvalidDomainError('Invalid domain')

    check_domain = email.split('.')[-1]
    if check_domain not in ['com', 'bg', 'org', 'net']:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    match = re.match(regex, email)
    if match:
        print('Email is valid')
    else:
        raise InvalidEmail("Email is not valid")

    email = input()
