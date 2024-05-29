class User:
    def __init__(self, username):
        """
        Inicializa un nuevo usuario con el nombre de usuario dado.
        
        :param username: Nombre de usuario
        """
        if not username:
            raise ValueError("El nombre de usuario no puede estar vacío")
        self.username = username
        self.messages = []

    def send_message(self, message, receiver):
        """
        Envía un mensaje a otro usuario.
        
        :param message: El mensaje a enviar
        :param receiver: El usuario que recibirá el mensaje
        """
        if not message:
            raise ValueError("El mensaje no puede estar vacío")
        receiver.receive_message(message, self)
        print(f"Mensaje enviado a {receiver.username}: {message}")

    def receive_message(self, message, sender):
        """
        Recibe un mensaje de otro usuario.
        
        :param message: El mensaje recibido
        :param sender: El usuario que envía el mensaje
        """
        self.messages.append((sender.username, message))
        print(f"{self.username} recibió un nuevo mensaje de {sender.username}: {message}")

    def list_messages(self):
        """
        Lista todos los mensajes recibidos por el usuario.
        """
        if not self.messages:
            print(f"{self.username} no tiene mensajes.")
        else:
            for idx, (sender, message) in enumerate(self.messages):
                print(f"{idx}. {sender}: {message}")

    def delete_message(self, index):
        """
        Elimina un mensaje de la lista de mensajes.
        
        :param index: Índice del mensaje a eliminar
        """
        if 0 <= index < len(self.messages):
            deleted_message = self.messages.pop(index)
            print(f"Mensaje eliminado: {deleted_message}")
        else:
            raise IndexError("Índice fuera de rango")

def main():
    users = {}

    while True:
        print("\nOpciones:")
        print("1. Crear usuario")
        print("2. Enviar mensaje")
        print("3. Listar mensajes")
        print("4. Eliminar mensaje")
        print("5. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            username = input("Nombre del nuevo usuario: ").strip()
            if username in users:
                print("El usuario ya existe.")
            else:
                try:
                    users[username] = User(username)
                    print(f"Usuario {username} creado con éxito.")
                except ValueError as e:
                    print(e)
        
        elif opcion == "2":
            sender_name = input("Nombre del remitente: ").strip()
            receiver_name = input("Nombre del receptor: ").strip()
            message = input("Mensaje: ").strip()
            if sender_name in users and receiver_name in users:
                sender = users[sender_name]
                receiver = users[receiver_name]
                sender.send_message(message, receiver)
            else:
                print("Usuario no encontrado.")
        
        elif opcion == "3":
            username = input("Nombre del usuario para listar mensajes: ").strip()
            if username in users:
                user = users[username]
                user.list_messages()
            else:
                print("Usuario no encontrado.")
        
        elif opcion == "4":
            username = input("Nombre del usuario para eliminar mensaje: ").strip()
            if username in users:
                user = users[username]
                user.list_messages()
                try:
                    index = int(input("Índice del mensaje a eliminar: ").strip())
                    user.delete_message(index)
                except ValueError:
                    print("Por favor, introduce un número válido.")
                except IndexError as e:
                    print(e)
            else:
                print("Usuario no encontrado.")
        
        elif opcion == "5":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
