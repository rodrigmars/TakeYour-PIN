def setup_routing(app):
    app.route('/new', ['GET', 'POST'], form_new)
    app.route('/edit', ['GET', 'POST'], form_edit)