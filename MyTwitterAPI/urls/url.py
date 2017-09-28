from handlers import index_handler,register_handler,about_handler

handlers = [
    (r'/index/',index_handler.IndexHandler),
    (r'/register/',register_handler.RegisterHandler),
    (r'/about/',about_handler.AboutHandler),
]
