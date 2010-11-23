== Description ==
A decorator that filters the result from a function that returns an iterable. 

== Example ==
@queryable
def get_persons():
    ...
    return (person for person in some_persons)

males = get_persons(gender='Male')
newborn = get_persons(age=0)

== TODO ==
Implement a similar API to Django's QuerySet.filter()

Examples:
get_persons(age__not=0)
get_persons(hobbies__in=('Music', 'Horses'))
get_persons(age__lt=6), get_persons(age__gte=18)
get_persons(grades__english__lte='B')

Things I might want to implement:
- not
- in
- lt, gt, lte, gte
- contains, icontains
- regex
- child field lookups
