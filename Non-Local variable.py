def hello():
    message = ('local')
    def greet():
        nonlocal message
        message = 'nonlocal'
        print("greet:", message)
    greet()
    print("hello:", message)
hello()