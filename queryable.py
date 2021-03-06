from functools import wraps

def queryable(func):
    """Makes a function queryable. It's supposed to be used as a decorator"""
    @wraps(func)
    def new_func(*args, **kwargs):
        # The functions must return an iterable
        rows = iter(func(*args))
        for row in rows:
            # Loop through the elements and filter out the ones that doesn't
            # match this particular query.
            for key, value in kwargs.iteritems():
                # Supporting both __getitem__ and __getattr__.
                try:
                    attr = getattr(row, key)
                except AttributeError:
                    attr = row[key]
                if hasattr(attr, '__call__'):
                    attr = attr()
                if attr != value:
                    break
            else:
                yield row
    return new_func

def main():
    @queryable
    def test1():
        return [{'a': True,  'b': '1'}, {'a': True,  'b': '2'},
                {'a': False, 'b': '3'}, {'a': True,  'b': '4'},
                {'a': True,  'b': '5'}, {'a': False, 'b': '6'}]
    
    @queryable
    def test2():
        class A:
            def __init__(self, a, b):
                self.a = a
                self.b = b

        return [A(True, '1'), A(True, '2'), A(False, '3'),
                A(True, '4'), A(True, '5'), A(False, '6')]
    
    @queryable
    def test3():
        class A:
            def __init__(self, a, b):
                self.a = a
                self.b = b
        def mkfun(ret):
            return lambda: ret
        return iter((A(mkfun(True),  '1'), A(mkfun(True),  '2'),
                     A(mkfun(False), '3'), A(mkfun(True),  '4'),
                     A(mkfun(True),  '5'), A(mkfun(False), '6')))

    print 'Running tests ..'

    assert '1245' == ''.join(map(lambda x:x['b'], test1(a=True)))
    assert '1245' == ''.join(map(lambda x:x.b, test2(a=True)))
    assert list(test1(a=False))== [{'a': False, 'b': '3'}, \
                                   {'a': False, 'b': '6'}]
    assert '123456' == ''.join(map(lambda x:x['b'], test1()))
    assert '123456' == ''.join(map(lambda x:x.b, test2()))
    assert '1245' == ''.join(map(lambda x:x.b, test3(a=True)))
    assert '123456' == ''.join(map(lambda x:x.b, test3()))

    print 'All tests ok'

if __name__ == '__main__':
    main()
