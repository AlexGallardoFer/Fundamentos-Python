###################################################
# Procesamiento Asíncrono                         #
###################################################

import asyncio

async def main():
    print("async main -> Hola....")
    await asyncio.gather(func1(), func2())
    print("async main -> ..... Adios !!!")

async def func1():
    print("async func1 -> Hola....")
    await asyncio.sleep(5)
    print("async func1 -> ..... Adios !!!")

async def func2():
    print("async func2 -> Hola....")
    print("async func2 -> ..... Adios !!!") 

print("Inicio Async")
asyncio.run(main())
print("Fin Async\n")





###################################################
# Procesamiento Síncrono                          #
###################################################

def main():
    print("main -> Hola....")
    print("main -> ..... Adios !!!")

print("Inicio Sync")
main()
print("Fin Sync\n")