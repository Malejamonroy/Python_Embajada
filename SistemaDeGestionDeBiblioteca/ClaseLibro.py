class Libro:
    def __init__(self, titulo, autor, isbn, disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.prestados = 0

    def prestar(self):
        if self.disponible > 0:
            self.disponible -= 1
            self.prestados += 1
            return True
        else:
            return False

    def devolver(self):
        if self.prestados > 0:
            self.disponible += 1
            self.prestados -= 1
            return True
        else:
            return False

    def mostrar(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {self.disponible}, Prestados: {self.prestados}"
    
    
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, titulo, autor, isbn, disponible):
        libro = Libro(titulo, autor, isbn, disponible)
        self.libros.append(libro)
        print(f"Libro '{titulo}' agregado a la biblioteca.")

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            for libro in self.libros:
                print(libro.mostrar())

    def buscar(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                print(libro.mostrar())
                return libro
        print("Libro no encontrado.")
        return None

    def prestar_libro(self, isbn):
        libro = self.buscar(isbn)
        if libro and libro.disponible == True:
            libro.prestar()
        else:
            print("El libro no está disponible.")

    def devolver_libro(self, isbn):
        libro = self.buscar(isbn)
        if libro:
            libro.devolver()
            print("Libro devuelto con éxito.")

# --- Uso del sistema ---

def main():
    biblioteca = Biblioteca()
    biblioteca.agregar("El Principito", "Antoine de Saint-Exupéry", "978-3-16-148410-0", True)
    biblioteca.agregar("Cien Años de Soledad", "Gabriel García Márquez", "978-84-376-0494-7" , True)
    biblioteca.agregar("El alquimista", "Paulo Cohelo", "978-84-376-0494-8" , True)

    print("\nLista de libros:")
    biblioteca.mostrar_libros()

    print("\nPréstamo de un libro:")
    biblioteca.prestar_libro("978-3-16-148410-0")

    print("\nIntento de volver a prestar el mismo libro:")
    biblioteca.prestar_libro("978-3-16-148410-0")

    print("\nDevolución del libro:")
    biblioteca.devolver_libro("978-3-16-148410-0")

    print("\nLista de libros actualizada:")
    biblioteca.mostrar_libros()
   
    while True:
        ## MENU DE USUARIOS
        print("\nBienvenido a la Biblioteca")
        print("1. Mostrar libros")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            biblioteca.mostrar_libros()
        elif opcion == 2:   
            isbn = input("Ingrese el ISBN del libro que desea prestar: ")
            biblioteca.prestar_libro(isbn)
        elif opcion == 3:
            isbn = input("Ingrese el ISBN del libro que desea devolver: ")
            biblioteca.devolver_libro(isbn)
        elif opcion == 4:
            print("Gracias por visitar la Biblioteca")
            break  # Sale del bucle while
    

# Ejecutar el programa
if __name__ == "__main__":
    main()