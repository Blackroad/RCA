#CARD_READER SERVICE IS ON

def test_input_units_REWORK(app):
    app.unit.find_units('REWORK')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    assert app.unit.text_presented('The specified reader is not currently available for use.')



def test_input_units_CONTINUE(app):
    app.unit.find_units('CONTINUE')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    assert app.unit.text_presented('The specified reader is not currently available for use.')