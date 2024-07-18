from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main = 0
        for form in self.forms:
            if form.cleaned_data["is_main"] == True:
                is_main += 1
        if is_main > 1:
            raise ValidationError("Выберите не более одного основного раздела")
        if is_main < 1:
            raise ValidationError("Выберите основной раздел")
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "text", "published_at", "image"]
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
