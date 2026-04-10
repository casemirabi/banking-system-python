import users
import banking

users.criarUsuario()

usuario = users.contas[0]
banking.deposito(usuario, 100)

print(usuario)