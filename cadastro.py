import abstra.forms as af
import abstra.workflows as aw

name = af.read("Nome")
email = af.read_email("Email")
description = af.read_textarea("Descrição do projeto")

aw.set_data("name", name)
aw.set_data("email", email)
aw.set_data("description", description)

af.display(f"Dados registrados, {name}! Aguarde nosso contato.")