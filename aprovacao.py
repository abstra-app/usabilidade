import abstra.forms as af
import abstra.workflows as aw

name = aw.get_data("name")
email = aw.get_data("email")
description = aw.get_data("description")

page = af.Page().display_markdown(f"""
- Nome: {name}
- E-mail: {email}
- Descrição: {description}
""").run(actions=["Aprovar", "Rejeitar"])

if page.action == "Aprovar":
    aw.set_data("status", "aprovado")
else:
    aw.set_data("status", "reprovado")
