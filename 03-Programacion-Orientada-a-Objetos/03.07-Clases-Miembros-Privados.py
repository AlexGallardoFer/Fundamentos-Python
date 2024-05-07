###################################################
# Clases - Miembros Privados                      #
###################################################

class Demo:
    __Variable = None

    def publico(self):
        print("Todos puede saber")

    def _privado(self):
        print("Nadie debería saber")

    def __secreto(self):
        print("Nadie puede saber")


demo = Demo()

demo.publico()
demo._privado()
# demo.__secreto()
demo._Demo__secreto()

print(dir(demo))