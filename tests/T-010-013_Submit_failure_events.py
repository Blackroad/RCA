def test_input_units_REWORK_NCP_T010(app):
    user_name = app.config['jira']["jira_user_id"]
    app.unit.find_units('REWORK')
    app.unit.submit_unit()
    app.unit.take_screenshot('Rework_NCP')
    assert app.unit.submit_without_fail() == True, "submit fail!"
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    app.unit.open_event_details()
    assigned_user = app.unit.assignee_field()
    assert app.unit.unit_status('In NCP')
    assert user_name == assigned_user
    app.unit.take_screenshot('Rework_NCP')

def test_input_units_REWORK_non_NCP_T011(app):
    user_name = app.config['jira']["jira_user_id"]
    app.unit.find_units('REWORK')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@id='ok_button']")
    app.unit.Rwk_submit_with_workpath('RwkTestFF')
    app.unit.take_screenshot('Rework_TestFF')
    app.unit.open_event_details()
    assigned_user = app.unit.assignee_field()
    assert app.unit.unit_status('Disposition Complete')
    assert user_name == assigned_user
    app.unit.take_screenshot('Rework_TestFF')

def test_input_units_SCRAP_T012(app):
    user_name = app.config['jira']["jira_user_id"]
    app.unit.find_units('SCRAP')
    app.unit.submit_unit()
    app.unit.take_screenshot('SCRAP')
    assert app.unit.submit_without_fail() == True, "submit fail!"
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    app.unit.open_event_details()
    assigned_user = app.unit.assignee_field()
    assert app.unit.unit_status('Scrap')
    assert user_name == assigned_user
    app.unit.take_screenshot('SCRAP')

def test_input_units_CONTINUE_T013(app):
    user_name = app.config['jira']["jira_user_id"]
    app.unit.find_units('CONTINUE')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@id='ok_button']")
    app.unit.submit_unit()
    app.unit.take_screenshot('CONTINUE')
    assert app.unit.submit_without_fail() == True, "submit fail!"
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    app.unit.open_event_details()
    assigned_user = app.unit.assignee_field()
    assert app.unit.unit_status('Disposition Complete')
    assert user_name == assigned_user
    app.unit.take_screenshot('CONTINUE')

