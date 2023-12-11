import main
from car import Car


def test_class():
    car = Car('Ford', 'Mustang', 1994)
    assert car.brand == 'Ford'
    assert car.model == 'Mustang'
    assert car.construction == 1994

def test_one_car(monkeypatch, capsys):
    inputs = iter(['VW', 'Golf', '2015', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == '2015\nVW\nGolf\n'

def test_multiple_cars(monkeypatch, capsys):
    inputs = iter(['Ford', 'Mustang', '1994', 'VW', 'Golf', '2015', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == '1994\nFord\nMustang\n2015\nVW\nGolf\n'