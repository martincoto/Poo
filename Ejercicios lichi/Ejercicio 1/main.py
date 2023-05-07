from Email import Email
from Email import manejadorEmail

if __name__ == '__main__':
    nom = input('Ingrese su nombre: ')
    id = input('Ingrese ID: ')
    dom = input('Ingrese dominio: ')
    tipoDom = input('Ingrese tipo de dominio: ')
    contraseña = input('Ingrese contraseña: ')
    mail = Email(id,dom,tipoDom,contraseña)
    print("Estimado",nom,"te enviaremos tus mensajes a la dirección",mail.retornamail(),".")
    print("El mail es: ",mail.retornamail())
    print("El dominio es: ",mail.getDominio())
    mail.ModificaContraseña()
    correo1 = "informatica.fcefn@gmail.com"
    mail2= mail.crearCuenta(correo1)
    lista = manejadorEmail()
    lista.testEmail()
    m = 0
    dominio = input('Ingrese dominio: ')
    cant = lista.controlDom(dominio,m)
    print("La cantidad de dominios es igual a ",cant)