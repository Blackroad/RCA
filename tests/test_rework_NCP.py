def test_rework_NCP(app):
    #user_name = app.config['card_data']["user_name"]
    app.unit.find_units('REWORK')
    app.unit.select_work_path('RwkNCP')
    #assert app.unit.element_presented("//div[@id='unit-details-mes-buttons']/input[@value='Select Disposition']")

