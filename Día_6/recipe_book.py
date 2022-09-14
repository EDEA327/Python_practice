"""Por aqui voy a dejar ciertas consideraciones con el fin de que mi
código se vea más profesional 😁
utilizaré el punto de entrada if __name__ == '__main__': por buenas
prácticas en el código, además de utilizar el tipado estático por cuestiones
de legibilidad de mi código y..
por ultimo casi todo el  código del proyecto está en inglés
si quieres saber más sobre tipado en python...
https://docs.python.org/es/3.10/library/typing.html?highlight=typing#typing.Union
"""
# Imports...

from typing import Iterable
from pathlib import Path
from shutil import rmtree
from colorama import init,Fore,Style
from os import system
import platform
import time

# Variables globales, se pueden usar en cualquier función
base: Path= Path("/Users/erick/OneDrive/Escritorio/ecode/Python")#Si lo quieren correr deben cambiar la ruta base
origin:Path = Path(base/'Recetas')
num_recipes:int = 8 # Numero de recetas iniciales en el archivo de la clase
menu = '''
MENU
1. Choose a category and read a recipe
2. Choose category and Create a new recipe
3. Create a new category
4. Delete an existent recipe
5. Delete an existent category
6. Exit
'''
options:Iterable[int] = (1,2,3,4,5,6)

# Funciones...
def greeting(name:str):
    welcome:str = f"""
Hi {Fore.YELLOW + Style.BRIGHT + name} !!
{Style.RESET_ALL + "Welcome to the Recipe Book recipes are at"}
{Fore.GREEN + Style.BRIGHT + str(origin)}
{Style.RESET_ALL + f'you have {Fore.CYAN + Style.BRIGHT + str(num_recipes)}'} {Style.RESET_ALL + 'recipes'}
"""

    print (welcome)

def validate_option(iterable:Iterable) -> int:
    foo = True
    while foo:
        option:int = int(input("Please select an option: "))
        if option not in iterable:
            print(f"{option} {Fore.RED + 'is not'} {Style.RESET_ALL +'a valid option'} ")
            continue
        else:
            foo = False
    return option

def clean_screen(seg:int):
    if platform.system() == 'Windows':
        time.sleep(seg)
        system('cls')
    else:
        time.sleep(seg)
        system('clear')

def choose_category(route:Path) -> Path:
    categories = [category.name for category in route.iterdir() if category.is_dir()]
    categories_index = [ index+1 for index,category in enumerate(categories)]

    # recorremos las categorias
    for index,categoria in enumerate(categories,start=1):
        print(f'{index} - {categoria}')
    opv: int = validate_option(categories_index) #validamos la opcion y la guardo en la variable
    clean_screen(0.5)

    #defino mis rutas de recetas
    recipe_route:Path = Path(route/str(categories[opv-1]))

    return recipe_route

def choose_recipe(recipe:Path):
    recipes = [recipe for recipe in recipe.iterdir() if recipe.is_file()]
    recipes_index = [index+1 for index, recipe in enumerate(recipes)]

    # recorremos las recetas
    print(f'The recipes in {recipe.name}  are : ')
    for index,recipe in enumerate(recipes,start=1):
        print(f'{index} - {recipe.stem}')
    rv= validate_option(recipes_index)

    # leemos la receta escogida por el usuario y la mostramos en pantalla
    chosen_recipe:Path = Path(str(recipes[rv-1]))
    print(chosen_recipe.read_text())

def create_recipe(recipe:Path):
    file_name:str = input("Please enter your file name: ")
    n_file:Path = Path(recipe/str(file_name + ".txt"))

    if n_file.exists():
        print(f'{Fore.RED + "Warning: Filename already exists"} {Style.RESET_ALL +"it will be overwritten"}')
        new_recipe = open(n_file,"w")
        text = input("Please Enter your recipe: ")
        new_recipe.write(text)
        new_recipe.close()
        print(f'The recipe {new_recipe} was created successfully')
    else:
        new_recipe = open(n_file,"w")
        text = input("Please Enter your recipe: ")
        new_recipe.write(text)
        new_recipe.close()
        print(f'The recipe {new_recipe} was created successfully')

def create_category(route:Path):
    category_name:str = input("Please enter your  dirname: ")
    n_category:Path = Path(route/category_name)
    n_category.mkdir(parents=True,exist_ok=True)
    print(f'The category {category_name} was created successfully')

def delete_recipe(recipe:Path):
    recipes = [recipe for recipe in recipe.iterdir() if recipe.is_file()]
    recipes_index = [index+1 for index, recipe in enumerate(recipes)]

    # recorremos las recetas
    print(f'The recipes in {recipe.name}  are : ')
    for index,recipe in enumerate(recipes,start=1):
        print(f'{index} - {recipe.stem}')
    print("Which recipe you want to delete?")
    rv= validate_option(recipes_index)
    chosen_recipe:Path = Path(str(recipes[rv-1]))
    chosen_recipe.unlink(missing_ok=True)
    print(f"{recipe[rv-1]} was deleted ")

def delete_category(route:Path):
    categories = [category.name for category in route.iterdir() if category.is_dir()]
    categories_index = [ index+1 for index,category in enumerate(categories)]

    # recorremos las categorias
    for index,categoria in enumerate(categories,start=1):
        print(f'{index} - {categoria}')
    opv: int = validate_option(categories_index)

    # elimianr categoria
    category_route:Path = Path(route/str(categories[opv-1]))
    rmtree(category_route)
    print("Successfully deleted category")

def run():
    # 1 Se da la bienvenida al usuario se le informa donde están las recetas y cuantas recetas tiene inicialmente
    name:str = input("Please enter your name: ")
    greeting(name)
    ## Limpieza de pantalla
    clean_screen(2)
    # # 2 Se le dan las opciones al usuario y se guarda la opcion escogida en la variable chosen_option
    keep_running = True
    while keep_running:
        print(menu)
        chosen_option = validate_option(options)
        clean_screen(0.5)
        #3 Se escoje que se va a hacer segun la opcion ingresada
        if chosen_option == 1:
            category = choose_category(origin)
            choose_recipe(category)
        elif chosen_option == 2:
            category = choose_category(origin)
            create_recipe(category)
            num_recipes = num_recipes + 1
        elif chosen_option == 3:
            create_category(origin)
        elif chosen_option == 4:
            category = choose_category(origin)
            delete_recipe(category)
        elif chosen_option == 5:
            delete_category(origin)
        elif chosen_option == 6:
            keep_running = False
            break
        wish = input("Want to continue? (y/n): ")
        if wish == "y":
            clean_screen(0.1)
            keep_running = True
        elif wish == "n":
            clean_screen(0.1)
            keep_running = False
        else:
            print("OK, lets play again HAHAHA!")
            continue

# entrypoint
if __name__ == '__main__':
    run()