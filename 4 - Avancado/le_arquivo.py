from memory_profiler import profile


class Leitor:
    @profile
    def __enter__(self):
        self.arquivo = open("file.txt", "r")
        return self.arquivo

    @profile
    def __exit__(self, exc_type, exc_value, traceback):
        self.arquivo.close()
