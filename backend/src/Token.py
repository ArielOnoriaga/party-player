class ReadToken:
    def get() -> str:
        pass

class ReadTokenImplementation(ReadToken):
    def get() -> str:
        return 'hola'


result = ReadTokenImplementation.get()
print(result)
