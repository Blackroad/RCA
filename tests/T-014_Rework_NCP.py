def test_rework_NCP(app):
    app.unit.find_units('REWORK')
    app.unit.Rwk_submit_with_workpath('RwkNCP')
    assert app.unit.contol_is_enable('release-from-ncp-button')
    assert app.unit.unit_serial_step_name('NCP')
    app.unit.release_from_NCP()
    assert app.unit.unit_serial_step_name('EngrDispo')
    assert app.unit.element_presented("//input[@id='select-disposition-button' and @value = 'Select Disposition']")



