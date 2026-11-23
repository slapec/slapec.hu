from slpages.site import Site

site = Site('src')


@site('index.html', name='home')
def home():
    return site.template('index.html').render(greeting='Hello World!')


if __name__ == '__main__':
    site.build('dist')
