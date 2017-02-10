def test_input_units_REWORK_NCP(app):
    user_name = app.config['jira']["login"]
    app.unit.find_units('REWORK')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@id='ok_button']")
    app.unit.submit_unit()
    assert app.unit.submit_without_fail() == True, "submit fail!"
    assert app.unit.element_presented("//div//button[@data-event='rca-popup-cancel' and text()='Close']")
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    app.unit.open_event_details()
    app.unit.take_screenshot('Rework_NCP')
    assigned_user = app.unit.assignee_field()
    assert app.unit.unit_status('In NCP')
    assert user_name == assigned_user
    app.unit.take_screenshot('Rework_NCP')

def test_input_units_REWORK_non_NCP(app):
    user_name = app.config['jira']["login"]
    app.unit.find_units('REWORK')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@id='ok_button']")
    app.unit.Rwk_submit_with_workpath('RwkTestFF')
    app.unit.open_event_details()
    assigned_user = app.unit.assignee_field()
    assert app.unit.unit_status('Disposition Complete')
    assert user_name == assigned_user

def test_input_units_CONTINUE(app):
    user_name = app.config['jira']["login"]
    app.unit.find_units('CONTINUE')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@id='ok_button']")
    app.unit.submit_unit()
    assert app.unit.submit_without_fail() == True, "submit fail!"
    assert app.unit.element_presented("//div//button[@data-event='rca-popup-cancel' and text()='Close']")
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    app.unit.open_event_details()
    assigned_user = app.unit.assignee_field()
    assert app.unit.unit_status('Disposition Complete')
    assert user_name == assigned_user

def test_input_units_SCRAP(app):
    user_name = app.config['jira']["login"]
    app.unit.find_units('SCRAP')
    app.unit.submit_unit()
    assert app.unit.submit_without_fail() == True, "submit fail!"
    assert app.unit.element_presented("//div//button[@data-event='rca-popup-cancel' and text()='Close']")
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    app.unit.open_event_details()
    assigned_user = app.unit.assignee_field()
    assert app.unit.unit_status('Scrap')
    assert user_name == assigned_user