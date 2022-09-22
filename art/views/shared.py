from django.views.generic import TemplateView


class AddContextMixin():
    """Примесь для сбора общего для всех страниц сайта контекста."""

    def add_context(self, context, **kwargs):
        """Добавляем контекст - меню, количество, категории итд."""
        # Либо передали указатель меню, либо получаем из self.template_name
        # обычно типа 'art/contacts.html' - вытаскиваем contacts
        context['active_cat'] = kwargs.get(
            'active_cat', self.template_name.split('.')[0].split('/')[-1])
        return context


class ClearTextView(AddContextMixin, TemplateView):
    """Класс для текстовых страниц - Спасибо Успешно."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.add_context(context)

