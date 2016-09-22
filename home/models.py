from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.blocks import StreamBlock

class EventBlock(blocks.StructBlock):
  start = blocks.DateTimeBlock()
  end = blocks.DateTimeBlock()
  name = blocks.CharBlock()
  description = blocks.CharBlock()
  location = blocks.CharBlock()

  class Meta:
    template = 'home/blocks/event.html'
    icon = 'calendar'

class EventList(Page):

  events = StreamField([
    ('event', EventBlock()),
  ])

  content_panels = Page.content_panels + [
    StreamFieldPanel('events')
  ]


class HomePage(Page):

  # Society & Technology News Fields
  main_news = models.ForeignKey(
    'home.NewsArticle',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+'
  )

  small_news_1 = models.ForeignKey(
      'home.NewsArticle',
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      related_name='+'
  )

  small_news_2 = models.ForeignKey(
      'home.NewsArticle',
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      related_name='+'
  )

  small_news_3 = models.ForeignKey(
      'home.NewsArticle',
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      related_name='+'
  )

  med_news_1 = models.ForeignKey(
      'home.NewsArticle',
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      related_name='+'
  )

  med_news_2 = models.ForeignKey(
      'home.NewsArticle',
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      related_name='+'
  )


  # Past Events Fields
  main_past_event_1 = models.ForeignKey(
    'home.NewsArticle',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+'
  )

  med_past_event_1 = models.ForeignKey(
    'home.NewsArticle',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+'
  )

  med_past_event_2 = models.ForeignKey(
    'home.NewsArticle',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+'
  )

  main_past_event_2 = models.ForeignKey(
    'home.NewsArticle',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+'
  )

  # Future Event Fields
  small_future_event_1 = models.ForeignKey(
    'home.NewsArticle',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+'
  )

  small_future_event_2 = models.ForeignKey(
    'home.NewsArticle',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+'
  )

  small_future_event_3 = models.ForeignKey(
    'home.NewsArticle',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+'
  )

  content_panels = Page.content_panels + [
    # Society & Tech News Panels
    FieldPanel('main_news', classname="full"),
    FieldPanel('small_news_1', classname="full"),
    FieldPanel('small_news_2', classname="full"),
    FieldPanel('small_news_3', classname="full"),
    FieldPanel('med_news_1', classname="full"),
    FieldPanel('med_news_2', classname="full"),
    # Past Events Panels
    FieldPanel('main_past_event_1', classname="full"),
    FieldPanel('med_past_event_1', classname="full"),
    FieldPanel('med_past_event_2', classname="full"),
    FieldPanel('main_past_event_2', classname="full"),
    # Future Events Panels
    FieldPanel('small_future_event_1', classname="full"),
    FieldPanel('small_future_event_2', classname="full"),
    FieldPanel('small_future_event_3', classname="full")
  ]

class ProfileBlock(blocks.StructBlock):
  fullname = blocks.CharBlock(required=True, unique=True)
  committee_role = blocks.CharBlock(required=True)
  biography = blocks.RichTextBlock(required=True)
  sex = blocks.ChoiceBlock(choices=[
    ('Male', 'Male'), 
    ('Female', 'Female'), 
    ('Other', 'Other')
  ])
  photo = ImageChooserBlock()

  class Meta:
    template = 'home/blocks/profile.html'
    icon = 'user'

class ProfileList(Page):
  template = "home/profile_list.html"

  profiles = StreamField([
    ('profile', ProfileBlock()),
  ])

  content_panels = Page.content_panels + [
    StreamFieldPanel('profiles')
  ]

class NewsArticle(Page):
  author = models.CharField(max_length=255)
  date = models.DateField("Post date")
  body = StreamField([
    ('heading', blocks.CharBlock(classname="full title")),
    ('paragraph', blocks.RichTextBlock()),
    ('image', ImageChooserBlock())
  ])

  content_panels = [
    FieldPanel('title'),
    FieldPanel('author'),
    FieldPanel('date'),
    StreamFieldPanel('body'),
  ]

class MediaBlock(blocks.StructBlock):
  heading = models.CharField()
  media = StreamBlock([
    ('image', ImageChooserBlock())
  ])

  class Meta:
    template = 'home/blocks/media.html'
    icon = 'image'

class MediaPage(Page):
  body = StreamField([
    ('media', MediaBlock()),
  ]) 

  content_panels = [
    FieldPanel('title'),
    StreamFieldPanel('body'),
  ]

class AboutPage(Page):
  body = StreamField([
    ('heading', blocks.CharBlock(classname="full title")),
    ('paragraph', blocks.RichTextBlock()),
    ('image', ImageChooserBlock())
  ])

  content_panels = [
    FieldPanel('title'),
    StreamFieldPanel('body'),
  ]