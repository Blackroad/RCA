#CARD_READER SERVICE IS OFF

def test_input_units_REWORK(app):
    app.unit.find_units('REWORK')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    assert app.unit.text_presented('Check if card reader daemon is running')

def test_input_units_CONTINUE(app):
    app.unit.find_units('CONTINUE')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    assert app.unit.text_presented('Check if card reader daemon is running')


