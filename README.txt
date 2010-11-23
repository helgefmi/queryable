== Description ==
Filters the result from a function that returns an iterable.

== Example ==
@queryable
def get_persons():
    ...
    return (person for person in some_persons)

males = get_persons(gender='Male')
newborn = get_persons(age=0)

== TODO ==
At some point, I want this to offer more functionality than this, and be more
like the way django queries the database.

!=: get_persons(age__not=0)

< and >: get_persons(age__lt=6), get_persons(age__gte=18)

querying children: get_persons(grades__english__lte='B')
person = {
    ...,
    'grades': {
        'english': 'A',
        ...
    }
}
