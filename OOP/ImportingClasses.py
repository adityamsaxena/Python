import PrivateAndPublicClasses
from PrivateAndPublicClasses import NotPrivate

test = NotPrivate('aadi')
test.display()

test._display() #private_method