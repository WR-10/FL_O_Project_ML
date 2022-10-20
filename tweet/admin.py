from django.contrib import admin
from tweet.models import Article, Tag, TweetComment

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(TweetComment)
