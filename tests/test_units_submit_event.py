def test_input_units_REWORK(app):
    user_name = app.config['card_data']["user_name"]
    app.unit.find_units('REWORK')
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@id='ok_button']")
    app.unit.submit_unit()
    assert app.unit.element_presented("//div[@class='buttonPanel']/button[@disabled]")
    app.unit.open_event_details()
    assert app.unit.unit_status('Disposition Complete')
   # assigned_user = app.unit.assignee_field()
    # assert user_name == assigned_user