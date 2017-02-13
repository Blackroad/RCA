#CARD_READER SERVICE IS ON


def test_input_units_REWORK(app):
    user_name = app.config['card_data']["user_name"]
    app.unit.find_units('REWORK')
    app.unit.take_screenshot('Rework_e-sign')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@id='ok_button']")
    recieved_user_id = app.unit.user_id()
    assert user_name == recieved_user_id


def test_input_units_CONTINUE(app):
    user_name = app.config['card_data']["user_name"]
    app.unit.find_units('CONTINUE')
    app.unit.take_screenshot('Continue_e-sign')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@id='ok_button']")
    recieved_user_id = app.unit.user_id()
    assert user_name == recieved_user_id

def test_input_units_SCRAP(app):
    user_name = app.config['card_data']["user_name"]
    app.unit.find_units('SCRAP')
    app.unit.take_screenshot('Scrap_e-sign')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@id='ok_button']")
    recieved_user_id = app.unit.user_id()
    assert user_name == recieved_user_id
