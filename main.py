import random


# clase menu porque no sabia como llamarla
class Menu:
    # constructor de clase, para poder usarlos como objeto en las funciones
    def __init__(self):
        self.colores = ['amarillo', 'azul', 'verde', 'rojo']
        self.usuarios = [{'Nombre': 'Josep'}, {'Nombre': 'Claudio'}, {'Nombre': 'Isabel'}, {'Nombre': 'Sheila'}]

    # Metod switch para realizar las llamadas a las funciones dependeindo de lo que selecione el usario
    def switch(self, option):
        if option == 1:
            self.add_color()
        elif option == 2:
            self.show_list()
        elif option == 3:
            print('1. Ordenar de forma alfabetica de a - z')
            print('2. Ordenar de forma alfabetica de z - a')
            option2 = int(input('Selecione una opcion: '))
            if option2 == 1:
                self.order_list()
            elif option2 == 2:
                self.order_list_reverse()
            else:
                print('Error a la hora de selciona ')
        elif option == 4:
            self.add_user()
        elif option == 5:
            self.add_users_colors()
        elif option == 6:
            print('1. Ordenar de forma alfabetica de a - z')
            print('2. Ordenar de forma alfabetica de z - a')
            option2 = int(input('Selecione una opcion: '))
            if option2 == 1:
                self.show_user_list_a()
            elif option2 == 2:
                self.show_user_list_z()
            else:
                print('Error a la hora de selciona ')
        elif option == 7:
            self.delete_user()
        elif option == 8:
            self.show_user_names()
        elif option == 9:
            self.say_goodbye()
            return False
        else:
            print("Opción no válida. Intente de nuevo.")
        return True

    # este metodo seria nuestro menu, esta en modo bucle
    def run(self):
        while True:
            print('')
            print("============== MENU ==============")
            print("1. Añadir colores a la lista")
            print("2. Mostrar lista de colores")
            print("3. Ordenar alfabéticamente la lista de colores")
            print("4. Añadir un nuevo usuario a la lista")
            print("5. Asignar colores a los usuarios")
            print("6. Mostrar lista de usuarios / alfabéticamente")
            print("7. Eliminar")
            print("8. Mostrar nombres de usuarios")
            print("9. Salir")
            print('')
            option = int(input("Seleccione una opción: "))
            if not self.switch(option):
                break

    # añadir un color
    def add_color(self):
        # esta funcion se repetira en caso de que el color ya se encuentre en la lista
        # ademas pasara a minusculas todo
        while True:
            new_color = str(input("Introduzca el nuevo color: ")).lower()
            if new_color.islower() and new_color not in self.colores:
                self.colores.append(new_color)
                print(f"Se añadió el color {new_color} a la lista.")
                break
            else:
                print("El contenido introducido no es correcto o el color ya existe.")

    # medainte un bucle for se muestra los colores
    def show_list(self):
        for color in self.colores:
            print(color)

    # se utiliza el metodo sorted par aordenadr elementos en un orden específico, ya sea ascendente o descendente
    def order_list(self):
        for color in sorted(self.colores):
            print(color)

    # el metodo sported al poner que el reves sea verdadero se procede a invertir la lista
    def order_list_reverse(self):
        for color in sorted(self.colores, reverse=True):
            print(color)

    # añadir un nuevo usario, se comprueba si el usuario tendra color en caso de que no se le debera añadir
    # un nuevo color par aque todos dispongan de uno
    def add_user(self):
        while True:
            try:
                user_name: str = str(input("Añada un nuevo usario a la lista: "))
                if user_name.isalpha():
                    new_user: dict = {'Nombre': user_name}
                    self.usuarios.append(new_user)
                    print(f"Se ha añadido {new_user['Nombre']} a la lista de jugadores")
                    if len(self.usuarios) > len(self.colores):
                        print('hay mas usarios que colores, \n debera de añadir un color a la lista')
                        self.add_color()
                        break
                else:
                    print("Debe introducir un nombre válido (solo letras)")
            except ValueError:
                print("Debe introducir un nombre")

    # fusion de color con usarios
    def add_users_colors(self):
        # comprobamos el numer de usarios par alos colores
        num_user = len(self.usuarios)
        if num_user == 0:
            print('No hay suficientes usuarios para asignar los colores')
            return
        # el metodo copy realiza la creacion de una nueva lista copiando exactamente la original la de self.colores
        color_for_user = self.colores.copy()
        # asignar la informacion de la nueva lista, y mediante shuffle reorganiza sus elementos en un orden aleatorio
        random.shuffle(color_for_user)
        # llamamos a la lista de usarios y la recoremos con un for
        for user in self.usuarios:
            # verifica que no este vacio, que contenga elementos
            if color_for_user:
                # al usar el metodo pop, esta sacando los ultimos elementos de la lista, y los asigna a la variable
                asign_color = color_for_user.pop()
                # aqui se añade el color al diccionario de usarios, y cada elemento recibe un color diferente
                user['Color'] = asign_color

        print('Se han asignado los colores a los usarios: ')
        for user in self.usuarios:
            # Muestro los usarios y sus colores
            print(f"'{user['Nombre']} : {user['Color']}")

    def show_user_list_a(self):
        # aqui aplico casi el mismo metodo que con los colores pero hay una diferencia, esto es un dict
        # lo que conlleva que se deba llamar a la llave y cada x representa cada elemento de la lista y x[nombre]
        # accede al valor nombre del diccionario
        for user in sorted(self.usuarios, key=lambda x: x['Nombre']):
            print(user['Nombre'])

    def show_user_list_z(self):
        for user in sorted(self.usuarios, key=lambda x: x['Nombre'], reverse=True):
            print(user['Nombre'])

    def delete_user(self):
        while True:
            # self.show_user_list_a()
            try:
                elim = int(input('Que usuario desea eliminar, introduzca su posicion y sera elimando:'))
                # se introduce un numero y se comprueba que se amenor o igual al largo del dict len(self.usuarios)
                if 1 <= elim <= len(self.usuarios):
                    # se procede a eliminar el usario selecionado del dict -1 es para restar una posicion de la lista
                    # user_elim nos permite acceder a los detalles del usario eliminado
                    user_elim = self.usuarios.pop(elim - 1)
                    print(f"Se ha eliminado al usuario {user_elim['Nombre']}")
                    break
                else:
                    # en caso de que se salga del rango le indicamos los numeros de la lista
                    n = 0
                    for num in self.usuarios:
                        n += 1
                        print(num.items(), n)
                    print("No se ha eliminado ningún usuario")
            except ValueError:
                print("Debe introducir un numero que este en la lista")
            except IndexError:
                print(f"El numero introducido esta fuera de rango, introduzca un numero entre {len(self.usuarios)}: ")

    def show_user_names(self):
        print("Nombres de los usuarios:")
        for user in self.usuarios:
            print(user['Nombre'])

    def say_goodbye(self):
        for user in self.usuarios:
            print(f"Hasta luego! {user['Nombre']}, gracias por contar con nosotros.")


if __name__ == '__main__':
    m: Menu = Menu()
    m.run()
