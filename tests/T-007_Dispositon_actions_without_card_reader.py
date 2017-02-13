#CARD_READER SERVICE IS ON

def test_input_units_REWORK(app):
    app.unit.find_units('REWORK')
    app.unit.take_screenshot('Rework_without_cardreader')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    assert app.unit.text_presented('The specified reader is not currently available for use.')


def test_input_units_CONTINUE(app):
    app.unit.find_units('CONTINUE')
    app.unit.take_screenshot('Continue_without_cardreader')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    assert app.unit.text_presented('The specified reader is not currently available for use.')


def test_input_units_SCRAP(app):
    app.unit.find_units('SCRAP')
    app.unit.take_screenshot('Scrap_without_cardreader')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    assert app.unit.text_presented('The specified reader is not currently available for use.')