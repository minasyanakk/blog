from django.contrib import admin
from .models import Post
from .for_telegram import Message

def make_published(modeladmin, request, queryset):
	telegram = Message()
	s = queryset.values('title','content','cover','slug')
	# title = s[0]['title']
	# content = s[0]['content']
	if s[0]['cover'] == '':
		telegram.send_without_image(s[0]['title'],s[0]['content'])
	else:
		telegram.send_with_image(s[0]['title'],s[0]['content'],s[0]['cover'],s[0]['slug'])
	
	


make_published.short_description = "Send to Telegram"

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_published]


  
admin.site.register(Post, PostAdmin)

