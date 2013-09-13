feincms-filer-content
=====================

A FeinCMS contenttype package for django-filer

This is still work in progress.

Usage
-----

Remove ``feincms.module.medialibrary`` from your ``settings.INSTALLED_APPS``.

In your ``models.py`` register the contenttypes as follows::

  from mediafiler.models import ImageContent, FileContent

  MEDIA_POSITION_CHOICES=(
      ('inline', _('Full width')),
      ('left', _('Left')),
      ('right', _('Right')),
  )

  Page.create_content_type(ImageContent, TYPE_CHOICES=MEDIA_POSITION_CHOICES)
  Page.create_content_type(FileContent)

Copy the templates into your project directory as well.