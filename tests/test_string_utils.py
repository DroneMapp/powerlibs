from powerlibs.string_utils import snake_case, camel_case


def test_snake_case():
    assert snake_case('already_snake') == 'already_snake'
    assert snake_case('camelCase') == 'camel_case'
    assert snake_case('PascalCase') == 'pascal_case'
    assert snake_case('I-dont-know-case') == 'i-dont-know-case'


def teste_camel_case():
    assert camel_case('camelCase') == 'camelCase'
    assert camel_case('PascalCase') == 'PascalCase'
    assert camel_case('snake_case') == 'snakeCase'
    assert camel_case('I-dont-know-case') == 'I-dont-know-case'
