def test_app_tiene_sintaxis_valida():
    with open('app.py', encoding='utf-8') as f:
        compile(f.read(), 'app.py', 'exec')


def test_app_define_las_rutas():
    with open('app.py', encoding='utf-8') as f:
        code = f.read()
    assert "@app.route('/')" in code
    assert "@app.route('/monster', methods=['POST'])" in code


def test_existe_la_plantilla_index():
    with open('templates/index.html', encoding='utf-8') as f:
        assert '<html' in f.read().lower()
