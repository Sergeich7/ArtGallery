"""Определяем свои тэги."""

import random

from django.utils.safestring import mark_safe
from django import template

from project.settings import DEBUG


register = template.Library()


@register.inclusion_tag('menu_items_cat_tec.html', takes_context=True)
def menu_items_cat_tec(context, items_type='cat', fl_no_all='all'):
    """Тэг генерит html меню (категории, техники, авторы)."""
    # тег вызывается 9 раз для одной страницы, те обращение к базе
    # не желательно.
    # если fl_no_all='all', то добавляет строку с общим количеством работ.
    return {
        'items_type': items_type,
        'items_no_all': fl_no_all,
        'total_obj': context['total_obj'],
        'all_items': context[f'all_items_{items_type}'],
    }


@register.simple_tag
def random_int(a: int, b=None) -> int:
    """Тэг с номером текущего желтого фона. Выбирается ранодомно."""
    if b is None:
        b = a
    return random.randint(a, b)


@register.simple_tag
def tracker() -> str:
    """Выводим трэкер если на продакшен."""
    return ('' if DEBUG else mark_safe("""

<!-- Yandex.Metrika counter -->
<script type="text/javascript" >
   (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
   m[i].l=1*new Date();
   for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
   k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

   ym(90974545, "init", {
        clickmap:true,
        trackLinks:true,
        accurateTrackBounce:true
   });
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/90974545" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->

"""))
