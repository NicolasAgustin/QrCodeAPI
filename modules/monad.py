
class Failure:

    def __init__(this, value):
        this.value = value
        this.error = ''

    def bind(this, f: callable):

        if this.value is None:
            return this.value

        try:
            computed = f(this.value)
            return Failure(computed)
        except Exception as e:
            this.value = None
            this.error = str(e)


if __name__ == '__main__':
    pass
