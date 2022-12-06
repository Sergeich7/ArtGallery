from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class APIRootView(APIView):

    def get(self, request):
        data = {
            'User login': reverse('rest_framework:login', request=request) + '?next=/api',
            'User logout': reverse('rest_framework:logout', request=request) + '?next=/api',
            'Create user': reverse('users-signup', request=request),
            'Update user': reverse('users-edit', request=request),
            'Change user password': reverse('users-changepassword', request=request),
            'Delete user': reverse('users-delete', request=request),

            'Categories (may added: /1/)': reverse('categories-list', request=request),
            'Technique (may added: /1/)': reverse('technique-list', request=request),
            'Author (may added: /1/)': reverse('author-list', request=request),
            'Products (may added: /1/)': reverse('product-list', request=request),

            'List products ID (may added: /author=1/category=4/technique=5/)': reverse('products-id-list', args={'/'}, request=request),
        }
        return Response(data)

#
#
#@api_view(['GET'])
#def api_root(request, format=None):
#    R = {
#        'Create user': reverse('users-signup', request=request, format=format),
#        'Update user': reverse('users-edit', request=request, format=format),
#        'Change user password': reverse('users-changepassword', request=request, format=format),
#        'Delete user': reverse('users-delete', request=request, format=format),
#
#        'Categories (may added: /1/)': reverse('categories-list', request=request, format=format),
#        'Technique (may added: /1/)': reverse('technique-list', request=request, format=format),
#        'Author (may added: /1/)': reverse('author-list', request=request, format=format),
#        'Products (may added: /1/)': reverse('product-list', request=request, format=format),
#
#        'List products ID (may added: /author=1/category=4/technique=5/)': reverse('products-id-list', args={'/'}, request=request, format=format),
#    }
#    return Response(R)
#
#