from behave import *

@given('{num01} y {num02}')
def step_impl(context, num01, num02):
    context.num01 = int(num01)
    context.num02 = int(num02)

@when('se suman ambos numeros')
def step_impl(context):
    context.sum = context.num01 + context.num02

@then('el resultado siempre debe ser {res}')
def step_impl(context, res):
    print(context.sum)
    assert context.sum is int(res)