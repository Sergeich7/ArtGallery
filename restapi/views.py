from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class APIRootView(APIView):
    """API root."""

    def get(self, request):
        data = {

            'Products (may added: /1/)':
                reverse('product-list', request=request),
            'Categories (may added: /1/)':
                reverse('category-list', request=request),
            'Techniques (may added: /1/)':
                reverse('technique-list', request=request),
            'Authors (may added: /1/)':
                reverse('author-list', request=request),

            'List products ID (may added: /author=1/category=4/technique=5/)':
                reverse('products-id-list', args={'/'}, request=request),

            'User login':
                reverse('rest_framework:login', request=request) + '?next=/api',
            'User logout':
                reverse('rest_framework:logout', request=request) + '?next=/api',
            'User create':
                reverse('users-signup', request=request),
            'User update':
                reverse('users-edit', request=request),
            'User change password':
                reverse('users-changepassword', request=request),
            'User delete':
                reverse('users-delete', request=request),
        }
        return Response(data)
