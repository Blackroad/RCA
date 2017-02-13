#CARD_READER SERVICE IS ON

def test_input_units_REWORK(app):
    app.unit.find_units('REWORK')
    app.unit.take_screenshot('Rework_without_card')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    assert app.unit.text_presented('The card has been removed')



def test_input_units_CONTINUE(app):
    app.unit.find_units('CONTINUE')
    app.unit.take_screenshot('Continue_without_card')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    assert app.unit.text_presented('The card has been removed')

def test_input_units_SCRAP(app):
    app.unit.find_units('SCRAP')
    app.unit.take_screenshot('Scrap_without_card')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    assert app.unit.text_presented('The card has been removed')
