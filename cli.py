import click
import lector_json

#   Traducir a español el resultado del parametro --help
class GrupoPersonalizado(click.Group):
    def get_help(self, ctx):
        help_text = super().get_help(ctx)
        help_text = help_text.replace("Usage", "Uso")
        help_text = help_text.replace("Options", "Opciones")
        help_text = help_text.replace("Commands", "Comandos")
        help_text = help_text.replace("Show this message and exit.", "Muestra este mensaje y sale.")
        return help_text


@click.group(cls=GrupoPersonalizado)
def cli():
    pass

@cli.command()
@click.option('--nombre', required=True, help='Nombre del usuario')
@click.option('--apellido', required=True, help='Apellidol del usuario')
@click.pass_context
def crear(ctx, nombre, apellido):
    if not nombre or not apellido:
        ctx.fail("Nombre y apellido requeridos")
    else:
        data = lector_json.leer()
        nuevo_id = len(data) + 1
        nuevo_usuario = {
            "id" : nuevo_id,
            "name" : nombre,
            "lastname" : apellido
        }
        data.append(nuevo_usuario)
        lector_json.escribir(data)

@cli.command()
def users():
    data = lector_json.leer()
    for user in data:
        print(f"ID: {user['id']} - Nombre: {user['name']} - Apellido: {user['lastname']}")


@cli.command()
@click.argument("id", type=int)
def user(id):
    data = lector_json.leer()
    user = next((x for x in data if x["id"] == id), None)

    if user is None:
        print(f"Usuario con ID {id} no encontrado")
    else:
        print(f"Usuario con ID {user['id']}: \n Nombre: {user['name']} \n Apellido: {user['lastname']}")


@cli.command()
@click.argument("id", type=int)
def eliminar(id):
    pass


if __name__ == "__main__":
    cli()

