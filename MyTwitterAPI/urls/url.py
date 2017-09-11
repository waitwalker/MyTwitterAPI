from handlers import index_handler,register_handler

handlers = [
    (r'/index/',index_handler.IndexHandler),
    (r'/register/',register_handler.RegisterHandler),
]
