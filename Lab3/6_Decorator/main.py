class UppercaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)

        return result.upper()


@UppercaseDecorator
def get_message():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in odio ultricies, venenatis libero ac."

@UppercaseDecorator
def hello_mess(name):
    return f"Hello, {name}! \n" + get_message()

print(get_message()+"\n")

print(hello_mess("Tom"))

