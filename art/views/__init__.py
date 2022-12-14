from .index import IndexView
from .favorites import FavoritesCMD, Cart
from .detail import DetailProdView
from .stripepayment import StripeBuyView
from .contact import ContactFormView

__all__ = [
    'IndexView', 'DetailProdView', 'ContactFormView',
    'FavoritesCMD', 'Cart', 'StripeBuyView',
    ]
