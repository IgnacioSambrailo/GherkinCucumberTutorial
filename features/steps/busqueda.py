from behave import given, then, when



@given(u'Un usuario que se encuentra en la pagina {pagina}')
def step_impl(context,pagina):
    pass


@given(u'Un usuario no registrado')
def step_impl(context):
    pass


@when(u'Realiza la busqueda de {texto}')
def step_impl(context,texto):
    pass


@then(u'Encuentra resultados que contengan {texto}')
def step_impl(context,texto):
    pass