from books.models import Publisher

p1 = Publisher(name='Apress', address='2855 Telegraph Avenue',
               city='Berkeley', state_province='CA', country='U.S.A.',
               website='http://www.apress.com/')

p2 = Publisher(name="O'Reilly1", address='10 Fawcett St.',
               city='Cambridge', state_province='MA', country='U.S.A.',
               website='http://www.oreilly.com/')

if __name__ == "__main__":
    p1.save()
    p2.save()

    publishers_list = Publisher.objects.all()
    print(publishers_list)