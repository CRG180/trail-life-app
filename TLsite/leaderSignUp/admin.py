from django.contrib import admin
from .models import trailGuideLeader, trailman ,eventType, group, event
from .models import subEvent, eventDocument
admin.site.register(trailGuideLeader)
admin.site.register(eventType)
admin.site.register(group)
admin.site.register(event)
admin.site.register(subEvent)
admin.site.register(eventDocument)
admin.site.register(trailman)