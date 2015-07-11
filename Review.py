class Review(object):
    def __init__(self, version, language, created_time, last_updated_time, stars, title, text, link):
        if not version:
            version = "0"
        self.version = version
        self.language = language
        self.created_time = int(created_time)
        self.last_updated_time = int(last_updated_time)
        self.stars = int(stars)
        self.title = title
        self.text = text
        self.link = link

    def __str__(self):
        return str(unicode(self))

    def __unicode__(self):
        return u'%s: %s' % (self.title, self.text)

    def to_dictionary(self):
        return {"version":self.version,
                "language":self.language,
                "created_time":self.created_time,
                "last_updated_time":self.last_updated_time,
                "stars":self.stars,
                "title":self.title,
                "text":self.text,
                "link":self.link}


